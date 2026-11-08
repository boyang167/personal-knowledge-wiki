---
title: Azure 中国区数据平台搭建实践
description: 从订阅与 Unity Catalog 到 Databricks、ADF 混合集成、Event Hubs 实时链路与 Power BI Embedded
category: DataPlatform
date: 2026-11-08
readTime: 42 分钟
icon: ☁
featured: false
draft: false
---

| 项目 | 内容 |
|------|------|
| **云环境** | Azure 中国区（世纪互联） |
| **核心产品** | Unity Catalog、Databricks、ADF、Event Hubs、Power BI、Purview |
| **集成形态** | 云上湖仓 + 本地 IDC 数据源（VNet / 自承载 IR / Private DNS） |
---

## 1. 你要建成什么样

在 Azure 上搭数据平台，目标通常不是买齐 PaaS，而是落成一条可运维的链路：

```text
IDC / 业务库（MySQL、PG 等）
        │
        ├─ 批处理 T+1 ──► ADF（自承载 IR）──► Onboarding / Raw（ADLS Gen2）
        │                      │
        │                      └─► Databricks Notebook / Job ──► ODS ──► DWD ──► DWS
        │
        └─ 实时 CDC ──► Kafka Connect + Debezium ──► Event Hubs ──► Spark Streaming ──► 湖仓卷
                                                                                │
                                                                                ▼
                                                         Power BI（Embedded + SaaS）/ API
```

- 宏观编排常在 **Azure Data Factory（ADF）**
- 微观计算与 SQL/Notebook 在 **Azure Databricks（ADB）**
- 公司级元数据与权限在 **Unity Catalog（UC）**
- 入湖对象在 **ADLS Gen2**（启用分层命名空间）

参考目标架构：

![Azure 数据平台参考架构](/blog-media/img/azure-platform/azure-ref-architecture.png)

*图 1-1：批流入湖、分层建模与 Power BI 消费*

---

## 2. 落地顺序：先公司级，再项目级

推荐按权限半径，由大到小实施，避免后期迁 Catalog 或反复开 RBAC。

| 阶段 | 做什么 | 典型产物 |
|------|--------|----------|
| 0 | 订阅、资源组、命名规范 | `rg-data-platform-{env}`、`chinanorth3` 等 |
| 1 | **Unity Catalog**（公司级元数据） | 存储账号 + Databricks Access Connector + Metastore |
| 2 | **Databricks 工作区**（项目级计算） | 工作区存储、`raw` / `catalog` 容器 |
| 3 | **UC 三层命名空间** | Catalog → Schema（ODS、Onboarding）→ Table / Volume |
| 4 | **ADF + 自承载 IR** | 连内网库、Copy 到 Onboarding |
| 5 | **实时** | Event Hubs、Spark 结构化流、Checkpoint |
| 6 | **消费与治理** | Power BI Embedded、Purview 扫描 |

---

## 3. 订阅、资源组与区域

1. 创建或选定**订阅**（生产 / 非生产分开）。
2. 创建**资源组**，区域示例：**China North 3**（按合规与延迟选型）。
3. 统一标签：`env`、`cost-center`、`owner`，便于 Purview 与成本分账。

后续所有数据资产（存储、ADB、ADF、Event Hubs）建议落在同一资源组或数据平台资源组树下，RBAC 按组授予，而不是按单个资源点选。

---

## 4. Unity Catalog：公司级元数据底座

Unity Catalog 管的是**全公司**的元数据、权限与审计，与工作区内的项目 Catalog概念不同：前者是 **Metastore + 账户级治理**，后者是在 UC 里划分的业务域。

### 4.1 自建 UC 的两块前置（也可由向导自动创建）

**（1）存储账号（供 UC Metastore 使用）**

- 创建存储账号，**启用分层命名空间（Hierarchical namespace）**——这是 ADLS Gen2 能力，Databricks 外部表/卷依赖它。
- 创建容器，例如 `databricks-unitycatalog`（名称仅作示例）。
- 在「终结点」页记录 **表服务 / DFS（Data Lake）** 的 URL，创建 Metastore 时会引用。

![存储账号终结点（脱敏）](/blog-media/img/azure-platform/1740033860976.png)

*图 4-1：分层命名空间与 DFS 终结点*

**（2）Azure Databricks Access Connector**

- 用途：用**托管标识**代替长期密钥，让 Databricks 安全访问存储与其它 Azure 服务。
- 创建后复制 **资源 ID**（格式示例）：

```text
/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RG>/providers/Microsoft.Databricks/accessConnectors/<CONNECTOR_NAME>
```

### 4.2 Metastore 与权限

- 在 Databricks **账户控制台**（中国区：`https://accounts.databricks.azure.cn/login`）创建或绑定 Metastore。
- UC 自动创建时可能带有专用 connector 资源组，**务必把 Catalog 使用的存储账号授予 connector 的托管标识「存储 Blob 数据参与者」**，否则外部位置/卷无法读写。

![为 Access Connector 分配存储 Blob 数据参与者](/blog-media/img/azure-platform/1740216271226.png)

*图 4-2：角色分配示意（截图已脱敏）*

**账户管理员**：在账户控制台为运维账号分配 `account.admin`（或最小权限组合），才能完成 Metastore 与账户级 UC 配置。

![账户角色分配](/blog-media/img/azure-platform/1740032273657.png)

![账户管理员配置](/blog-media/img/azure-platform/1740034031927.png)

中国区注意：**Unity Catalog Metastore 在国内实例可能存在数量限制**（实践上常规划为**一个公司级 Metastore**），再在其下用 Catalog 划分业务线。

---

## 5. Databricks 工作区与存储规划

### 5.1 工作区级存储

1. 再建一个（或复用）存储账号，放**项目级**数据湖文件。
2. 典型容器：
   - **`raw`**：客户/业务源系统最原始落地，未经规范化。
   - **`databricks-data`**（或 `catalog`）：经 ADF / Notebook 处理后的 ODS、DWD 等文件。

3. 创建工作区时选择 **Runtime 14.x LTS** 等长期支持版 Spark，减少作业兼容成本。

### 5.2 UC 三层命名空间

| 层级 | 含义 | 示例 |
|------|------|------|
| **Catalog** | 业务域 / 产品线 | `demo_catalog` |
| **Schema** | 分层或主题 | `onboarding`、`ods`、`dwd` |
| **Table / Volume** | 表或托管/外部卷 | Delta 表、`/Volumes/.../raw` |

创建 Catalog 通常需要 **Metastore Admin 或 Catalog Owner**；不指定存储根时，可能落在账户默认存储下——生产环境建议**显式绑定外部位置**。

![创建 Catalog 与 Schema（ODS / Onboarding）](/blog-media/img/azure-platform/1740208631102.png)

**外部位置（External Location）**：把 ADLS 路径注册到 UC，创建 **Volume** 时选择「存储位置」。

![注册外部位置](/blog-media/img/azure-platform/1740208923772.png)

**Schema**：例如 ODS 层可直接挂在 Catalog 下，不必再套一层多余目录。

![创建 Schema](/blog-media/img/azure-platform/1740209921454.png)

在 UC 界面集中管理授予：**USE CATALOG / USE SCHEMA / SELECT** 等，避免只在存储层开 RBAC 而 UC 层未授权。

![Unity Catalog 权限](/blog-media/img/azure-platform/1739761331173.png)

![权限细化](/blog-media/img/azure-platform/1739761422594.png)

---

## 6. Azure Data Factory：批集成与混合网络

### 6.1 关联服务与数据集

在 ADF 中提前配置 **源（MySQL、PostgreSQL 等）** 与 **接收器（ADLS、数据库）** 的数据集；Copy Activity 只做搬运，分层转换放在 Databricks。

![ADF 源与接收器](/blog-media/img/azure-platform/1740211618460.png)

### 6.2 VNet 集成与自承载 IR

**要点**：ADF 在 **VNet 注入模式**下，**不能**直接连非 PaaS 的内网服务；访问 IDC 或内网 MySQL 的常见做法是：

1. 在 VNet 内或能访内网的 **Windows VM** 上部署 **自承载集成运行时（SHIR）**。
2. ADF 管道通过该 IR 执行 Copy。

![集成运行时拓扑](/blog-media/img/azure-platform/1740213165440.png)

在 VM 上安装微软提供的 SHIR 安装包，在 ADF 门户注册密钥。

![SHIR 安装](/blog-media/img/azure-platform/1740214936834.png)

### 6.3 编排与规模化

- **宏观编排**：ADF Pipeline —— 多源多目标、依赖、调度、告警。
- **微观编排**：Databricks Notebook / Workflow —— SQL、PySpark、参数化重跑。
- **触发器**：Azure Functions 处理复杂表达式或外部事件；也可 ADF 原生 Schedule / Tumbling Window。

Pipeline 数量上去后，建议维护一张**外部依赖表**（库表或 Git），记录 **Pipeline 名、参数、上下游依赖**，避免纯靠 ADF 画布手工维护。规模化编排可抽象为：

1. **调度器（ADF / Function）** 周期性查询依赖表：当前批次、状态为 waiting、上游已成功、时间窗满足，则拉取待运行 Pipeline 列表。
2. **执行**：通过 ADF API 触发运行，结果写回同一元数据库（成功则推进批次，失败则标记批次失败并止损）。
3. **链路分层（示意）**：**ADF Copy** 入 **Raw** → **ADB / AKS 上的 Notebook 或 Job** 写 **ODS（Delta / SQL）** → 再入 **DWD/DWH**；旁路可用 **Change Feed / Event Grid** 做事件驱动补数。

缩写对照：**EH** = Event Hubs，**ADB** = Azure Databricks。

---

## 7. 批处理链路（T+1）

典型 T+1：**业务库 → Onboarding → ODS →（DWD/DWS）**。

### 7.1 ADF Copy 到 Onboarding

- 使用 **自承载 IR** 从 MySQL 等内网库全量/增量抽取。
- 落地到 UC Volume 或 ADLS 路径，对应 **Onboarding** Schema（原始区 + 文件元数据）。

![MySQL → ADF Copy → Onboarding](/blog-media/img/azure-platform/1740220041754.png)

### 7.2 Databricks Notebook 入 ODS

- Notebook 从 Onboarding 路径读 Parquet / CSV，清洗后 **COPY INTO** 或 `saveAsTable` 写入 **ODS**（Delta 为佳）。
- **增量策略**：单独建 **Azure SQL Database**（或配置表）保存 **水位、Checkpoint、表级参数**；Notebook 通过 **widgets 参数** 接收 ADF 传入的批次日期、表名。

![Notebook 参数与增量配置](/blog-media/img/azure-platform/1740220305141.png)

### 7.3 三种入湖方式对比

| 方式 | 适用 | 说明 |
|------|------|------|
| 应用写 Parquet 上传 ODS | 小批量、定制强 | 自行保证分区与 schema |
| ADF Copy | 规整批同步 | 配置成本低，复杂转换弱 |
| Databricks Notebook | 清洗、合并、DQ | 与 UC、Delta 契合最好 |

生产上常见组合：**ADF Copy 到 Onboarding + Databricks 入 ODS 及下游**。

---

## 8. 实时链路：Event Hubs 与 Spark

### 8.1 Event Hubs 能力边界

- **只能接收推送过来的数据**，不能像 Debezium 一样直连 MySQL binlog（CDC 在 Kafka Connect 层完成后再写入 EH）。
- Event Hubs 提供 **Kafka 协议端点**（9093），可用 Spark 的 `kafka` 格式读取；**不要**在 EH 上指望完整 Kafka Connect 插件生态与原集群等价行为。

### 8.2 流式读取示例（脱敏）

依赖包示例：`spark-sql-kafka`、`azure-eventhubs-spark`（版本与集群 Runtime 对齐）。

```python
from pyspark.sql.functions import col

event_hub_namespace = "<EVENTHUB_NAMESPACE>"
event_hub_name = "<HUB_NAME>"
sas_key_name = "RootManageSharedAccessKey"
sas_key = "<FROM_KEY_VAULT>"  # 勿硬编码到 Notebook

kafka_bootstrap = f"{event_hub_namespace}.servicebus.windows.net:9093"
jaas = (
    'org.apache.kafka.common.security.plain.PlainLoginModule required '
    f'username="$ConnectionString" password="Endpoint=sb://{event_hub_namespace}.servicebus.windows.net/;'
    f'SharedAccessKeyName={sas_key_name};SharedAccessKey={sas_key}";'
)

df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", kafka_bootstrap)
    .option("subscribe", event_hub_name)
    .option("kafka.security.protocol", "SASL_SSL")
    .option("kafka.sasl.mechanism", "PLAIN")
    .option("kafka.sasl.jaas.config", jaas)
    .option("startingOffsets", "earliest")
    .load()
)

parsed = df.select(col("value").cast("string").alias("body"))

query = (
    parsed.writeStream.format("delta")
    .option("checkpointLocation", "/Volumes/<catalog>/<schema>/<volume>/checkpoints/<job>")
    .table("<catalog>.<schema>.<target_table>")
)
query.awaitTermination()
```

Checkpoint 必须落在 UC **Volume** 或 ADLS 持久路径，且与消费组策略一致，避免重复或丢数。

### 8.3 Event Hubs 在拓扑中的位置

![Event Hubs 与周边组件](/blog-media/img/azure-platform/1740278821887.png)

![Event Hub 配置示意](/blog-media/img/azure-platform/1740463975514.png)

---

## 9. CDC：Kafka Connect + Debezium → Event Hubs

源端：**MySQL / PostgreSQL**；汇端：**Event Hubs**（作为 Sink）。

Kafka Connect 需在 Kafka（或兼容存储）上保留 **config / offset / status** 三个内部 Topic。迁到 Event Hubs 时需显式命名，例如：

```properties
config.storage.topic=connect-cluster-configs
offset.storage.topic=connect-cluster-offsets
status.storage.topic=connect-cluster-status
```

![Debezium Connector 配置](/blog-media/img/azure-platform/1740122544805.png)

架构上与批链路并列：**CDC → EH → Databricks Structured Streaming → ODS/DWD**；批链路仍走 ADF T+1 兜底。

---

## 10. Power BI：Embedded 与 SaaS

- **Power BI Desktop** 开发报表，发布到 **Power BI 服务（SaaS）**。
- **Embedded** 承载嵌入场景下的算力与容量；与 SaaS 工作区一体规划。
- **重要限制**：Embedded **不能直连接内网源**；需通过 **云侧语义层**、**Dataflow/Gateway** 或 **把数据同步到云上 DWD** 再 Import/DirectQuery。

元数据与小型配置库可用 **Azure SQL Database**

---

## 11. Purview 与数据目录

**Microsoft Purview** 用于跨订阅的数据地图、分类与策略（视许可而定）。在混合场景下常配合 **Private Endpoint**，让 ADF、ADB 在专网内访问注册源，避免公有端点暴露。

典型用途：

- 扫描已入湖的 SQL、ADLS 路径，统一 **术语表 / 血缘**（与 UC 互补：UC 偏计算侧授权，Purview 偏企业目录）。
- 为敏感字段打标签，联动隐私合规流程。

---

## 12. 网络与 DNS：IDC 打通 Azure

### 12.1 Private Endpoint 与 ADF

内网源、非 Azure 主机上的库，往往通过 **Private Endpoint + VNet** 或 **SHIR** 进入 ADF；**Purview / SQL / Storage** 的 PE 需在中心 hub 网段统一规划。

### 12.2 DNS 转发（混合解析）

- **本地 GDS / IDC DNS** 负责内网记录。
- **Azure DNS**（世纪互联场景下注意与全球云差异）可做**条件转发**：把 `database.windows.net` 等后缀转发到 Azure 提供的 DNS 或 **DNS Private Resolver**。
- Azure DNS 在部分部署模型中**跨订阅共享、实例数量有限**，需在 Landing Zone 阶段统一规划，避免多团队重复创建。

解析路径示意（通用架构图）：

![IDC → Azure DNS 转发](/blog-media/img/azure-platform/1740300377787.png)

*图 12-1：本地条件转发 + Azure 专用解析到 Private Endpoint*

与 **AWS / 阿里云** 对比时需注意：Azure 中国区 DNS 与区域绑定方式、Private Link 域名规则与友商不同，转发规则需按官方文档逐条核对。

---

## 13. 私有连接与内网数据库连通性

内网 MySQL 部署成功后，若 **VNet / 对等连接 / DNS** 任一环节未通，ADF Copy 与 BI Gateway 都会失败。排查顺序：

1. SHIR 能否 ping / telnet 源库端口；
2. NSG 与路由表是否放行；
3. 源库防火墙是否放通 IR 机器网段；
4. 若走 Private Link，私网 A 记录是否解析到正确 PE IP。

![内网连通排障示意](/blog-media/img/azure-platform/1740278788139.png)

![网络与安全组](/blog-media/img/azure-platform/1740278762891.png)

---

## 14. 与阿里云、腾讯云、自建平台对照

 **Azure POC、国内公有云与 IDC 自建**。下表按**能力域**做映射，不是 SKU 一一对应；方法论仍可统一为 Onboarding → ODS → DWD、元数据驱动与分层治理（《[数据平台架构演进](/blog/data/dataplatformarchitecturedesign/)》《[阿里云湖仓数据中台](/blog/data/alicloudy/)》《[自建企业级数据平台](/blog/data/enterprisedataplatform/)》）。

| 能力域 | Azure | 阿里云 | 腾讯云 | 自建（开源 + 门户） |
|--------|-------------------|--------|--------|---------------------|
| **开发 + 治理一站式** | Databricks Workspace + Unity Catalog；Purview 目录 | **DataWorks**（集成 / 开发 / 建模 / 质量 / 数据地图） | **WeData** | **OpenMetadata / DataHub** + 自研企业门户；质量/标准流程自建 |
| **离线 / 湖仓计算** | **Databricks**（Spark/Delta）、可选 Synapse | **MaxCompute**（离线数仓）+ **Hologres**（实时分析 / Serving） | **DLC**（数据湖计算） | **Apache Spark** on K8s / YARN；SQL 可走 Trino / Kyuubi |
| **对象存储与表格式** | **ADLS Gen2** + Delta（UC 托管） | **OSS** + MaxCompute / 湖外表；Hologres 快查 | **COS** + DLC 表 | **Iceberg / Hudi** + MinIO / Ceph / 现有对象存储 |
| **实时采集与计算** | **Event Hubs**（Kafka 协议）+ Spark Structured Streaming | **Flink**、**DataHub**（实时通道） | **Oceanus**（Flink） | **Kafka** + **Flink**；库表 CDC 用 **Flink CDC** / Debezium |
| **批集成与调度** | **ADF**（云）+ **自承载 IR**（IDC）；Function 触发 | DataWorks **数据集成** + 任务调度 | 数据集成 + WeData 调度 | **SeaTunnel** / DataX + **DolphinScheduler**（或 Airflow） |
| **元数据与权限** | **Unity Catalog**（计算侧）+ **Purview**（企业目录） | DataWorks 数据地图 + **RAM** | WeData 治理 + 云 CAM | **OpenMetadata / DataHub** 血缘资产；**Apache Ranger** 等需按引擎插件落地 |
| **混合云 / 内网库** | SHIR、**Private Endpoint**、DNS Private Resolver | 专线 / VPN + **Landing Zone** 多账号 | 类似：VPC + 专线 / VPN | 机房 **SeaTunnel / Flink CDC** 直抽；无托管 IR，网络与防火墙自管 |
| **BI 与语义层** | **Power BI**（Embedded + SaaS） | **Quick BI**、Hologres 作 Serving | 自有 BI 或第三方 | **Superset / Metabase**；语义层可接指标平台或轻量多维模型 |
| **机器学习（可选）** | Databricks **MLflow** | **PAI** | 云上的 TI / 自建 | **MLflow** + 训练集群；与中台数据分层解耦部署 |

**怎么读这张表**

- **Azure**：强项是 **UC + Databricks + ADF + Power BI** 在微软栈内闭环；混合企业要补 **SHIR 与 DNS**，成本与账号边界要想清楚。
- **阿里云**：**DataWorks + MaxCompute + Hologres** 的「开发治理 + 离线 + 实时 Serving」路径成熟，适合已上阿里 Landing Zone 的团队（见《阿里云湖仓数据中台构建》）。
- **腾讯云**：**WeData + DLC + Oceanus** 分工接近「治理开发 / 湖计算 / Flink 实时」，BI 往往还需另选或自研。
- **自建**：组件可换，但须自建 **门户、发布流程、权限与观测**；集成与调度建议 **主选一个引擎**（如 SeaTunnel + DolphinScheduler），湖表 **Iceberg 优先**，避免与云版能力重复造轮子。

---

## 15. 实施 checklist

> 实际项目请在 **变更单 / 项目管理工具** 中维护勾选状态，与 POC 环境解耦。

| 序号 | 域 | 检查项 | 验收要点 |
| --- | --- | --- | --- |
| 1 | **身份与治理** | Metastore 与 Access Connector 存储 RBAC | Connector **托管标识** 对 UC 所用 ADLS 容器已分配 **存储 Blob 数据参与者**；抽样读写外部位置成功 |
| 2 | **身份与治理** | Unity Catalog 权限最小化 | Catalog / Schema / Table 按角色 **USE / SELECT** 收敛；无全员可读生产 Catalog |
| 3 | **身份与治理** | 密钥与凭据 | 连接串、SAS **进 Key Vault**；Notebook / Job 经 **Secret Scope** 引用，仓库与日志无明文 |
| 4 | **数据链路** | 分层命名一致 | Onboarding / ODS / DWD（及卷路径）与《分层规范》一致，与 UC 三层命名空间映射表已评审 |
| 5 | **数据链路** | 批流监控分离 | **T+1 ADF** 与 **实时 Event Hubs** 分通道告警；延迟、失败率、积压各有 Owner |
| 6 | **数据链路** | Checkpoint 与水位 | 流作业 Checkpoint 路径持久化；**水位 / 配置表** 有备份与恢复演练记录 |
| 7 | **网络** | 自承载 IR | **至少 2 节点** 或 documented 故障切换；内网源连通性有定期探测 |
| 8 | **网络** | 混合 DNS | 条件转发 / Private Resolver 规则 **文档化**；变更走变更单，非口头修改 |
| 9 | **消费** | BI 与产数 SLA | Power BI **Refresh** 与 DWD 产出 SLA 对齐；失败有重试与通知 |
| 10 | **消费** | Embedded 与许可 | Embedded 容量与 SaaS **许可证 / 成本** 有预算与扩容预案 |

**建议顺序：** 先完成 **1–3**（否则后续入湖即越权风险），再 **4–6** 数据链路，**7–8** 与混合网同步验收，最后 **9–10** 消费侧。

---

## 16. 小结

在 **Azure 中国区** 搭建数据平台，主线是：**Unity Catalog 定标准与权限 → ADLS 分层存 → Databricks 算 → ADF 批集成 → Event Hubs 流 → Power BI 看**。混合企业必须提前设计 **自承载 IR、Private Endpoint 与 DNS 转发**，否则内网源无法稳定入湖。批流并存时，用 **Onboarding 承接原始落地、ODS 承接规范明细**，增量水位与 Checkpoint 表是运维排障的基础设施。

