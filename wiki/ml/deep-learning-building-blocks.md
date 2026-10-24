---
title: 深度学习网络构件
summary: 整理全连接层、激活函数和两类优化器的选用边界，作为网络配置备忘
tags: [ml, deep-learning, activation, optimizer]
status: draft
updated: 2026-10-24
sources:
  - path: raw/1-Note/3-DeepLearning/1-deep-learning.md
    note: 常见层、网络配置、全连接、激活函数和优化器列表
---

# 深度学习网络构件

## 结论摘要

- 笔记把网络拆成三块：层（全连接、卷积、循环、归一化、Dropout、Embedding 等）、训练配置（损失、优化器、初始化、正则）和训练流程（预训练、归一化、数据增强）。
- 全连接层把前面提取的特征合在一起，参数量通常最大。
- 隐藏层用 ReLU、tanh、softplus 这类非线性；分类输出用 sigmoid 或 softmax；回归输出可以用线性函数。
- 优化器分成“只看当前梯度”和“带动量”两类。笔记点名了 SGD、Adagrad、Adadelta、Momentum、Adam、FTRL、RMSProp。

## 激活函数怎么选

| 位置 | 笔记中的选择 |
|------|----------------|
| 隐藏层 | ReLU、tanh、softplus，用来引入非线性 |
| 二分类或概率输出 | sigmoid，数值越大越接近 1 |
| 多分类 | softmax，取概率最大的类 |
| 回归 | 线性输出 |

Leaky ReLU 出现在笔记的曲线对照里，没有单独写使用条件。

## 待核实

- 优化器只列了 TensorFlow 的类名，没有学习率或适用数据规模。笔记把第一类写成「不带重量」，这里按上下文理解为不带动量。
- 原笔记到优化器列表为止，卷积和循环层没有展开。

## 相关

- [NLP 表示与预训练模型](./nlp-representation-and-pretrained-models.md)
- [生成模型](./generative-models.md)
- [MOC](../MOC.md)
