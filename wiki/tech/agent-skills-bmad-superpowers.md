---
title: Agent Skill 体系：Superpowers 与 BMAD
summary: 对照 raw/4-Skill 中 Superpowers 与 BMAD 的入口 Skill，说明触发规则、分工与 Agent 操作清单
tags: [tech, cursor, agent, skill, bmad, superpowers]
status: draft
updated: 2026-11-01
sources:
  - path: raw/4-Skill/superpowers/SKILL.md
    note: Superpowers 索引与 using-superpowers 规则
  - path: raw/4-Skill/bmad/SKILL.md
    note: BMAD 安装、Agent 角色与 Think→Build 链路
  - path: raw/4-Skill/superpowers/references/skill-catalog.md
    note: Superpowers 技能目录详情
  - path: raw/4-Skill/bmad/references/skill-catalog.md
    note: BMAD 菜单码与 Skill 列表
---

# Agent Skill 体系：Superpowers 与 BMAD

## 结论摘要

- **Superpowers**：通用 **工程流程** Skill（先 Read Skill 再动作；brainstorming → TDD → verification；用户规则与 `AGENTS.md` 优先）。
- **BMAD Method**：**产品→交付** 全链路（brief / PRD / 架构 / `bmad-build`）；通过 `npx bmad-method install` 写入 `.agents/skills/bmad-*`，raw 目录仅为 **索引与门户展示**。
- 二者可并存：例如 BMAD 产出 PRD，Superpowers 的 `test-driven-development` 与 `verification-before-completion` 约束实现阶段。
- 门户 `/skills/` 读取 `raw/4-Skill/**/SKILL.md`；Cursor 运行时以 IDE 插件 + 项目 `.agents/skills/` 为准。

## Superpowers 要点

| 场景 | 首选 Skill |
|------|------------|
| 新功能 / 改行为 | `brainstorming` → 设计批准后再实现 |
| Bug / 测试失败 | `systematic-debugging` |
| 有书面计划 | `executing-plans` / `subagent-driven-development` |
| 写实现代码 | `test-driven-development` |
| 声称完成 / commit | `verification-before-completion` |

核心规则：**任务有 ≥1% 可能适用 Skill 时，在改文件前先 Read 完整 SKILL.md**；流程 Skill 优先于实现 Skill。

## BMAD 要点

| 类型 | 示例 Skill | 用途 |
|------|------------|------|
| 枢纽 | `bmad` | 推荐下一步、setup/status |
| 探索 | `bmad-brainstorming`、`bmad-deep-recon` | 想法与研究 |
| 规格 | `bmad-prd`、`bmad-architecture` | PRD / 架构 |
| 实现 | `bmad-build` | 工作项→代码+评审 |
| 角色 Agent | `bmad-agent-dev` 等 | 菜单短码切换任务 |

安装：项目根 `npx bmad-method install`，选 Cursor；增删模块后需重装同步。

## Agent 操作清单

1. 用户提到 Superpowers / 技能 / 调试 / TDD → Read `raw/4-Skill/superpowers/SKILL.md`，再 Read 场景 Skill 全文。
2. 用户提到 BMAD / PRD / bmad-build → Read `raw/4-Skill/bmad/SKILL.md`，再 Read 目标 `bmad-*` 目录下完整 SKILL（`.agents/skills/`）。
3. 勿用本 wiki 页替代安装器生成的 BMAD Skill 正文。
4. Git 操作遵守项目 `git-conventions` 与用户 commit 规则。

## 相关

- [个人 LLM Wiki 实践](./llm-personal-wiki-practice.md)
- [MOC](../MOC.md)
