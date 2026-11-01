---
title: 个人 LLM Wiki 从 0 到 1（方法与实践）
summary: 提炼 raw/3-blog/llm-wiki.md：Markdown+Git 真源、raw/wiki/publish/Skill 分层及 11-Profile-Web 双仓落地
tags: [tech, knowledge-management, llm, wiki, para]
status: draft
updated: 2026-11-01
sources:
  - path: raw/3-blog/llm-wiki.md
    note: 博客成稿全文；含 personal-knowledge-wiki 与 personal-tech-portal 工程说明
---

# 个人 LLM Wiki 从 0 到 1（方法与实践）

## 结论摘要

- **LLM Wiki** = Wiki 层（Markdown + Git）+ LLM 层（整理/摘要落盘）+ **边界层**（raw 与 publish 分离，避免误公开）。
- **PARA 思想**：按「下一步行动」归档；新内容先进可随意写的 **raw**，审核后再进 **publish** 或博客。
- 四层角色：`raw`（真源）→ `wiki`（Agent 结构化知识 + INDEX）→ `publish`（人工审核对外）→ `raw/3-blog`（叙事成稿）；**`4-Skill`** 固化 Agent 流程。
- 本仓库实例：`personal-knowledge-wiki` 存内容，`personal-tech-portal`（Astro）构建站点；门户优先读 sibling wiki，CI 用 submodule 锁定版本。

## 内容分层

| 层 | 路径 | 读者 / 用途 |
|----|------|-------------|
| raw | `raw/1-Note`、`2-StudyMaterials` 等 | 作者自用，可冗长 |
| wiki | `wiki/` + `INDEX.llm.md` | Cursor Agent 主检索区 |
| publish | `publish/` | 站点 `/knowledge/`，须 reviewed |
| blog | `raw/3-blog/` | 站点 `/blog/`，`draft` 控制发布 |
| Skill | `raw/4-Skill/` | 站点 `/skills/`，驱动 Agent |

**raw 与 publish 不得自动同步**；重复流程写成 Skill，而非每次口述 prompt。

## 门户读取规则（摘要）

| 站点路径 | 数据来源 |
|----------|----------|
| `/notes/` | `raw/1-Note/**/*.md` |
| `/knowledge/` | `publish/**/*.md` |
| `/blog/` | `raw/3-blog/**/*.md` |
| `/skills/` | `raw/4-Skill/**/SKILL.md` |

构建前笔记图片复制到 `public/notes-media/`；wiki 更新后运行 `python scripts/build_llm_index.py`。

## LLM 协作边界

- **适合自动化**：大纲、术语统一、frontmatter、链接修复、按 Skill 做发布检查。
- **必须人工**：是否对外、敏感信息、事实核对、publish 达标。
- 探索在对话里，**结论在文件里**。

## 相关

- [Agent Skill 体系](./agent-skills-bmad-superpowers.md)
- [1-Note 全量索引](./one-note-raw-index.md)
- 仓库 [AGENTS.md](../../AGENTS.md)、[README.md](../../README.md)
