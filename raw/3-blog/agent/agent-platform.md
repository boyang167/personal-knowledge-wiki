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

# X-Agent 平台全景
    面向生物工艺数据 Agent 
**阅读地图**

| 章节 | 内容 |
|------|------|
| §1–3 | 业务、用户、PRD 目标 vs 现状 Scope、Wren / Skill / RAG 三条取数轨道 |
| §4 | 四类数据面：业务表、MDL、`dct_*`、COS + Qdrant |
| §5 | Nginx → Next 鉴权 BFF → Gateway `lead_agent`；Wren 已 in-process |
| §6–7 | 场景对照、技术债（共享 corpus、Gateway 管理面弱鉴权） |
| §8 | 项目向口述题 Q1–Q32 |
| §10 | Agent 架构师题 A1–A90（无 §9，目录从 8 跳到 10） |

**面试提示**：先声明讲的是 **PRD 目标** 还是 **代码现状**。Thread 问答闭环已有；Dashboard 闭环、ABCDE 规则化归因、Workspace 多租户 RAG 仍在演进或未落地。

## 1. 一句话

**X-Agent** 是面向生物制药工艺数据的对话式 AI Agent 平台：用户用自然语言提出跨项目、跨批次问题，系统编排取数 → 分析 → 归因 → 建议 → 结构化报告，并把结果沉淀为可回看的问题树、章节与图表。

不是从零自研的通用聊天机器人，而是把三套能力缝合成企业工作台：

| 底座 | 来源 | 在  中的角色 |
|------|------|-----------------|
| DeerFlow 2.0 | 开源 LangGraph Super Agent | Agent Runtime：中间件、Skills、MCP、Subagent、Sandbox、SSE |
| Wren（已内化） | 参考新版 WrenAI 重写进 harness | 语义层 NL2SQL、SQL dry-plan/执行、业务库连接、图表生成 |
| file-search-RAG | 自研 | PDF/Office/视频文档解析、混合检索、带引用的文档问答 |

## 2. 业务背景

### 2.1 场景

工艺管理中，**Function Head / Function Lead** 要在同一套态势里同时回答四类问题：

| 维度 | 典型关注点 |
|------|------------|
| 范围 | 多个项目、多个批次、多个工艺阶段（NPP Upstream、cMFG 等） |
| 结果指标 | Titer（表达量）分布是否异常 |
| 过程指标 | Lactate、VCD、VIA、pCO2、Glucose、pO2 等（常称 **ABCDE** 相关因子） |
| 决策 | 是否出现风险批次、原因是什么、下一步如何调整 |

分析师的传统路径是：切报表 → 透视 → 画图 → 写结论。瓶颈不在「会不会分析」，而在 **入口分散、口径靠人、链路断、结论难沉淀**：

- **数据散**：项目视图、批次视图、文档、培养时序表不在同一入口。
- **口径不统一**：风险批次判定高度依赖个人经验。
- **链路长**：从「看见异常」到「归因 + 建议 + 汇报材料」需反复切换工具。
- **难复盘**：结论散落在聊天、PPT、个人笔记，无法按问题树回看。

> 管理层需要的不是更多原始切片，而是 **结论 + 风险 + 建议 + 图表 + 可追溯证据** 的一体化输出。

### 2.2 产品要解决什么

产品目标是把一次提问从「听懂」到「可汇报」收成 **一条 Agent 编排链路**，而不是散落在多个工具里的手工步骤：

```text
意图识别 → 上下文构建 → 任务规划 → 能力执行 → 结果校验 → 管理输出
```

用户在 **对话工作台（Thread）** 内应能闭环完成以下能力（与 §2.1 的四类问题一一对应）：

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

产品有两层 Scope：PRD 目标态，以及当前代码已落地的工作台。面试或评审时先声明「讲目标还是讲现状」。

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

> **现状一句话**：默认体验更接近 **「聊天流内嵌结构化报告」**，而不是 PRD 里完整的三栏独立 Question Panel。

#### 已具备

| 类别 | 能力要点 |
|------|----------|
| **运行时** | 多轮 Thread、SSE 流式、可恢复流；可选 Plan Mode / Subagent |
| **库表取数** | `database_query`（Wren 语义层，in-process） |
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

- Dashboard 看板与「风险行动项提交锁定」完整闭环
- ABCDE 归因与因子重要性的 **细粒度规则化**
- 报告 **正式导出中心**（现多在对话内 ReportCard / SectionCard）

#### 明确未落地（设计稿）

- **Workspace 多租户**与按团队隔离的 RAG corpus（现状 `corpus_id=default` 全站共享）
- **自研 Workflow Orchestrator**（已被 DeerFlow `lead_agent` 取代；**勿按 V2 架构稿改编排层**）

### 3.3 产品边界：取数轨道（库表 / 领域 / 文档）

核心原则：**语义所有权分轨**——汇总指标走 Wren，培养时序与模型走 Skill+沙箱，规程证据走 RAG；禁止跨轨「猜 JOIN」或从文档词推断库表字段。

| 轨道 | 适用问题 | 执行方式 | 禁止事项 |
|------|----------|----------|----------|
| 语义层（Wren） | 项目/批次/年份等业务汇总：`total_titer`、`project_info`、排名、趋势 | Agent 调 `database_query` | 不要用沙箱 Python 画静图 |
| 领域 Skill + 沙箱 |  `cultureid` 时序、模型推荐 | `python3` + 技能内 `db_config.yaml` | `toolbox-*` 显式 `disallowed-tools: database_query`，避免两套语义打架 |
| 文档 RAG | 上传 PDF/Office/视频、选定 references | `rag_file_search` | 文档未写字段（如分子类型）**不得**从 titer 等词推断 |

路由契约见 `skills/public/question-and-answer/SKILL.md`：**Skill 是决策合同**，真正执行仍走子技能与工具。

## 4. 数据

X-Agent 里至少有 **四类数据平面**，不要当成「一张库、一个向量库」：

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

语义层对接内部工艺汇总模型,实体词典默认扫描列包括 `project_base_info` 上的 `cell_bank`、`purpose` 等

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

**主线**：体验层只打 Next BFF → Gateway 跑 `lead_agent` → 能力面（Wren / file-search / 沙箱 Skill）→ 四类存储（§4）。

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

### 5.5 鉴权与治理（现状，不要美化）

| 层级 | 现状 |
|------|------|
| **Nginx** | 只分流，**无鉴权** |
| **Next.js** | **主鉴权**（JWT / 白名单 / Casbin）；Thread / Report / Persistence 绑 **X-Agent owner** |
| **RAG / 上传** | 默认 **全局共享 corpus**（产品例外，非私有隔离） |
| **Gateway 管理面** | Memory / MCP / Skills 安装等仍有「代码层弱鉴权」债；生产靠统一入口 + 内网不直连 |

Workspace 多租户见 `workspace多租户与文件权限设计.md`，**尚未实现**。面试勿包装成「已零信任」。


### 5.6 仓库拓扑（找代码）

```text
digital-control-tower/
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

wren-ai-service/、wren-ui/ 若仍出现在旧文档或残留目录中，视为历史世代，不以它们为运行时真相。

## 6. 端到端场景对照

典型问法与 §3.3 三轨取数、§4.5 主路径对照：

| 用户问题类型 | 产品模块 | 数据 | 技术路径 |
|--------------|----------|------|----------|
| 「各项目今年 Titer 怎么样」 | 跨项目报表 / Titer 分布 | Wren 业务汇总表 | Q&A → `database_query` → Vega |
| 「这批为什么低，和 Lactate 有没有关」 | 风险归因 | 汇总表 + 可选文档 | 双路检索 + 证据分栏 |
| 「cultureid 3228FX059 建议怎么调」 | 工艺推荐 | BioFoundry + PRC 模型 | `toolbox-batch-process-recommendation` 沙箱 |
| 「方案里 acceptance criteria 怎么写的」 | 文档问答 | 上传 PDF/Office | file-search + 引用页码 |
| 「把这张图钉到看板」 | Dashboard | `dct_chart` → dashboard_item | 前端 Prisma BFF |

## 7. 风险、技术债与后续方向

- **文档世代混乱**：V2 PRD 的外部 Wren / 自研编排器已过时；改代码先信 `ARCHITECTURE_AND_JOURNEY.md` 与 compose 实际服务列表。
- **RAG 单租户共享**：上传即全员可检索/删除风险；workspace 是下一阶段治理重点。
- **Gateway 管理面鉴权不均**：Memory/MCP/Skills 写接口需管理员收口。
- **共库迁移**：Prisma 与 Wren/X-Agent 表同库，禁止后端擅自 `CREATE TABLE`。
- **平台锁定**：`wren-core-py` 仅 linux/amd64。
- **评测**：金标 SQL + 证据冲突标注应一起演进，避免只优化「能跑出 SQL」。

**建议建设顺序**（产品 + 工程一致）：Gateway 二次校验与 workspace corpus 隔离 → 评测覆盖融合/冲突 → 再扩专项工作流模板。

## 8. 会被问到什么（项目向口述）

| 小节 | 题号 | 主题 |
|------|------|------|
| 8.1 | Q1–Q5 | 开场与业务 |
| 8.2 | Q6–Q12 | 架构与系统设计 |
| 8.3 | Q13–Q19 | Agent、中间件、Skills |
| 8.4 | Q20–Q26 | 数据、NL2SQL、RAG、图表 |
| 8.5 | Q27–Q32 | 质量、评测、协同 |
| 8.6 | — | 追问速查 |
| 8.7 | — | 不该说的话 |

> **使用约定**：这是多人协作平台。先讲系统理解，再用 1–2 个自己落地过的点（工艺推荐 Skill、早期 Wren 图表/追问）证明能力。答案按 **结论 → 机制 → 代价/边界** 口述约 45–90 秒；被追问再下钻到文件名。**目标态（PRD）与现状（代码）务必分开说**。

### 8.1 开场与业务

#### Q1. 用两分钟介绍这个项目。

**X-Agent** 是工艺数据 Agent 工作台。Function Head / Lead 要用自然语言问跨项目、跨批次的问题，例如 Titer 分布、风险批次、过程指标归因、培养批次怎么调。我们不是做通用 Chatbot，而是把「取数 → 分析 → 归因 → 建议 → 结构化报告」编排起来，结果落成可回看的问题树、章节和 Vega 图。

技术上是三套底座缝合：DeerFlow/LangGraph 做 Agent Runtime；Wren 语义层做 NL2SQL（已从外部服务收成进程内库）；自研 file-search 做 PDF/Office/视频 RAG。我个人主要落地过 BioFoundry 的 titer 查询 Skill，以及 PRC/PEV 工艺推荐 Skill（模型在沙箱里跑、库表取数、特征缓存挂可写卷），早期还改过 Wren 侧 titer 箱线图契约和追问推荐。

#### Q2. 用户是谁？他们原来怎么干活？你们替代了什么？

用户是工艺管理层和科学家。原来靠分析师切报表、透视、画图、写 PPT，口径靠经验，从「看见异常」到「可汇报材料」链路很长，结论难复盘。我们替代的是这条分析与汇报工作流的入口和沉淀，不是替代 LIMS/MES，也不自动改生产参数。输出必须带证据：库表、文档、缺失和冲突要分开写。

#### Q3. 这个产品和 ChatGPT 挂个数据库有什么本质区别？

三点：① 语义层契约——不能让模型直接对业务库写任意 SQL，要走 MDL、dry_plan、SELECT-only 和列守卫；② 证据与落库——回答会解析成 dct_question/section/chart，刷新后还能回看，不是一过性 token；③ 领域分轨——通用报表走 Wren，培养时序和 PRC 模型走 Skill+沙箱，避免两套表语义打架。ChatGPT + DB 缺的是治理、可追溯和业务口径。

#### Q4. 产品 Scope 里你认为最核心的 P0 是什么？现在做到哪？

P0 是跨项目报表、Titer 分布、风险批次识别和因子归因。现状是对话里能问汇总指标、双路检索（库+文档）、图表 enrichment、部分宿主对比和工艺推荐 Skill。Dashboard 完整看板、行动项提交锁定、细粒度 ABCDE 规则化归因还在演进。Workspace 多租户 RAG 是设计稿未落地。面试时主动说「Thread 问答闭环已有，管理看板和治理隔离还在补」。

#### Q5. 为什么不做自动调工艺参数？

这是药企合规边界。错误建议进生产风险不可逆。产品定位是决策支持：给结论、证据、建议，人来确认。Skill 里的 PRC/PEV 也是推荐摘要，不是下发执行指令。

### 8.2 架构与系统设计

#### Q6. 画一下整体架构。

浏览器 → Nginx（只分流）→ Next.js BFF（JWT/白名单/Casbin，注入 user_id）→ FastAPI Gateway。Agent 是 lead_agent：中间件链 + 工具。取数走 database_query（LLM 生成 SQL，WrenEngine 进程内 dry_plan/query）。文档走 file-search → Qdrant。结构化结果写 Postgres 的 dct_。两条硬边界：浏览器不对 Gateway 直连；Harness（`deerflow.*`）禁止反向 import app.*。

#### Q7. 为什么用 DeerFlow / LangGraph，而不是自研一个 workflow 编排器？

早期 V2 PRD 想自研 Orchestrator（意图→规划→门控→子流程）。后来用 DeerFlow，因为每轮要动态路由库/文档、打断澄清、多步 SQL、失败重试、SSE 与 checkpoint，固定 DAG 适合 ETL，不适合这种对话 Agent。代价是更难测，所以用大量契约测试锁行为（例如实体改写不得改可见 query）。面试加分：承认「编排器稿已过时，别照着改现有层」。

#### Q8. Wren 为什么要从独立服务收成 in-process？代价是什么？

动机：少 6 个容器（ai-service/ui/engine/ibis/bootstrap + Wren 用 Qdrant），缩短 NL2SQL 往返，部署和排障简单。做法：引擎进 packages/wren，工具进 community/wren_ai，管理面改 Gateway /api/dbquery。对外仍叫 database_query 且 payload 契约不变，因为图表 enrichment 和 X-Agent parser 按工具名硬编码。

代价：wren-core-py 锁 linux/amd64；SQL 必须四层护栏（单语句、SELECT-only、函数黑名单、行数/timeout）；本机 ARM 开发要踩镜像坑。这是「内化但不打破消费方」的企业改造。

#### Q9. Harness / App 为什么要防腐？

Harness 是可复用 Agent 框架，App 是 Gateway 和 IM。若 deerflow import app，框架就绑死药明网关，无法测试、无法演进。CI 有 test_harness_boundary.py。需要网关能力就依赖注入，而不是反向引用。这题在考察你有没有模块边界意识。

#### Q10. 前端为什么做 BFF，而不是浏览器直打 LangGraph？

鉴权、同源、用户上下文注入都在 Next。缺 `user_id` 时 X-Agent 落库会静默跳过，表现为「答案有了问题树没有」。生产 Nginx 不把 Gateway/Qdrant/Postgres 暴露到公网。这是企业 Agent 的标准形态：协议兼容层叫 langgraph，不等于独立公网 LangGraph Server。

#### Q11. 鉴权你怎么评价？如果面试官说「你们安全吗」？

诚实讲：Thread/Report 等核心资源已绑 **X-Agent owner**，主鉴权在 Next。但上传/RAG 默认全站共享 corpus；Gateway 上 Memory/MCP/Skills 安装等管理面历史上代码层弱鉴权，生产靠统一入口+内网。这不是「已企业级零信任」。下一步应是 Gateway 二次校验和 workspace→独立 Qdrant collection。主动说债比吹已经完美更加分。

#### Q12. 如果让你重新设计，会改什么？

优先级：① 租户级 corpus 与 Gateway 鉴权拉齐；② 评测从「SQL 对不对」扩到「冲突/缺失标注对不对」；③ Skill 与 Wren 路由门控再收紧，工艺脚本绝不误走语义层。不会先扩更多模型或更多 Skill 包装。

### 8.3 Agent、中间件、Skills

#### Q13. Agent 的一次提问内部发生了什么？

提交后 DctBootstrap 写入 dct_thread + dct_question(PENDING)。Followup/NL2SQL 澄清/实体改写可能打断让用户选义项，但屏幕上的问句和 tool 的 query 字段保持原文，glossary 只进 hidden system。Lead 按 Q&A Skill 决定查库、查文档或双路。工具返回后 SSE 给前端；after_agent 解析章节和图表。前端用 React Query 轮询问题树，不只依赖 onFinish。

#### Q14. 为什么用中间件而不是全写进 System Prompt？

Prompt 不可靠：澄清必须能挂起 run、写 checkpoint、恢复；落库必须有 user_id；非法 tool call 要剥掉重试；上下文截断不能改 checkpoint 里的真实消息。这些是图节点上的副作用和中断，Prompt 做不到幂等和可测。Prompt 负责风格和 Skill 契约，中间件负责机制。

#### Q15. Skill 和 Tool 有什么区别？

Tool 是可调用函数（database_query、rag_file_search、bash）。Skill 是给模型加载的决策与操作合同（何时用、禁止什么、如何融合证据）。例如 question-and-answer 自己不跑 SQL，只规定默认同查库和文档。toolbox-titer 则禁止 database_query，强制沙箱读 BioFoundry 表。面试官若问「Skill 是不是多包一层 Tool」——不是，是路由和约束。

#### Q16. 为什么工艺推荐不走 Wren？

PRC/PEV 依赖预训练模型和历史配对特征，不是「一张汇总表的 NL2SQL」。Wren 回答不了 cosine 相似对照和模型推理。所以 Skill + 沙箱 python3，依赖预装在镜像里的 pandas/psycopg，禁止运行时 pip。和 Wren 分轨是为了口径正确，不是炫技。

#### Q17. 沙箱里你踩过什么坑？（STAR，个人贡献）

技能目录在沙箱里常是只读；PEV 要给大量 lookup_id 建特征缓存，写进技能目录会失败，写 /tmp 换容器就没了。做法是宿主机目录挂到 /mnt/pev-cache，用环境变量指定缓存路径。另外解释器必须 python3，不能绑本机 conda。这是把离线数据科学资产接到 Agent 的典型工程问题。

#### Q18. 多步 SQL / 子问题怎么调度？

有 completion-driven 的顺序 DAG：子步骤在自己的依赖完成后就可以启动，不必等无关步骤。空上游有稳定错误码（upstream_empty 等）。compaction 只保留有界摘要，不能把逐步原始 SQL 和全量格子塞回上下文。失败重试后失败结果不能进最终总结。这些都是生产上「看起来会规划、实际会把脏数据编进答案」的坑。

#### Q19. 模型乱调工具、死循环怎么办？

有 LoopDetection、非法 tool call 先 nudge 再失败、DanglingToolCall 补齐历史、StrictWrenRouting 把内部数据问题按到 database_query、Clarification 放在链末拦截。最终空答案且无合法证据时 persistence 会拒写。不是靠「再写一句 please use the tool」。

### 8.4 数据、NL2SQL、RAG、图表

#### Q20. 你们的数据在哪？有几类？

四类：① 业务事实——Wren 连的工艺汇总表，以及 BioFoundry ev_dt / preprocessed_dt；② 语义元数据——MDL、词典、SQL-pair、加密连接串；③ 对话产物——dct_*；④ 文档——COS + Qdrant chunk。Postgres 被 Prisma、DCT、Wren 元数据共库，后端禁止擅自 CREATE TABLE。Wren 记忆在 LanceDB，文档向量在 Qdrant，不要说成一个向量库。

#### Q21. 为什么不让 LLM 直接写 SQL？

表多、同义字段多、批次号有 X/Y 后缀、Postgres 不接受 CAST(... AS DOUBLE)。裸 SQL 会选错表、错 JOIN、类型报错。MDL 提供业务名；生成后 dry_plan；列守卫对确定缺失失败、解析不确定则 fail-open；数值用 DOUBLE PRECISION。LLM 负责规划，引擎负责契约。

#### Q22. 实体歧义怎么处理？用户说「那个细胞库」怎么办？

词典扫描字面量，对不上就打断澄清。Resolved 标注只进最新 HumanMessage 的 hidden entity_context，不改可见内容和 tool query。这是为了归档与评测仍是用户原话，同时模型能看见 glossary。字典命中不能当成「只查这一张表」的授权。

#### Q23. 库表答案和 PDF 冲突怎么办？

Q&A Skill 默认双路。回答必须分栏：数据库证据、文档证据、缺失、冲突。分子类型等禁止从 protein/titer 等词推断，文档没写就 N/A。引用带文件名和页码。这是管理层「可解释、可审计」的产品约束。

#### Q24. RAG 流水线怎么做的？为什么 PDF 要页级混合解析？

工艺 PDF 里文字页和图表页混排。文字页直出，图表页走 Vision OCR，否则检索要么丢图要么噪声极大。Office 转 PDF，视频走转写 Markdown，再切片进 Qdrant dense+BM25。现状单 corpus 共享是产品债。视频 ingest 有 COS 断点、sidecar（DOCX/PPTX）、单 worker 限制（分析限流是进程内的）。

#### Q25. 图表为什么不用 matplotlib？

数据库问答的图必须进  的 Vega enrichment，才能落 dct_chart、前端统一渲染、钉看板。静图 PNG 进沙箱输出既不可交互，也破坏契约。Skill 里若需要科学作图是另一条轨道，和 Wren 报表要分开。早期我改过 titer 的 BoxPlot+jitter schema 和 SQL 必带列，就是为了前后端口径一致、图不会空或错编码。

#### Q26. 空数据、失败 SQL 怎么展示？

空数据不应出 chart；图表类型若用户显式指定应尽量保留，多 section 时不要用硬编码指标别名乱推断；失败要警告并在自动 fallback 时排除失败类型，避免默默画出另一种图。失败重试结果不能混进总结。这些都是「看起来有图、其实在撒谎」的事故模式。

### 8.5 质量、评测、协同

#### Q27. 怎么证明 Agent 变好了而不是 prompt 碰巧？

有独立 eval-service、金标集 eval_golden_set、run 级 dct_eval_evidence（不回给业务 API）。后端有大量契约测试：实体改写、SQL 方言、列守卫、多步 binding、chart parity、harness 边界。好的指标不只是「SQL 能跑」，还包括证据是否 value-free、compaction 是否越界、冲突是否标注。

#### Q28. 和开源 DeerFlow 的关系？你们改了什么？

DeerFlow 提供 super agent harness。DCT 加了：deerflow.dct 持久化内核、Wren 内化与 database_query 契约、Q&A/工艺 Skills、实体/NL2SQL 澄清中间件、file-search 集成、前端问题树与 Vega、药明鉴权与部署。上游可吸收更新要单独评估，不能无脑 rebase。

#### Q29. 你在项目里具体做什么？和别人怎么分工？

git 上我可见的提交集中在：Wren 时期 titer 图表/SQL 必带列与追问推荐；toolbox-titer 与 toolbox-batch-process-recommendation（PRC/PEV 脚本、db 配置、沙箱缓存、顺序执行与错误处理）。平台内核、Wren 内化、RAG、鉴权是团队同事为主。协作方式：Skill 契约与语义层契约先对齐，避免工艺脚本和 NL2SQL 抢同一张表。

#### Q30. 最大的技术挑战是什么？

选你真正做过的讲透。推荐两条：① 把 PRC/PEV 离线模型接到只读沙箱，解决缓存持久化与禁止 pip；② 语义层输出必须满足前端 Vega/SQL 列契约，而不是模型「看起来对」。若被问团队挑战，讲 Wren 内化时保持 database_query 契约、以及落库依赖 user_id 注入。

#### Q31. 如果线上「有回答但没有报告/问题树」，你怎么查？

按顺序：① 这次 run 的 context 有没有 user_id（BFF 是否注入）；② dct_question 是否停在 PENDING、after_agent 是否走到 persist；③ 最终消息是否被 persistence 判为空/非法 tool call；④ 前端轮询的 thread_id 是否已从 onCreated 回填。不要先去调 prompt。

#### Q32. 你还缺什么经验？怎么补？

可以说：多租户隔离还没落地，生产 Gateway 管理面鉴权我更多是读现状而非主导改造；评测体系参与有限。补法：把 workspace 设计稿讲清楚，并主张评测加上冲突标注。面试官听的是自知，不是谦虚套话。

### 8.6 可能的追问速查（短答）

| 追问 | 短答 |
|------|------|
| 用的什么模型？ | 走 LiteLLM/公司 AI Gateway，可配多模型；摘要用轻量且 nostream，避免污染用户 SSE。 |
| Checkpoint 存在哪？ | LangGraph checkpointer（配置决定）；Run 另有 runs 表做跨 Pod lease。 |
| 记忆呢？ | 会话 checkpoint + MemoryMiddleware；Wren 侧 LanceDB；全局 memory.json 仍是治理债。 |
| 为什么 Vega 不是 ECharts？ | 与 enrichment 产出的 Vega-Lite spec 对齐，便于校验、禁外链、前端统一编译。 |
| 批次号 X/Y 是什么？ | JOIN 两侧规范化去掉末尾 X/Y，但不能当普通 filter 乱切。 |
| 为什么 Gateway 还留 execution_mode=http？ | 遗留旁路，默认 in_process，别当成现行架构。 |
| 你能写 SQL 吗？ | 能讲清 MDL 与物理表差异、DOUBLE PRECISION、禁止选错表；具体表以词典/SCHEMA 为准，不装成背全库。 |

### 8.7 不该说的话

- 「Gateway 已经完整鉴权。」「文件按用户隔离了。」
- 「LLM 直接查生产库，有 prompt 就行。」
- 泄露内网 Gateway 地址、API Key、客户项目号细节。
- 把 V2 外部 Wren 架构讲成当前实现。

## 10. Agent 架构师（A1–A90）

**本节目录**：10.1–10.6（A1–A30）→ 10.7 白板 → 10.8 说明 → 10.9–10.18（A31–A90）→ 10.19 速查 → 10.20 雷区

面向「Agent 架构师 / AI 平台架构 / 企业 Agent Runtime」岗位。面试官通常不满足于「我们用了 LangGraph」，而会追问：控制面与执行面如何切、契约如何版本化、失败如何成为状态机、自治与确定性如何配比、如何避免把 Prompt 当成架构。

口述结构建议仍是：结论 → **X-Agent 里**怎么落地 → 代价与若重来会怎么改。第 8 节偏「这个项目」；本节偏「你作为架构师如何决策」。V2 文档里「不要整体上 LangGraph、自研 Orchestrator」是历史决策；现状主编排已是 DeerFlow lead_agent。面试时主动点破世代，避免被旧稿带偏。

### 10.1 架构定位与选型

#### A1. 什么是企业级 Agent 架构？和「做一个能调工具的 Chatbot」差在哪？

企业级 Agent 是带状态的工作系统：有身份、有工具契约、有可中断的人机回路、有一等公民的产物（Artifact）、有评测与审计，而不是一次 HTTP 里把 function call 跑完。Chatbot 优化的是回复质量；平台优化的是 Run 生命周期（创建、挂起、恢复、取消、落库、计费）。DCT 用 Thread + Run + dct_question 把一次提问变成可回放对象，这才是架构差异。

#### A2. 你会怎么给 Agent 平台分层？

四层，禁止混写：

| 层 | 职责 | X-Agent 对应 |
|----|------|----------|
| 体验 / BFF | 鉴权、注入身份、聚合问题树 | Next.js |
| 控制面 | Thread/Run/取消/lease、管理 API | Gateway + `runs` 表 |
| 执行面 | 模型循环、中间件、工具、沙箱 | Harness `lead_agent` |
| 能力面 | 语义取数、RAG、领域 Skill | Wren / file-search / `skills` |

架构师的工作是定义层间契约（谁拥有 user_id、谁拥有 SQL 真源、谁拥有图表 spec），而不是选一个框架名。Harness 禁止 import App，就是在用编译期约束守住这张图。

#### A3. ReAct 单循环、固定 Workflow、两者混合，你怎么选？

固定 DAG：步骤已知、要审计每步 I/O、失败可重放（ETL、批评分）。

ReAct：路由未知、要澄清、工具集随 Skill 变化（DCT 主对话）。

混合：外层 Agent 决定「要不要走库/文档/工艺 Skill」，内层对 SQL 用有依赖的多步计划（DCT 的 query plan / sequential DAG）。

X-Agent 用混合是对的：完全固定 DAG 接不住实体澄清；完全自由 ReAct 接不住「图表必须是 Vega、SQL 必须过 MDL」。架构师要能说出哪一段必须确定性、哪一段允许模型探索。

#### A4. 早期文档说不要整体迁 LangGraph，现在却用了。你如何评价这次架构转向？

当时缺口是 Thread/Artifact/审计，栈还在 Wren pipeline 上，整体换编排器风险是「三套编排并存」。后来产品变成真正的多轮 Agent，DeerFlow 提供了 checkpoint、SSE、中间件、沙箱，自研 Orchestrator 的 ROI 变差。正确叙事不是「选错了再推翻」，而是 编排器是手段，产物模型和治理才是目的；当执行面复杂度超过自研 workflow.py，就该换执行引擎，但 database_query 契约和 dct_ 模型要留下*。这题考你是否会为框架而框架。

#### A5. 什么时候不该用 Agent？

口径稳定、输入输出 schema 固定、延迟要 <300ms、必须比特级可复现：用普通 API + 规则/SQL 模板。Agent 适合路由不确定、需要工具组合、允许 10s–分钟级、失败可澄清的任务。DCT 的 Dashboard KPI 若能写死查询，就不该每刷一次都走 lead_agent。架构师要会砍 Agent 范围，这比会加 Agent 更重要。

### 10.2 控制面：Run、状态、中断

#### A6. 请设计 Agent Run 的状态机。

至少：pending → running → (interrupted | success | failed | cancelled)。interrupted 用于澄清/实体选择，必须可 resume，且 resume 不改用户可见原问句。取消与失败要解耦：cancel_requested_at 不是终态本身。跨 Pod 要有 owner_pod_id + lease，超时回收，避免双跑。DCT 的 runs 表已经在朝这个方向：operation_kind 区分真 run 与 checkpoint 预约，finalizing 窗口互斥。面试时补一句：SSE 断线策略（cancel vs 后台继续）是产品决策，必须写进契约，不能靠默认。

#### A7. Human-in-the-loop 在图里怎么放，才不会把业务状态弄脏？

原则：打断是执行面事件，业务真源仍是用户原文 + 单独的 annotation。**X-Agent** 把 glossary 放进 additional_kwargs.entity_context，不改 HumanMessage.content，也不改 checkpoint 里的 tool 参数（对模型的 hidden 参数用深拷贝注入）。错误设计是直接 rewrite 用户问题再存档——评测、合规、落库会对不上。澄清中间件必须能 commit 到 checkpoint 再 suspend，顺序（NL2SQL 澄清在 EntityRewrite 前）是架构，不是风格。

#### A8. Checkpoint、业务库、向量库各存什么？为什么不能只存一份？

| 存储 | 存什么 | 不存什么 |
|------|--------|----------|
| Checkpointer | 消息、tool 轨迹、图位置 | 权限源、报表真源 |
| `dct_*` | UI/审计的结构化产物 | 全部 SSE 帧镜像 |
| Qdrant | 文档 chunk | 业务指标库 |
| LanceDB | Wren 语义记忆 | 与 file RAG 混 collection |

「单一存储简化架构」在 Agent 里通常是错的：恢复执行、展示报告、检索文档的一致性模型不同。架构师要定义 哪一份在冲突时说了算（指标以 SQL 结果为准，报告以 persist 后的 section 为准，聊天回放以 checkpoint 为准）。

#### A9. 流式（SSE）在架构上的陷阱？

三类流不能混：① 用户可见 token；② 工具/子图事件；③ 侧信道（摘要模型、内部 nudge）。DCT 给 summarization 打 nostream，就是防污染。可恢复流要有 thread_id 回填（onCreated）和 join。前端问题树不该只信 onFinish，因为图表 enrichment 是异步于文本结束的。架构上把「文本完成」和「产物就绪」做成不同信号（chart_enrichment_status），这是对的。

### 10.3 工具、Skill、契约

#### A10. 如何设计 Tool 契约，让消费方不绑死模型？

Tool 是平台 API：稳定的名字、JSON schema、错误码、幂等语义、体积上限。DCT 把细粒度 Wren 子能力聚合成 database_query，输出 status/sub_results/partial_failures，图表和 parser 只认这一层。内化 Wren 时引擎换了，契约没换——这是架构胜利。反面教材是让每个中间件去 parse 模型自然语言。版本策略：加字段要可忽略，删字段/改语义要新工具名或显式 version，因为 checkpoint 里躺着旧 call。

#### A11. 工具是多了好还是少了好？

模型的工具选择错误率随数量和描述重叠上升。架构原则：对外少、对内可拆。 路由用 Skill 合同（Q&A vs titer vs PRC），执行用少数量工具。disallowed-tools 是负向契约，比再写一段 prompt 更硬。超过阈值就做 tool search / deferred schema（DCT 已有 DeferredToolFilter 的位置），而不是一次 bind 80 个工具。

#### A12. Skill 在架构里是什么？会不会变成又一套微服务？

Skill 应是 策略与运行手册（何时用、数据源、禁令），不是新的 RPC 服务。它改变的是模型可见的指令和允许的工具集，执行仍走统一 Runtime（沙箱/Wren/RAG）。变成微服务的信号是：Skill 自己起端口、自己管鉴权、自己定义另一套 thread。DCT 的 toolbox Skill 走沙箱脚本，仍在同一 lead_agent 生命周期里，这是合适的。治理上要有安装鉴权、签名包、全局 vs 租户启用——现状偏弱，架构师面试要主动提。

#### A13. 领域模型（PRC）和通用 NL2SQL 为什么必须分轨？画一下决策树。

```text
绑定 cultureid + 预训练响应模型？
  是 → Skill/沙箱（禁 database_query）
  否 → 问内部汇总表？
         是 → Wren database_query（MDL + 护栏）
         否 → 问文档/选定 references？
                是 → RAG
                都可能 → Q&A 双路 + 冲突标注
```

分轨的本质是 语义所有权：MDL 拥有「项目 titer 汇总」；SCHEMA.md 拥有「培养时序列单位」；pkl 拥有「推荐策略」。让一个 LLM 跨过所有权去猜 JOIN，是架构失败。

### 10.4 上下文、记忆、检索

#### A14. Context Engineering 你的原则是什么？

上下文是稀缺预算，不是日志桶。分层：① 系统契约（短、稳定）；② 本轮 Skill；③ 隐藏 glossary；④ 压缩后的工具结果（有界、无原始 SQL 格子）；⑤ 对话摘要。截断只切发给模型的副本，不改 checkpoint（DCT ContextTruncation）。多步 SQL 的 compaction 必须每步都有摘要，否则 Agent 会「遗忘自己刚查出的空结果」。架构师要规定 什么永远不准进模型上下文（PII 全量、原始单元格、密钥）。

#### A15. 记忆怎么分层，才不会变成提示注入面？

- **工作记忆**：checkpoint（本 thread）
- **过程记忆**：todo/plan（可选）
- **语义记忆**：Wren LanceDB / 词典（要租户范围）
- **长期偏好**：per-user；不可被任意 tool 写入系统层
- **X-Agent 债**：全局 `memory.json` 无 owner——任一写入可影响所有用户下一轮。方向：记忆 API 走 verified actor、按 user/workspace 分区、高危 import 要 RBAC。可归属、可撤销、可审计优先于「越大越好」。

#### A16. RAG 在 Agent 里应该是工具还是默认前置检索？

默认前置适合「每问必查文档」的产品；工具化适合「有时查库有时查文档」。DCT 用 Skill 把默认双路写成合同，但执行仍是工具调用，这样能被轨迹、评测、compaction 看见。纯前置检索的问题是：路由不可见、失败难标 partial。纯工具的问题是：模型偷懒不调。折中是 冻结本轮 route profile（DCT 在 make_lead_agent 里 freeze qa_execution_profile），运行中途不许模型改「这轮该不该查库」。这是架构级的确定性注入。

#### A17. 多源融合（库 + 文档）的架构原则？

融合发生在回答层，不是检索层把分数加起来。两边检索独立、证据类型打标、冲突显式、禁止跨源推断（分子类型）。图表只允许数据库 enrichment 管线产出。评测要对「冲突是否标出」打分，否则优化会偏向哪边召回高就信哪边。这是产品约束上升为架构：融合策略属于 Q&A Skill 合同，不属于某个模型的个人风格。

### 10.5 可靠性、安全、多租户

#### A18. Agent 的失败模型怎么设计？

把失败分成：模型失败、工具失败、契约失败、业务空结果。工具失败应变为 ToolMessage 而不是撑爆图；契约失败（非法 tool call、空答案无证据）应拒写 dct 并给安全错误；业务空结果是合法终态，要有 subreason（upstream_empty），禁止用另一张表「找点东西回来」。重试预算要有上限（DCT：非法 call 一次 nudge，第二次 InvalidFinalAnswer）。部分成功用 partial_failures 而不是全盘 500。架构师要让「空」和「错」在 API 上可区分。

#### A19. SQL Agent 的安全边界怎么画？

默认零信任：模型永远碰不到生产写权限。执行引擎只接受 SELECT、单语句、函数黑名单、行数与 timeout；dry_plan 先于 query。连接串加密、密钥不进 prompt。即使用户说「帮我 delete」，工具层无此 capability。沙箱轨同样：预装依赖、禁 pip、只读技能目录、可写卷白名单。Prompt 里的「你是只读助手」只是提示，能力面不存在的工具才是控制。

#### A20. Prompt injection 从哪进来，架构怎么防？

来源：上传文档、工具返回、记忆、MCP 第三方。原则：检索内容当数据不当指令；引用要可追溯；高权限工具（bash、MCP 写配置）与不可信内容隔离。DCT 文档进 RAG、SQL 结果进 compact 摘要，都是降权。未完成的是：共享 corpus 意味着租户 A 的文档可污染租户 B 的检索——这是注入的产品级放大，要用 workspace collection 切开。面试官要听的是 信任边界图画得清。

#### A21. 多租户你怎么切数据面？

至少四层命名空间：Tenant → Workspace → Corpus/Collection → Document。身份在 BFF 验证，Gateway 二次校验，检索带 corpus 强制过滤，禁止「默认 default」。对象存储 key 带租户前缀。评估：逻辑隔离够不够取决于数据敏感度；工艺文档通常要到 collection 级物理隔离。DCT 现状是单 corpus，设计稿已有路径。架构师落地顺序：先封共享删除/全局记忆，再迁 collection，最后才做漂亮的 Workspace UI。

#### A22. 水平扩展时 Agent 平台最容易踩什么？

① 进程内限流/缓存当全局（DCT 视频分析 limiter 要求 Gateway 单 worker）；② 沙箱与本地盘；③ 内存 mutation gate；④ checkpointer 与 lease 双跑；⑤ 单机 artifact 卷。扩展策略应按工作负载拆：无状态 Gateway 副本可以多，带本地状态的 ingest/sandbox 要 sticky 或外置状态。面试时主动提「哪些组件 fail-fast 禁止多副本」，比空谈 K8s 更像架构师。

### 10.6 模型、评测、可观测、组织

#### A23. Model Gateway 在架构里做什么？

统一：鉴权、路由、超时、降级、限流、成本标签、禁用思考模型误开 thinking。业务 Agent 只认逻辑模型名。侧信道调用（摘要、标题）用便宜模型且 nostream。Q&A 的 lead 模型可按 profile 冻结，避免中途换模型导致工具风格漂移。不要让每个中间件自己 new 一个 SDK。

#### A24. 评测如何成为架构的一部分，而不是上线后的脚本？

金标问题进独立服务；raw evidence 进只读表且不进业务 API；契约测试锁「不该变的不变量」（query 字节不变、harness 不 import app）。评测维度要覆盖：SQL 正确、图表类型、冲突标注、拒答、延迟与成本。没有 eval 闸门的 Agent 迭代 = 随机游走。架构师应要求：改 Skill 合同和改 tool schema 必须带回归集。

#### A25. Trace 里你必须能回答哪五个问题？

这轮 route profile 是什么；调了哪些工具、参数是否被 hidden 注入；在哪次 interrupt resume；persist 写了哪些 section/chart；花费多少 token。缺任何一项都无法做事故复盘。语义 run_events 优于保存全部 SSE。注意 value-free：trace 也不该把业务单元格打到日志中心。

#### A26. 单 Lead + 工具 vs 多 Subagent，怎么选？

默认单 Lead：延迟、一致性、调试成本都更低。Subagent 只用于可并行、上下文互不需要细粒度共享的子任务（大文档分片、独立调研），并硬限制并发（DCT SubagentLimit）。合成阶段必须回到 Lead，且引用/语言对齐要用用户原问而不是委派 prompt。多 Agent 不是高级，是成本；说不清共享状态就不许拆。

#### A27. 若让你为新业务加一条「风险归因工作流」，架构步骤是什么？

不要先画新图框架。① 定义输入输出 Artifact（风险列表、因子表、建议章节）进 dct_section schema；② 决定数据所有权（Wren 还是 Skill）；③ 写成 Skill 合同 + 必要工具；④ 补澄清点（实体、阈值）；⑤ 金标与冲突用例；⑥ 权限与审计字段。只有当状态机比 ReAct 更简单时才抽固定子图。这是「平台可扩展」的检验。

#### A28. 你如何带一个 Agent 平台团队？边界怎么拆？

建议四队对齐四层：体验（BFF/问题树）、Runtime（中间件/Run）、Data 能力（MDL/RAG）、领域 Skill（工艺）。契约 Owner 必须唯一：database_query payload 不能三队各改一版。平台团队提供护栏与评测，领域团队不直接碰 harness 边界。这题看你会不会用康威定律，而不是堆人堆 prompt。

#### A29. 12 个月技术演进你怎么排？

P0 治理：Gateway 二次鉴权、workspace corpus、记忆分区。P0 可靠性：多副本状态外置、ingest 与 Gateway 扩缩容策略写进 runbook。P1 质量：评测含融合/冲突、Skill 门控。P1 产物：报告导出与 Dashboard 真源仍走 dct_*。P2 才是更多模型、更多 Agent 角色。架构师的 roadmap 以风险和契约排序，不以 Demo 酷炫排序。

#### A30. 如果只能改 X-Agent 的三件事，你改哪三件？为什么？

身份与租户贯穿执行面（user_id/workspace_id 进所有检索与落库，消除静默 skip 与共享 corpus）。

把 Tool/Skill/产物 schema 当成公开 API 做版本与兼容测试（这是平台能活过一次引擎替换的原因，Wren 内化已经证明）。

把「空/冲突/部分失败」提升为一等公民（错误码、UI、评测同一套）。

不选「换更强模型」或「再写一个编排器」——那是能力幻觉，不是架构。

### 10.7 架构师现场白板：DCT 一分钟版

```text
Client → BFF(Auth) → Control Plane(Run/Thread)
                          ↓
              Execution (lead_agent middleware)
                ├─ Policy: Skill + route profile
                ├─ Tools: database_query | rag | sandbox
                ├─ Interrupt: clarify / entity
                └─ Persist: dct_question/section/chart
                          ↓
              Data: PG(MDL+dct) | Qdrant | LanceDB | COS
```

面试官让你「设计一个企业 Agent」时，先画这张，再往各框填 SLO、契约和失败码。先画模型圆圈的，通常不是架构师。

### 10.8 追加题说明

以下为架构师岗仍高频出现的追问（A31–A90），按主题追加。A1–A30 不重复；答题仍用「结论 → **X-Agent 怎么落地** → 代价 / 若重来」。

### 10.9 框架、协议与 Build vs Buy

#### A31. LangGraph、Temporal、自研状态机，怎么选主编排？

LangGraph 适合「模型循环 + 工具 + 可中断 HITL + checkpoint」的短中时延对话（秒到数分钟）。Temporal 适合「跨小时/天、要精确重试与补偿、活动是确定性代码」的长事务（审批、批次回算）。自研状态机只在步骤极少且不想引入依赖时。DCT 主路径是对话 Agent → LangGraph/DeerFlow；若以后做「报告定时生成 + 人工签字」，审批段可以 Temporal，不要把 LLM 循环塞进 Temporal activity 里当 Chat。混用标志：LLM 循环用图，业务长事务用工作流引擎，中间用 Run id 关联。

#### A32. 为什么不是 CrewAI / AutoGen / 纯 OpenAI Assistants API？

多角色框架默认假设「多个 LLM 互相对话」，企业里会放大延迟、成本和不可复现性，且工具治理弱。Assistants API 把线程与工具锁在供应商控制面，checkpoint、落库、SQL 护栏、Casbin 都难插入。DeerFlow 的价值是 可自托管的执行面 + 中间件插入点。可以兼容 OpenAI 协议当接入层，但不能把控制面外包。

#### A33. MCP 在架构里扮演什么？和 Function Calling、OpenAPI Tool 的关系？

Function Calling 是模型与运行时的调用约定。OpenAPI 是内部已有 HTTP 能力的描述。MCP 是跨进程工具总线（独立生命周期、可替换实现）。原则：核心、高敏、高 QPS 能力（database_query、RAG）留 in-process；外围、多语言、实验性工具走 MCP。DCT 已有 MCP 配置面，但配置全局无 owner——必须把 MCP 当代码执行面：安装、stdio、header 密钥都要 RBAC 和脱敏。协议热不等于核心路径都该 MCP。

#### A34. A2A / Agent 互调协议要不要上？

组织内多个 Agent 产品要协作时才需要；先共享 同一控制面（身份、trace、工具契约） 比上新协议重要。两个 lead_agent 互调很容易递归打爆预算。DCT 更合理的边界是：一个 Lead，子任务用受限 Subagent 或普通工具，而不是 Agent 网。

#### A35. 继续用开源 DeerFlow 还是 fork 成内部框架？

Harness 边界保持可同步上游；DCT 特有（deerflow.dct、wren_ai、Skills）放在明确扩展点，不要改到无法 rebase。Wren 内化已经是一次「吸收上游、冻结对外契约」。治理方式是 吸收清单 + 契约测试，而不是无脑跟版或彻底分叉。

#### A36. Semantic Kernel / ADK / 自研 Python agent loop 呢？

能插入中间件、可中断、可 checkpoint、工具 schema 一等公民，就可以。DCT 选 LangGraph 生态是因为 SSE/协议/前端 SDK 已对齐。换框架的成本在迁移 checkpoint 与工具契约，不在「循环怎么写」。

### 10.10 规划模式、结构化输出与确定性

#### A37. ReAct、Plan-and-Execute、ReWOO、LAT，生产怎么配？

ReAct：工具结果强依赖、要澄清。Plan-and-Execute：步骤可预告（plan mode + Todo）。ReWOO：先规划证据需求再并行取证，适合  双路检索。LAT/辩论：成本高，留给评测或高价值归因，不进默认路径。DCT 已是 冻结 route profile + 可选 todo + 多步 SQL DAG，不必再套一个论文名。

#### A38. 要不要强制模型先输出 JSON 计划再执行？

对「必须审计步骤」的流程（风险报告章节）值得；对「先澄清实体」的流程会增加一轮延迟且计划常过期。更好的是 平台生成计划骨架（路由/依赖），模型填参数。SQL 侧  已有 query planner；对话侧不要让模型同时发明章节结构和 SQL。

#### A39. 结构化输出、JSON Schema、语法约束 SQL，怎么用？

图表 spec、section 列表、工具参数：用 schema / constrained decoding，失败可重试一次。自然语言结论：不要塞进同一个 JSON，以免模型为了凑 schema 牺牲证据。SQL：文法约束减少语法错，语义错仍要 MDL + dry_plan。约束解码不是语义层的替代品。

#### A40. 温度、采样、可复现性如何作为架构约束？

取数、路由、工具参数：低温度或冻结 profile。措辞可略高。评测与金标回放：固定 seed/模型版本。把「本轮 execution profile」写入 runs.metadata，事故才能复现。不要承诺比特级可复现 LLM，但要承诺 工具入参与 SQL 可复现。

#### A41. 并行 tool call 与依赖 tool call 怎么调度？

无依赖（库 + 文档）可并行。有依赖（先批次列表再下钻）必须 DAG，完成驱动而不是全局 barrier。DCT 多步 SQL 已按依赖完成调度。错误是用 prompt 写「你可以并行」而不在运行时做依赖检查。并行度要有上限。

#### A42. Code Interpreter / 写 Python 当万能工具，行不行？

沙箱代码是逃生舱，不是默认取数平面。一默认「模型写 pandas」，MDL、权限、审计、Vega 契约全部失效。DCT 分轨：Wren 报表禁 matplotlib；工艺 Skill 才允许预装环境里的 Python。规定：代码执行的输入必须是已授权数据快照，输出必须过体积与类型门。

#### A43. 要不要 Fine-tune？和 RAG、Skill、MDL 怎么排？

优先顺序：契约与护栏 → Skill/MDL 口径 → RAG 证据 → 路由小模型 → 最后才 SFT。工艺推荐已经用 pkl 模型当工具，比微调聊天模型更可审计。微调适合稳定分类/路由，不适合把「哪张表」背进权重——表会变。

### 10.11 可靠性、一致性、容量与发布

#### A44. Checkpoint 与 dct_ 双写如何保证用户看到的一致？

双写问题：SSE 已把答案推到浏览器，persist 可能失败。策略：① persist 失败则 question 保持非 READY，前端显示「报告生成中/失败」；② persist 必须幂等（同一 run_id 重建 section）；③ 不以 checkpoint 当报表真源。DCT 已有 enrichment 状态机，要把「文本完成 ≠ 产物就绪」当成 UX 契约。更强方案：outbox（run_events 已是雏形）+ 补偿任务。

#### A45. 同一 Thread 多 Tab / 连发，怎么设计？

必须有 multitask 策略：reject / interrupt / enqueue。DCT runs.multitask_strategy 默认 reject 合理，避免两套工具轨迹交叉污染 checkpoint。排队要有公平性：交互优先于 eval 批量。不要靠前端 debounce 当互斥。

#### A46. 客户端断开后 Run 继续还是取消？

产品选项，必须显式：on_disconnect=cancel | continue。长报告可能 continue；澄清等待应 cancel 或超时回收 lease。断开 ≠ 失败终态，要有 reaper。计费与沙箱占用按 continue 计算，否则漏账。

#### A47. 幂等、重试、死信怎么做？

工具按语义分类：只读可重试；写操作不可自动重试除非幂等键。LLM 可 hedged/降级，但要防双计费。ingest、视频转写用 checkpoint_attempt / execution_epoch。死信进可重放队列。Poison 消息要熔断该 Skill，而不是打满重试。

#### A48. 给 Agent 定什么 SLI/SLO？

不要只定「可用性 99.9%」。建议：交互首 token 时延；端到端 P95（含工具）；工具错误率（契约失败 vs 业务空）；persist 成功率；幻觉投诉率；单问成本 P95；澄清率。空结果只要错误码正确可计成功。Agent 不确定性下 SLO 是区间不是幻数。

#### A49. 限流、配额、吵闹邻居？

按 tenant/user/skill 三维 token 桶；危险工具单独 bulkhead；RAG ingest 与交互查询隔离队列。DCT 视频分析进程内限流导致单 worker——扩展必须先外置计数器。成本硬顶比软提示重要：超预算应 interrupt 并写可见原因。

#### A50. 缓存：精确、语义、Prompt cache，各用在哪？

精确缓存：同一 SQL、同一文档版本检索。语义缓存：只用于非关键闲聊，工艺数字禁止。Prompt/前缀缓存：系统提示 + Skill 稳定前缀。缓存键必须含：模型版本、MDL 版本、corpus 版本、locale。按租户隔离防投毒。

#### A51. LLM 熔断、降级、hedged request？

超时 → 备用模型（工具 schema 必须兼容）。连续错误 → 熔断该 provider。Hedged 只对只读且能去重的调用。降级路径预定义：仅 RAG、仅缓存报表、或「系统繁忙请缩小问题」。禁止降级成「解除 SQL 护栏」。

#### A52. Skill/Prompt 怎么做灰度与回滚？

Skill 当配置发布：版本号、签名、比例放量、一键 kill switch。Shadow mode（DCT NL2SQL 澄清已有）：新策略只记日志不打断。Prompt 变更走评审 + 金标闸门。执行面只拉「已发布版本」，禁止无人知晓地热改生产提示词。

#### A53. 如何对非确定性系统做测试金字塔？

底层：契约测试（字节级不变量、harness 边界、SQL 方言）。中层：固定轨迹 replay。上层：小金标 + LLM-as-judge（只评冲突标注/格式，不评文采）。禁止用 judge 给自己的 SQL 打满分当回归。Eval 集要防泄漏进 prompt/记忆。

### 10.12 安全进阶、身份、药企合规

#### A54. 工具层的 Confused Deputy / SSRF 怎么防？

Agent 拿着服务身份去调内部网：必须 audience 分离（file-search、OnlyOffice、RAG rebuild 不能互冒）。禁止模型指定任意 URL 给抓取工具。沙箱无出站或出站 allowlist。上传回调验签。经典 deputy：用户话术驱动高权身份。

#### A55. Casbin 全局 RBAC vs 工具级授权，差在哪？

页面能进工作台 ≠ 能跑 bash 或装 MCP。应 RBAC + 工具 capability：每类工具声明所需 permission，middleware 在 bind 前过滤。DCT 前端 Casbin 较强、Gateway 管理面较弱，缺口在「执行面未复用同一策略引擎」。Workspace 设计要把 Casbin 升到 domain=workspace_id，而不是抄 RAGFlow 的 tenant==user。

#### A56. 沙箱威胁模型？K8s provisioner 什么时候要？

本地沙箱：文件系统逃逸、吃光磁盘/CPU、读技能目录密钥。缓解：只读挂载、seccomp、cpu/mem/pid 限额、禁 pip、密钥注入。多租户不信任代码时上 K8s provisioner（DCT 已有可选 profile）。工艺 pkl 推理也应视为不可信二进制，限制网络。

#### A57. 检查点、对话、SQL 结果里的 PII 怎么办？

分类：标识、工艺参数、客户名。策略：进模型前脱敏或截断；trace value-free；落库最小必要；导出水印与权限。删除权：thread + checkpoint + 向量点 + 记忆都要能按 user/thread 擦除。「遗忘」是跨存储事务，不是删 UI 行。

#### A58. 药企场景还要多说什么（GxP / 审计）？

计算机化系统要 变更控制：Skill、MDL、Prompt、模型版本进变更记录。决策用报告需要审计追踪（谁、何时、哪次 run、哪版 SQL）。persist 后的 section/chart 应视为快照，重跑是新版本。DCT 结构化落库是合规友好点；缺口是导出签名、不可篡改日志。明确：当前不是已认证 GxP 系统，但架构要能长出审计。

#### A59. 连接串轮换、MDL 变更、embedding 升级如何做不停机？

连接：Fernet 密钥轮换要批处理重加密。MDL：版本化部署，in-flight run 钉住开始时的 schema 版本。Embedding：双写或别名 collection，检索双路直到回填完成。任何全局单文件 config 热更新都要定义 in-flight 行为。

#### A60. 密钥与配置拓扑？

模型 key 只在 Gateway/LiteLLM；业务库密钥只在 Wren 连接加密列；沙箱只拿短时凭证。config.yaml / extensions_config.json gitignore 是对的，生产应用配置中心 + 审计。架构师要画 secret 流向图。

### 10.13 语义层、Text-to-SQL、指标架构

#### A61. Wren/MDL、dbt metrics、Cube、LookML，怎么放？

语义层解决「业务名 → 可执行查询」。dbt 更偏转换与治理仓；Cube/LookML 偏 BI 查询加速。Agent 需要 可被工具调用的、带关系与同义词的模型，Wren 更贴 Text-to-SQL。不要让 Agent 直接扫 information_schema。DCT 选 Wren 是因为 NL2SQL + 关系 + 知识指令；内化是为了运行时，不是否定语义层。

#### A62. Text-to-SQL 为什么在生产远难于 Spider/BIRD？

生产有同名列、脏值、权限、方言、批次号规则、空结果也是答案。Benchmark 假设 schema 小而干净。所以投资在 词典、澄清、列守卫、方言测试、JOIN 规范化，而不是更大模型。能讲「唯一高置信词典命中只做可见性、不授权锁表」，说明你懂 false precision。

#### A63. Schema linking、值召回、查询改写，各放哪一层？

Schema linking：MDL + 检索（LanceDB 记忆）+ 本轮词典。值召回：实体词典/澄清，禁止把全表 distinct 灌进 prompt。查询改写：followup 中间件可改写内部问法，归档仍用原文。分层错误是全塞进一条 super prompt。

#### A64. 自修正 SQL 循环如何防止空转？

dry_plan 错误结构化、value-free、有预算（次数与 token）。同一错误签名第二次应停并澄清或失败。DCT 强调 generation/correction/eval 共用契约。禁止「再试一遍」无记忆。

#### A65. 指标口径冲突（两张表两个 titer）谁说了算？

语义层 Owner（MDL + 指令 + SQL-pair）说了算，Skill 文档写清例外（BioFoundry 轨道）。Agent 不得平均两个口径。冲突时返回冲突标注，让人改 MDL。这是数据治理问题，不是模型问题。

#### A66. 查询治理：超时、扫描上限、只读副本？

Agent 流量与人用 BI 隔离：只读副本、statement_timeout、行数上限、禁止无过滤全表。高峰时拒收新 Agent SQL 并排队。WrenEngine.query 的护栏是产品特性不是实现细节。

### 10.14 RAG、文档、多模态进阶

#### A67. 长上下文能不能替代 RAG？

不能作为默认：成本、缓存失效、引用页码、权限过滤都变差。长上下文适合「用户本轮选定的少量文件」。DCT 的 selected_references 就是这个口子。架构：默认检索，显式引用可跳过广搜或收窄 filter。

#### A68. GraphRAG、知识图谱、MDL 何时用哪个？

MDL：表格指标与关系。RAG：非结构化规程/报告。图谱：多跳实体关系且边是一等公民。工艺控制塔先把 MDL+RAG 做好；图谱是第三数据面，需要主数据质量。不要用 GraphRAG 名字回避建语义层。

#### A69. Embedding 模型换代、分块策略、父块展开的架构约束？

chunk 与 parent 必须一起版本化（pipeline_version 写入 uploaded_document）。换 embedding 等于新 collection 或双向量。DCT 已把 parent_text 放 payload、混合 dense+BM25。权重与 rerank 是可配置策略，要进评测。

#### A70. 图片、表格、视频在 Agent 里怎么成为一等证据？

图片：视觉模型中间件（ViewImage）或页级 OCR。表格：尽量结构化进 SQL/XLSX 解析。视频：转写+时间戳引用，ingest 与问答限流隔离。引用必须能定位（页、时间）。多模态按需，不要默认进 lead 每次调用。

#### A71. OnlyOffice / 预览 在安全架构里的位置？

预览是独立信任域：短时 scoped token、DocumentServer JWT 与 Gateway 服务断言分离。不要把编辑器当 RAG 写入口。共享上传意味着 token 持有者能读文件——产品例外要写进威胁模型。

### 10.15 产物、前端、体验即架构

#### A72. Artifact 协议怎么设计？

统一块类型：text、table、chart、citation、clarification、action_item，带 schema 版本。DCT 用 section + chart_detail（Vega）。前端只消费协议，不 parse 模型 Markdown 当真源。导出 = 序列化同一协议。这正是 V2「Analysis Panel」要的东西，现状用 dct_* 部分满足。

#### A73. 为什么问题树要轮询而不是只靠 SSE？

产物异步（图表 enrichment）、刷新页面、多端。SSE 管对话；资源 GET 管报告。这是 CQRS：写在执行面，读在 BFF/Prisma。代价是短暂不一致，用 status 字段表达。强行一条 SSE 塞所有终态会让 enrichment 阻塞首屏。

#### A74. 语言对齐、单位、时区是不是小事？

不是。回答语言跟本轮用户问题走，不跟文档语言（LanguageAlignment）。单位在 SCHEMA/MDL，Agent 不得擅自换算。时区影响批次日界。评测要覆盖中英问句。

#### A75. 要不要给用户看置信度分数？

谨慎。校准极差的分数会制造过度信任。更好的是 证据类型 + 冲突 + 缺失。若要分数，只能来自可定义规则（检索分、是否唯一词典命中），并注明非概率。

### 10.16 成本、路由与小模型

#### A76. 如何做模型级联（FrugalGPT）？

分类/路由用小模型或规则；复杂归因用大模型；摘要用便宜模型且 nostream。DCT 已有 Q&A profile 冻结 lead 模型。关键是 工具 schema 兼容的模型才能降级，否则级联会破坏 function call。

#### A77. 成本归集怎么做才有管理意义？

按 user、workspace、thread、skill、模型、阶段（生成 SQL / 嵌入 / VLM）打点。DCT 文档 ingest 已有 token/人民币字段，对话侧 TokenUsageMiddleware 应对齐同一账本。Showback 给业务部门，才能反向约束「什么问题不该进 Agent」。

#### A78. 内部小模型做意图识别，替代 Skill 描述行不行？

可以做前置分类器降低 tool 误选，但要可回退到 Lead。训练集要覆盖工艺术语。不要让分类器直接触发写操作。DCT 更稳的是 UI 显式选 Skill + 合同，分类器作为辅助。

### 10.17 组织、供应商与平台化

#### A79. Agent 平台 vs 嵌入业务的 Agent 产品，团队怎么切？

平台：Runtime、护栏、评测、身份、可观测。产品：DCT 工艺口径、Skill、MDL、报告。产品团队通过契约扩展，不 fork 中间件链。若只有一个团队，用目录边界模拟，否则三个月后 Prompt 里会长出私有 SQL。

#### A80. 供应商锁定：模型、框架、向量库、语义引擎？

模型：OpenAI 兼容网关（LiteLLM 方向）。框架：状态导出能力。向量：标准 embedding 维度与重建剧本。语义引擎：database_query 契约是抗锁定层（Wren 内化已验证）。锁得最死的往往是 checkpoint 格式和前端协议，迁移预算要算这里。

#### A81. 要不要做内部 Skill 市场？

先做允许列表 + 评审 + 评测，再做市场。没有沙箱签名和数据分级就是影子 IT。DCT toolbox 已经是「领域插件」，治理应先于货架 UI。

### 10.18 现场设计题与事故题

#### A82. 白板：设计支撑 1k 并发会话的企业 Agent。

先拆交互与 ingest；Gateway 无状态可水平扩；checkpointer/Postgres/Qdrant 是瓶颈；Run lease 防双跑；沙箱池化；LLM 网关限流与排队；按租户配额；单 worker 组件（视频）单独服务化。给出 P95 时延预算：网关、模型 TTFT、SQL、检索、persist。不先画 20 个 Agent 角色。

#### A83. 白板：设计 Agent 评测平台。

数据集版本、离线 replay、在线采样、维度（正确/接地/安全/成本）、LLM-as-judge 只评子集、人审队列、发布门禁、污染防护。DCT 已有 eval-service 与 evidence 表，补融合冲突维度和 Skill 回归。

#### A84. 事故：SQL 把生产打满。你怎么改架构？

立刻：网关熔断 database_query、杀查询、只读副本。根因：缺超时/扫描上限/并发。长期：查询准入、解释计划预算、租户配额、dry_plan 拒绝无过滤。复盘写入 SLI。这不是「提示词加一句小心」。

#### A85. 事故：文档投毒导致 Agent 泄露其他项目。

立即禁用 RAG 或切到 allowlist corpus；审计近期 thread。根因：共享 default corpus。长期：workspace collection、检索强制过滤、跨租户红队。对照设计稿承认未落地。

#### A86. 事故：澄清死循环 / 用户骂「一直问」。

指标：澄清率、同一 term 重复次数。DCT 有 ask-once 与跨会话 choice。架构修复：词典质量、默认双路少问源、UI 选 references。把澄清当失败预算，不是越多越负责。

#### A87. 事故：有答案无报告（架构视角）。

上升为：身份不在执行面、双写失败、非法终态拒写。加告警：PENDING 超时、persist error rate。不要只教同事「看日志」。排查顺序见第 8 节 Q31。

#### A88. 设计：让 Agent 定时每天生成风险简报。

这是批处理：调度器创建 Run，身份用服务账号 + 模拟 workspace，产物写入 dct_dashboard 或邮件，失败进死信，不占用交互配额。不要让用户 Thread 里挂着 24h checkpoint。可用 Temporal 调度 + 短 LangGraph Run。

#### A89. 设计：Agent 触发「创建偏差调查单」。

写操作：分步确认（HITL）、幂等键、最小权限系统用户、审计、补偿。默认只生成草稿，人提交。能力面单独 tool，不进通用 bash。

#### A90. 反问面试官的问题（也是加分项）。

执行面与控制面谁 owner？Tool 契约谁审批？评测是否挡发布？租户隔离做到哪一层？LLM 预算谁买单？断线策略？这些问不出来说明对方可能没有 Agent 平台，只有 Demo。

### 10.19 架构师速查：题型对照

| 面试官题型 | 先答哪几条 |
|------------|------------|
| 画架构 | §10.7 白板 + A2 四层 |
| 为什么 LangGraph | A3、A4、A31 |
| 如何保证正确 | A10、A18、A24、A62 |
| 如何保证安全 | A19、A20、A54–A58 |
| 如何规模化 | A22、A48–A51、A82 |
| 如何演进 | A29、A35、A52、A80 |
| 你如何决策 | A5、A13、A30、A42 |

### 10.20 架构师不该说的话

- 「LangGraph 就是架构。」「换 Multi-Agent 就更智能。」
- 「安全靠 System Prompt。」「评测上线后再说。」
- 「记忆越多越好。」「工具越多越好。」
- 「上了 MCP/A2A 就是平台。」「Fine-tune 一下就准。」
- 「置信度 0.9 所以可自动下发工单。」
- 把 V2「不要迁 LangGraph」和现状「已经是 lead_agent」混成一套时间线还假装始终正确——要会讲 **决策反转的条件**。
- 把未落地的 workspace 多租户讲成已上线。

---

## 维护说明

- 真源以仓库 `ARCHITECTURE_AND_JOURNEY.md`、`docker-compose` 实际服务列表为准；V2 PRD 中的外部 Wren / 自研 Orchestrator **勿当作现行架构**。
- 若 compose、鉴权链或 `dct_*` / Wren 表结构变更，请同步修订本节与仓库内 `docs/DCT项目全景梳理.md`（若存在）。
