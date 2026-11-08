---
title: Metadata & Data Catalog：SaaS、云模块与开源二开怎么选
description: 围绕 Catalog、Lineage、Security、Discovery 与审批工作流，沉淀五维评估框架、开源深潜、Informatica/Collibra 与双云厂商模块对比
category: DataPlatform
date: 2026-11-08
readTime: 28 分钟
icon: 📋
featured: false
draft: false
---

| 项目 | 内容 |
|------|------|
| **主题** | 元数据、数据目录、数据服务与访问治理 |
| **评估方法** | 五维能力模型 + Research 表 ✅/⚠️/❌ |
| **典型栈** | 腾讯 WeData、阿里 DataWorks、Azure Purview / Unity Catalog |
| **开源备选** | DataHub、OpenMetadata、ODD、Apache Atlas 等 |

---

## 0. 文档要解决什么问题

| 问题 | 结论方向 |
|------|----------------|
| 买 SaaS、用云厂商模块，还是开源二开？ | 生产以**云厂商数据平台内置治理**为主（腾讯 WeData、阿里 DataWorks、Azure Purview / UC）；独立目录产品作**补充**或**跨云统一层** |
| Catalog / Lineage / Security / Discovery 如何评？ | 用 **五维能力模型**对标；POC 表格按同一维度打分 |
| 开源能否替代商业目录？ | 能覆盖 Catalog + Lineage + Discovery；**业务审批、行列级权限、等保/个保闭环** 多数需二开或外接 IAM |
| Databricks / 双云 | 关注 **Unity Catalog** 与数据平台连接器；**Apache Atlas** 默认不原生支持 Databricks（需 HMS / Connector / REST 等） |

---

## 1. 能力评估框架

**主干能力**：

| 维度 | 含义 | POC 时建议验收点 |
|------|------|------------------|
| **Data Catalog** | 元数据采集、业务/技术元数据、分类分级、搜索 | 能否自动采 DLC / MC / UC；搜索是否 **关键字 + 标签 + 域**；业务描述是否可协作编辑 |
| **Data Lineage** | 表/字段/任务级血缘、影响分析 | 集成任务 + ETL 是否 **自动出血缘**；是否支持 **导出 / API** |
| **Data Security** | 敏感识别、脱敏、策略、审计 | 内置规则（手机/身份证）；**动态脱敏** 是否生产可用；是否对接 CAM / RAM / AD |
| **Data Discovery** | 找数效率、推荐、Marketplace | 业务用户能否 **自助**；是否有 **历史/推荐**；是否支持 API 订阅 |
| **Approval Workflow** | 访问申请、多级审批、OA 集成 | 企微/钉钉/飞书；会签/或签；是否与 **表权限** 联动 |
| **Data Quality**（扩展） | 规则、监控、阻塞下游 | 表/字段级规则；是否绑 Pipeline；告警渠道 |
| **Data Asset / 资产运营** | 上架、目录树、健康度、API 化 | 与 WeData 资产目录盘点同类能力 |

**符号约定**（Research 表）：✅ 支持 / ❌ 不支持 / ⚠️ 部分支持。

---

## 2. 开源数据目录深潜

### 2.1 体验与二开总览

| 产品 | 体验（调研） | 二开难度 | Catalog | Lineage | Security | Discovery |
|------|--------------|----------|---------|---------|----------|-----------|
| **Apache Atlas** | 3/5，偏技术语言 | 4/5 难 | 动态分类（PII 等） | 可视化 + REST | GDPR/CCPA 倾向 | 基础/高级/关联搜索 |
| **DataHub** | 3.5/5 | 3.5/5 | 类型/Owner/Term/Tag/Domain | 实时端到端 | 角色限制，需增强 | 模糊搜索 + 推荐 |
| **OpenMetadata** | 4/5，树形清晰 | 3.5/5 | Assets/Domain/Tag/Tier | Metric lineage | 有基础实现 | 条件清晰，Tag 模糊弱 |
| **OpenDataDiscovery (ODD)** | 4/5，偏 C 端友好 | 3.5/5 | 筛选 + Table 视图 | 逐层打开 | Policy→Role | 全文/语义/上下文（需实操） |
| **Amundsen** | 偏技术化 | — | 有 | 有 | 弱 | 搜索为主 |
| **CKAN** | UI 体验差 | — | 弱 | 无 | 无 | 开放数据门户场景 |

**数据平台选型经验（开源）**

- 要 Hadoop 生态 + 可深度改 Java：**Apache Atlas + Ranger**（权限插件），但前端老旧（Backbone/jQuery），业务用户友好度低。
- 要现代 UI + 社区活跃 + LinkedIn 场景验证：**DataHub**（React + Neo4j + Kafka，GitHub ⭐ 最高档）。
- 要统一元数据平台 + Workflow + Data API（Sheet 矩阵唯一勾选）：**OpenMetadata**（Dropwizard，复杂度 5/5，功能全但需裁剪）。
- 要 Discovery/权限策略体验优先、架构相对轻：**ODD**（Spring Boot + PG，复杂度 3/5），社区较新。
- 仅要 SQL 血缘：**sqllineage** 作补充，非完整目录。

### 2.2 技术栈与二开参考

| 产品 | 后端 | 前端 | 复杂度 | 二开参考项目 |
|------|------|------|--------|--------------|
| **DataHub** | Spring Boot 3、Neo4j、ES、MySQL/PG、Flyway | React、Ant Design | 4 | simple-datahub |
| **OpenMetadata** | Dropwizard、ES、MySQL、Flyway、JWT | React、Ant Design | 5 | jiron-cloud |
| **ODD** | Spring Boot 3、jOOQ、PG、Flyway | React、Emotion/TanStack | 3 | ODD Spec + Provectus 等生态 |

**沉淀**：二开成本不在「装起来」，而在 **采集器对接数据平台现有链路**（WeData/DLC/ADF）、SSO/CAM、中英文业务术语、与**发布审批流程统一**。

### 2.3 开源能力矩阵

| 能力 | DataHub | OpenMetadata | Amundsen | ODD | CKAN | sqllineage | Ranger | Superset |
|------|---------|--------------|----------|-----|------|------------|--------|----------|
| Catalog | ✅ | ✅ | ✅ | ✅ | — | — | — | — |
| Lineage | ✅ | ✅ | ✅ | ✅ | — | ✅ | — | — |
| Security | ✅ | ✅ | ✅ | ✅ | — | — | ✅ | — |
| Discovery | ✅ | ✅ | ✅ | ✅ | — | — | — | — |
| Workflow | — | ✅ | — | — | — | — | — | — |
| Data API | — | ✅ | — | — | ✅ | — | — | — |
| SQL Query | ✅ | — | — | — | — | — | — | — |

**Demo**：[DataHub Demo](https://demo.datahubproject.io/) | [OpenMetadata Sandbox](https://sandbox.open-metadata.org/) | [ODD Demo](https://demo.opendatadiscovery.org/)

---

## 3. 商业 SaaS：Informatica vs Collibra

| 维度 | Informatica | Collibra |
|------|-------------|----------|
| **定位** | 数据集成 + 工程驱动治理 | 业务协作 + 数据民主化 |
| **用户** | 数据工程师、IT | Data Steward、合规、业务 |
| **Catalog** | 300+ 连接器，偏技术元数据 | 业务术语表为核心 |
| **Lineage** | 字段级，ETL/SQL 解析强（CLAIRE） | 表级为主，业务注释 |
| **Quality** | 图形化规则、流式监控 | 依赖外部工具，工作流触发 |
| **Security** | 模式 + ML 敏感发现 | 业务标签 + 可视化审批流 |
| **部署** | 混合 / 多云 | 全托管 SaaS |
| **业务视角** | 发现效率中，需 IT 协助 | 发现效率高，协作强 |

**经验**：跨国企业、已有 Informatica 集成链 → CLAIRE；强合规与业务 Steward 体系 → Collibra。数据平台 POC 阶段**均未作为默认生产目录**，因成本、国内延迟、与 WeData 重复建设。

---

## 4. 多产品横向能力

### 4.1 四大能力与 Databricks

| 产品 | Databricks | Catalog  | Lineage | Security | Discovery |
|------|------------|--------------|---------|----------|-----------|
| **Informatica** | 是 | 关键字 + 关联建议 | 端到端 + 影响分析 | BCR/GDPR | 质量指标 + 记分卡 |
| **Collibra** | 是 | 统一资产视图 | 自动沿袭 + 代码上下文 | 隐私自动执行 | Marketplace |
| **Apache Atlas** | 需 HMS/Connector/REST/NiFi 等 | 界面晦涩 | 可视化 | GDPR/CCPA | 名称/类型/Owner |
| **DataHub / OM / ODD** | 是 / 是 / Collector | 见 §2 | 可视化、实时（DH） | 角色/Policy | 多维过滤 + 推荐 |
| **腾讯云 WeData** | — | 关键字 + 标签 + 分级 | 可视化、端到端 | 敏感规则 + 分级 | 跨引擎检索 |
| **脉聪 / truedat / 亿信** | 脉聪是；truedat 否；亿信间接 | 国内 BI 化搜索、标签 | 字段级（脉聪强） | 等保、脱敏、角色流程 | 业务化搜索与推荐 |

### 4.2 云厂商治理模块

| 产品 | Permission | Catalog | Security | Lineage | Quality | 计费特点 |
|------|------------|---------|----------|---------|---------|----------|
| **Informatica** | AI 最小权限、字段/行级 | GPT 搜索、CLAIRE 标签 | 动态脱敏、合规报告 | ETL/API/DB 全链路 | AI 规则 | 订阅，贵 |
| **Collibra** | 多级并行审批 | 业务术语 + NL | 脱敏模板 | 业务血缘 | 质量看板 | 订阅 |
| **Azure Purview** | 单/多级审批、自动回收 | NL 搜索、治理域 | 加密 + 审计 + 合规报告 | 时序血缘 | 计划扫描 + 分数 | 按扫描 GB |
| **Unity Catalog** | 继承 + 行列级 | SQL 分析、常用查询 | 标记 + 审计 | Delta 血缘 | 外接工具 | 随 DBU |
| **Lake Formation** | IAM + 角色 | 关键字检索 | CloudTrail | Glue 血缘 | 需 Athena 等 | 按 Glue/Macie 用量 |
| **WeData** | RBAC + 列/行/资源 + 有效期 | 标签 + 表格浏览 | 分级分类 + 静/动脱敏 | 端到端 | 表/字段规则 + 阻塞下游 + 企微等告警 | 包年 + 资源组 |
| **阿里云 DataWorks** | RAM + 钉钉/飞书 | 跨 MC/OSS 搜索 | 等保、识别规则 | 任务血缘 | 自定义规则 | CU + 存储 |
| **数澜 DataFancy** | 钉钉/企微、会签/或签 | NL + 行业模板 | 等保、国密 | 自动+手动血缘 | 批量清洗为主 | 订阅/本地 |

---

## 5. 访问审批与数据服务专题

调研强调 **Discovery 与 Approval 是一体两面**：找数之后必须 **可审计地申请权限**。

| 产品 | 检索方式 | 审批亮点 | 数据平台相关 |
|------|----------|----------|--------------|
| **Informatica CLAIRE** | NLQ | 多级链 + AI 风险加签 | 能力标杆，成本高 |
| **Collibra** | 标签 + 全文 | 拖拽审批、条件分支 | 业务 Steward 场景 |
| **DataWorks** | SQL 语法搜索 | RAM 表单 + 钉钉/飞书 | 与 [AliCloudy.md](./AliCloudy.md) 国内 OA 一致 |
| **WeData** | 关键字 + 预览 | 企微模板、API 订阅审批 | 与腾讯云栈一致；复杂路由需二开 |
| **Lake Formation** | Glue Catalog | Lambda 自定义 | AWS 专用 |
| **Purview** | 全局搜索 | Power Automate | Azure 栈 |

**沉淀**：若主栈在**腾讯**，优先把 WeData **元数据 + 资产目录 + 权限申请**做满；**Azure** 侧用 **Purview + UC** 覆盖 ADF/Databricks，避免再引入第三套 SaaS 目录。

---

## 6. 数据平台推荐落地架构

```text
                         ┌────────────────────────────────────┐
                         │     业务用户：检索 / 申请 / API 订阅     │
                         └─────────────────┬──────────────────┘
                                           │
              ┌─────────────────────────────┼─────────────────────────────┐
              │                             │                             │
              ▼                             ▼                             ▼
       ┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
       │      腾讯 WeData      │     │    Azure Purview      │     │     (可选) 统一层      │
       │      元数据+资产      │     │    + Unity Catalog    │     │      DataHub/OM      │
       │       目录+质量       │     │                       │     │       跨云搜索        │
       └──────────┬───────────┘     └──────────┬───────────┘     └──────────┬───────────┘
                  │                            │                            │
                  ▼                            ▼                            ▼
         DLC / COS / WeData API       ADF / Databricks / ADLS         Federated 元数据聚合
```

| 层级 | 建议 | 原因 |
|------|------|------|
| **L1 生产** | WeData 功能说明 9 全流程；Azure Purview 扫描 + UC 权限 | 与现有 POC 建设一致，无额外采购 |
| **L2 增强** | 质量规则阻塞下游、资产 **上架** 再开放 API | 0311 国内产品共性；WeData 已支持强弱规则 |
| **L3 可选** | 开源 DataHub 作跨云 **元数据聚合**（只读 Federated） | 社区成熟；二开 3.5/5；不替代 WeData 审批 |
| **不推荐默认** | 单独上 Informatica/Collibra 全栈 SaaS | 成本高、与双云重复 |
| **Databricks** | 以 Unity Catalog 为权威；Atlas 等补充时需 Connector | 0311 明确非原生对接路径 |

---

## 7. 选型 Checklist（POC → 生产）

1. 五维能力是否覆盖：**Catalog / Lineage / Security / Discovery / Workflow**
2. 与 DataWorks 或 WeData **发布流** 是否一体（采集任务是否仅管理员、是否绑 pipeline）
3. **业务目录树** 是否与 `{DOMAIN}`、部门缩写一致
4. **敏感分级** 是否满足 GB/T 35273 / 个保 / 等保审计口径
5. **审批** 是否对接企微/钉钉/飞书或 ITSM
6. **血缘** 是否到集成 + ETL **任务级**，能否导出影响分析
7. **API 数据服务** 是否与目录 **同一套元数据**（避免 API 市场与资产地图不一致）
8. Databricks / UC 若启用，是否验证 HMS / Connector 路径
9. 开源二开是否评估 **Neo4j/ES 运维成本** 与 SSO

---

## 8. 国内产品与参考链接

| 产品 | 特点摘要 | 链接 |
|------|----------|------|
| **数澜 DataFancy** | NL 搜索、行业模板、钉钉/企微审批、ETL 级血缘 | 数澜数据地图（产品官网） |
| **truedat** | 自动化发现、语义关联 | truedat catalog 文档 |
| **亿信华辰** | 等保、动态脱敏 | 数据治理产品线 |
| **脉聪** | 字段级血缘、标签管理（表格评价强） | 见 0311 行内描述 |
| **明源云** | 与地产数据场景相关 | 0311 并列项 |

---

## 9. 与现有项目文档映射

| 能力 | 腾讯 | 阿里 | Azure / 自建 |
|------|------|------|----------------|
| 元数据采集 / 血缘 / 质量 / 资产目录 | WeData（见架构设计对照表） | DataWorks 数据地图（[AliCloudy.md](./AliCloudy.md) 治理链） | [AzureDataPlatform.md](./AzureDataPlatform.md) Purview、UC |
| API + 网关 | WeData 数据服务 | AliCloud 功能说明 API 网关 | Power BI Embedded 等 |
| 开源目录 + 门户 | 可选 DataHub 聚合 | 可选 OpenMetadata | [EnterpriseDataPlatform.md](./EnterpriseDataPlatform.md) DataHub / Portal |

---

**阅读延伸**：[DataPlatformArchitectureDesign.md](./DataPlatformArchitectureDesign.md)（云上 One Data 蓝图）、[EnterpriseDataPlatform2.md](./EnterpriseDataPlatform2.md)（WeData 与 DataHub 并存策略）。
