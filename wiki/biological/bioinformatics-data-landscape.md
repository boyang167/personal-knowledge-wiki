---
title: 生物信息学数据资源总览与蛋白数据整合线索
summary: 按数据类型和使用场景整理 GenBank、UniParc、JGI、MGnify 等资源，辅助设计可持续更新的蛋白与基因数据库
tags: [biological, bioinformatics, protein, genome, database]
status: draft
updated: 2026-10-24
sources:
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/README.md
    note: 数据库项目进度表、数据内容与用途
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/MSR_prodb_survey/MSR_prodb_survey.md
    note: UniParc、JGI、MGnify、GenBank 的数据来源、格式和下载线索
---

# 生物信息学数据资源总览与蛋白数据整合线索

## 结论摘要

- 不同资源覆盖的数据对象不同：序列库、基因组/注释库、宏基因组数据、蛋白结构和通路库不能简单互相替代。
- 如果目标是构建持续更新、去重的蛋白数据库，应把序列主表与来源交叉引用、版本、状态和 TaxID 等元数据分开管理。
- UniParc 的定位是非冗余蛋白序列归档；其他来源的功能、注释和交叉引用需要回到来源数据库查询。
- GenBank 同时包含传统 flatfile、WGS/TSA/TLS 和 genome 等数据组织方式，解析时需要按记录类型设计适配器。

## 资源与适用场景

| 资源 | 主要内容 | 典型用途 | 常见获取线索 |
|------|----------|----------|-------------|
| UniParc | 非冗余蛋白序列及来源交叉引用 | 蛋白序列归档、去重 | FASTA、XML、FTP |
| JGI GOLD | 基因组/宏基因组项目及元数据 | 项目、样本和测序信息 | Portal / 数据下载 |
| JGI IMG/IMG-M | 微生物基因组与注释 | 比较基因组与注释分析 | Portal / 下载 |
| MGnify | 微生物组分析及衍生肽序列 | 宏基因组与蛋白集合 | ENA FTP、peptide database |
| GenBank | DNA 序列、注释和组装数据 | 基因、基因组及序列查询 | FTP、flatfile、Assembly |

## 建议的数据模型

对“持续更新 + 去重”的需求，可拆成以下几层：

1. **Sequence**：规范化后的蛋白序列、稳定内部 ID 和序列哈希。
2. **Source record**：来源数据库、accession、版本、抓取时间和原始状态。
3. **Cross-reference**：UniProt、PDB、GenBank、JGI 等外部标识之间的关联。
4. **Annotation**：功能、分类、结构域、物种等可变注释，保留来源和版本。
5. **Ingestion audit**：下载批次、解析器版本、失败记录和重复合并结果。

这样可以让序列去重与来源记录保留同时成立，避免把不同来源的版本变化误当成新序列。

## 处理注意事项

- 原始序列与注释的生命周期不同，不能只用一个“最新时间”字段表达全部变化。
- 蛋白序列去重后仍需保留来源 accession，否则无法追溯到原始数据库。
- 下载和解析要记录版本；来源站点的统计数字具有时间点属性，不应视为永久事实。
- 该资料目录中的部分数据源是调研或项目进度记录，具体字段和下载权限需再次核对。

## 待核实

- 各资源当前版本、规模、下载入口及许可条款会变化；本页不把原始资料中的历史统计当作当前状态。

## 相关页面

- [本地化项目地图](./bioinformatics-local-data-project.md)
- [人类基因注释与 GenBank 发布](./human-annotation-and-expression.md)
- [KEGG 通路数据库调研](./kegg-pathway-database.md)
- [MOC](../MOC.md)
