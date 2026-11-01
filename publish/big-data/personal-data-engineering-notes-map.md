---
title: 个人数据工程笔记地图（Spark / Flink / Hive）
summary: 对齐 Spark、Flink、Hive 笔记与知识库大数据页面，说明主笔记目录与工程侧重点
tags: [big-data, spark, flink, hive, notes]
status: reviewed
updated: 2026-11-01
sources:
  - path: wiki/big-data/personal-data-engineering-notes-map.md
    note: 对外发布副本
---

# 个人数据工程笔记地图

## 结论摘要

- **主笔记**在 [Flink 笔记](/notes/4-DataEngineering/2-flink/)、[Spark 笔记](/notes/4-DataEngineering/1-spark/) 等；早期 `8-BigData` 目录与之重叠，以 `4-DataEngineering` 为准。
- 知识库概念页：[数据平台架构演进](/knowledge/big-data/data-platform-architecture/)、[Flink 流处理核心](/knowledge/big-data/flink-stream-processing/)。
- Flink 笔记侧重 **落地**：Standalone / YARN / K8s、MySQL CDC、Dinky 生态、State Backend 与运维命令。
- Spark 笔记篇幅长，适合作算子、调优与作业模型的 **完整原件**；知识库尚未全文提炼。

## 对照

| 笔记主题 | 说明 | 知识库 |
|----------|------|--------|
| Flink | 部署、CDC、K8s | [Flink 流处理核心](/knowledge/big-data/flink-stream-processing/) |
| Spark | 全量 Spark 笔记 | [数据平台架构](/knowledge/big-data/data-platform-architecture/)（部分重叠） |
| Hive | Hive 笔记 | 待专页 |

## 相关

- [1-Note 主题索引](/knowledge/tech/one-note-raw-index/)
- [知识库首页](/knowledge/)
