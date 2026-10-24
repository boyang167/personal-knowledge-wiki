---
title: MCMC、M-H 与 Gibbs 采样
summary: 记录马尔可夫链平稳分布、M-H 采样的两个缺点，以及 Gibbs 采样适用的条件
tags: [ml, mcmc, gibbs, sampling]
status: reviewed
updated: 2026-10-24
sources:
  - path: wiki/ml/mcmc-sampling.md
    note: 对外发布副本，原始资料路径不对外
---

# MCMC、M-H 与 Gibbs 采样

## 结论摘要

- 马尔可夫链的转移矩阵若收敛到平稳分布，该分布与初始分布无关。笔记认为这对多数链、以及连续状态也成立。
- M-H 采样要计算接受率。维度高时计算贵，接受率还会拖慢收敛。
- 有些高维数据的条件分布好写、联合分布难写，因此转向 Gibbs 采样。
- Gibbs 至少需要两个维度。一维分布仍然用 M-H。

## 细致平稳

对非周期马尔可夫链，若对所有状态 i、j 有

`π(i) P(i, j) = π(j) P(j, i)`

则 π 是平稳分布。采样算法用这个条件构造能收敛到目标分布的转移。

## 待核实

- 原笔记很短，连续状态“也成立”没有给出证明范围。

## 相关

- [机器学习地图](/knowledge/ml/machine-learning-map/)
- [MOC](/knowledge/)
