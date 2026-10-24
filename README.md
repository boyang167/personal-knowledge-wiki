# wiki — LLM 个人知识库

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

## 自动收录

把新资料放进 `raw/` 后，在仓库根目录运行：

```powershell
powershell -File scripts/watch_raw.ps1
```

安静 30 秒后，脚本会登记新文件、按主题更新 wiki、重建 `wiki/INDEX.llm.md`，然后提交并推送到 `origin/main`。压缩包、录像、嵌套仓库和疑似口令文件不会进入提交。

只处理一次、不提交：

```powershell
python scripts/ingest_raw.py --dry-run
python scripts/ingest_raw.py
```

第一次如果还没有 `wiki/_meta/ingest-ledger.json`，脚本只把当前 `raw/` 记成基线，不会把已有文件重新写成 wiki。

## 与 personal-tech-portal 关联

| 项 | 说明 |
|----|------|
| 门户仓库 | [boyang167/boyang167.github.io](https://github.com/boyang167/boyang167.github.io) |
| 消费目录 | 仅 **`publish/`**（经审核副本） |
| 自动部署 | push `publish/**` 到 `main` → 触发门户 `repository_dispatch` |

在 **本仓库** Settings → Secrets → Actions 添加 **`PORTAL_REPO_TOKEN`**（对门户仓库有 dispatch 权限的 PAT）。未配置时 workflow 会跳过通知，需手动更新门户 submodule 或 push 门户。

公开站点入口：https://boyang167.github.io/knowledge/

## 后续扩展（未实现）

- 独立 MkDocs / VitePress 子站（当前由 Astro 门户渲染 `publish/`）
- 本地向量 RAG

目录与 frontmatter 已为上述扩展预留字段（`summary`、`tags`、`status`）。
