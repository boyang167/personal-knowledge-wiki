# LLM 个人知识库 — 设计说明

**日期：** 2026-10-24  
**方向：** Agent 优先（Markdown wiki + Cursor 规则 + LLM 索引）

## 目标

在现有 `raw/` 学习资料之上，建立可让 Cursor Agent 稳定读写、带来源、分审核阶段的个人知识库。

## 架构

- **raw**：原件归档，Agent 按需深读。
- **wiki**：提炼知识；YAML frontmatter（title、summary、tags、status、sources）。
- **publish**：人工闸门后的对外副本。
- **INDEX.llm.md**：由脚本从 frontmatter 生成，供 Agent 快速路由。

## 非目标（本期）

- 静态站点、向量 RAG、自动从 raw 批量灌库。

## 扩展预留

- frontmatter 与目录结构兼容后续 MkDocs / 向量索引。
- `scripts/build_llm_index.py --with-raw-stats` 可输出 raw 分类统计。
