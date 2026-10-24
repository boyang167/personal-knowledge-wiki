---
title: 强化学习的基本划分
summary: 用状态、动作、策略和奖赏整理笔记中的 Model-free/Model-based、价值/策略、在线/离线划分
tags: [ml, reinforcement-learning, q-learning, policy]
status: draft
updated: 2026-10-24
sources:
  - path: raw/1-Note/3-DeepLearning/3-AI.md
    note: Reinforcement Learning 一节的分类和 Q-learning 术语
---

# 强化学习的基本划分

## 结论摘要

- 智能体通过观察环境得到状态，按策略选动作，环境返回奖赏。状态只包含智能体观察得到的那部分特征。
- 笔记用三组对立概念分类：是否建模环境、优化的是价值还是策略、更新发生在回合结束还是单步。
- 在线学习和离线学习是另一条轴。笔记点名的算法包括 Q-learning、Sarsa、Policy Gradient 和 Actor-Critic。
- 不确定来自策略，也来自环境。

## 分类

| 轴 | 两端 |
|----|------|
| 环境模型 | Model-Free 不建环境模型；Model-Based 建环境模型 |
| 学习对象 | Value-Based 学价值；Policy-Based 学策略 |
| 更新粒度 | 单步更新；回合更新 |
| 数据使用 | 在线学习；离线学习 |

策略写成 \(\pi(a \mid s) = P(A=a \mid S=s)\)。奖赏在笔记里排成状态为行、动作为列的矩阵。

## 和示例代码的关系

算法台阶和可运行脚本见 [PyTorch 强化学习示例目录](./pytorch-reinforcement-learning-notes.md)。本页只固定术语，不描述那些脚本的实现。

## 待核实

- `3-AI.md` 这一节后还有大量公式图，本页没有逐式转录。

## 相关

- [MCMC 采样](./mcmc-sampling.md)
- [MOC](../MOC.md)
