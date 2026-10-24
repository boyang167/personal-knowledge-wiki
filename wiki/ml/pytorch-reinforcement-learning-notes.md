---
title: PyTorch 强化学习示例目录
summary: 按本地教程仓库的章节顺序整理从 Q-learning 到 Actor-Critic 的算法台阶，便于按目录回读代码
tags: [ml, reinforcement-learning, pytorch, dqn]
status: draft
updated: 2026-10-24
sources:
  - path: raw/2-StudyMaterials/3-ReinforcementLearning/Reinforcement-learning-with-PyTorch/README.md
    note: 仓库来源说明，由 TensorFlow 教程改写为 PyTorch
---

# PyTorch 强化学习示例目录

## 结论摘要

- 本地目录是 MorvanZhou 强化学习教程的 PyTorch 改写，示例按算法由表格法走到策略梯度和 Actor-Critic。
- 每个章节是可运行脚本，不是论文笔记；公式和超参数以对应 `RL_brain.py` 为准。
- 价值方法在前，策略方法在后。Double、优先回放和 Dueling 都是 DQN 的变体，不是替代 Q-learning 的另一套问题设定。

## 阅读顺序

| 目录 | 内容 |
|------|------|
| `content/1_treasure_on_right` | 最小环境，熟悉回合循环 |
| `content/2_Q-learning-maze` | 表格 Q-learning |
| `content/3_Sarsa_maze` | 同策略的 Sarsa |
| `content/4_Sarsa_lambda_maze` | 带资格迹的 Sarsa(λ) |
| `content/5_Deep_Q_Network` | 用网络近似 Q 的 DQN |
| `content/5.1_double_DQN` | Double DQN |
| `content/5.2_Prioritized_Replay_DQN` | 优先经验回放 |
| `content/5.3_Dueling_DQN` | Dueling 网络结构 |
| `content/7_Policy_gradient_softmax` | 离散动作的策略梯度 |
| `content/8_Actor_Critic_Advantage` | Advantage Actor-Critic，含 CartPole 与连续 Pendulum |

目录编号从 5.3 跳到 7，中间没有第 6 章。环境脚本（迷宫、CartPole、MountainCar、Pendulum）和算法脚本是分开的。

## 待核实

- 本页只根据目录和 README 建立索引，没有逐文件核对实现是否与原始 TensorFlow 教程一致。

## 相关

- [MOC](../MOC.md)
