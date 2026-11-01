# Superpowers Skill 目录（参考）

本文档为 **速查**，不构成 Skill 正文。Agent 执行步骤必须以各 Skill 的 `SKILL.md` 为准。

## 推荐流水线

### 新功能（默认）

```text
brainstorming（设计 + 用户批准）
  → writing-plans（可选，多步时）
  → using-git-worktrees（需要隔离时）
  → test-driven-development 或 subagent-driven-development / executing-plans
  → verification-before-completion
  → requesting-code-review（合并前）
  → finishing-a-development-branch
```

### 修 Bug

```text
systematic-debugging
  → test-driven-development（回归测试）
  → verification-before-completion
```

### 并行杂项

```text
dispatching-parallel-agents
  → 各分支仍遵守各自适用的流程 Skill
```

## 各 Skill 触发要点

### using-superpowers

- **何时**：每次新对话、不确定用哪个 Skill 时。
- **要点**：Skill 检查先于澄清问题与读仓库；Plan 模式前若未 brainstorm 则先 brainstorm。

### brainstorming

- **何时**：新功能、新组件、改行为、任何「创造性」实现。
- **硬门槛**：未呈现设计并得到用户批准前，不得写代码、不得 scaffold。

### writing-plans

- **何时**：需求已清楚且步骤 ≥2，动代码前。
- **产出**：可交给 `executing-plans` 或人工分 session 执行的计划文档。

### executing-plans

- **何时**：已有书面计划，可能在 **另一会话** 执行。
- **要点**：按检查点暂停、对照计划 review。

### subagent-driven-development

- **何时**：计划已在 **当前会话**，任务可拆成独立 subagent。
- **要点**：任务间 code review，不跳过 review 步。

### dispatching-parallel-agents

- **何时**：2+ 任务无共享状态、无顺序依赖。
- **反例**：同一文件两处冲突修改应串行。

### using-git-worktrees

- **何时**：功能分支隔离、执行大计划前避免污染当前工作区。

### test-driven-development

- **何时**：任何功能或 bugfix 的 **实现代码之前**。
- **要点**：先失败测试 → 最小实现 → 重构。

### systematic-debugging

- **何时**：bug、失败测试、非预期行为；**在提出 fix 之前**。
- **要点**：根因与复现优先，避免猜修。

### verification-before-completion

- **何时**：要说「完成 / 修好了 / 通过」、commit、开 PR 之前。
- **要点**：必须运行命令并 **阅读输出**；无证据不断言成功。

### requesting-code-review / receiving-code-review

- **何时**：大块完成或合并前 / 收到 review 评论后。
- **要点**：接收 review 时先验证再改，不表演式同意。

### finishing-a-development-branch

- **何时**：实现完成且测试通过，需要 merge / PR / 清理决策。

### writing-skills

- **何时**：新建 Skill、改 Skill、部署前验证 Skill 行为。

## 安装与更新（给人看）

1. Cursor 中安装 **Superpowers** 插件（或启用自带 superpowers skills 源）。
2. 本 wiki 副本用于 **文档与 Git 备份**；与插件版本不一致时，以插件内 SKILL.md 为准，并酌情更新本目录。
3. 门户展示：`personal-tech-portal` 构建时读取 `raw/4-Skill/**/SKILL.md`。

## 与 personal-knowledge-wiki / portal 实践

- Wiki Agent 规则：`AGENTS.md`、`wiki/_meta/conventions.md`。
- 项目级 Skill 可放在 `.cursor/skills/`（wiki 或 portal 仓库）。
- 个人收藏的统一入口：`raw/4-Skill/`（含本 `superpowers` 与领域 Skill）。
