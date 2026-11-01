---
title: Agent Skill 体系：Superpowers 与 BMAD
summary: Superpowers 工程流程 Skill 与 BMAD 产品交付 Skill 的分工、典型场景与使用要点
tags: [tech, cursor, agent, skill, bmad, superpowers]
status: reviewed
updated: 2026-11-01
sources:
  - path: wiki/tech/agent-skills-bmad-superpowers.md
    note: 对外发布副本；完整 Skill 正文见 /skills/
---

# Agent Skill 体系：Superpowers 与 BMAD

## 结论摘要

- **Superpowers**：通用 **工程流程**（先读 Skill 再动手；brainstorming → TDD → 完成前验证；用户规则优先）。
- **BMAD Method**：**产品→交付**（brief / PRD / 架构 / build）；需在项目中安装后使用 `.agents/skills/bmad-*`。
- 二者可并存：BMAD 定范围与规格，Superpowers 约束实现与验证。
- 本站 **[Skill 目录](/skills/)** 展示 `bmad`、`superpowers` 等索引正文；运行时以 IDE 内完整 SKILL 为准。

## Superpowers 典型场景

| 场景 | 首选 Skill |
|------|------------|
| 新功能 / 改行为 | brainstorming → 设计批准后再实现 |
| Bug / 测试失败 | systematic-debugging |
| 有书面计划 | executing-plans / subagent-driven-development |
| 写实现代码 | test-driven-development |
| 声称完成 / commit | verification-before-completion |

## BMAD 典型场景

| 类型 | 示例 | 用途 |
|------|------|------|
| 枢纽 | bmad | 推荐下一步、环境状态 |
| 探索 | bmad-brainstorming、bmad-deep-recon | 想法与研究 |
| 规格 | bmad-prd、bmad-architecture | PRD / 架构 |
| 实现 | bmad-build | 工作项→代码与评审 |

安装：项目根执行 `npx bmad-method install` 并选择 Cursor；模块变更后需重装同步。

## 阅读入口

- [Superpowers Skill](/skills/superpowers/)
- [BMAD Skill](/skills/bmad/)

## 相关

- [个人 LLM Wiki 实践](/knowledge/tech/llm-personal-wiki-practice/)
- [知识库首页](/knowledge/)
