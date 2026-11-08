---
title:  X-Agent 平台全景
description: DeerFlow+Wren+RAG 架构
category: AI Agent
date: 2026-11-02
readTime: 45 分钟
icon: ◈
featured: true
draft: false
tags: [Agent, LangGraph, Wren, NL2SQL, RAG, 面试]
---

## 1. 简介

**X-Agent** 是面向生物制药工艺数据的对话式 AI Agent 平台：用户用自然语言提出跨项目、跨批次问题，系统编排取数 → 分析 → 归因 → 建议 → 结构化报告，并把结果沉淀为可回看的问题树、章节与图表。

不是从零自研的通用聊天机器人，而是把三套能力缝合成企业工作台：

| 底座 | 来源 | 在  中的角色 |
|------|------|-----------------|
| DeerFlow 2.0 | 开源 LangGraph Super Agent | Agent Runtime：中间件、Skills、MCP、Subagent、Sandbox、SSE |
| Wren（已内化） | 参考新版 WrenAI 重写进 harness | 语义层 NL2SQL、SQL dry-plan/执行、业务库连接、图表生成 |
| file-search-RAG | 自研 | PDF/Office/视频文档解析、混合检索、带引用的文档问答 |

## 2. 业务背景

### 2.1 场景

工艺管理中，**Function Head** 要回答四类问题：

| 维度 | 典型关注点 |
|------|------------|
| 范围 | 多个项目、多个批次、多个工艺阶段（Cell Line,Upstream,DownStream,MFG 等） |
| 结果指标 | Titer（表达量）分布是否异常 |
| 过程指标 | Lactate、VCD、VIA、pCO2、Glucose、pO2 等（常称 **ABCDE** 相关因子） |
| 决策 | 是否出现风险批次、原因是什么、下一步如何调整 |

传统路径是：切报表 → 透视 → 画图 → 写结论。瓶颈不在会不会分析，而在 **入口分散、口径靠人、链路断、结论难沉淀**：

- **数据散**：项目视图、批次视图、文档、培养时序表不在同一入口
- **口径不统一**：风险批次判定高度依赖个人经验
- **链路长**：从看见异常到归因 + 建议 + 汇报材料需反复切换工具
- **难复盘**：结论散落在聊天、PPT、个人笔记，无法按问题树回看

> 老板需要的不是更多原始切片，而是 **结论 + 风险 + 建议 + 图表 + 可追溯证据** 的一体化输出。

### 2.2 产品要解决什么

产品目标是把一次提问从听懂到可汇报做成 **一条 Agent 编排链路**，而不是散落在多个工具里的手工步骤：

```text
意图识别 → 上下文构建 → 任务规划 → 能力执行 → 结果校验 → 管理输出
```

用户在 **对话工作台（Thread）** 内应能闭环完成以下能力：

| 用户要完成的事 | 典型产出 |
|----------------|----------|
| 跨项目监控与报表问答 | KPI / 趋势 / 对比表与 Vega 图 |
| Titer / 工艺指标分析 | 分布、分层、异常批次视图 |
| 风险批次识别与因子归因 | 风险等级、ABCDE 等因子解释 |
| 改善建议与结构化报告 | 行动项、章节化摘要、可导出报告区 |
| 文档与库表证据并用 | 方案/报告/视频纪要与 SQL 结果 **分栏引用**；冲突与缺失 **显式标注** |

编排层负责路由（Wren / RAG / 领域 Skill）、打断澄清与落库；体验层负责多轮推进与 **问题树回看**（`question` → section / chart）。

### 2.3 目标用户

| 角色 | 关注点 |
|------|--------|
| Function Head | 跨项目态势、风险分布、可汇报摘要与图表 |
| Function Lead / 工艺科学家 | 单项目、单批次、单指标深挖与调参建议 |
| Platform Admin | 登录鉴权、RBAC、建模配置、评测与审计 |

### 2.4 明确不做（非目标）

不自动改生产系统参数、不闭环执行工艺调整

不是通用 AutoML / 全自动实验设计平台

不是无边界开放式闲聊助手

不允许脱离业务规则与证据的自由结论

## 3. 产品 Scope

产品有两层 Scope：PRD 目标态，以及当前代码已落地的工作台。

### 3.1 目标态能力地图（PRD V2）

PRD 按优先级分三档；**P0 = 决策闭环必需**，P1 = 汇报与建议增强，P2 = 平台化与治理。

| 优先级 | 能力 | 描述 |
|--------|------|------|
| **P0** | 跨项目数据报表查看 | 多项目 KPI、趋势、对比 |
| **P0** | Titer 分布分析 | 项目/批次分布、分层、异常 |
| **P0** | 风险批次识别 | 规则 + 多指标偏离，输出等级与标签 |
| **P0** | 风险原因 / 因子重要性 | Lactate、VCD、VIA、pCO2、Glucose、pO2 等单因子/多因子 |
| **P1** | AI 改善建议 | 优先改善指标与行动建议 |
| **P1** | 图表生成与导出 | 管理汇报可用图 + 说明 |
| **P1** | 分析报告生成与导出 | 摘要 + 图 + 归因 + 建议 |
| **P2** | 定制工作流 / 专项模板 | 周期报告、专项场景 |
| **P2** | 历史记忆与案例复用 | 已确认结论与规则沉淀 |
| **P2** | 评测与建议质量治理 | 准确性、解释性、可接受度 |

**页面目标形态（PRD 收敛为三块）**

| 页面 / 区域 | 职责 |
|-------------|------|
| **Dashboard** | 跨项目/年度总览（KPI、反应器/规模分布、Titer overview） |
| **Thread** | 唯一深度分析页：对话 + 多轮推进 + 结构化产物 |
| **Analysis Panel** | 图表、表格、结论、行动项、导出（产品上是报告区，**不一定是独立路由**） |

### 3.2 当前已落地 Scope（工作台）

> **现状一句话**：默认体验更接近 **聊天流内嵌结构化报告**，而不是 PRD 里完整的三栏独立 Question Panel。

#### 已具备

| 类别 | 能力要点 |
|------|----------|
| **运行时** | 多轮 Thread、SSE 流式、可恢复流；可选 Plan Mode / Subagent |
| **库表取数** | `database_query`（Wren 语义层） |
| **文档问答** | `rag_file_search`（file-search-RAG）：PDF 页级解析、Office、视频转写 |
| **默认 Q&A** | `question-and-answer` Skill：未指定来源时 **库 + 文档双路**；回答须标注库证、文档证、缺失与冲突 |
| **产物落库** | `thread` → `question` → `section` → `chart`；前端轮询问题树 |
| **图表契约** | Vega-Lite enrichment（库表答案 **禁止** matplotlib 静图） |
| **澄清** | 实体词典 + NL2SQL 澄清（歧义可打断；**可见问句保持用户原文**） |
| **领域 Skill**（与通用报表分轨） | `database-query` / `file-search`（Q&A 子技能） |
| **建模管理** | Gateway `/api/dbquery/*`（数据源、模型、关系、知识、SQL-pair） |
| **登录** | JWT + 邮箱白名单 + Casbin RBAC（**主鉴权在 Next.js**） |
| **评测** | 独立 `eval-service` + `eval_golden_set` / `eval_evidence` |
| **Office** | OnlyOffice 预览/编辑 |

#### 部分落地 / 演进中

- Dashboard 看板与风险行动项提交锁定完整闭环
- ABCDE 归因与因子重要性的 **细粒度规则化**
- 报告 **正式导出中心**（现多在对话内 ReportCard / SectionCard）

#### 明确未落地（设计稿）

- **Workspace 多租户**与按团队隔离的 RAG corpus（现状 `corpus_id=default` 全站共享）


### 3.3 产品边界：取数轨道（库表 / 领域 / 文档）

核心原则：**语义所有权分轨**——汇总指标走 Wren，培养时序与模型走 Skill+沙箱，规程证据走 RAG；禁止跨轨猜 JOIN或从文档词推断库表字段。

| 轨道 | 适用问题 | 执行方式 | 禁止事项 |
|------|----------|----------|----------|
| 语义层（Wren） | 项目/批次/年份等业务汇总：`total_titer`、`project_info`、排名、趋势 | Agent 调 `database_query` | 不要用沙箱 Python 画静图 |
| 领域 Skill + 沙箱 |  `cultureid` 时序、模型推荐 | `python3` + 技能内 `db_config.yaml` | `toolbox-*` 显式 `disallowed-tools: database_query`，避免两套语义打架 |
| 文档 RAG | 上传 PDF/Office/视频、选定 references | `rag_file_search` | 文档未写字段（如分子类型）**不得**从 titer 等词推断 |

路由契约见 `skills/public/question-and-answer/SKILL.md`：**Skill 是决策合同**，真正执行仍走子技能与工具。

## 4. 数据

X-Agent 里至少有 **四类数据平面**，不要当成一张库、一个向量库：

```text
┌─────────────────────────────────────────────────────────────┐
│ A. 业务事实数据（工艺/培养，给 NL2SQL 或 Skill 查询）         │
│ B. 语义与建模元数据（Wren MDL、词典、SQL-pair、连接串）       │
│ C. 对话与结构化产物（Thread / Question / Section / Chart）  │
│ D. 非结构化文档与向量（上传件、Qdrant chunk、视频字幕）       │
└─────────────────────────────────────────────────────────────┘
```

| 存储 | 承载平面 | 备注 |
|------|----------|------|
| **Postgres** | A 部分汇总表、B 元数据、C 全量、D 文档元数据 | Prisma（前端/RBAC）、`wren_*` **共库**；后端 psycopg **只读写、不擅自建表** |
| **Qdrant** | D 文档 chunk | dense + BM25；`collection ≈ {prefix}_{corpus_id}` |
| **LanceDB** | B 侧 Wren 语义记忆 | **不与** file-search 向量混 collection |
| **COS** | D 原件与转换件 | 与 ingest / 预览 sidecar 配合 |

### 4.1 A. 业务事实数据

#### 4.1.1 业务汇总表（Wren / `database_query`）

语义层对接内部工艺汇总模型,实体词典默认扫描列包括 `project_info` 上的 `cell_bank`、`purpose` 等

- **典型问法**：项目信息、批次汇总、年份分布、total titer / yield、部门/位点/分子类型维度。
- **SQL 约束**：必须走 MDL 模型名与列名；PostgreSQL 数值用 `DOUBLE PRECISION`；批次号 JOIN 有 **X/Y 后缀规范化** 规则。
- **连接安全**：Fernet 加密存储（`connection_security.py`），**不与**应用 JWT 密钥混用。


### 4.2 B. 语义与建模元数据（Wren）

由 Prisma / Gateway `dbquery` 管理，核心对象：

| 对象 | 表/模型 | 含义 |
|------|---------|------|
| 项目 | `wren_project` | 数据源、catalog/schema、连接、语言 |
| 模型 | `wren_model` + columns | MDL：逻辑表 ↔ 物理表 |
| 关系 / 视图 / 指令 / SQL-pair | `wren_*` | 少样本、业务指令、已知好 SQL |
| 实体词典 | `entity_dictionary_entry` | 项目/批次/细胞库等字面量消歧 |
| 澄清选择 | `nl2sql_clarification_choice` | 跨会话「一人一票」澄清记忆 |

**运行时**：LLM 做 NL2SQL → `WrenEngine.dry_plan` / `query` **进程内**执行；语义记忆用嵌入式 **LanceDB**（Wren 不再用 Qdrant 召回）。

**`database_query` 对外契约**（内化 Wren 时不得破坏）：`status` / `sub_results` / `partial_failures` / `internal_metrics`。图表 enrichment、message parser、strict routing 均按此工具名硬编码。

### 4.3 C. 对话与结构化产物（Postgres / Prisma `dct_*`）

| 表 | 作用 |
|----|------|
| `thread` | 与 LangGraph `thread_id` 对齐；`created_by` 为 owner |
| `question` | 单轮问题：PENDING→完成/失败、短答、推荐追问、图表 enrichment 状态 |
| `section` | 章节：标题、摘要、`table_sql`、`answer_detail` JSON |
| `chart` | Vega spec（`chart_detail`）+ 可选 SQL |
| `dashboard` / `dashboard_item` | 图表钉看板 |
| `runs` / `run_events` | Run 可恢复、跨 Pod lease、语义事件（非 SSE 镜像） |
| `eval_evidence` | 评测原始 tool 证据（**业务 HTTP 不得返回**） |
| `eval_golden_set` | 回归金标（问题 / 参考答案 / SQL） |

**落库入口**（内核均在 `deerflow.persistence`）

- **自动**：`BootstrapMiddleware`（`before_agent` 建档，`after_agent` 解析）
- **显式**：`POST /api/persistence`

**关键约束**

- LangGraph context **缺 `user_id`** → 静默跳过落库（联调第一嫌疑）
- 可见 `HumanMessage` 与 `database_query.query` **保持用户原文**；实体 glossary 只进 hidden system
- 多步 SQL 的 compaction：**不得**把逐步原始 SQL / 全量 `sql_data` 塞进上下文
- 失败重试后的失败结果 **不得**进入答案总结

### 4.4 D. 文档与向量

| 存储 | 内容 |
|------|------|
| Postgres `upload_document` 等 | 文件名、COS key、ingest 状态、版本、视频字幕、费用 |
| **COS** | 原件、转换件、视频 sidecar（DOCX 转写 / PPTX 校正） |
| **Qdrant** | file-search：dense + 服务端 BM25 |
| **现状 corpus** | 默认 `"default"`，**全登录用户共享检索**（产品债） |

**Ingest（简述）**：Gateway 上传 → file-search 增量 skip → 按格式解析（PDF 文字页 / 图表页 Vision OCR、Office→PDF、XLSX、视频 Markdown）→ 切片 → embedding → upsert。

**检索**：混合召回，可选 rerank 与父块展开；返回带 `document_name` / `page_number` 的 evidence。

### 4.5 数据流主路径（记住这一条）

```text
用户提问
  → Next.js（JWT）注入 user_id
  → Gateway 执行 lead_agent
  → Bootstrap：dthread + question(PENDING)
  → Skill 路由：database_query 和/或 rag_file_search（或沙箱 Skill）
  → SSE 流式答案
  → persist：section / chart
  → 前端轮询 /api/frontend/thread-questions 刷新问题树
```


## 5. 技术架构

**主线**：体验层只打 Next BFF → Gateway 跑 `lead_agent` → 能力面（Wren / file-search / 沙箱 Skill）→ 四类存储。

### 5.1 分层

```text
浏览器
  → Nginx :2026（只分流，不做鉴权）
  → Next.js UI + BFF（主鉴权：JWT / 白名单 / Casbin）
      → /api/frontend/*   问题树、me、dashboard
      → /api/backend/*    转 Gateway
      → /api/langgraph/*  LangGraph 兼容协议（上游仍是 Gateway）
  → FastAPI Gateway :8001 → lead_agent 图执行
      （独立 LangGraph Server 已从主路径下线，以 compose/现状文档为准）
  → harness：中间件 + tools + dct + community/wren_ai
  → packages/wren：WrenEngine + LanceDB
  → file-search-service :8008 → Qdrant
  → Postgres / OnlyOffice / eval-service / 可选 sandbox provisioner
```

两条硬边界：

- 浏览器只打 Next 同源路由；后端不对公网暴露。
- Harness（`deerflow.*`）禁止 `import app.*`，由 `test_harness_boundary.py` 守护。

### 5.2 技术栈

| 子系统 | 运行时 | 关键依赖 |
|--------|--------|----------|
| `frontend/` | Node / TS | Next.js 16、React 19、LangGraph SDK、TanStack Query、Prisma、Casbin、Vega |
| `backend/` Gateway + Harness | Python 3.12+ | FastAPI、LangGraph/LangChain、sse-starlette、psycopg |
| `backend/packages/wren` | in-process | wren-core-py（Rust wheel，锁 linux/amd64）、sqlglot、duckdb、LanceDB |
| `file-search-RAG/` | Python | FastAPI、PyMuPDF、VLM OCR、Qdrant |
| `eval-service/` | Python | 独立评分服务 |
| 模型 | 统一网关 | LiteLLM / 公司 AI Gateway；可观测预留 Langfuse |

本地/生产入口（根目录 Makefile）：`make config` / `install` / `dev` / `docker-start` / `up`。浏览器统一 `localhost:2026`（生产宿主机常映射 `12026`）。

### 5.3 Agent 运行时

`make_lead_agent` 装配模型、工具与中间件。**中间件是可 checkpoint 的图节点**，不是 prompt 里的 if-else。

| 链路段 | 中间件（节选） |
|--------|----------------|
| **运行时段** | ThreadData → Uploads → Sandbox → DanglingToolCall → StrictWrenRouting → ToolErrorHandling |
| **业务段** | DctBootstrap → Followup → NL2SQL 澄清 → EntityRewrite → Summarization → Todo（plan）→ Title → Memory → LoopDetection → LanguageAlignment → CitationEvidence → ContextTruncation → **Clarification（链末拦截）** |

**生产 Agent vs Demo**：实体消歧不改可见 query；非法 tool call 可重试一次；多步 SQL **按依赖 DAG** 完成（非全局串行）；图表类型尊重用户显式请求。

### 5.4 Wren 内化（架构迁移要点）

原先 **6 个容器**（wren-ai-service / wren-ui / wren-engine / ibis-server / wren-bootstrap + Wren 用 Qdrant）已下线。能力迁移：

| 位置 | 职责 |
|------|------|
| `backend/packages/wren` | 引擎与记忆 |
| `deerflow/community/wren_ai/*` | NL2SQL、聚合工具、护栏、图表 |
| `app/gateway/dbquery/` | 管理面 REST |

**SQL 安全四层**：单语句、SELECT-only、函数黑名单、行数 / `statement_timeout`。Apple Silicon 本地开发需注意 **amd64 wheel**。

### 5.5 鉴权与治理

| 层级 | 现状 |
|------|------|
| **Nginx** | 只分流，**无鉴权** |
| **Next.js** | **主鉴权**（JWT / 白名单 / Casbin）；Thread / Report / Persistence 绑 **X-Agent owner** |
| **RAG / 上传** | 默认 **全局共享 corpus**（产品例外，非私有隔离） |
| **Gateway 管理面** | Memory / MCP / Skills 安装等仍有「代码层弱鉴权」债；生产靠统一入口 + 内网不直连 |

Workspace 多租户见 `workspace多租户与文件权限设计.md`，**尚未实现**。面试勿包装成「已零信任」。


### 5.6 仓库拓扑（找代码）

```text
X-Agent/
├── frontend/                 # UI + BFF + Prisma + Casbin
├── backend/
│   ├── app/gateway/          # FastAPI、dbquery、persistence
│   └── packages/
│       ├── harness/deerflow/ # Agent、dct、wren_ai、skills 运行时
│       └── wren/             # in-process 引擎
├── file-search-RAG/
├── eval-service/
├── skills/public/            # 产品 Skills（Q&A、toolbox、host）
├── docker/                   # compose + nginx
└── docs/
```


## 6. 端到端场景对照


| 用户问题类型 | 产品模块 | 数据 | 技术路径 |
|--------------|----------|------|----------|
| 「各项目今年 Titer 怎么样」 | 跨项目报表 / Titer 分布 | Wren 业务汇总表 | Q&A → `database_query` → Vega |
| 「这批为什么低，和 Lactate 有没有关」 | 风险归因 | 汇总表 + 可选文档 | 双路检索 + 证据分栏 |
| 「cultureid 3228FX059 建议怎么调」 | 工艺推荐 | BioFoundry + PRC 模型 | `toolbox-batch-process-recommendation` 沙箱 |
| 「方案里 acceptance criteria 怎么写的」 | 文档问答 | 上传 PDF/Office | file-search + 引用页码 |
| 「把这张图钉到看板」 | Dashboard | `dct_chart` → dashboard_item | 前端 Prisma BFF |

## 7. 风险、技术债与后续方向

- **RAG 单租户共享**：上传即全员可检索/删除风险；workspace 是下一阶段治理重点。
- **Gateway 管理面鉴权不均**：Memory/MCP/Skills 写接口需管理员收口。
- **共库迁移**：Prisma 与 Wren/X-Agent 表同库，禁止后端擅自 `CREATE TABLE`。
- **平台锁定**：`wren-core-py` 仅 linux/amd64。
- **评测**：金标 SQL + 证据冲突标注应一起演进，避免只优化「能跑出 SQL」。