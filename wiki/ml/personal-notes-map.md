---
title: 个人学习笔记地图
summary: 说明 raw/1-Note 里数学、机器学习、深度学习和 LLM 笔记各自覆盖什么，并链到已提炼的 wiki 页
tags: [ml, notes, map]
status: draft
updated: 2026-11-01
sources:
  - path: raw/1-Note/2-MachineLearning/1-math.md
    note: 采样笔记
  - path: raw/1-Note/2-MachineLearning/2-machine-learning.md
    note: 机器学习流程与算法提纲
  - path: raw/1-Note/3-DeepLearning/1-deep-learning.md
    note: 网络层、激活函数和优化器
  - path: raw/1-Note/3-DeepLearning/2-NLP.md
    note: 表示学习与预训练模型
  - path: raw/1-Note/3-DeepLearning/3-KG.md
    note: 知识图谱
  - path: raw/1-Note/3-DeepLearning/4-llm.md
    note: LLM 专题
  - path: raw/1-Note/3-DeepLearning/5-GraphNeuralNetwork.md
    note: 图神经网络
  - path: raw/1-Note/3-DeepLearning/6-ReinforcementLearning.md
    note: 强化学习
  - path: raw/1-Note/3-DeepLearning/7-GenerateModel.md
    note: 生成模型
  - path: raw/1-Note/3-DeepLearning/8-ComputerVision.md
    note: 计算机视觉
  - path: raw/1-Note/3-DeepLearning/llm.md
    note: Function calling 与 MCP
  - path: raw/1-Note/15-RecommandSystem/1-推荐系统.md
    note: 推荐系统
  - path: raw/1-Note/18-GPU/1-cuda.md
    note: CUDA
---

# 个人学习笔记地图

## 结论摘要

- 可阅读的个人笔记在 `raw/1-Note/`，配图在 `raw/1-Note/img/`。
- 深度学习笔记已 **按文件拆分**（不再使用旧的 `3-AI.md` 单文件）；下列 wiki 页为提炼入口，公式与图仍以 raw 为准。
- 全路径登记见 [raw/1-Note 全量索引](../tech/one-note-raw-index.md)。

## 对照

| 原笔记 | 覆盖 | wiki |
|--------|------|------|
| `2-MachineLearning/1-math.md` | MCMC、M-H、Gibbs | [采样](./mcmc-sampling.md) |
| `2-MachineLearning/2-machine-learning.md` | 项目流程、监督/无监督算法地图 | [机器学习地图](./machine-learning-map.md) |
| `3-DeepLearning/1-deep-learning.md` | 网络层、激活函数、优化器 | [深度学习构件](./deep-learning-building-blocks.md) |
| `3-DeepLearning/2-NLP.md` | 词向量、注意力、Transformer | [NLP 表示与预训练](./nlp-representation-and-pretrained-models.md) |
| `3-DeepLearning/3-KG.md` | 知识图谱 | [知识表示与实体链接](../kg/knowledge-graph-representation.md) |
| `3-DeepLearning/4-llm.md` | LLM 通用 | 与 [Function calling 与 MCP](./llm-function-calling-and-mcp.md) 互补 |
| `3-DeepLearning/5-GraphNeuralNetwork.md` | GNN | [图表示学习](./graph-representation-learning.md) |
| `3-DeepLearning/6-ReinforcementLearning.md` | RL | [强化学习概念](./reinforcement-learning-concepts.md) |
| `3-DeepLearning/7-GenerateModel.md` | VAE/GAN/扩散等 | [生成模型](./generative-models.md) |
| `3-DeepLearning/8-ComputerVision.md` | 视觉 | [视觉模型索引](./computer-vision-models.md) |
| `3-DeepLearning/llm.md` | Function calling、MCP | [Function calling 与 MCP](./llm-function-calling-and-mcp.md) |
| `15-RecommandSystem/1-推荐系统.md` | 推荐 | [深度学习推荐资料索引](./deep-learning-source-index.md) |
| `18-GPU/*.md` | CUDA / PyTorch GPU | [架构与 GPU 笔记](../tech/personal-architecture-and-misc-notes.md) |

## 相关

- [PyTorch 强化学习示例目录](./pytorch-reinforcement-learning-notes.md)
- [MOC](../MOC.md)
