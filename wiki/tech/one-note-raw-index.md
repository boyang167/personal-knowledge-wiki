---
title: raw/1-Note 笔记全量索引
summary: 登记 personal-knowledge-wiki 下 1-Note 全部 Markdown 路径，供 Agent 路由到原件；细节以 raw 为准
tags: [tech, notes, index, ingest]
status: draft
updated: 2026-11-01
sources:
  - path: raw/1-Note/README.md
    note: 1-Note 目录说明（若存在）
---

# raw/1-Note 笔记全量索引

## 结论摘要

- 门户「笔记」模块直接读取 `raw/1-Note/**/*.md`；wiki 侧用本页做 **路径登记**，避免重复自动摘录页。
- 已提炼的主题见各域 **地图页**（生信、大数据、ML、基础设施等）；未单独建 wiki 的条目仍在此表。
- 配图统一在 `raw/1-Note/img/`，wiki 不复制图片。

## 主题地图（wiki）

| 域 | 地图页 |
|----|--------|
| 生信 / 蛋白 / CMC | [个人生信笔记地图](../biological/personal-bioinformatics-notes-map.md) |
| Spark / Flink / Hive | [数据工程笔记地图](../big-data/personal-data-engineering-notes-map.md) |
| ML / DL / LLM | [个人学习笔记地图](../ml/personal-notes-map.md) |
| Redis / Kafka / SQL | [数据库与消息中间件笔记](../database/personal-database-messaging-notes.md) |
| K8s / 云 / 虚拟化 | [基础设施笔记地图](../infrastructure/personal-infrastructure-notes-map.md) |
| 架构 / 云厂商 / 杂项 | [架构与扩展主题笔记](./personal-architecture-and-misc-notes.md) |

## 文件登记

| 路径 | 主题 |
|------|------|
| `raw/1-Note/1-Bioinformatics&Data/1-Bioinformatics.md` | 生信综合 |
| `raw/1-Note/1-Bioinformatics&Data/Bio Business summary.md` | 生信商业 |
| `raw/1-Note/1-Bioinformatics&Data/README.md` | 目录说明 |
| `raw/1-Note/1-Bioinformatics&Data/Protein/molecule_anlysis.md` | 分子分析 |
| `raw/1-Note/1-Bioinformatics&Data/Protein/protein.md` | 蛋白 / CMC 工艺 |
| `raw/1-Note/2-MachineLearning/1-math.md` | 采样与数学 |
| `raw/1-Note/2-MachineLearning/2-machine-learning.md` | 机器学习流程 |
| `raw/1-Note/3-DeepLearning/1-deep-learning.md` | 深度学习构件 |
| `raw/1-Note/3-DeepLearning/2-NLP.md` | NLP |
| `raw/1-Note/3-DeepLearning/3-KG.md` | 知识图谱 |
| `raw/1-Note/3-DeepLearning/4-llm.md` | LLM |
| `raw/1-Note/3-DeepLearning/5-GraphNeuralNetwork.md` | 图神经网络 |
| `raw/1-Note/3-DeepLearning/6-ReinforcementLearning.md` | 强化学习 |
| `raw/1-Note/3-DeepLearning/7-GenerateModel.md` | 生成模型 |
| `raw/1-Note/3-DeepLearning/8-ComputerVision.md` | 计算机视觉 |
| `raw/1-Note/3-DeepLearning/llm.md` | Function calling / MCP |
| `raw/1-Note/4-DataEngineering/1-pyspark.md` | PySpark |
| `raw/1-Note/4-DataEngineering/1-spark.md` | Spark |
| `raw/1-Note/4-DataEngineering/2-flink.md` | Flink 运维与 CDC |
| `raw/1-Note/4-DataEngineering/3-hive.md` | Hive |
| `raw/1-Note/5-Infrastructure/Ambari-HDP.md` | Ambari / HDP |
| `raw/1-Note/5-Infrastructure/Azure.md` | Azure |
| `raw/1-Note/5-Infrastructure/ELK.md` | ELK |
| `raw/1-Note/5-Infrastructure/K8s.md` | Kubernetes / Traefik 等 |
| `raw/1-Note/5-Infrastructure/OpenStack-Kolla.md` | OpenStack Kolla |
| `raw/1-Note/5-Infrastructure/VMWare.md` | VMWare |
| `raw/1-Note/5-Infrastructure/计算机基础知识.md` | 计算机基础 |
| `raw/1-Note/7-Programming/1-go.md` | Go |
| `raw/1-Note/7-Programming/2-python.md` | Python |
| `raw/1-Note/7-Programming/3-vue.md` | Vue |
| `raw/1-Note/7-Programming/4-torch.md` | PyTorch |
| `raw/1-Note/7-Programming/面试编程题/面试编程题-算法整理.md` | 算法面试 |
| `raw/1-Note/8-BigData/0-basic-knowledge.md` | 大数据基础 |
| `raw/1-Note/8-BigData/1-spark.md` | Spark（旧目录） |
| `raw/1-Note/8-BigData/2-flink.md` | Flink（旧目录） |
| `raw/1-Note/8-BigData/2-flink-Dinky.md` | Dinky |
| `raw/1-Note/8-BigData/3-pyspark.md` | PySpark（旧目录） |
| `raw/1-Note/8-BigData/8-hadoop实际操作实验记录.md` | Hadoop 实验 |
| `raw/1-Note/10-TechSharing/1-network.md` | 网络分享 |
| `raw/1-Note/10-TechSharing/README.md` | 技术分享目录 |
| `raw/1-Note/11-Database/1-redis.md` | Redis |
| `raw/1-Note/11-Database/2-kafka.md` | Kafka |
| `raw/1-Note/11-Database/3-rabbitmq.md` | RabbitMQ |
| `raw/1-Note/11-Database/4-nets.md` | 网络相关 |
| `raw/1-Note/11-Database/5-etcd.md` | etcd |
| `raw/1-Note/11-Database/6-consul.md` | Consul |
| `raw/1-Note/11-Database/7-qdrant.md` | Qdrant |
| `raw/1-Note/11-Database/8-mysql.md` | MySQL |
| `raw/1-Note/11-Database/message.md` | 消息总览 |
| `raw/1-Note/11-Database/README.md` | 数据库目录 |
| `raw/1-Note/11-Database/sql.md` | SQL |
| `raw/1-Note/12-Architecture/1-Monitoring.md` | 监控 |
| `raw/1-Note/12-Architecture/2-分布式.md` | 分布式 |
| `raw/1-Note/12-Architecture/3-lowcode.md` | 低代码 |
| `raw/1-Note/12-Architecture/15-分布式.md` | 分布式（补充） |
| `raw/1-Note/12-Architecture/overall.md` | 架构总览 |
| `raw/1-Note/12-Architecture/README.md` | 架构目录 |
| `raw/1-Note/13-Stock/web.md` | 股票 Web |
| `raw/1-Note/13-Stock/基本知识.md` | 股票基础 |
| `raw/1-Note/15-RecommandSystem/1-推荐系统.md` | 推荐系统 |
| `raw/1-Note/15-RecommandSystem/README.md` | 推荐目录 |
| `raw/1-Note/16-Cloud/1-azure.md` | Azure 云 |
| `raw/1-Note/16-Cloud/2-tencent.md` | 腾讯云 |
| `raw/1-Note/16-Cloud/3-ali.md` | 阿里云 |
| `raw/1-Note/16-Cloud/README.md` | 云目录 |
| `raw/1-Note/17-PM/1-Manage.md` | 项目管理 |
| `raw/1-Note/17-PM/README.md` | PM 目录 |
| `raw/1-Note/18-GPU/1-cuda.md` | CUDA |
| `raw/1-Note/18-GPU/2-pytorch-gpu.md` | PyTorch GPU |
| `raw/1-Note/18-GPU/README.md` | GPU 目录 |

## 相关

- [MOC](../MOC.md)
- [个人 LLM Wiki 实践](./llm-personal-wiki-practice.md)
