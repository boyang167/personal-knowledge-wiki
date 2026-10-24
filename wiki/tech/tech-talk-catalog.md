---
title: 技术分享题目索引
summary: 把 raw 中技术分享 README 的题目收成主题索引，具体提纲仍回 raw 阅读
tags: [tech, talks, distributed-systems, golang]
status: draft
updated: 2026-10-24
sources:
  - path: raw/2-StudyMaterials/9-Tech/技术博客/README.md
    note: 分享题目列表与各篇提纲
---

# 技术分享题目索引

## 结论摘要

- `raw/2-StudyMaterials/9-Tech/技术博客/README.md` 是一份分享提纲目录，不是可直接引用的结论页。
- 题目集中在长连接与消息、Go、Kubernetes 与服务网格、Redis、MySQL，以及 HTTP/2、QUIC、Raft。
- 需要细节时打开该 README 的对应小节；本页不复制提纲正文。

## 主题

| 主题 | 提纲中的题目 |
|------|----------------|
| 接入与消息 | 海量长连接消息推送、分布式消息推送、Kafka、分布式行情推送 |
| 网络 | 网络编程、TCP、HTTP/2 与 QUIC、CDN、gRPC |
| Go | 项目实战、高级技巧、高性能实战、高级讲义 |
| 编排与网格 | Kubernetes、Istio、Service Mesh、集群管理 |
| 数据与一致性 | Redis、Redis Cluster、MySQL 速成、MySQL ACID、Raft、Etcd |
| 运行时与工程 | Python GIL、Python 内存、多进程、异步 IO 调度、git、分布式任务系统 |

其中「Qcon 海量长连接消息推送」一节写了分享日期 2021-06-30，并列出百万级长连接、每日近百亿消息、峰值每秒 70 万以上等目标量级。这些数字属于该次分享材料，不是本知识库实测。

## 相关

- [MOC](../MOC.md)
