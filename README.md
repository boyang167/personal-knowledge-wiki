# 25-wiki — LLM 个人知识库

基于 Markdown 的个人知识库，面向 **Cursor Agent** 读写：原始资料在 `raw/`，提炼后的知识在 `wiki/`，经人工审核的副本在 `publish/`。

## 快速开始

1. 阅读 [AGENTS.md](./AGENTS.md) 与 [wiki/_meta/conventions.md](./wiki/_meta/conventions.md)。
2. 从 [wiki/_templates/page.md](./wiki/_templates/page.md) 复制模板，在对应主题目录下新建页面。
3. 更新机器可读目录：

   ```powershell
   python scripts/build_llm_index.py
   ```

4. 在 Cursor 中让 Agent「根据 raw 某资料更新 wiki 某主题」，并核对 `sources` 引用。

## 目录结构

| 路径 | 用途 |
|------|------|
| `raw/` | 原始资料（勿擅自覆盖） |
| `wiki/` | 结构化知识、MOC、LLM 索引 |
| `publish/` | 审核后可对外分享的内容 |
| `scripts/` | 索引与维护脚本 |
| `.cursor/rules/` | Agent 行为约束 |

## 与 raw 资料的对应关系

见 [wiki/_meta/topic-map.md](./wiki/_meta/topic-map.md)。

## 内容状态

- `raw` 中的 Markdown 调研已按主题提炼进 `wiki/`（生信库、Flink、数据平台、ants、强化学习目录、技术分享题目）。
- 基础设施、数据库、Java/Spring、知识图谱、深度学习论文与推荐课件仍是 PDF。对应 wiki 页只做文件索引，打开 PDF 后再补结论。
- 安装包目录 `raw/2-StudyMaterials/12-InstallPackage/` 不建知识页。

## 后续扩展（未实现）

- 静态站点（MkDocs / VitePress）
- 本地向量 RAG

目录与 frontmatter 已为上述扩展预留字段（`summary`、`tags`、`status`）。
