---
title: 生物药公开数据本地化项目地图
summary: 按用途归纳 Bioinfo_Data 要本地化的公开库，并指向各类调研页；统计数字与入库进度以 raw 快照为准
tags: [biological, bioinformatics, data-platform, catalog]
status: draft
updated: 2026-10-24
sources:
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/README.md
    note: 项目进度表中的库名、数据内容和潜在用途
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/Proposal/bioinfodata_proposal.md
    note: 本地化、清洗、存储与查询工具的目标
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/9db_info/README.md
    note: 抗体、酶、信号肽、非典型氨基酸等九类库的归类
---

# 生物药公开数据本地化项目地图

## 结论摘要

- 项目目标是把生物药研发常用的公开数据落到本地，并做基因、序列和药物查询一类工具，而不是再造每个上游库。
- 库按用途分组：序列注释、抗体免疫、通路互作、药物靶点、结构域与结构、表达与工艺相关公开库、文献术语。
- 字段级 schema 和入库明细留在各库的 raw metadata，wiki 只保留选型与使用边界。
- 进度表里的完成状态和条目规模都是调研当时的快照，不能当成当前在线规模。

## 用途分组

| 用途 | 主要库 | wiki |
|------|--------|------|
| 序列、基因组与注释 | GenBank、UniProt、SwissProt、MANE、EMBL 专利蛋白序列 | [序列注释与表达](./human-annotation-and-expression.md)、[蛋白数据总览](./bioinformatics-data-landscape.md) |
| 抗体、纳米抗体与免疫 | IMGT、SAbDab、Thera-SAbDab、INDI、ADCdb、IEDB、DOTAD、Tabs | [抗体与免疫库](./antibody-immunology-databases.md) |
| 通路与相互作用 | KEGG、Reactome、MetaCyc、STRING、BioGRID | [互作与通路](./interaction-and-pathway-databases.md)、[KEGG](./kegg-pathway-database.md) |
| 药物、靶点与获批 | ChEMBL、DGIdb、TTD、Drugs@FDA、CAS | [药物与靶点](./drug-and-target-databases.md) |
| 结构域、酶与结构 | Pfam、CAZy、PDB、AlphaFold DB、iNClusive、SPSED | [结构域、酶与结构](./protein-domains-structures-enzymes.md) |
| 文献与术语 | PubMed、UMLS | [文献、术语与专利序列](./literature-terminology-and-patents.md) |

提案里的工具面是三条：基因信息查询、序列查询、药物信息查询。药物查询的字段拼装见药物页。

## 本地化时的共同约束

- 序列主数据、来源 accession、注释和下载批次要分开存。去重不能丢掉来源。
- 很多库只给 accession 或交叉引用，序列要回到 NCBI、UniProt 等源库取。
- 商业库或订阅库（Tabs、MetaCyc 后期获取方式）不能假设有稳定的公开批量下载。
- 进度表中出现、但没有独立调研正文的候选（如 GO、OAS、PDB、UniProt 图库、CHO 多组学、等位基因频率库）只记为待补，不在本页展开结论。

## 待核实

- 各库「已入库 / 已下载」状态以 README 进度表为准，本页不复述责任人和内部系统名。
- 许可、FTP 布局和条目数会变，使用前回到 raw 调研文档或官网核对。

## 相关

- [蛋白与基因数据总览](./bioinformatics-data-landscape.md)
- [MOC](../MOC.md)
