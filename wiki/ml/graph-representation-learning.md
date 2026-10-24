---
title: 图表示学习方法索引
summary: 按个人笔记的小节顺序，把图嵌入、图神经网络和动态图方法列成索引
tags: [ml, graph, gnn, embedding]
status: draft
updated: 2026-10-24
sources:
  - path: raw/1-Note/3-DeepLearning/3-AI.md
    note: Graph Network 一节的方法标题
---

# 图表示学习方法索引

## 结论摘要

- 笔记先写图嵌入，再写图神经网络，最后写动态图。本页按这个顺序做索引，不复述各方法的公式。
- 嵌入一节从 DeepWalk 排到 EGES。网络一节从 GCN、GAT、GraphSAGE 排到 HAN、GTN，以及 metapath2vec、BiNE 等异构或二部图标题。
- 动态图方法关注表示随时间变化，和静态嵌入不是同一任务。

## 笔记中的方法

| 分组 | 笔记标题 |
|------|----------|
| 图嵌入 | DeepWalk、LINE、node2vec、SDNE、struc2vec、EGES |
| 图神经网络 | 图卷积、GNN、GCN、GAT、GraphSAGE（含 minibatch 与 embedding）、HAN、GTN |
| 异构或符号图 | metapath2vec、GATNE、BiNE、SGCN、SiGAT、SDGNN |
| 动态图 | DySAT、EvolveGCN、Streaming GNN、DGNN、TGAT |

图示和更新公式在 `3-AI.md` 的 Graph Network 一节。

## 待核实

- 若干标题在笔记中拼写不一致（如 GraphSAGE）。对照论文时以标准写法为准。
- 本页没有核对每个方法的原论文是否被笔记正确概括。

## 相关

- [知识表示与实体链接](../kg/knowledge-graph-representation.md)
- [MOC](../MOC.md)
