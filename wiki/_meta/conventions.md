# Wiki 写作规范

## Frontmatter（必填）

每个 wiki 页面（`_meta/`、`_templates/` 除外）必须以 YAML frontmatter 开头：

```yaml
---
title: 页面标题
summary: 一句话说明，供 INDEX.llm.md 与 Agent 路由
tags: [tag1, tag2]
status: draft   # draft | reviewed | uncertain
updated: 2026-10-24
sources:
  - path: raw/2-StudyMaterials/7-BigData/design.md
    note: 架构对比表与湖仓格式小节
---
```

### 字段说明

| 字段 | 说明 |
|------|------|
| `title` | 中文或英文标题 |
| `summary` | ≤120 字摘要，写「这篇解决什么问题」 |
| `tags` | 小写、短标签，便于检索 |
| `status` | `draft` 初稿；`reviewed` 你已核对；`uncertain` 含待核实结论 |
| `updated` | ISO 日期，内容实质变更时更新 |
| `sources` | 至少一条指向 `raw/` 的路径；可多条 |

## 正文结构建议

1. **结论摘要**（3–5 条 bullet，可扫描）
2. **正文**（分节、表格、图示可链到 raw 内资源）
3. **待核实**（可选，与 uncertain 对应）
4. **相关页面**（链到 MOC 内其他 wiki）

## 与 publish 的关系

- wiki 允许 `draft` / `uncertain`。
- 进入 `publish/` 前：改为 `reviewed`，去掉不应外泄的信息，并由人工确认。

## 文件命名

- 路径：`wiki/<主题>/<slug>.md`
- slug：小写英文与连字符，如 `data-platform-architecture.md`
- 同一主题避免一篇覆盖过多 unrelated 内容；可拆页并在 MOC 互链
