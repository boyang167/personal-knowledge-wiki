# 数据库笔记索引

## 综合 / MySQL / SQL

- **[8-mysql.md](8-mysql.md)** — 自 Desktop `2024/7-DataBase.md` 迁移并整理（目录 + 章节标题；含 SQL/MySQL、Redis、ES、MongoDB、Hive、Consul、Kafka/RabbitMQ 等）

# Redis


# kafka


# RabbitMQ


# ETCD

# NATS



| 特性                 | NATS               | Kafka            | RabbitMQ           |
| -------------------- | ------------------ | ---------------- | ------------------ |
| **持久化**     | JetStream支持      | 是               | 是                 |
| **协议复杂度** | 极简（基于文本）   | 高（二进制协议） | 中等（AMQP）       |
| **延迟**       | 亚毫秒级           | 毫秒级           | 毫秒级             |
| **适用规模**   | 中小到大规模       | 超大规模         | 中小规模           |
| **典型场景**   | 实时通信、事件驱动 | 日志流、大数据   | 任务队列、企业集成 |
