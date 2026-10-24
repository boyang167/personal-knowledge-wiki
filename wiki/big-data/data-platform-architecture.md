---
title: 数据平台架构演进（Lambda / Kappa / 湖仓一体）
summary: 对比 Lambda、Kappa 与湖仓一体架构的短板及 Table/列式/序列化存储格式选型要点
tags: [big-data, lakehouse, lambda, kappa, architecture]
status: draft
updated: 2026-10-24
sources:
  - path: raw/2-StudyMaterials/7-BigData/design.md
    note: Architecture evolution、对比表、Storage-layer / Table Format 小节
---

# 数据平台架构演进

## 结论摘要

- **Lambda**：离线 + 实时双链路，常见代价是双份开发、资源占用高、离线与实时结果不一致、批量可能 T+1 跑不完、存储需求大。
- **Kappa**：以流为核心，常见短板包括 Kafka 难以承载海量存储、OLAP 支持弱、血缘复用难、缺少 update/upsert 语义。
- **湖仓一体（Data Lakehouse）**：通过统一存储、分层 OLAP、血缘与实时更新等能力，**部分**缓解 Kappa 侧问题；对 Lambda 更多是架构简化与能力增强，而非一一「对症下药」。
- **存储分层**：湖存储层常见 **Table Format** 为 Delta Lake、Apache Hudi、Apache Iceberg；列存 Parquet/ORC；序列化 Avro 等（细节以 raw 原文为准）。

## Lambda

双路径（批 + 流）满足同一业务需求。主要缺点见下表（与 raw 资料一致）。

| 架构 | 主要缺点（摘要） |
|------|------------------|
| Lambda | 两套实现、资源多、离线与实时不一致、批量时效、存储大 |

## Kappa

以 Kafka 等流处理为主轴。主要缺点包括存储规模、OLAP、血缘、更新语义等（见 raw 对比表）。

## 湖仓一体

统一存储 + 分层分析 + 血缘复用 + 实时更新等，与 Kappa 短板的对照关系见 raw 中「湖仓一体对其缺点的解决」列。

## 存储与表格式（备忘）

- **Table Format**：Delta Lake、Apache Hudi、Apache Iceberg
- **列式**：Parquet、ORC
- **二进制序列化**：Avro

> 图示（lambda/kappa/lakehouse 等 SVG）位于 raw 同目录 `img/`，wiki 不复制图片，需要时直接打开 raw 路径。

## 待核实

- 湖仓对 Lambda 各条缺点的「间接缓解」程度需结合具体产品栈再核对。

## 相关

- [MOC](../MOC.md)
- [Apache Flink 流处理](./flink-stream-processing.md)
