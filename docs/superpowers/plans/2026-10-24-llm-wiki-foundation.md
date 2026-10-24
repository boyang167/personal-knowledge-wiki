# LLM Wiki Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Agent 优先的个人知识库底座（wiki 规范、Cursor 规则、索引脚本、示例页）。

**Architecture:** raw → wiki 提炼 + publish 审核；`INDEX.llm.md` 机器目录。

**Tech Stack:** Markdown, YAML frontmatter, Python 3 stdlib, Cursor rules.

## Global Constraints

- 不修改 raw 原件；关键结论必须有 sources。
- 不确定须标记；禁止自动写入 publish/。

---

## Tasks（已完成于 2026-10-24）

- [x] 项目 README、`.gitignore`
- [x] `wiki/` 规范、MOC、模板、主题对照
- [x] `.cursor/rules/knowledge-wiki.mdc`
- [x] `scripts/build_llm_index.py` + `wiki/INDEX.llm.md`
- [x] 示例页 `wiki/big-data/data-platform-architecture.md`
- [x] `publish/` 说明

## 后续建议

- [x] 按 `topic-map` 提炼 raw 中的 Markdown 笔记（2026-10-24）
- [ ] PDF 原件（基础设施、数据库、Java/Spring、知识图谱、深度学习论文与课件）只建了文件索引，尚未读正文
- [ ] 初始化 git，并按需用 `.cursorignore` 排除安装包
- [ ] 可选：MkDocs / 本地 RAG
