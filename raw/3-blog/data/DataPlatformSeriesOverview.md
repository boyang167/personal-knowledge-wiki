---
title: 数据平台：从架构演进到多云与自建落地
description: 在架构蓝图、腾讯云、阿里云、Azure 与开源自建之间建立统一认知
category: DataPlatform
date: 2026-11-08
readTime: 22 分钟
icon: ⌁
featured: false
draft: false
---

| 项目 | 内容 |
|------|------|
| **覆盖形态** | 理论蓝图 · 元数据选型 · 自建 HLD · 阿里云 · 腾讯云 · Azure |
| **统一主张** | One Data, One Service · 湖仓一体 · 元数据驱动 · 分层入湖 |

---

## 0. 这套文档在讲什么

是一套**可互相对照**的企业数据平台知识库：先从批流架构与一套数据、一种服务的顶层蓝图出发，再分别沉淀**阿里云、腾讯云、Azure** 上的 POC 与落地 checklist，并给出**开源组件 + 自研门户**的完整 HLD；最后用**数据目录与治理选型**把多云与自建串成一张能力地图。

如果你只关心今天该先装什么，可以跳到 [推荐阅读路径](#5-推荐阅读路径)；如果要找某朵云与自建之间的 SKU 映射，直接看 [ 统一能力对照](#4-统一能力对照)。

### 0.1 术语：HLD / LLD / POC / SKU

| 缩写 | 英文全称 | 中文习惯叫法 | 写什么、不写什么 |
|------|----------|--------------|------------------|
| **HLD** | High-Level Design | **高层设计** / 概要设计 | **写**：建设目标与边界、分层与子系统划分、主要数据流、关键技术选型、分阶段路线与验收方向。**不写**（留给 LLD / 实施文档）：安装参数、Namespace 清单逐条、表字段、接口 JSON Schema、变更单级操作步骤。 |
| **LLD** | Low-Level Design | **详细设计** | 组件部署拓扑、资源配置、库表与 API 契约、任务依赖明细、告警阈值等可交给开发与运维直接实施的细节。本目录**未单独成篇**。 |
| **POC** | Proof of Concept | **概念验证** / 试点 | 在有限环境验证选型与链路是否可行；各云长文与 [DataCatalogMetadataGovernance.md](./DataCatalogMetadataGovernance.md) 含 POC 用例与 Checklist。 |
| **SKU** | Stock Keeping Unit | 原义**库存单位**；在云/采购语境常指**可单独下单、计费的产品或规格** | 本文 [统一能力对照](#4-统一能力对照) 按**能力域**对齐（如「批集成」「湖仓计算」），**不是**各云控制台里某一个 SKU 与另一个 SKU 的逐条等价表；选型时应对能力，再落到各家具体产品名与计费项。 |

**本目录与 HLD 的对应关系**

| 文档 | 文档类型（读者预期） |
|------|----------------------|
| [EnterpriseDataPlatform2.md](./EnterpriseDataPlatform2.md) | **正式 HLD（V2.0）**：八层架构、治理域、门户、四阶段与 POC 验收，篇幅最长。 |
| [EnterpriseDataPlatform.md](./EnterpriseDataPlatform.md) | **V1 架构方案 / HLD 精要**：与 V2 同主栈，章节更短，适合评审初稿或招标附件摘要。 |
| [DataPlatformArchitectureDesign.md](./DataPlatformArchitectureDesign.md) | **架构蓝图 / 方法论文**：偏演进与 One Data 能力域，非项目实施 HLD。 |
| AliCloudy / TencentWeDataPlatform / AzureDataPlatform | **云厂商落地实践笔记**：含 POC 顺序与 checklist，介于 HLD 与运维手册之间。 |

---

## 1. 文档地图与彼此关系

```text
                    ┌─────────────────────────────────────┐
                    │ DataPlatformArchitectureDesign      │
                    │  Lambda/Kappa/湖仓 · One Data 蓝图   │
                    └──────────────┬──────────────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         │                         │                         │
         ▼                         ▼                         ▼
┌─────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│ Enterprise V1   │    │ DataCatalog 治理选型 │    │ Enterprise V2 (HLD) │
│ 七层逻辑架构    │◄──►│ 五维评估 · 开源/SaaS │◄──►│ 八层 · Portal · 四阶段 │
│ 组件清单 · 三期 │    │ 与三云治理模块映射   │    │ POC 验收 · 最终栈    │
└────────┬────────┘    └──────────┬──────────┘    └──────────┬──────────┘
         │                        │                          │
         └────────────────────────┼──────────────────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
       ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
       │ AliCloudy    │   │ Tencent      │   │ Azure        │
       │ DataWorks+MC │   │ WeData+DLC   │   │ UC+ADB+ADF   │
       │ +Hologres    │   │ +Oceanus     │   │ +Purview     │
       └──────────────┘   └──────────────┘   └──────────────┘
```

| 序号 | 文件 | 标题（frontmatter） | 角色 |
|------|------|---------------------|------|
| 1 | [DataPlatformArchitectureDesign.md](./DataPlatformArchitectureDesign.md) | 大数据平台架构演进与云上 DataPlatform 设计 | **理论入口**：Lambda / Kappa / Lakehouse、存储格式、OLTP vs OLAP、One Data One Service 能力域、Azure 与腾讯云产品节选对照 |
| 2 | [EnterpriseDataPlatform.md](./EnterpriseDataPlatform.md) | 自建企业级数据平台架构设计方案 | **自建 V1**：七层逻辑架构、SeaTunnel / Spark / Flink / Iceberg / DolphinScheduler、治理与 Portal、三期实施与最终选型表 |
| 3 | [EnterpriseDataPlatform2.md](./EnterpriseDataPlatform2.md) | 自建企业级数据平台总体架构设计 2 | **自建 V2（HLD）**：在 V1 上扩展治理域（审批、发现、资产运营）、DataHub/OpenMetadata 决策、统一门户菜单、四阶段路线图与 POC 验收标准 |
| 4 | [DataCatalogMetadataGovernance.md](./DataCatalogMetadataGovernance.md) | Metadata & Data Catalog 选型 | **治理横切**：Catalog / Lineage / Security / Discovery / Workflow 五维评估；Informatica / Collibra / 开源矩阵；WeData、DataWorks、Purview / UC 生产建议 |
| 5 | [AliCloudy.md](./AliCloudy.md) | 阿里云湖仓数据平台搭建 | **阿里云实战**：Landing Zone、MaxCompute、DataWorks 一站式、Hologres 实时 Serving、Flink/DataHub、POC 用例矩阵与腾讯对照 |
| 6 | [TencentWeDataPlatform.md](./TencentWeDataPlatform.md) | Tencent WeData / DLC 数据平台搭建实践 | **腾讯云实战**：Landing Zone → KMS → CAM 权限 → DLC 命名分层 → WeData 集成发布 → Oceanus / CKafka → API 网关 → COS / SCF→PG 入湖 → 数据资产闭环 |
| 7 | [AzureDataPlatform.md](./AzureDataPlatform.md) | Azure 中国区数据平台搭建实践 | **Azure 实战**：Unity Catalog 公司级元数据、Databricks + ADLS、ADF 批流与自承载 IR、Event Hubs 实时、Purview、混合网 DNS，含四云能力对照表 |

**版本关系说明**：`EnterpriseDataPlatform.md` 与 `EnterpriseDataPlatform2.md` 是同一建设思路的 **V1 精要版** 与 **V2 完整 HLD**；V2 在治理、门户与实施阶段上更细，技术主栈（Iceberg + Spark + Flink + SeaTunnel + DolphinScheduler + DataHub）与 V1 一致。三篇云实践文档在文内已互相引用，并与架构演进、治理选型文档交叉链接。

---

## 2. 跨文档共识（读任何一篇都应带走的框架）

### 2.1 数据架构演进

[DataPlatformArchitectureDesign.md](./DataPlatformArchitectureDesign.md) 将企业常见路线归纳为三条主线，并说明湖仓一体不是消灭 Lambda/Kappa，而是用**统一存储、表格式与元数据**降低双链路维护成本：

- **Lambda**：批层 + 速度层 + 服务层合并，一致性与重复建设是典型痛点。
- **Kappa**：以 Kafka 为中心用流统一计算，长期存储与大规模 OLAP、血缘统一是短板。
- **Lakehouse**：对象存储 + Delta / Hudi / **Iceberg** + OLAP 引擎，支撑分层分析、增量与 upsert 类能力。

入湖与主题层实践上，各篇一致倾向：**列式（Parquet/ORC）+ 表格式** 承载分析；边界接入保留 JSON/CSV 并在治理层约束清洗；业务 **OLTP 库为真相源**，经集成进入 **ODS → DIM → DWD → DWS → ADS**（或 Azure 侧的 Onboarding → ODS → DWD）。

### 2.2 One Data, One Service

顶层蓝图在架构演进篇中展开为**1 个技术底座 + 1 个门户 + 3 个平台 + 4 个中心 + 3 个保障体系**：

| 能力域 | 含义（摘要） |
|--------|----------------|
| **数据治理平台** | 元数据、标准、质量、安全、血缘 |
| **数据共享开发平台** | 集成、开发、调度、发布 |
| **数据分析平台** | SQL/Notebook、OLAP、BI、API |
| **门户** | 统一找数、申请、订阅与运营入口 |

自建两篇把上述能力落到 **Kubernetes 控制面 + 自研 Unified Data Portal**；三云文档则分别由 **DataWorks、WeData、Databricks+Purview/UC** 承担「开发+治理」主战场，差异在托管深度与混合网集成方式。

### 2.3 Landing Zone 先于数据产品

阿里云、腾讯云、Azure 三篇都强调：**账号/网络/合规/密钥基线（Landing Zone）** 应先于 WeData、DLC、MaxCompute、Unity Catalog 等产品开通。腾讯云实践额外把 **KMS、CAM 三层权限、集成专项项目命名** 列为「权限先于开发」的硬前置；Azure 则把 **Metastore / Access Connector 存储 RBAC** 放在实施 checklist 前几项。

### 2.4 治理与目录：生产以云内置为主，开源作跨云聚合

[DataCatalogMetadataGovernance.md](./DataCatalogMetadataGovernance.md) 的结论是：

- **生产默认**：主栈在腾讯 → **WeData 元数据 + 资产目录 + 质量 + 权限申请**；在 Azure → **Purview + Unity Catalog**；在阿里 → **DataWorks 数据地图 + RAM**。
- **可选增强**：**DataHub / OpenMetadata** 作跨云 **Federated 元数据聚合**（只读），不替代各云审批与权威权限。
- **不推荐 POC 默认全栈上** Informatica / Collibra（成本高、与国内数据平台能力重叠）。

该结论与自建 V2 中「**各环境保留原生权威系统，门户只做聚合**」原则一致。

### 2.5 自建技术主栈（与云能力可对照）

| 类别 | 推荐（V1/V2 一致） | 云侧常见映射 |
|------|-------------------|--------------|
| 集成 | SeaTunnel | DataWorks 集成 / WeData 集成 / ADF Copy |
| 调度 | DolphinScheduler | DataWorks 调度 / WeData 工作流 / ADF |
| 批计算 | Spark | MaxCompute / DLC Spark / Databricks |
| 流计算 | Flink（Dinky 运维） | Flink+DataHub / Oceanus / Event Hubs+Spark 流 |
| 消息 | Kafka | DataHub / CKafka / Event Hubs |
| 湖表 | Iceberg + 对象存储 | OSS/COS/ADLS + 各云表格式 |
| OLAP | Doris / StarRocks | Hologres / DLC Presto / Serving 层 |
| 元数据 | DataHub / OpenMetadata | WeData / DataWorks 地图 / Purview+UC |
| 门户 | 自研 Unified Portal | 无等价单机产品，需 BI/API/审批聚合 |

---

## 3. 分篇精要

### 3.1 架构演进与云上蓝图

**[DataPlatformArchitectureDesign.md](./DataPlatformArchitectureDesign.md)**（约 18 分钟）

- 用图示对比 Lambda、Kappa、Lakehouse 及企业分层示例。
- 梳理表格式、Parquet/Avro/JSON 的使用边界与 OLTP/OLAP 差异表。
- 给出 One Data One Service 总览与 Azure / 腾讯云**节选**产品对照，适合**立项、汇报、对齐术语**。

### 3.2 自建企业平台 V1 / V2

**[EnterpriseDataPlatform.md](./EnterpriseDataPlatform.md)**（约 10 分钟）

- 七层逻辑架构 + 推荐数据流 ASCII 图（SeaTunnel / Flink / Iceberg / Doris / Portal）。
- 覆盖 DataOps、血缘、质量、权限、Portal 模块、K8s 命名空间与 **Phase 1–3** 实施。
- **最终选型清单**（P0/P1/P2）适合作为 IDC/私有云招标或 POC 组件表。

**[EnterpriseDataPlatform2.md](./EnterpriseDataPlatform2.md)**（约 50 分钟）

- 八层架构、完整治理子域（审批、发现、资产运营、安全合规）。
- **Data Catalog 产品比较**、多 Catalog + Unified Portal 策略、Portal 菜单建议与自研边界。
- **四阶段路线图**、计算/治理/开源三类 POC 验收标准、风险表与架构决策总结。

### 3.3 元数据与数据目录选型

**[DataCatalogMetadataGovernance.md](./DataCatalogMetadataGovernance.md)**（约 28 分钟）

- **五维能力模型** + ✅/⚠️/❌ 符号，用于 POC 打分。
- 开源深潜：Atlas、DataHub、OpenMetadata、ODD 的体验、二开成本与能力矩阵。
- Informatica vs Collibra、Databricks/Unity Catalog 注意事项、访问审批与数据服务专题。
- **推荐落地架构图**（WeData | Purview+UC | 可选 DataHub）与 **POC→生产 Checklist**（9 条）。

### 3.4 阿里云湖仓中台

**[AliCloudy.md](./AliCloudy.md)**（约 48 分钟）

- 主线：**Landing Zone → RAM → MaxCompute（离线）+ DataWorks（开发治理）+ Hologres（实时/Serving）+ Flink/DataHub（流）**。
- 专章节：网络专线/VPN、MaxLake 场景、DataWorks 五层数仓、HTTP API 入仓、OSS 非结构化、LandZone 云/数据双着陆区。
- **POC 用例矩阵**（批处理 CDP、实时同步、批流混合等）、与腾讯云方案对照、Hologres vs ClickHouse/Doris 附录。

### 3.5 腾讯云 WeData / DLC

**[TencentWeDataPlatform.md](./TencentWeDataPlatform.md)**（约 55 分钟）

- **平台搭建总览表**：从 Landing Zone、KMS、CAM、DLC 引擎到治理与服务、SCF→云 PG→DLC 补数链路。
- 九大「功能说明」：命名规范、Oceanus 流、Kong/TKE 网关、KMS、Landing Zone、Serverless 采集、COS 非结构化、Notebook、**数据资产（功能说明 9）**。
- 附录 **端到端 MVP** 路径，适合按 checklist 逐项验收。

### 3.6 Azure 中国区

**[AzureDataPlatform.md](./AzureDataPlatform.md)**（约 42 分钟）

- 目标链路：**IDC/业务库 → ADF（SHIR）批入湖 / Debezium→Event Hubs 实时 → Databricks 分层 → Power BI**。
- 强调实施顺序：**先公司级 Unity Catalog，再项目级工作区**；UC 三层命名空间与 Onboarding/ODS 分工。
- 混合云专题：Private Endpoint、DNS 转发、内网库连通排障。
- **§14 四云能力对照表**（开发治理、离线计算、实时、集成、元数据、混合网、BI、ML）— 本总览 §4 在此基础上做索引。

---

## 4. 统一能力对照

下表整合 [AzureDataPlatform.md ](./AzureDataPlatform.md)、三云正文与自建文档，按**能力域**映射（非 SKU 一一对应）：

| 能力域 | 自建（开源+门户） | 阿里云 | 腾讯云 | Azure |
|--------|-------------------|--------|--------|-------|
| 开发 + 治理一站式 | OpenMetadata/DataHub + 自研门户 | **DataWorks** | **WeData** | Databricks + UC；**Purview** 目录 |
| 离线 / 湖仓计算 | Spark on K8s | **MaxCompute** | **DLC** | **Databricks** / Delta |
| 实时分析 / Serving | Doris / StarRocks | **Hologres** | DLC Presto + 下游同步 | Serving 层 + BI |
| 流计算 | Flink + Kafka | Flink + **DataHub** | **Oceanus** + CKafka | Event Hubs + Spark 流 |
| 批集成调度 | SeaTunnel + DolphinScheduler | DataWorks 集成与调度 | WeData 集成与工作流 | **ADF** + 自承载 IR |
| 对象存储 | MinIO/COS + Iceberg | **OSS** | **COS** | **ADLS Gen2** |
| 元数据与权限 | DataHub + Ranger/SSO | DataWorks 地图 + RAM | WeData 治理 + CAM | **UC** + Purview |
| 混合网 / 内网源 | 自管防火墙与 CDC | 专线/VPN + Landing Zone | VPC + 专线/Private Link | SHIR + PE + DNS |
| 数据服务 / API | 自研 API 网关层 | API 网关 + DataWorks 服务 | WeData 数据服务 + Kong | Embedded / 语义层 |
| BI | Superset 等 | Quick BI 等 | 第三方/自有 BI | **Power BI** |

**选型提示**

- 已深度上**阿里**且要走湖仓+实时 Serving → 优先读 [AliCloudy.md](./AliCloudy.md)，Hologres 章节与 POC 矩阵是验收主干。
- 已上**腾讯**或以 WeData 为控制面 → [TencentWeDataPlatform.md](./TencentWeDataPlatform.md) 的 **0 节总览 + 功能说明 9（资产）** 应最先走通。
- **微软栈 + 混合 IDC** → [AzureDataPlatform.md](./AzureDataPlatform.md) 的网络与 UC 顺序不可跳过。
- **多云或必须留在机房** → 以 [EnterpriseDataPlatform2.md](./EnterpriseDataPlatform2.md) 为实施主文档，用 [DataCatalogMetadataGovernance.md](./DataCatalogMetadataGovernance.md) 决定目录是「云内置满配」还是「加一层 DataHub 聚合」。

---

## 5. 推荐阅读路径

### 5.1 数据架构师 / 平台 Owner（首次通读）

1. [DataPlatformArchitectureDesign.md](./DataPlatformArchitectureDesign.md) — 统一语言与蓝图  
2. 按主云选一篇：**AliCloudy** / **TencentWeDataPlatform** / **AzureDataPlatform**  
3. [DataCatalogMetadataGovernance.md](./DataCatalogMetadataGovernance.md) — 治理与目录 POC 维度  
4. 若存在自建或跨云诉求：[EnterpriseDataPlatform2.md](./EnterpriseDataPlatform2.md)

### 5.2 开发 / 集成工程师

- **腾讯栈**：[TencentWeDataPlatform.md](./TencentWeDataPlatform.md) §0、DB/表命名、Pipeline 生命周期、集成类型  
- **阿里栈**：[AliCloudy.md](./AliCloudy.md) §6 DataWorks、§POC 批流用例、命名与 HTTP 入仓  
- **Azure 栈**：[AzureDataPlatform.md](./AzureDataPlatform.md) §6 ADF、§7 批链路、§8–9 实时与 CDC  
- **自建栈**：[EnterpriseDataPlatform.md](./EnterpriseDataPlatform.md) §3 组件、§5 调度发布

### 5.3 数据治理 / 安全 / 合规

- 主线：[DataCatalogMetadataGovernance.md](./DataCatalogMetadataGovernance.md) 全文 + Checklist  
- 落地对照：腾讯 **功能说明 9**、阿里 DataWorks 数据地图、Azure Purview/UC 章节  
- 自建扩展：[EnterpriseDataPlatform2.md](./EnterpriseDataPlatform2.md) §6 治理架构、§7 Catalog 选型

### 5.4 立项汇报（30 分钟摘录）

| 页/节 | 来源 | 用途 |
|-------|------|------|
| 架构短板与湖仓回应 | DataPlatformArchitectureDesign §2.5 | 为什么上湖仓 |
| One Data 能力域图 | DataPlatformArchitectureDesign §5 | 目标态 |
| 四云对照表 | AzureDataPlatform §14 或本文 §4 | 多云策略 |
| 推荐治理架构 | DataCatalogMetadataGovernance §6 | 目录与审批 |
| 最终开源栈一句 | EnterpriseDataPlatform §14 | 自建结论 |

---

## 6. 实施与验收：跨文档 Checklist 摘要

各云文档均带有可勾选 checklist，以下为**全集共性**（细节以分篇为准）：

| 域 | 共性检查项 |
|----|------------|
| **基座** | Landing Zone（账号/网络/合规）；密钥进 KMS/Key Vault，禁止明文进 Git |
| **权限** | 先于大规模开发；云 IAM（RAM/CAM/AD）与数据引擎角色分层 |
| **命名与分层** | ODS/DWD/DWS（或 Onboarding/ODS）与库表命名规范评审归档 |
| **集成** | 批/流分通道监控；失败率、延迟、积压各有 Owner |
| **治理** | 元数据自动采集；血缘到**任务级**；质量规则是否阻塞下游 |
| **资产与服务** | 资产上架后再开放 API；目录与 API 市场共用一套元数据 |
| **混合网** | 专线/VPN/PE + DNS 文档化；IR/网关探活与变更单 |
| **消费** | BI 刷新 SLA 与 ADS/DWD 产出对齐 |

腾讯云 [附录 MVP](./TencentWeDataPlatform.md)、Azure [§15 checklist](./AzureDataPlatform.md)、阿里 [LandZone 上线前 Checklist](./AliCloudy.md)、治理篇 [§7](./DataCatalogMetadataGovernance.md)、自建 V2 [§14 POC](./EnterpriseDataPlatform2.md) 可拼接为完整验收包。

---

## 7. 小结

本目录七篇文章构成一条完整链路：**先用架构演进与 One Data 蓝图定目标态，再用三云实践验证托管路线的落地顺序与踩坑，用治理选型文档统一 Catalog/审批/安全评估语言，最后用自建 HLD 描述在机房或多云场景下用开源栈复现同等能力域的路径**。



---

## 8. 快速链接索引

| 主题 | 跳转 |
|------|------|
| Lambda / Kappa / Lakehouse | [DataPlatformArchitectureDesign.md](./DataPlatformArchitectureDesign.md) |
| 自建组件清单与三期计划 | [EnterpriseDataPlatform.md](./EnterpriseDataPlatform.md) |
| 门户、审批、四阶段路线 | [EnterpriseDataPlatform2.md](./EnterpriseDataPlatform2.md) |
| 开源目录 vs 三云治理 | [DataCatalogMetadataGovernance.md](./DataCatalogMetadataGovernance.md) |
| MaxCompute + DataWorks + Hologres | [AliCloudy.md](./AliCloudy.md) |
| WeData + DLC + 数据资产 | [TencentWeDataPlatform.md](./TencentWeDataPlatform.md) |
| UC + ADF + 混合网 | [AzureDataPlatform.md](./AzureDataPlatform.md) |
