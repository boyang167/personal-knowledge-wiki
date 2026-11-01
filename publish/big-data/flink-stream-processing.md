---
title: Apache Flink 流处理核心概念与作业模型
summary: 梳理 Flink 的批流统一、状态计算、时间语义、窗口、Checkpoint、算子链与部署模式，作为学习和设计实时作业的速查页
tags: [big-data, flink, stream-processing, state, checkpoint]
status: reviewed
updated: 2026-11-01
sources:
  - path: wiki/big-data/flink-stream-processing.md
    note: 对外发布副本，原始资料路径不对外
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

- **Client**：提交作业的入口。
- **JobManager**：调度、协调 Checkpoint、管理 TaskManager。
- **TaskManager**：提供 Slot，每个 Slot 通常运行一个 Task 线程。

常见部署与提交模式包括 Standalone、YARN、Kubernetes 等；生产环境需按资源隔离与作业模式（Session / Application / Per-Job）选型。

## 算子链

当多个算子满足相同并行度、Forward 连接、同一 Slot Sharing Group 等条件时，Flink 可能将其合并为算子链以减少开销。`keyBy`、`rebalance`、`broadcast` 或并行度变化通常会打断链。

## Table API / SQL 备忘

表名通常组织为 Catalog / Database / Table；SQL 结果可能表现为 append、upsert 或 retract 等更新语义，需按连接器与版本核对。

## 工程实践延伸

个人笔记（见 [数据工程笔记地图](/knowledge/big-data/personal-data-engineering-notes-map/)）还覆盖：Dinky / StreamPark 生态、Flink on K8s、MySQL CDC 连接器选型、State Backend 与 Session 集群运维等。**概念层以本页为准，部署与运维细节以笔记为准。**

## 待核实

- 未绑定具体 Flink 版本；生产配置、Checkpoint 与 SQL 语义需按目标版本复核。

## 相关页面

- [数据平台架构演进](/knowledge/big-data/data-platform-architecture/)
- [数据工程笔记地图](/knowledge/big-data/personal-data-engineering-notes-map/)
- [知识库首页](/knowledge/)
