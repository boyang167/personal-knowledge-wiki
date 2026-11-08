---
title: Tencent WeData / DLC 数据平台搭建实践
description: 数据平台在Tencent落地顺序：Landing Zone、KMS、DLC 命名与权限、WeData 集成发布、Oceanus、API 网关、COS、SCF→PG 入湖与数据资产闭环
category: DataPlatform
date: 2026-11-08
readTime: 55 分钟
icon: ☁
featured: false
draft: false
---

| 项目 | 内容 |
|------|------|
| **主线** | WeData + DLC + COS +（可选）Oceanus / CKafka |
| **分层** | ODS → DIM → DWD → DWS → ADS |
| **命名占位** | `{PREFIX}` / `Corp_` 表示企业自定义前缀（集成项目、KMS 等），非云产品名称 |
| **关联** | 与 [AliCloudy.md](./AliCloudy.md)、[AzureDataPlatform.md](./AzureDataPlatform.md)、[DataCatalogMetadataGovernance.md](./DataCatalogMetadataGovernance.md)  |

---

## 0. 平台搭建总览（先做什么）

| 阶段 | 关键动作 | 经验要点 |
|------|----------|----------|
| 云基座 | **Landing Zone** 账号/网络/合规基线 → 再开数据产品 | 未先划清共享基座 vs 工作负载时，WeData/DLC/TKE 易出现重复 VPC、权限敞口 |
| 密钥 | **KMS** 托管 CMK，凭据与加密与 CAM 联动 | API Secret、库密码、COS 加密密钥**勿写进文档/Git**；数据平台上线前需完成 KMS 接入 |
| 账号与权限 | CAM Admin → Platform Admin/Member → 项目角色 → DLC 角色 | **权限先于开发**：未理顺 CAM / WeData 项目 / DLC 三层时，后期补权成本高 |
| 网络与登录 | SSO 域账号映射；IT 放行腾讯相关域名 | 页面空白、控制台打不开，优先查**公司 DNS/安全策略是否拦截腾讯域名** |
| 资源规划 | 集成资源组、DLC 引擎（Spark/Presto）、Notebook 工作空间 | dev/prd 靠**资源隔离**区分，不是完全独立环境；发布流要按标准项目模型走 |
| 数据入湖 | 统一集成项目 + 命名规范 + ODS 落地 | 集成任务集中在 **`{PREFIX}_Data_Integration`** 专项 WeData 项目；**非结构化文件**先入 **COS** `raw-data` 再集成/解析入 DLC |
| 治理与服务 | 元数据采集 → 质量 → **数据资产** → API | 资产**上架**前补全业务信息与负责人；详见 **功能说明 9** |
| 下游消费 | 云 MySQL 同步 GDS、FineBI、API 市场 | 内网库需提前打通 VPC/专线/Private Link；POC 常见卡点：**云上 MySQL 已部署但 IDC 未通** |
| 补数/抓数 | **Serverless（SCF）** 定时拉源 → **云 PG** → WeData 入 DLC | 源系统仅 API、或网络只能到 VPC 内 PG 时，用 SCF 做轻集成再交 WeData 批同步 |

**SSO 登录**：[域账号 SSO 入口](https://tencentcloudsso.com/login)（角色映射以 CAM 配置为准）。

**分层口径**：ODS → DIM → DWD → DWS → ADS。

---

## DLC（Data Lake Compute）

### 定位

- 湖仓**计算与 Catalog 层**：Spark / Presto / PySpark / SQL 脚本的主战场。
- **Catalog** 由平台默认生成；库表按 `{DOMAIN}_{ENV}`（如 `Project_DEV` / `Project_PRD`）规划。

### 引擎与命名（落地经验）

- 引擎名：`{部门}_{Spark|Presto}_{用途}_{DEV|PRD}`，环境标识必须显式区分。
- 表名：`{分层}_{实体_粗_细}`（如 `ods_user_base_info`、`dwd_order_detail_item`）。
- View：`..._V`；Function / Field 遵循文档附录命名，**上线前在 DLC 与 WeData 侧名称一致**，避免血缘对不齐。

### 权限模型

| 角色 | 职责 |
|------|------|
| DLC 管理员 | 库表/引擎/成员与工作组；表级授权 |
| DLC 成员 | 按工作组或表授权开发、查询 |

Platform Admin 可将 Platform Member 加为 DLC Member，再按库表/工作组拆分。常见工作：建库、授表、引擎规格升级（与项目 ENV 对齐）。

### 开发与算力（Q&A ）

| 开发位置 | 运行时资源 |
|----------|------------|
| 离线开发 → **DLC 模块**脚本 | **DLC 引擎**（PySpark/SQL 等） |
| **通用模块** Python/Shell | **WeData 调度资源组** |
| 通用模块 JDBC SQL | 下发到数据源自带引擎（如 MySQL、Doris） |
| **Notebook 探索** | Jupyter Pod**本身不单独计费**；任务提交到 DLC/ML 资源组则**占用 DLC/ML 配额并计费** |

**团队约定**：交互调试在 **Notebook**；定稿 ETL 在 **DLC 模块**建正式脚本任务，再纳入工作流编排。详见 **功能说明 8：Jupyter Notebook（探索）**。

### 搭建 checklist

- [ ] DEV/PRD 各建对应 Database（`*_DEV` / `*_PRD`）
- [ ] Spark/Presto 引擎规格与 ENV 标签就绪
- [ ] 项目成员 DLC 表权限最小化（按域/层授权）
- [ ] 与 COS/CHDFS 等存储适配参数（Flink/Oceanus 场景另配 Hadoop FS 适配项）

---

## 功能说明 1：DB / Schema / Table 命名

> 依据腾讯 DLC 命名规范；数据平台落地时在 **Catalog → Database →（Schema）→ Table → Field** 上保持一致，便于血缘、权限与跨环境迁移。

### 层级关系（DLC / 湖仓）

| 层级 | 谁创建 | 命名规则 | 示例 |
|------|--------|----------|------|
| **Catalog** | 腾讯侧默认生成 | 一般不改；代表平台/账户级元数据空间 | （平台默认 Catalog） |
| **Database（库）** | DLC 管理员 | `{DOMAIN}_{ENV}`，`ENV` 仅 `DEV` / `PRD` | `Project_DEV`、`Process_PRD` |
| **Schema（模式）** | 数据工程师 | `{LAYER}` 小写，与数仓分层一致 | `ods`、`dim`、`dwd`、`dws`、`ads` |
| **Table（表）** | 数据工程师 | `{layer}_{entity}_{coarse}_{fine}`，**layer 小写** | `ods_user_base_info`、`dwd_order_detail_item` |
| **View** | 数据工程师 | `{layer}_{domain}_{entity}_{coarse}_{fine}_V` | `dwd_finance_order_summary_V` |
| **Field（字段）** | 数据工程师 | 小写 + 下划线；见下表 | `order_id`、`created_time` |

**Catalog / Database / Schema 怎么选**

- **Database = 数据域 × 环境**（与 WeData **项目命名** `{数据域}_{项目}_{REGION}` 对齐）。
- **Schema = 分层**（推荐）：同一 Database 下用 `ods`、`dwd` 等 Schema 隔离层，表名仍保留层前缀。
- 若团队**不在 DLC 建 Schema**，则分层**只体现在表名前缀**，集成与 ETL 任务命名必须带 `ods_` / `dwd_` 等。

### Database 命名字段

| 字段 | 含义 | 示例 |
|------|------|------|
| DOMAIN | 数据域 | `project`、`process` |
| ENV | 环境 | `dev`、`prd`（规范文档用大写 `DEV`/`PRD`，团队内统一即可） |

### Table / View 示例（与分层）

| 场景 | 表名 |
|------|------|
| 用户域 ODS 基础信息 | `ods_user_base_info` |
| 订单域 DWD 明细 | `dwd_order_detail_item` |
| 内容域 DWS 汇总 | `dws_content_video_play_summary` |
| 财务域 ADS 应用 | `ads_finance_monthly_revenue` |

### Field 命名约定（实践补充）

| 类型 | 约定 | 示例 |
|------|------|------|
| 主键 / 外键 | `{实体}_id` | `user_id`、`order_id` |
| 时间 | `{动作}_time` / `{业务}_date` | `created_time`、`biz_date` |
| 布尔 | `is_` / `has_` 前缀 | `is_deleted` |
| 金额 / 数量 | 语义 + 单位后缀（可选） | `amount_cny`、`qty` |
| 枚举 / 编码 | `{含义}_code` | `status_code` |

### 与 WeData 侧命名对齐

| WeData 对象 | 与 DLC 关系 |
|-------------|-------------|
| 数据集成任务 `ods_{src}_t` | 目标表建议落在 `{Domain}_{ENV}.ods.ods_*` 或 `{Domain}_{ENV}` 下 `ods_*` |
| DLC SQL / PySpark 脚本 | 脚本内 **fully qualified** 名与上表一致 |
| 元数据采集 | 库名、表名与 DLC 一致，资产目录按 **DOMAIN + LAYER** 挂载 |

---

## WeData

### 角色体系（三层）

1. **CAM**：Admin / Full Access（Platform Admin）/ Read-Only（Platform Member）
2. **WeData 平台级**：如 Asset Admin（资产管理员）
3. **WeData 项目级**：Project Admin / Engineer / Ops

**流转经验**：CAM Admin 创建账号 → Platform Admin 建项目并任首任 Project Admin → 移交 PM → PM 加成员 → 按需授 Asset Admin、DLC Member。**权限申请走邮件 + PM/TL 审批**。

### 数据开发

#### Pipeline 生命周期（建议顺序）

1. **需求与规划**：指标口径、字段清单、数据流向图
2. **建模设计**：分层表设计 + 数据字典
3. **数据集成**：管理员配数据源 → 同步到 ODS（全量/增量）
4. **ETL**：**Notebook 探索** → **DLC 模块**定稿 → 工作流编排（功能说明 8）
5. **质量校验**：完整性 / 准确性 / 与源系统对账
6. **发布**：提交 → 发布包 → **Project Admin 审批** → prd 运行
7. **运维**：实例运维、失败告警、数据量波动

#### 集成（Ingestion）

- **统一项目**：`{PREFIX}_Data_Integration`（示例 `Corp_Data_Integration`）管理所有集成任务。
- **资源组**：dev/prd 集成资源组（规格以采购为准，常见 8C/16G）。
- **增量**：源表需 **时间戳或自增 ID**；映射、调度（T+1）、dev/prd 表需一次说清。
- **命名**：`{分层}_{源表}_{t|v|a|f}`，例：`ods_ebr_order_t`；**文件入湖**后缀 `f`，例：`ods_lims_export_f`。
- **数据源命名**：`{部门}_{系统}_{REGION}_{MYSQL|PG|COS}_{INGEST|EXPORT}`。

**结构化 vs 非结构化**

| 类型 | 典型来源 | 首选路径 |
|------|----------|----------|
| 结构化 | MySQL、PG、API 落库 | WeData JDBC 集成 → DLC 表 |
| 半结构化 | JSON/CSV/Excel/日志文件 | **COS** → WeData 文件集成或 DLC PySpark 解析 → ODS |
| 非结构化 | PDF、图片、仪器原始包 | **COS** `raw-data` **归档** → 元数据登记；需结构化时另起解析任务 |

非结构化详见 **功能说明 7**。

#### 编排空间与工作流

- 在 **离线开发 → 编排空间** 建工作流（周期 `*_Sched` / 手动 `*_Manual`）。
- 单工作流 = 一条 pipeline 全链路（集成 + ETL + 发布 + 监控）。
- **跨工作流依赖**：workflow B 可引用 workflow A 的集成任务。
- 测试通过后 **提交 → 发布包 → 审批**；支持回滚。

#### 包依赖

- **仅项目管理员**可安装 Python/PySpark 第三方包。

#### 命名速查

| 对象 | 规则 |
|------|------|
| 项目/目录 | 大写 + 下划线（如 `PROCESS_CCPD_SHANGHAI`） |
| 任务脚本 | 小写 + 下划线（功能描述） |
| 工作流 | `{描述}_Sched` / `{描述}_Manual` |

#### 开发侧踩坑

- WeData 代码**暂不能同步公司 GitLab** — 关键脚本需人工/流程备份。
- 控制台：**控制台 → 搜索 WeData**。
- 页面异常：除权限外，优先排查 **DNS 拦截**。

### 数据服务

1. **新建 API**：业务目录；Path、**推荐应用认证**。
2. **网关环境**：dev / prod 使用不同网关 ID（以租户控制台为准）。
3. **开发**：脚本模式 + SQL；**DLC 不能作为 API 源**，用云库/GDS 等。
4. **发布**：上线后 **API 市场**可见；调用方建应用拿 Key/Secret（HMAC 签名）。
5. **日志**：**日志暂不支持环境隔离**，排障需结合网关与时间窗口。

#### API 命名

- 路径：`/{domain}/{entity}/{category}/{purpose}`
- 应用：`{user_system}_{category}`

#### 经验

- 免认证无法追溯调用方，**生产禁用**。
- NPP/Davinci 对接报错：查 **网关环境、Key 绑定、SQL 数据源权限、Path 与发布状态**。

（与 **云原生网关 / Kong** 分工见 **功能说明 3**。）

### 数据治理（与开发平台一体）

| 步骤 | 动作 | 权限/注意 |
|------|------|-----------|
| 元数据采集 | DLC 自动采集 + GDS 等手动采集 | **仅 Project Admin** 建采集任务；执行资源选 dev/prd 对应资源组 |
| 元数据管理 | 血缘、标签、业务描述、权限申请 | 无权限表走审批流 |
| 数据质量 | 规则模板 → 表级监控 → 绑定 pipeline | 自定义规则常用 DLC SQL；告警 Teams/邮件 |
| **数据资产** | 业务目录 → 盘点 → **上架/下架** → 检索 | 见 **功能说明 9** |

---

## PG / MySQL

### 在平台中的角色

- **源库**：通过 WeData **数据源 + 数据集成** 入湖（ODS）。
- **中转/服务库**：**云上 MySQL** 同步 **GDS MySQL**，供 FineBI 等内网 BI 消费。

### 配置经验

| 项 | 建议 |
|----|------|
| 数据源 | **平台管理员**统一注册；命名带 REGION、INGEST/EXPORT |
| 连通性 | 云上：安全组 + 子网 + 集成资源组可达；IDC：专线/VPN，POC 常仅公网可测 |
| 增量 | binlog/时间戳；大表首次全量 + 增量策略写进设计文档 |
| 权限 | 只读账号用于集成；DLC/ETL 与源库隔离 |
| PG vs MySQL | 集成任务类型与 JDBC 任务走对应引擎 |

### POC 结论

- 云上 MySQL **部署成功** ≠ **内网 BI 可用**；需单独排 **GDS 路由与同步 pipeline**。
- 连接 **IDC MySQL** 与 Azure ADF「自承载 IR」同类，需前置网络项目。

---

## 功能说明 2：Oceanus 流计算

> [流计算 Oceanus](https://cloud.tencent.com/document/product/849) 基于 **Apache Flink**；可与 **CKafka** 组成实时链路，批处理仍以 WeData + DLC 为主。

### 产品能力

| 能力 | 说明 |
|------|------|
| 作业形态 | **SQL / JAR** 为主；旧版 ETL 作业勿用 |
| 开发运维 | Web IDE、依赖管理、发布、监控、Flink UI |
| 数据源 | CKafka、CDC、MongoDB、HBase 等；Connector 对接 COS、**DLC**、Iceberg、Paimon |
| 与湖仓衔接 | 写入 **DLC**、Iceberg/Paimon 或 **TCHouse-D** |
| 日志 | 可采集至 **ES Serverless** |

### 典型数据流（参考架构）

```text
业务库 / Binlog / 埋点
    → CKafka（缓冲、解耦、多订阅）
    → Oceanus（Flink SQL / JAR）
    → DLC（ods/dwd 实时表）或 Doris / 云 MySQL
    → WeData 批补数 / BI / API（T+0 看板 + T+1 对账）
```

### 搭建与开发要点

| 项 | 经验 |
|----|------|
| **集群与 CU** | 按峰值 QPS 与状态大小选 CU |
| **CKafka 消费** | `earliest` / `latest` / `timestamp`；注意分区倾斜 |
| **Checkpoint** | 对象存储路径稳定；保存点策略 |
| **CHDFS / COS** | 配 Hadoop FS 适配（AppId、region、tmp 目录等） |
| **CDC** | 源库权限与网络；IDC 源受专线限制 |
| **环境** | dev/prd 作业、Topic **分开** |

### 与 WeData / DLC 分工

| 链路 | 工具 |
|------|------|
| T+1 批式入湖、发布审批 | WeData + DLC + 工作流 |
| 秒级 / 分钟级 | Oceanus + CKafka |
| 实时资源组 | WeData **实时**资源组与 Oceanus **分开采购** |

### POC 结论

- Oceanus、CKafka 可独立验证；上线前对齐 **功能说明 1** 目标库表。
- 实时变更需 **保存点、双跑对账** 习惯。

---

## Kafka（CKafka）

- **定位**：消息队列与 CDC 管道；Oceanus Source 或 Kafka Connect。
- **Connect 状态 Topic**：`config` / `offset` / `status` 按环境隔离。
- 不能替代离线数仓；需显式建设 **Connect + 流计算**。

---

## 功能说明 3：云原生网关与 API Server

> 「对外给数」常见 **两层**：WeData **数据服务**（SQL 即 API + 托管网关）；**云原生 API 网关（Kong 等 on TKE）** 负责南北向统一入口。勿混用同一套域名与 Key。

### 架构关系

```text
调用方（ERP / PMS / 内网应用 / Fine 系）
        │
        ▼
┌───────────────────────────────┐
│ 云原生 API 网关（Kong 等）       │  统一域名、路由、限流、WAF
│ 部署：TKE / 云原生网关产品        │
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│ WeData 数据服务                 │
│  · API Server：SQL 定义接口     │
│  · 托管 API 网关：dev/prod 实例  │  HMAC、API 市场
└───────────────┬───────────────┘
                ▼
        云 MySQL / GDS / PG（非 DLC 直出）
```

### WeData 数据服务要点

| 环节 | 说明 |
|------|------|
| 数据源 | 云库、GDS；**DLC 不能作为 API 数据源** |
| 认证 | **应用认证**（HMAC）；生产禁用免认证 |
| 网关 | dev / prod **网关 ID 不同** |
| 路径 | `/{domain}/{entity}/{category}/{purpose}` |

### Kong / TKE 要点

1. **先** WeData 调通 API，**再** Kong Route 指到 WeData 网关 Host。
2. 调用方 Key 仍由 **WeData 应用**签发。
3. 与公司 **DNS / 安全放行** 联动。

### 边界

| 组件 | 是否算 API Server |
|------|-------------------|
| WeData 数据服务 | **是** |
| DLC / Oceanus | **否** — 需落库后消费 |
| Kong | **否** — 基础设施网关 |

---

## 功能说明 4：KMS（密钥管理服务）

> [KMS](https://cloud.tencent.com/document/product/573) 提供 **CMK** 与加解密 API；是企业侧凭据与静态数据加密的统一锚点。

### 在数据平台中的职责

| 场景 | KMS 作用 | 关联组件 |
|------|----------|----------|
| 凭据托管 | DB 密码、AppSecret、Kafka SASL | WeData 数据源、CDB、CKafka |
| 对象存储 | COS **SSE-KMS** | raw-data、Oceanus Checkpoint |
| 数据库 | TDE 可选绑定 KMS | 云上 MySQL |
| 容器 | TKE Secret 引用 KMS/凭据 | Kong 等工作负载 |
| API | AppSecret、TLS 私钥轮换 | 功能说明 3 |

### 实践要点

| 概念 | 说明 |
|------|------|
| CMK | 按环境拆分 `{prefix}-dev` / `{prefix}-prd`（示例 `corp-dev`、`corp-prd`） |
| CAM | Encrypt/Decrypt 仅 Platform Admin 与自动化角色 |
| 轮换 | 开启自动轮换；应用支持多版本解密 |
| 审计 | 云审计 + WeData 发布记录交叉排障 |

### checklist

- [ ] LandZone 创建 CMK；跨账号 CAM 若多账号
- [ ] COS `raw-data` 启用 **SSE-KMS**
- [ ] WeData 数据源密码走凭据流程；**文档只留占位符**
- [ ] TKE Helm values **禁止**明文 SecretKey

### 踩坑

- 轮换 KMS 后未更新 WeData 数据源 → 集成批量失败。
- Oceanus 写 Checkpoint 缺 KMS 权限 → AccessDenied。
- Notebook / Git 硬编码 AppSecret → 违背治理。

---

## 功能说明 5：Landing Zone

> **① 云 Landing Zone** — 账号/网络/合规；**② 数据 Landing Zone** — 原始数据第一站。

### 5.1 云 Landing Zone

```text
                    ┌─────────────────────────┐
                    │ 管理账号 / CAM / SSO     │
                    │ 组织与策略、审计、预算    │
                    └───────────┬─────────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          ▼                     ▼                     ▼
   ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
   │ 网络 / DNS    │      │ 安全 / KMS    │      │ 共享服务      │
   └──────┬───────┘      └──────┬───────┘      └──────┬───────┘
          └─────────────────────┼─────────────────────┘
                                ▼
                    ┌─────────────────────────┐
                    │ 工作负载：WeData / DLC   │
                    │ Oceanus / TKE / CDB ...  │
                    └─────────────────────────┘
```

| 模块 | 落地经验 |
|------|------------|
| 账号与组织 | CAM Admin → Platform Admin/Member |
| 网络 | VPC、专线、Forward DNS；内网未通勿当生产 |
| 身份 | SSO；页面空白先查 **DNS** |
| TCR | Kong、自研服务同 Region 拉镜像 |
| Tag | 与 `{DOMAIN}_{ENV}`、CAM 按 Tag 鉴权对齐 |

**顺序**：LandZone → WeData + DLC → 集成 → TKE 网关 → Oceanus/CKafka。

### 5.2 数据 Landing Zone

| 要素 | 说明 |
|------|------|
| 物理位置 | COS `raw-data/`；DLC Catalog |
| 逻辑项目 | `{PREFIX}_Data_Integration`；`ods_*_f` 文件任务 |
| 分层入口 | `ods_{src}_t` → DLC ODS |
| 权限 | 着陆区只授集成与运维；分析从 DWD/ADS 消费 |

```text
源（MySQL / PG / API / 文件）
        ▼
  Data Landing Zone（COS raw-data、staging、ODS）
        ▼
  DWD → DWS → ADS → API / BI / GDS
```

### checklist

- [ ] 云 LandZone：SSO、VPC、KMS、TCR、审计
- [ ] 数据 LandZone：集成项目、raw/ODS、元数据采集
- [ ] dev/prd 边界清晰
- [ ] POC 公网方案不直接等同生产

---

## 功能说明 6：Serverless 定时采集 → 云 PG → DLC

> **[云函数 SCF](https://cloud.tencent.com/document/product/583)** 定时拉源 → **云 PostgreSQL（Staging）** → **WeData 集成** → **DLC ODS**。适用于源仅 HTTP API、复杂鉴权、WeData 不宜直连的场景。

### 6.1 适用场景

| 情况 | 建议 |
|------|------|
| 源库 JDBC 且集成资源组可达 | 优先 **WeData 直连** |
| REST/GraphQL API | **SCF 定时** → PG staging |
| 源在 IDC，仅 VPC/HVIP 可达 | SCF **绑定 VPC** |
| 分钟级小批量 | SCF Cron + PG upsert |
| 血缘与审批 | DLC 段仍走 **WeData 工作流** |

### 6.2 端到端链路

```text
源系统 (API / 内网 HTTP)
        ▲
        │ 定时 SCF（VPC/HVIP、鉴权、分页、游标）
        ▼
云 PostgreSQL（staging / 可选 ods 镜像）
        │ WeData 集成（{PREFIX}_Data_Integration）
        ▼
DLC · {Domain}_{ENV}.ods · ods_{entity}_t
        ▼
DWD / DWS / ADS / API / BI
```

| 段 | 命名示例 |
|----|----------|
| PG staging | `staging.api_{system}_{entity}` |
| DLC | `{Domain}_DEV.ods.ods_{entity}_t` |

### 6.3 SCF 要点

| 配置项 | 说明 |
|--------|------|
| 触发器 | Cron，如 T+1 `0 30 2 * * *` |
| 网络 | VPC + 子网；**HVIP** dev/prd 分别验证 |
| 鉴权 | Token/Key 用 **环境变量 + KMS** |
| 增量 | PG `sync_meta` 表；**幂等 upsert** |

SCF **不直连 DLC**（避免双通路、难审计）。

**逻辑示例（Python，非生产完整代码）**：

```python
def main(event, context):
    cursor = pg_fetch_one("SELECT last_ts FROM sync_meta WHERE job='erp_orders'")
    rows = fetch_source_api(since=cursor, page_size=500)
    pg_upsert("staging.erp_orders", rows, key="order_id")
    pg_execute("UPDATE sync_meta SET last_ts=%s WHERE job='erp_orders'", max_ts(rows))
    return {"fetched": len(rows)}
```

### 6.4 云 PG（Staging）

- Schema：`staging`（SCF 写）、可选 `ods`。
- 字段：主键 + `source_updated_at` + `etl_loaded_at`；可选 `payload jsonb`。
- 权限：SCF 仅 DML staging；WeData **SELECT**；防火墙放行集成资源组。

### 6.5 WeData：PG → DLC

1. 数据源 `{DEPT}_{SYSTEM}_{REGION}_PG_INGEST`
2. 集成任务 `ods_{entity}_t` → DLC
3. 调度 **晚于 SCF**（如 SCF 02:00，集成 02:30）
4. dev 试跑 → 发布包 → Project Admin 审批

### 6.6 环境、监控与对账

- dev/prd：**独立 SCF + PG + 集成任务**
- 对账：源 API 总量 vs PG vs DLC ODS；`sync_meta` 与时间戳
- 常见：HVIP 不通超时；PG 连接打满；集成早于 SCF 结束 → 空跑

### 6.7 checklist

- [ ] VPC、KMS、PG staging + `sync_meta`
- [ ] SCF 定时、VPC、CAM
- [ ] WeData PG 数据源 + 调度晚于 SCF
- [ ] DLC 命名、元数据、质量

---

## 功能说明 7：非结构化文件与 COS

> [COS](https://cloud.tencent.com/document/product/436) 为 **非结构化 / 半结构化** 主存储。生产需 **桶、策略、KMS、WeData 数据源** 四件套。

### 7.1 适用场景

| 场景 | 用 COS | 入 DLC |
|------|--------|--------|
| CSV/JSON/Excel 导出 | 是 | WeData 文件集成或 PySpark |
| PDF/图片/仪器包 | 是（`raw-data` 归档） | 元数据 + 可选解析 |
| Parquet/ORC 批量 | 是 | Spark 直读入湖 |
| 仅数据库表 | 否 | JDBC 集成 |

### 7.2 COS 目录建议

```text
{bucket}/
  raw-data/
    {ENV}/{DOMAIN}/{SYSTEM}/{biz_date=YYYY-MM-DD}/...
  processed/          # 可选中间层
  checkpoint/         # Oceanus/Flink，与 raw 分离
```

- dev/prd **分桶或分前缀**；**SSE-KMS**
- 无公共读；生命周期与合规对齐

### 7.3 链路（文件 → DLC）

```text
文件来源 → COS raw-data/
    ├─ WeData 文件集成（ods_*_f）→ DLC ODS
    └─ DLC PySpark read cosn:// → ODS/DWD
         ▼
   质量 / 元数据 / 资产目录
```

**路径 C — 纯非结构化**：只进 `raw-data`，元数据登记为文件资产，不强行宽表。

### 7.4 命名对齐

| 对象 | 示例 |
|------|------|
| COS 数据源 | `NPP_LIMS_SHANGHAI_COS_INGEST` |
| 集成任务 | `ods_lims_result_f` |
| DLC 表 | `ods_lims_result` |

### 7.5 踩坑

- Region 不一致 → 权限与流量错误
- CSV BOM、Excel 日期 → Notebook 先验样本
- POC「没桶/没权限」→ 先 LandZone 建桶与 CAM

### 7.6 checklist

- [ ] 桶 + `raw-data/` 前缀 + SSE-KMS
- [ ] WeData 数据源 + `ods_*_f` 或 DLC 读 COS
- [ ] 非结构化原件资产目录登记

---

## 功能说明 8：Jupyter Notebook（WeData 探索）

> **Notebook 只用于探索**；生产逻辑在 **DLC 模块** + **工作流 + 发布包**。

### 8.1 定位

| 模块 | 生产调度 |
|------|----------|
| Notebook 探索 | **否** |
| DLC 模块脚本 | **是** |
| 通用 Python/Shell | 视场景 |

### 8.2 流程

```text
Notebook 调试 → 复制到 DLC PySpark/SQL → 工作流 → 发布审批 → prd
```

### 8.3 计费

| 选择 | 行为 |
|------|------|
| 绑定 DLC 引擎 | 提交到 DLC → **计费** |
| Notebook Pod | **资源组本身不单独收费** |

探索阶段限制 `collect()`、用 `limit` 防烧 CU。

### 8.4 规范

- 禁止硬编码密码/AppSecret
- 代码**暂不能同步 GitLab** → 定期导出备份
- dev/prd **不同项目或 Workspace**

### 8.5 checklist

- [ ] 绑定 **DLC Spark（DEV）**
- [ ] 生产逻辑已迁到 DLC 模块
- [ ] 第三方包由 **项目管理员** 安装

---

## 功能说明 9：WeData 数据资产

> **数据资产**管业务目录、上架、检索；**DLC Catalog** 管技术库表。见 [DataCatalogMetadataGovernance.md](./DataCatalogMetadataGovernance.md) 五维框架对照。

### 9.1 相关菜单

| 概念 | 说明 |
|------|------|
| 元数据管理 | 采集、血缘、标签、权限申请 |
| 数据质量 | 规则与监控 |
| **数据资产** | 业务目录树、盘点、上架、检索 |
| 数据服务 | API（功能说明 3） |

路径：**数据建模 → 数仓规划 → 资产目录**；**治理中心 → 资产目录盘点**；**数据资产 → 数据检索**。

### 9.2 治理链路

```text
集成/ETL 落地
  → ① 元数据采集（Project Admin）
  → ② 元数据管理（业务描述、血缘）
  → ③ 数据质量
  → ④ 盘点 + 上架
  → ⑤ 检索 / API / BI
```

**经验**：**prd 稳定后再采集**；上架前 **对账 + 至少 1 条质量规则**。

### 9.3 元数据采集

| 项 | 说明 |
|----|------|
| 谁可创建 | **仅项目管理员** |
| 对象 | **DLC** 自动采集、**GDS** 等手动选库 |
| 执行资源 | 与数据环境一致的 dev/prd 资源组 |
| 运维 | **实例运维** 看采集日志；失败多为权限或资源组选错环境 |

### 9.4 元数据管理（与资产强相关）

| 能力 | 用途 |
|------|------|
| 基本信息 / 字段 | **数据预览**需表权限 |
| 血缘 | 集成 → ETL → ADS 影响面 |
| 业务信息 / 字段描述 | **上架必填** |
| 标签 / 重要等级 / 生命周期 | 与资产目录联动 |
| 权限申请 | 无权限用户 → **Project Admin 审批** |

### 9.5 数据资产：核心功能

#### （1）新建业务资产目录

- 入口：**数据建模 → 数仓规划 → 资产目录**。
- 树形节点按 **数据域 / 业务线 / 主题** 划分，与 `{DOMAIN}` 对齐。

#### （2）盘点（绑定业务目录）

| 方式 | 入口 | 适用 |
|------|------|------|
| 单表/库批量 | 元数据管理 → 修改资产目录 | 少量新表 |
| 盘点 | 治理中心 → **资产目录盘点** | 按标签批量 |

#### （3）上架 / 下架

| 状态 | 含义 |
|------|------|
| 未上架 / 审批中 | 不可消费或不可见 |
| **已上架** | 资产目录、检索可见（仍受权限过滤） |
| 下架 | 审批后从目录隐藏 |

缺负责人或业务信息会导致上架失败 → 在元数据管理补全后再试。

#### （4）数据检索

- **数据资产 → 数据检索**：目录、关键词、上架状态、权限过滤。
- **上架** ≠ 全员可看：仍须 **表权限申请** 才能预览。
- API 已发布但资产未上架 → 数据地图与 API 市场不一致。

#### （5）COS 文件资产

COS `raw-data` 可在元数据管理登记，作为 **文件类资产** 挂目录（功能说明 7）。

### 9.6 与 Pipeline 衔接

| 阶段 | 数据资产动作 |
|------|----------------|
| 建模 | 预定目录节点、负责人 |
| prd 上线 | 触发元数据采集 |
| 发布后 | 质量 + 业务字段补全 |
| 盘点上架 | 开放检索 |
| 变更/下线 | 工作流回滚 + **下架** |

### 9.7 常见踩坑

- 只建 DLC 表不做采集 → 搜不到。
- dev 表进 prd 目录 → 库名/资源组未隔离。
- 以为上架 = 全员可读 → 仍需 DLC 权限。

### 9.8 角色

| 角色 | 职责 |
|------|------|
| Asset Admin | 跨项目资产策略 |
| Project Admin | 采集任务、上架审批、权限审批 |
| Project Engineer | 业务描述、配合盘点 |
| 业务用户 | 检索、申请权限 |

### 9.9 checklist

- [ ] 业务 **资产目录树** 与 Domain 对齐
- [ ] prd **元数据采集** 周期运行
- [ ] 核心表业务描述、负责人完整
- [ ] **盘点 + 上架** 首批资产
- [ ] 业务用户可 **数据检索** 验证

---

## 监控与运维

- **任务运维** / **实例运维**；质量报告、API 日志纳入值班。
- 关注耗时、资源、运行记录；发布审批与回滚纳入变更管理。

---

## 参考链接

- [WeData 产品文档](https://cloud.tencent.com/document/product/1267/50645)
- [KMS](https://cloud.tencent.com/document/product/573)
- [SCF](https://cloud.tencent.com/document/product/583)
- [云数据库 PostgreSQL](https://cloud.tencent.com/document/product/409)
- [COS](https://cloud.tencent.com/document/product/436)
- [Oceanus](https://cloud.tencent.com/document/product/849)

---

## 附录：端到端最小可行路径（MVP）

1. LandZone：SSO、VPC/DNS、KMS、TCR
2. CAM/SSO + WeData 项目（dev/prd）
3. DLC：`{Domain}_DEV` + Spark 引擎
4. COS `raw-data/` + `{PREFIX}_Data_Integration` → `ods_*_t` / `ods_*_f`
5. Notebook 验证 → DLC 任务 → 单工作流
6. 发布审批 → 元数据采集 + 质量 → **数据资产上架**（功能说明 9）
7. 可选：API 或 云 MySQL → GDS → BI
8. 可选（API 源）：SCF → 云 PG → WeData → DLC（功能说明 6）

按此路径可在 1～2 个迭代内完成「入湖 → 开发 → 发布 → 治理」闭环，再扩展 Oceanus 与多域。

---

