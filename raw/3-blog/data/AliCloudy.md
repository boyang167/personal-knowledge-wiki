---
title: 阿里云数据中台平台架构笔记
description: 基于 Landing Zone、MaxCompute、DataWorks、Hologres 的阿里云大数据平台能力梳理，含网络打通、连接工具、数仓分层与湖仓一体价值主张；附录落地扩展清单。
category: DataPlatform
date: 2026-11-02
readTime: 18 分钟
icon: ☁
featured: false
draft: false
---

| 项目 | 内容 |
|------|------|
| **文档性质** | 云平台能力梳理 + 实施扩展建议 |
| **计算/storage 主线** | MaxCompute（离线数仓）+ Hologres（实时分析/ Serving）+ Flink/DataHub（流） |
| **开发与治理** | DataWorks（集成 / 开发 / 建模 / 质量 / 服务 / 地图） |
| **账号示例** | RAM 用户组 `Atlas_admin`、`Atlas_developer`（见源 PDF） |

> 正文 **§1–§8** 对应原培训幻灯内容；**§9** 为落地扩展清单。  
> **配图**：`../img/alicloudy/` 共 18 张，已按主题插入各节。

## 1. 总体架构鸟瞰

```text
Landing Zone（账号 / 安全 / 网络 / 成本）
        │
        ├── API Gateway、Function Compute、RAM
        │
        └── Alicloud DataPlatform
                ├── DataWorks（开发治理一站式）
                ├── MaxCompute（AI-Native 云数仓，原 ODPS）
                ├── Hologres（实时数仓 / OLAP / Serving）
                ├── Flink、DataHub（流与实时通道）
                ├── OSS（对象存储 / 湖 / 外表）
                └── PAI、Serverless K8s（智能与弹性算力，构建中台）
```

**定位**：企业上云的「样板间 / 总部基地」+ 大数据中台引擎组合，而不是单一产品。

![湖仓一体总架构（幻灯第 13 页）](../img/alicloudy/p13-xref197.png)

*图 1-1：DataWorks + MaxCompute + Hologres 湖仓一体总览（高清原图）。*

---

## 2. Landing Zone 与网络打通

### 2.1 Landing Zone 是什么

**不是单一产品**，而是一套 **解决方案框架**，预先配置：

| 维度 | 内容 |
|------|------|
| **多账号** | 资源目录（Resource Directory）：管理账号 → 成员账号树形结构，生产 / 测试 / 开发隔离与集中管控 |
| **安全基线** | 统一策略、RAM、审计与合规检查 |
| **网络规划** | VPC、网段、互通方式 |
| **财务治理** | 统一费用管理与成本分摊 |

「Landing Zone **打通**」的首要任务是 **建立混合云 / 多云网络连接**。

### 2.2 专线 vs VPN（选型）

| 特性 | VPN 连接 | 专线连接 |
|------|----------|----------|
| **方式** | 公网加密隧道 | 运营商物理光纤 |
| **优势** | 分钟级部署、成本低、灵活 | 高稳定、超低延迟、高带宽、安全性高 |
| **劣势** | 受公网质量影响，可能抖动 | 部署周期长（数周）、成本高 |
| **适用** | 开发测试、临时连接、混合云备份/灾备 | 核心生产、大数据同步、实时库访问 |

后续落地常配合 **云企业网 CEN**、**PrivateLink**、**NAT 网关** 与安全组规划（见 §9.1）。

![混合云网络打通：VPN / 专线架构（幻灯第 2 页）](../img/alicloudy/p02-xref72.png)

*图 2-1：Landing Zone「打通」— 网络选型与连接路径。*

---

## 3. 身份与权限（RAM）

- **用户组（示例）**：`Atlas_admin`、`Atlas_developer`。
- **企业登录**：可配置 SSO 登录页（具体 URL 见源 PDF 环境说明）。
- **MaxCompute 细粒度授权**（对象与行为）：

| 对象/范围 | 管控点 |
|-----------|--------|
| 项目（Project）、Quota、Networklink | 项目级与算力/网络边界 |
| 表、函数、资源、实例 | 项目内对象操作 |
| Tunnel 下载、敏感数据访问、跨项目访问 | 高风险行为单独策略 |

原则：按人员操作范畴 **精细化授权**，而非仅项目级粗粒度角色。

![数据中台构建与 Atlas 组件（幻灯第 11 页）](../img/alicloudy/p11-xref179.png)

*图 3-1：DataWorks / MaxCompute / Hologres / RAM 等在中台中的位置（含 PAI、API Gateway 等）。*

![Atlas 环境要素条（幻灯第 11 页）](../img/alicloudy/p11-xref182.png)

*图 3-2：登录与用户组（*`Atlas_admin` */* `Atlas_developer`*）示意条。*

---

## 4. MaxCompute（计算与存储）

### 4.1 产品定位

企业级 **SaaS 化智能云数据仓库**（**AI-Native Datawarehouse**，原名 ODPS）。

![MaxCompute 权限、计算与存储（幻灯第 4 页）](../img/alicloudy/p04-xref97.png)

*图 4-1：细粒度权限、CU/Quota、内外部表与 MaxFrame。*

### 4.2 计算资源

- **CU**：1 CU = 1 CPU + 4 GB 内存。
- **Quota**：包年包月计算资源 vs 按量计费，对应不同规格类型。
- **MaxFrame**：镜像等扩展计算形态（见官方文档与 Quota 规划）。

### 4.3 存储模型

| 类型 | 说明 |
|------|------|
| **内部表** | 数据落在 MaxCompute；列类型为 MC 支持的类型 |
| **外部表** | MC **不持有**数据，元数据在 MC，数据在 **OSS / OTS**；可处理非结构化（音视频、基因、气象、地理等） |

读写路径：仓内分析为主；支持 **Tunnel / JDBC** 批量读写；**外部表 + 湖仓一体** 写 OSS 等湖存储。

![内部表 / 外部表与 OSS（幻灯第 5 页）](../img/alicloudy/p05-xref106.png)

*图 4-2：内部表 vs 外部表（OSS/OTS）与读写路径。*

### 4.4 数据采集（Data Collector）

开源采集插件集合，按通道分为两类：

| 通道 | 插件示例 | 场景 |
|------|----------|------|
| **DataHub（实时）** | Flume、OGG | 实时接入 |
| **Tunnel（批量）** | Sqoop、Kettle、Hive Data Transfer UDTF | 离线批量 |

另：**数据集成** 在 DataWorks 侧统一编排（见 §6）。

![Data Collector 与 DataHub / Tunnel（幻灯第 6 页）](../img/alicloudy/p06-xref116.png)

*图 4-3：Flume/OGG（实时）与 Sqoop/Kettle（批量）及 ODS 等分层引入。*

### 4.5 开放存储 Storage API

提供 **高效、低延迟、安全** 的读路径，第三方引擎（Spark on EMR、StarRocks、Presto、PAI 等）可访问 MC 底层存储；部分引擎可通过 **Connector** 直读，简化集成。

![Storage API 与多引擎读 MaxCompute（幻灯第 9 页）](../img/alicloudy/p09-xref158.png)

*图 4-4：Spark / StarRocks / Presto / PAI 等通过 Storage API / Connector 访问 MC。*

### 4.6 MaxLake（场景示例）

「入湖入仓 + 多引擎联动」：例如车联网 GPS → 里程/速度分析 → 即时报表、跨团队脱敏协作、AI 训练等 **一份数据多重价值**。

![MaxLake 与 DataWorks 关系（幻灯第 10 页）](../img/alicloudy/p10-xref175.png)

*图 4-5：MaxLake 入湖入仓与 DataWorks 衔接。*

![车联网 GPS 示例：一份数据多重价值（幻灯第 10 页）](../img/alicloudy/p10-xref176.png)

*图 4-6：MaxLake 场景流程（报表 / 协作 / AI 等）。*

---

## 5. 连接与生态工具

按 **场景** 选型，避免「一种工具打天下」。

| 类别 | 适用场景 | 代表工具 / 入口 |
|------|----------|-----------------|
| **SQL 分析** | 轻量分析、权限管理 | 控制台 **SQL 分析**（推荐 Chrome） |
| **命令行** | 脚本化批处理 | **云 odpscmd**（免安装，有会话/地域限制）vs **本地 odpscmd**（需 JDK 1.8+） |
| **IDE** | Java/Python UDF | **MaxCompute Studio**（IDEA ≥18.2.4 / PyCharm，JDK 1.8+） |
| **一站式** | 集成、调度、服务 | **DataWorks** |
| **库管 GUI** | 表管理 | DBeaver / DataGrip / SQL Workbench/J（JDBC 版本见官方） |
| **ETL 调度** | EL 到 MC | Kettle、Airflow、Azkaban 等 |
| **BI** | 可视化 | Quick BI、FineBI/Report、Tableau、观远、Metabase 等（驱动/版本见官方矩阵） |

**JDBC 版本**：不同工具对 MaxCompute JDBC 最低版本要求不同（常见 ≥3.0.1 / ≥3.2.8 / ≥3.7.0），上线前对照 [官方连接文档](https://help.aliyun.com/zh/maxcompute/) 锁定驱动。

> 幻灯第 7–8 页为连接工具与 BI/ETL 对照表（文字为主），未单独导出嵌入图；矩阵见上文表格。

---

## 6. DataWorks：开发治理一站式

### 6.1 能力全景

基于 MaxCompute / EMR / Hologres 等引擎，覆盖：

```text
数据集成 → 开发 → 建模 → 分析 → 质量 → 服务 → 数据地图 → 开放能力
```

> DataWorks 能力全景图见 **图 3-1**（与 RAM/中台同页）。

### 6.2 开发模式

- **标准模式**：开发 / 生产环境隔离（任务发布与运维规范的基础）。
- **智能数据建模**（四模块）：**数仓规划**、**数据标准**、**维度建模**、**数据指标**。
- **Data Studio**：可视化数据开发、运维与 **任务监控定位**。

![标准模式与任务监控（幻灯第 12 页）](../img/alicloudy/p12-xref187.png)

*图 6-1：标准模式、任务监控与 Data Studio 入口。*

![智能数据建模四模块（幻灯第 12 页）](../img/alicloudy/p12-xref192.png)

*图 6-2：数仓规划 / 数据标准 / 维度建模 / 数据指标。*

### 6.3 湖仓一体 + 流批融合（架构叙事）

![湖仓一体方案标语（幻灯第 13 页）](../img/alicloudy/p13-xref195.png)

*图 6-3：MaxCompute + Hologres 流批融合定位。*

> 总架构大图见 **图 1-1**（`p13-xref197`）。

源幻灯归纳的四条主线：

1. **统一接入与分层**

   Data Integration 接入业务库、日志、Kafka/DataHub 等 → 统一 **ODS → DWD → DWS → ADS**（与 DIM 配合），一份数据服务离线 + 实时。
2. **离线 T+1（基座）**

   DataStudio + MaxCompute SQL 对 TB/PB 历史数据批量 ETL；调度在凌晨自动跑批，支撑画像、ML 特征、宏观分析。
3. **实时 / 准实时**
   - **Flink SQL**：毫秒级流处理（风控、大屏、推荐）。  
   - **Hologres**：对已落盘数据 **秒级即席查询**，业务自助探查，不必等 T+1。
4. **融合分析与统一服务**

   Hologres 加速查询 MaxCompute 数据，实时 + 离线关联；**DataService Studio** 封装 API，供应用、BI、大屏统一出口。

![流批融合与统一服务（幻灯第 14 页）](../img/alicloudy/p14-xref201.png)

*图 6-4：统一接入、T+1、实时/准实时、融合分析与 API 服务。*

![核心价值与数仓分层（幻灯第 15 页）](../img/alicloudy/p15-xref209.png)

*图 6-5：降本增效 / 时效 / 全民分析 / 创新 + 分层引入。*

### 6.4 核心价值（官方主张，实施时需自行验证 ROI）

- **架构简化 / 降本**：一套存储、一套开发、多套引擎；材料称综合成本可显著下降（源 PDF 写「50%+」，以账单为准）。
- **时效**：T+1 → 分钟 / 秒级。
- **全民分析**：交互式查询减轻「提数」负担。
- **创新**：风控、营销、供应链等数据驱动场景。

### 6.5 默认数仓五层（DataWorks 数仓分层）

| 分层 | 英文 | 职责 |
|------|------|------|
| 数据引入层 | **ODS** | 接收原始数据，表结构与源系统一致，准备区 |
| 公共维度层 | **DIM** | 维度表 / 维度定义，统一分析口径，降低口径不一致风险 |
| 明细数据层 | **DWD** | 业务事件最细粒度事实；可宽表冗余维度，减少关联 |
| 汇总数据层 | **DWS** | 按分析主题构建公共粒度汇总指标 |
| 应用数据层 | **ADS** | 面向产品/报表的个性化指标输出 |

> 五层定义全文见幻灯第 16 页（与 **图 6-5** 衔接）；下图为 Data Studio 相关示意。

![Data Studio 界面示意（幻灯第 17 页）](../img/alicloudy/p17-xref218.png)

*图 6-6：Data Studio 开发界面。*

![Data Studio 能力补充（幻灯第 17 页）](../img/alicloudy/p17-xref220.png)

*图 6-7：Data Studio 与运维监控。*

---

## 7. Hologres

- **定位**：一站式 **实时数仓** — 海量实时写入/更新/分析。
- **协议**：标准 SQL（**兼容 PostgreSQL**）。
- **能力**：PB 级 OLAP / 即席分析 + **高并发低延迟 Serving**。
- **融合**：与 MaxCompute、Flink、DataWorks 深度集成，支撑 **离在线一体化**。

选型与表设计（分布键、分区、行列共存、AZ 容灾等）见 §9.3。

![Hologres 产品架构与融合（幻灯第 18 页）](../img/alicloudy/p18-xref224.png)

*图 7-1：实时写入/更新/分析，兼容 PG 协议，与 MaxCompute / Flink / DataWorks 集成。*

---

## 8. 与自建数据平台对照（阅读提示）

若同时阅读 wiki 内 [EnterpriseDataPlatform.md](./EnterpriseDataPlatform.md)：

| 维度 | 阿里云方案（本文） | 自建开源底座 |
|------|-------------------|--------------|
| 数仓引擎 | MaxCompute SaaS | Spark + Iceberg/Hudi 等 |
| 实时 | Hologres + Flink | Flink + OLAP 引擎自运维 |
| 治理开发 | DataWorks 全家桶 | Airflow/DolphinScheduler + 自研 Portal |
| landing | Landing Zone + RD | 私有云 / K8s + IAM 自建 |

---

## 9. 落地扩展清单（在原 PDF 能力之上的补充）

当前 PDF 偏 **能力与连接矩阵**；要形成可执行方案，建议沿下列维度补 **参数、SOP 与监控**（保留原 `AliCloudy.md` 提纲，仅压缩表述）。

### 9.1 底层基础与安全（Landing Zone 深化）

- **资源目录**：核心 / 日志 / 安全 / 生产·测试账号划分；跨账号 VPC 互通与共享服务（日志、审计集中账号）。
- **审计与合规**：ActionTrail、CloudConfig；KMS 静态加密（MaxCompute/OSS）；SDDP 分类分级。
- **RAM 深化**：企业 SSO、RAM Role + STS；MaxCompute Label 权限、Package 跨项目授权。
- **网络**：CEN 多 VPC、PrivateLink 访问云服务、NAT 与安全组基线。

### 9.2 数据集成与流转

- DataWorks 数据集成（DataX）限流、脏数据策略；SLS 日志源。
- 全量/增量策略（时间戳、binlog）、连接池、任务监控告警。
- Kafka/MQ 缓冲层；Flink Checkpoint/Savepoint 与状态后端。

### 9.3 引擎与存储细化

- **MaxCompute**：Quota 隔离与优先级；生命周期、冷热分层、小文件合并；SQL 倾斜与物化视图。
- **Hologres**：规格与读写分离；分布键/分区键；跨 AZ 与备份。
- **数据湖**：OSS 上 Delta/Hudi/Iceberg 与 MaxLake 关系；存储包与归档成本。

### 9.4 DataWorks 运维

- Git 集成、Code Review、发布审批；基线（Baseline）、告警（钉钉/Webhook）；独享调度/集成资源组。
- **DQC**：空值率、唯一性、行数波动与阻断发布。

### 9.5 治理与服务

- 数据地图血缘/影响分析；逻辑→物理建模流程。
- DataService + API Gateway 限流鉴权；FinOps（Tag 分摊、闲置回收）。

### 9.6 架构演进

- PAI-Designer/DSW 读 MC/Hologres；FeatureStore。
- 湖仓一体：外表、统一元数据、Storage API 性能验证。
- 同城双活 / 异地灾备（跨 Region 备份、跨地域调度）。

### 9.7 组织与规范

- 平台运维 / 开发 / 分析 / 治理角色与 **Data Owner**；内部 SQL/命名规范与新人接入手册。

---

## 10. 下一步建议

1. 以 **§2 网络 + §3 RAM + §4 Quota** 写一页「Atlas 生产基线检查表」。
2. 以 **§6.5 分层** 固定 ODS/DWD 命名与项目空间映射。
3. 从 **§9.2 集成监控** 和 **§9.4 DQC** 选 3 条规则做试点，再扩面。
4. 成本：打开 **Tag + 账单按 Project/Quota** 做首版 FinOps 看板。

---

