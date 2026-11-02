---
name: andrej-karpathy-skills
description: >-
  Karpathy 启发的编码 Agent 行为准则：编码前思考、简洁优先、精准修改、目标驱动验证。
  Use when writing or reviewing code, refactoring, reducing LLM over-engineering,
  or when the user mentions Karpathy guidelines、karpathy-guidelines、精准 diff、可验证成功标准.
---

# Andrej Karpathy Skills（Karpathy 编码准则）

## 是什么

**andrej-karpathy-skills** 源自 [Andrej Karpathy 对 LLM 编码陷阱的观察](https://x.com/karpathy/status/2015883857489522876)，用四条行为原则约束 Agent：**少假设、少过度设计、少无关 diff、用可验证目标驱动执行**。上游仓库：<https://github.com/multica-ai/andrej-karpathy-skills>（MIT）。

本目录是个人 wiki 的 **索引与真源副本**；门户 `/skills/andrej-karpathy-skills/` 读取本文件。Cursor 运行时可将 [references/karpathy-guidelines.mdc](references/karpathy-guidelines.mdc) 复制到项目的 `.cursor/rules/`，或将 [references/karpathy-guidelines-SKILL.md](references/karpathy-guidelines-SKILL.md) 放入个人 `~/.cursor/skills/`。

## 四条原则（摘要）

| 原则 | 针对的问题 |
|------|------------|
| **编码前思考** | 错误假设、隐藏困惑、缺少权衡 |
| **简洁优先** | 过度复杂、臃肿抽象 |
| **精准修改** | 无关编辑、触碰不应碰的代码 |
| **目标驱动执行** | 模糊「做完就行」、缺少验证循环 |

完整英文 Skill 正文见 [references/karpathy-guidelines-SKILL.md](references/karpathy-guidelines-SKILL.md)。中文背景与安装说明见 [references/upstream-overview.zh.md](references/upstream-overview.zh.md)。代码正反例见 [references/examples.md](references/examples.md)。

**权衡：** 准则偏向谨慎而非速度； trivial 改动（明显的一行修复）可酌情简化流程。

## 安装与使用

### Cursor（推荐）

1. **项目规则**：将 [references/karpathy-guidelines.mdc](references/karpathy-guidelines.mdc) 复制到目标项目的 `.cursor/rules/`（详见 [references/cursor-setup.md](references/cursor-setup.md)）。
2. **个人 Skill**：复制或 symlink [references/karpathy-guidelines-SKILL.md](references/karpathy-guidelines-SKILL.md) 到 `~/.cursor/skills/karpathy-guidelines/SKILL.md`（目录名可按你现有习惯调整）。

### Claude Code

```text
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

### 仅 CLAUDE.md / 合并用户规则

将 [references/claude-md-template.md](references/claude-md-template.md) 合并进项目 `CLAUDE.md` 或 Cursor 用户规则（与现有「最小 diff、不过度工程」类规则高度一致）。

## 与 `4-Skill` 其它条目的关系

| 条目 | 关系 |
|------|------|
| **superpowers** | 流程 Skill（brainstorming、TDD、verification）；Karpathy 准则偏 **编码行为与 diff 纪律**，可叠加在同一任务上 |
| **bmad** | 产品→交付链路；PRD/架构之后实现阶段可 Read 本 Skill 约束改动范围 |
| **apple-design-philosophy** | 领域设计 Skill；与本准则正交（UI 质量 vs 代码改动纪律） |

## Agent 操作清单

1. 用户 @ 本 Skill，或任务涉及 **重构 / 大范围改文件 / 易过度设计** → Read [references/karpathy-guidelines-SKILL.md](references/karpathy-guidelines-SKILL.md) 全文。
2. 实现前：说明假设；歧义时列出解释；存在更简单方案时主动提出。
3. 改代码时：每一行变更应能追溯到用户请求；不「顺手」格式化或重构无关代码。
4. 多步任务：写出「步骤 → verify: 检查」计划；与 `verification-before-completion`（Superpowers）一并使用时，成功标准要可执行、可观测。
5. 需要示例对照时 Read [references/examples.md](references/examples.md)。

## 参考资料

- [karpathy-guidelines-SKILL.md](references/karpathy-guidelines-SKILL.md) — 上游可执行 Skill 正文
- [cursor-setup.md](references/cursor-setup.md) — Cursor 规则与个人 Skill 布局
- [upstream-overview.zh.md](references/upstream-overview.zh.md) — 中文概述与安装
- [examples.md](references/examples.md) — 原则对应的代码示例
