---
title: 个人 LLM Wiki 从 0 到 1（方法与实践）
summary: Markdown+Git 真源、raw/wiki/publish/Skill 分层，以及个人站四模块（笔记、知识库、博客、Skill）的落地方式
tags: [tech, knowledge-management, llm, wiki, para]
status: reviewed
updated: 2026-11-01
sources:
  - path: wiki/tech/llm-personal-wiki-practice.md
    note: 对外发布副本；博客原文见站点 /blog/
---

# 个人 LLM Wiki 从 0 到 1（方法与实践）

## 结论摘要

- **LLM Wiki** = Wiki 层（Markdown + Git）+ LLM 层（整理落盘）+ **边界层**（草稿与对外内容分离）。
- **PARA 思想**：按下一步行动归档；新内容先进可随意写的层，审核后再进对外知识库或博客。
- 本站点四模块：**[笔记](/notes/)**（原始）、**[知识库](/knowledge/)**（审核副本）、**[博客](/blog/)**（叙事成稿）、**[Skill](/skills/)**（Agent 流程）。
- 探索适合在对话里进行；**结论应写入文件**并经过发布前人工核对。

## 内容分层

| 层 | 角色 | 本站入口 |
|----|------|----------|
| 原始笔记 | 真源、可冗长 | /notes/ |
| 结构化 wiki | Agent 维护、对内 | 仓库内 wiki/（不直接上站） |
| publish | 审核后可引用 | /knowledge/ |
| 博客 | 观点与过程 | /blog/ |
| Skill | 可复用 Agent 规范 | /skills/ |

**笔记与知识库不得自动双向同步**；重复流程应写成 Skill。

## LLM 协作边界

- **适合自动化**：大纲、术语统一、frontmatter、链接修复、发布前检查清单。
- **必须人工**：是否对外、敏感信息、事实核对、publish 是否达标。

## 一条想法的发布路径

1. 在笔记层快速记录。
2. 用 Agent + Skill 整理结构（仍留在笔记或对内 wiki）。
3. 值得对外：改写为知识库条目并标记 `reviewed`。
4. 需要讲故事：写成博客并关闭 draft。
5. 更新内容仓后，刷新门户构建/submodule，使线上与仓库一致。

## 相关

- [Agent Skill 体系](/knowledge/tech/agent-skills-bmad-superpowers/)
- [1-Note 主题索引](/knowledge/tech/one-note-raw-index/)
- [知识库首页](/knowledge/)
