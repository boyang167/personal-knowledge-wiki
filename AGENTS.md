# Knowledge Workflow

## 目录

| 路径 | 用途 |
|------|------|
| `raw/` | 原始资料（只读，勿覆盖） |
| `wiki/` | LLM / Agent 主知识区（Markdown + frontmatter） |
| `publish/` | 人工审核后可对外内容 |
| `wiki/INDEX.llm.md` | 机器可读目录（`python scripts/build_llm_index.py`） |

## 规则

1. 原始资料存放在 raw/，未经允许不要覆盖原件。
2. 阅读资料后，将有价值的知识更新到 wiki/（规范见 `wiki/_meta/conventions.md`）。
3. 新资料可能影响已有结论时，检查相关知识页面与 `wiki/MOC.md`。
4. 关键结论必须保留来源引用（frontmatter `sources`）。
5. 不确定的结论必须明确标记，不要编造事实；`status: uncertain`。
6. 只有经过人工审核的内容才能进入 publish/。
7. 禁止自动发布私人资料、公司内部资料或秘密信息。
8. 更新 wiki 页面后运行 `python scripts/build_llm_index.py` 刷新索引。
9. `raw/` 的新文件由 `scripts/watch_raw.ps1` 收录。自动页带 `ingest: auto`，复核后应改写成正式结论并去掉该字段。疑似口令的文件不得写入 wiki 或提交。