---
title: 个人学习笔记地图
summary: 说明 raw/1-Note 里数学、机器学习、深度学习和 LLM 笔记各自覆盖什么，并链到已提炼的 wiki 页
tags: [ml, notes, map]
status: draft
updated: 2026-10-24
sources:
  - path: raw/1-Note/2-MachineLearning/1-math.md
    note: 采样笔记
  - path: raw/1-Note/2-MachineLearning/2-machine-learning.md
    note: 机器学习流程与算法提纲
  - path: raw/1-Note/3-DeepLearning/1-deep-learning.md
    note: 网络层、激活函数和优化器
  - path: raw/1-Note/3-DeepLearning/2-NLP.md
    note: 表示学习与预训练模型
  - path: raw/1-Note/3-DeepLearning/3-AI.md
    note: 图谱、强化学习、视觉、图网络和生成模型
  - path: raw/1-Note/3-DeepLearning/llm.md
    note: Function calling 与 MCP
---

# 个人学习笔记地图

## 结论摘要

- 可阅读的个人笔记现放在 `raw/1-Note/`，配图在 `raw/1-Note/img/`。
- 笔记按主题拆成下面的 wiki 页；公式、图和长代码仍以原笔记为准。
- 原笔记里的图示没有复制进 wiki。

## 对照

| 原笔记 | 覆盖 | wiki |
|--------|------|------|
| `2-MachineLearning/1-math.md` | MCMC、M-H、Gibbs | [采样](./mcmc-sampling.md) |
| `2-MachineLearning/2-machine-learning.md` | 项目流程、监督/无监督算法地图、偏差与不平衡 | [机器学习地图](./machine-learning-map.md) |
| `3-DeepLearning/1-deep-learning.md` | 网络层、激活函数、优化器 | [深度学习构件](./deep-learning-building-blocks.md) |
| `3-DeepLearning/2-NLP.md` | 词向量、注意力、Transformer 与预训练模型 | [NLP 表示与预训练模型](./nlp-representation-and-pretrained-models.md) |
| `3-DeepLearning/3-AI.md` | 知识图谱、强化学习、视觉、图网络、生成模型 | 见下方分篇 |
| `3-DeepLearning/llm.md` | Function calling 与 MCP | [Function calling 与 MCP](./llm-function-calling-and-mcp.md) |

`3-AI.md` 拆成：

- [知识表示与实体链接](../kg/knowledge-graph-representation.md)
- [强化学习概念](./reinforcement-learning-concepts.md)
- [图表示学习](./graph-representation-learning.md)
- [生成模型](./generative-models.md)
- [视觉模型](./computer-vision-models.md)

多模态和时间序列仍主要留在 `3-AI.md`，这一轮没有单独展开。

## 相关

- [PyTorch 强化学习示例目录](./pytorch-reinforcement-learning-notes.md)
- [MOC](../MOC.md)
