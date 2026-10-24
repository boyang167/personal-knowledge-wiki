# raw → wiki 主题对照

`raw/1-Note/` 与 `raw/2-StudyMaterials/` 下目录和 wiki 路径的推荐映射（新建页面时优先放入对应 wiki 目录）。

| raw 目录 | wiki 目录 | 说明 |
|----------|---------|------|
| `1-Note/2-MachineLearning` | `wiki/ml/` | 个人机器学习与采样笔记 |
| `1-Note/3-DeepLearning` | `wiki/ml/` | 深度学习、NLP、图谱、生成模型和 LLM 笔记 |
| `1-Biological` | `wiki/biological/` | 生物、生信、CMC 等 |
| `2-MachineLearning` | `wiki/ml/` | 机器学习 |
| `3-ReinforcementLearning` | `wiki/ml/` | 强化学习（可用 tags 区分） |
| `4-DeepLearning` | `wiki/ml/` | 深度学习 |
| `5-Infrastructure` | `wiki/infrastructure/` | K8s、云原生等 |
| `6-Database` | `wiki/database/` | 数据库 |
| `7-BigData` | `wiki/big-data/` | 数据平台、Flink 等 |
| `8-ProgramerLanguage` | `wiki/programming/` | Java、Spring 等 |
| `9-Tech` | `wiki/tech/` | 技术博客等 |
| `10-KG` | `wiki/kg/` | 知识图谱 |
| `11-OpneSource` | `wiki/opensource/` | 开源源码阅读笔记 |
| `12-InstallPackage` | — | 安装包归档，通常不单独建 wiki 页 |

## 引用 raw 的路径写法

始终使用仓库相对路径，例如：

`raw/2-StudyMaterials/7-BigData/design.md`

PDF 等同理；若 Agent 无法直接读 PDF，在 `sources.note` 中说明已人工阅读的范围。
