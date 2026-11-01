---
name: superpowers
description: >-
  Cursor Superpowers 技能体系入口：在对话开始时检查并调用相关 Skill，按流程技能优先于实现技能。
  Use when starting work in Cursor, choosing which skill to invoke, planning features, debugging,
  writing plans, TDD, code review, or when the user mentions Superpowers、技能、brainstorming、系统化调试.
---

# Superpowers（Cursor Agent Skills）

## 是什么

**Superpowers** 是 Cursor 上的一套 **流程型 Agent Skill** 集合：把「先想什么、再做什么、如何验证」写进 `SKILL.md`，让 Agent 在编码前走固定工作流，而不是每次从空白 prompt 即兴发挥。

本文件是个人 wiki 中的 **索引与约定**；完整 Skill 正文由 Cursor **Superpowers 插件**（或 IDE 内已加载的 superpowers skills）提供。Agent 执行时应 **Read 对应 Skill 的完整 SKILL.md**，不要只凭摘要行动。

## 核心规则（using-superpowers）

1. **先 Skill，后动作**：只要任务有 ≥1% 可能适用某个 Skill，在回复、澄清、读代码、改文件之前先 Read 该 Skill。
2. **用户指令优先**：`AGENTS.md`、用户明确指令 > Skill > 默认行为。
3. **流程 Skill 优先于实现 Skill**：例如先 `brainstorming` / `systematic-debugging`，再写 UI 或业务代码。
4. **子 Agent 例外**：若仅作为 subagent 执行单一 dispatched 任务，可忽略 `using-superpowers` 的「会话开场」要求。
5. **宣布用法**：Invoke 后简要说明 `Using [skill] to [purpose]`；Skill 内含 checklist 时，按项执行（可用 todo 跟踪）。

### 常见场景 → 首选 Skill

| 场景 | 首选 Skill |
|------|------------|
| 新功能 / 改行为 / 做组件 | `brainstorming` →（批准设计后）`writing-plans` 或实现类 Skill |
| Bug / 测试失败 / 异常行为 | `systematic-debugging` |
| 已有书面实现计划 | `executing-plans` 或 `subagent-driven-development` |
| 写代码前（功能或修复） | `test-driven-development` |
| 多任务互不依赖 | `dispatching-parallel-agents` |
| 需要隔离工作区 | `using-git-worktrees` |
| 声称完成 / 要 commit 或 PR | `verification-before-completion` |
| 合并前自检 | `requesting-code-review` |
| 收到 review 意见 | `receiving-code-review` |
| 分支收尾 | `finishing-a-development-branch` |
| 新建或修改 Skill | `writing-skills` |

### 反模式（出现这些想法时应停下并查 Skill）

- 「问题很简单，不用 Skill」
- 「先看代码再说」
- 「我 remember 这个 Skill 了」（Skill 会更新，必须 Read 当前版）
- 「先做一步再补流程」

## Superpowers 技能目录

| Skill | 用途摘要 |
|-------|----------|
| `using-superpowers` | 会话开场：如何发现与强制调用 Skill |
| `brainstorming` | 创意/功能/改行为前：澄清意图与设计，**未批准设计不得写代码** |
| `writing-plans` | 有多步需求时，动代码前写实现计划 |
| `executing-plans` | 在单独会话中按计划执行（含检查点） |
| `subagent-driven-development` | 当前会话内按独立任务驱动 subagent + 任务间 review |
| `dispatching-parallel-agents` | 2+ 互不依赖任务并行 |
| `using-git-worktrees` | 功能隔离 / 执行计划前的独立工作区 |
| `test-driven-development` | 实现前先写测试 |
| `systematic-debugging` | 修 bug 前先根因分析 |
| `verification-before-completion` | 声称完成前必须跑验证命令并看输出 |
| `requesting-code-review` | 完成大块工作或合并前发起 review |
| `receiving-code-review` | 处理 review：验证后再改，不盲目采纳 |
| `finishing-a-development-branch` | 测试通过后：合并 / PR / 清理选项 |
| `writing-skills` | 编写、修改、部署前验证 Skill |

更细的触发说明与典型流水线见 [references/skill-catalog.md](references/skill-catalog.md)。

## 与本 wiki 的关系

- **收藏位置**：`raw/4-Skill/superpowers/`（门户 `/skills/superpowers/` 可浏览）。
- **运行时来源**：Cursor **Superpowers 插件**（或 IDE 已注入的 superpowers skills）提供完整正文；本目录便于版本管理与对外展示。
- **与 `4-Skill` 其它条目**：如 `apple-design-philosophy` 属于 **领域/设计** Skill；Superpowers 属于 **元流程** Skill，二者可串联（先 brainstorming，再 apple-design-philosophy 做 UI）。

## Agent 操作清单

1. 判断任务类型，从上表选 **一个流程 Skill** Read 全文。
2. 若用户 @ 本 Skill 或提到 Superpowers，先 Read `using-superpowers`，再 Read 场景 Skill。
3. 设计/计划类任务未获用户认可前，不调用 TDD、不提交实现 diff。
4. 完成前 Read `verification-before-completion`，运行项目内真实验证命令（如 `npm run build`、测试脚本）。
5. 需要 Git 操作时，同时遵守 wiki / 项目内的 `git-conventions` 等项目 Skill（若存在）。
