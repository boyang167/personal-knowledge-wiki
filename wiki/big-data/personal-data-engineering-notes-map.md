---
title: 个人数据工程笔记地图（Spark / Flink / Hive）
summary: 对齐 raw/1-Note 下 4-DataEngineering 与 8-BigData，并链到 wiki 大数据提炼页
tags: [big-data, spark, flink, hive, notes]
status: draft
updated: 2026-11-01
sources:
  - path: raw/1-Note/4-DataEngineering/1-spark.md
    note: Spark 个人笔记（主）
  - path: raw/1-Note/4-DataEngineering/2-flink.md
    note: Flink 部署、CDC、Dinky、K8s Session
  - path: raw/1-Note/4-DataEngineering/1-pyspark.md
    note: PySpark
  - path: raw/1-Note/4-DataEngineering/3-hive.md
    note: Hive
  - path: raw/1-Note/8-BigData/2-flink-Dinky.md
    note: Dinky 相关（旧目录）
---

# 个人数据工程笔记地图

## 结论摘要

- **主笔记目录**为 `raw/1-Note/4-DataEngineering/`；`8-BigData/` 为早期并行目录，主题重叠，以 4-DataEngineering 为准更新。
- Wiki 概念速查：[数据平台架构演进](./data-platform-architecture.md)、[Flink 流处理核心](./flink-stream-processing.md)（来源含 StudyMaterials + 本目录笔记）。
- **`2-flink.md`** 侧重 **工程落地**：Standalone/YARN/K8s 提交模式、MySQL CDC、State Backend、Dinky/StreamPark 生态、运维命令与 PyFlink 链接。
- **`1-spark.md`** 为长篇 Spark 笔记，适合作算子、调优与作业模型的 **原件**；wiki 尚未全文提炼。

## 对照

| raw | 说明 | wiki |
|-----|------|------|
| `4-DataEngineering/2-flink.md` | 部署、CDC、K8s | [Flink 流处理核心](./flink-stream-processing.md) |
| `4-DataEngineering/1-spark.md` | Spark 全笔记 | [数据平台架构](./data-platform-architecture.md)（部分重叠） |
| `4-DataEngineering/3-hive.md` | Hive | 待专页 |
| `8-BigData/*` | 历史副本 | 本地图登记，避免重复 ingest |

## 相关

- [raw/1-Note 全量索引](../tech/one-note-raw-index.md)
- [MOC](../MOC.md)
