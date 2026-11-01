---
name: bmad
description: >-
  BMAD Method 入口：用命名 Skill 驱动 Agent 角色、多步工作流与单任务；适合产品探索、PRD/架构、bmad-build 实现与评审。
  Use when the user mentions BMAD、bmad-prd、bmad-build、bmad-agent-dev、产品 brief、架构 spine、
  or wants structured think-then-build software delivery in Cursor.
---

# BMAD Method（Breakthrough Method for Agile AI-Driven Development）

## 是什么

**BMAD Method** 是一套在 IDE（含 Cursor）里通过 **Skill 名称** 调用的 AI 软件开发方法：一部分 Skill 负责 **想清楚**（探索、研究、PRD、架构、UX），另一部分负责 **做出来**（`bmad-build`、代码评审、测试、Epic 回顾）。你可以只用「思考链」，也可以小改动直接 build。

官方文档：<https://docs.bmad-method.org/>

本目录是个人 wiki 的 **索引与约定**。Cursor 中 **可执行的完整 SKILL.md** 由安装器生成，位于项目的 `.agents/skills/`（或 `~/.agents/skills/`）。Agent 执行具体工作流时，应 **Read 对应 `bmad-*` 目录下的完整 SKILL.md**，并按其中指令加载 BMAD 源文件。

## 安装（Cursor）

在项目根目录：

```bash
npx bmad-method install
```

安装时选择 **Cursor**。安装器会在项目内写入 `.agents/skills/bmad-*/SKILL.md`（每个 Skill 一个目录，**目录名即 Skill 名**）。增删模块后需 **重新运行安装器** 以同步 Skill 列表。

Cursor 也会从 `.cursor/skills/` 加载 Skill；BMAD 官方默认目标目录为 **`.agents/skills/`**。

安装后可用 **`bmad`** Skill 作为枢纽：询问「下一步该用哪个 Skill」，或执行 `bmad setup` / `bmad status` 等。

## 两种启动方式

| 方式 | 用法 | 适用 |
|------|------|------|
| **Skill 名** | 在 Agent 中输入/选择 `bmad-prd`、`bmad-build` 等 | 已明确要跑的工作流 |
| **Agent 菜单码** | 先加载 Agent（如 `bmad-agent-dev`），再输入短码如 `BD`、`CR` | 已在某角色对话中切换任务 |

菜单码 **因 Agent 而异**（例如 Analyst 与 Developer 的 `CR` 含义不同）。完整对照见 [references/skill-catalog.md](references/skill-catalog.md)。

## 六类 Agent（BMad Method 模块）

| 角色 | Skill ID | 典型职责 |
|------|----------|----------|
| Analyst (Mary) | `bmad-agent-analyst` | 头脑风暴、市场/领域/技术调研、竞品、产品 brief |
| PM (John) | `bmad-agent-pm` | 创建/更新/校验 PRD |
| PO (Sofia) | `bmad-agent-po` | 需求拆 ticket、看板、验证、重规划 |
| Architect (Winston) | `bmad-agent-architect` | 架构 spine（`CA`） |
| Developer (Amelia) | `bmad-agent-dev` | Build、QA 测试生成、Code review、Epic 回顾 |
| UX (Sally) | `bmad-agent-ux-designer` | UX 设计（`CU`） |

Technical Writer（Paige）暂休；项目上下文可用 Analyst 的 `PC` 或 **`bmad-project-context`**。

## 核心 Skill（任意项目可用）

| Skill | 用途摘要 |
|-------|----------|
| `bmad` | 枢纽：推荐下一步 Skill、setup/status、initiative 管理 |
| `bmad-brainstorming` | 结构化头脑风暴，大量 idea 再整理 |
| `bmad-forge-idea` | 半成型想法对谈压测 |
| `bmad-deep-recon` | 决策向研究（市场/技术/竞品/代码库等） |
| `bmad-advanced-elicitation` | 对已有草稿多视角施压、修订建议 |
| `bmad-review` | 多 lens 评审 diff/文档（对抗/边界/验证缺口/结构/文笔等） |
| `bmad-party-mode` | 多 Agent 同场讨论 |
| `bmad-shard-pro` | 长文档分片/目录，便于 Agent 导航 |
| `bmad-ingest` | 会议/线程/访谈等 raw 转结构化 note |
| `bmad-customize` | 用自然语言写 `_bmad/custom/` 覆盖配置 |

## 方法模块 Skill（Think → Specify → Build）

| 阶段 | Skill | 产出方向 |
|------|-------|----------|
| 定义 | `bmad-product-brief`、`bmad-prfaq`、`bmad-prd` | Brief、PRFAQ、PRD |
| 设计 | `bmad-ux`、`bmad-architecture` | UX 与架构决策文档 |
| 上下文 | `bmad-project-context` | 仓库 Agent 说明维护 |
| 实现 | `bmad-build`、`bmad-build-auto` | 工作项 → 代码 + 评审/验证 |
| 质量 | `bmad-code-review`、`bmad-walkthrough`、`bmad-qa-generate-e2e-tests` | 评审、走读、E2E |
| 收尾 | `bmad-retrospective` | Epic 完成度与证据 |

典型 **Greenfield** 思路：探索（brainstorm / forge / recon）→ brief → PRD → UX + architecture → project-context → PO 拆 ticket → **`bmad-build`**。细节以官方流程章节为准。

## 与本 wiki 的关系

- **收藏**：`raw/4-Skill/bmad/` → 门户 `/skills/bmad/`。
- **运行**：以项目内 `.agents/skills/bmad-*` 为准；本文件不替代安装器生成的 SKILL。
- **与 Superpowers**：Superpowers 偏 **通用工程流程**（brainstorming、TDD、debug）；BMAD 偏 **产品→交付全链路 Skill**。可并存：例如 BMAD 写 PRD，Superpowers 做实现阶段 TDD。

## Agent 操作清单

1. 用户提 BMAD 或不确定从哪开始时：优先建议或加载 **`bmad`** 获取下一步 Skill 列表。
2. 执行具体工作流前：Read **该 Skill 目录下完整 SKILL.md**（如 `bmad-prd/SKILL.md`），按指令加载 BMAD 配置与模板。
3. 需要压测文档/决策时：考虑 `bmad-advanced-elicitation` 或 `bmad-review`，不要跳过 finalize 评审步骤。
4. 实现类任务：优先 **`bmad-build`**（含评审层）；勿与项目内 `git-conventions` 等冲突——用户/仓库规则优先。
5. 旧 Skill 名（如 `bmad-create-prd`）可能仅为转发器；新工作使用当前名（如 `bmad-prd`）。

更多 Agent 菜单码、Toolsmith、排错见 [references/skill-catalog.md](references/skill-catalog.md)。
