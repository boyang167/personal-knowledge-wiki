---
title: Apache Flink 流处理核心概念与作业模型
summary: 梳理 Flink 的批流统一、状态计算、时间语义、窗口、Checkpoint、算子链与部署模式，作为学习和设计实时作业的速查页
tags: [big-data, flink, stream-processing, state, checkpoint]
status: draft
updated: 2026-10-24
sources:
  - path: raw/2-StudyMaterials/7-BigData/Flink/Flink.md
    note: Flink 基本概念、四个基石、JobManager/TaskManager、部署模式、算子链与 Table/SQL 相关笔记
---

# Apache Flink 流处理核心概念与作业模型

## 结论摘要

- Flink 面向有界和无界数据流，支持事件时间（event time）与处理时间（processing time）。
- 有状态计算的可靠性核心是状态（State）、Checkpoint、时间（Time）和窗口（Window）。
- JobManager 负责作业管理与调度，TaskManager 负责执行被拆分后的 Task。
- 算子链在满足并行度、Forward 传输和 Slot Sharing 等条件时，可把多个算子合并到同一 Task，减少网络传输与线程切换。

## 核心模型

### 数据流与时间

- **有界数据流**：有明确结束位置的数据集，可按批处理方式计算。
- **无界数据流**：持续到达、没有自然终点的数据，需要持续运行的作业处理。
- **事件时间**：事件实际发生的时间，适合处理乱序和迟到事件。
- **处理时间**：算子处理事件的机器时间，语义简单但受处理延迟影响。

### 四个基石

| 概念 | 作用 |
|------|------|
| State | 保存跨事件、跨记录的中间计算结果 |
| Checkpoint | 持久化一致性快照，用于故障恢复 |
| Time | 定义计算何时发生以及如何处理乱序 |
| Window | 将持续流切分为可计算的有限范围 |

## 集群架构与提交模式

Flink 采用 JobManager + TaskManager 的主从式执行模型：作业提交后会被拆分为多个 Task，由 JobManager 调度到不同 TaskManager 执行；运行期间，集群还负责状态管理、监控、失败恢复或重试。

资料中列出的作业部署模式包括：

- Standalone
- Session mode
- Per-job mode
- Application mode

这些模式的差异主要体现在集群与作业的生命周期、资源隔离和提交边界上，实际选择应结合平台运维方式与资源管理器再确认。

## 算子链

算子链（Operator Chaining）把多个逻辑算子合并为一个 Task，使数据在同一线程内以函数调用方式传递，减少网络传输和序列化开销。

常见形成条件：

1. 上下游算子并行度相同。
2. 上下游数据传输方式为 Forward。
3. 算子处于相同的 Slot Sharing Group。
4. 没有显式禁用算子链。

如果发生 `keyBy`、`rebalance`、`broadcast` 等需要重新分区的传输，或者并行度不同，通常不能直接合并为同一条算子链。

## Table API / SQL 备忘

资料将 Flink 的表组织为 Catalog、Database 和 Table name 三层，并区分临时表与永久表。SQL 结果还可能表现为 append、upsert 或 retract 等更新流语义；具体语义取决于查询和连接器能力，使用前应核对目标版本文档。

## 待核实

- 本页保留的是原始学习笔记中的概念总结，未绑定具体 Flink 版本；生产配置、Checkpoint 细节和 SQL 更新语义需按目标版本复核。

## 相关页面

- [数据平台架构演进](./data-platform-architecture.md)
- [MOC](../MOC.md)
