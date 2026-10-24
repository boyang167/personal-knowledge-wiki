---
title: 数据平台架构演进（Lambda / Kappa / 湖仓一体）
summary: 对比 Lambda、Kappa 与湖仓一体架构的短板及 Table/列式/序列化存储格式选型要点
tags: [big-data, lakehouse, lambda, kappa, architecture]
status: reviewed
updated: 2026-10-24
sources:
  - path: wiki/big-data/data-platform-architecture.md
    note: 对外发布副本，已人工审核
---

# 数据平台架构演进

## 结论摘要

- **Lambda**：离线 + 实时双链路，常见代价是双份开发、资源占用高、离线与实时结果不一致。
- **Kappa**：以流为核心，常见短板包括 Kafka 难以承载海量存储、OLAP 支持弱、血缘复用难。
- **湖仓一体（Data Lakehouse）**：通过统一存储、分层 OLAP、血缘与实时更新等能力，部分缓解流式架构侧问题。

## Lambda

双路径（批 + 流）满足同一业务需求，但需要维护两套实现与一致性策略。

## Kappa

以 Kafka 等流处理为主轴，适合实时场景，但要提前规划存储规模与分析路径。

## 湖仓一体

统一存储 + 分层分析 + 血缘复用 + 实时更新，是近年数据平台演进的常见方向。

## 相关

- 完整笔记与来源见私有 wiki 仓库 `personal-knowledge-wiki`。
