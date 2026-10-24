---
title: 蛋白质互作与代谢通路数据库
summary: 对比 STRING、BioGRID、Reactome、MetaCyc 与 KEGG 的证据类型，并记录代谢网络整合时要准备的四份源表
tags: [biological, pathway, ppi, string, reactome, metacyc]
status: draft
updated: 2026-10-24
sources:
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/STRING/string调研文档.md
    note: 证据通道、combined score 与和 BioGRID 的对比
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/BioGrid/BioGrid调研文档.md
    note: 遗传/蛋白/化合物相互作用及下载文件
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/Reactome/reactome.md
    note: 物理实体、反应和推断事件
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/MetaCyc/MetaCyc_investigation.md
    note: 手工代谢通路及与 KEGG 的互补
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/Meta_dbs_merge/merge.md
    note: KEGG、STRING、Reactome、BioGRID 的整合输入文件
---

# 蛋白质互作与代谢通路数据库

## 结论摘要

- STRING 混合实验、预测和文本挖掘，并用 combined score 表示总置信度；BioGRID 以文献中的实验相互作用为主。
- Reactome 把人类生物学建成「物理实体 + 事件」；修饰状态和亚细胞区室不同，就算不同实体。
- MetaCyc 收录实验报道过的代谢通路，和 KEGG 互补：KEGG 便于按名称或代谢物检索并做跨物种总图，MetaCyc 更强调物种差异和化合物性质。
- 代谢网络整合笔记准备了四份源：KEGG 通路表、STRING 链接、Reactome 元数据、BioGRID 全量。标准化和入库步骤在 raw 里仍是提纲。

## STRING 与 BioGRID

| | STRING | BioGRID |
|--|--------|---------|
| 证据 | 实验、数据库、文本挖掘、共表达、基因邻近、融合、共现，以及跨物种转移 | 文献中的实验相互作用，含物理、遗传、化合物和翻译后修饰 |
| 分数 | 各通道分开，再合成 combined score | 笔记强调实验来源，不把预测通道当主数据 |
| 适合 | 功能预测、网络扩展、富集 | 要实验支持的相互作用 |

STRING v12 的 `links.full` 保留 neighborhood、fusion、cooccurrence、coexpression、experiments、database、textmining 及对应 transferred 列。蛋白 ID 以 Ensembl 蛋白为主，别名文件可映射到 UniProt 和 NCBI Gene。笔记记录的版本是 v12.0，并写发布于 2021 年，该年份需再核对。

BioGRID 笔记中的版本 4.4.233（约 2024-05）包含蛋白/基因相互作用、化合物相互作用和翻译后修饰。下载入口是 Latest-Release 的 `BIOGRID-ALL-LATEST.tab3.zip`。和 KEGG 的对比小节在 raw 中是空的。

## Reactome

- 反应是通路中的一步：结合、激活、转位、降解、经典催化、修饰和多聚化都可建成反应。
- 物理实体包括分子、复合物和可互换的实体集。未修饰与修饰形式分开；不同区室中的同一化学物质分开，跨膜转运是把一个区室的实体变成另一个区室的实体。
- 不变的化学特征放在 ReferenceEntity，物理实体再叠加定位和修饰。
- 催化用物理实体配 GO molecular function；多个活性就建多个 CatalystActivity。
- 除人工通路外，还有计算推断到其他物种的事件。交叉引用包括 NCBI、Ensembl、UniProt、KEGG、ChEBI、PubMed、GO。

## MetaCyc 与 KEGG

- MetaCyc 属于 BioCyc，目标是为每条实验阐明的代谢通路保留一个代表样本，覆盖初生和次生代谢。
- 笔记记录的 MetaCyc 28.0 规模（通路 3538、酶促反应 19017 等）是版本快照。BioCyc 27.5（2023-12-08）的库数量同样是快照。
- 相对 KEGG：代谢物附带更多化学性质；检索往往要高级搜索；通路按物种分化，可补 KEGG 总图里缺的步骤。
- 笔记称 2017 年后获取方式改为订阅。当前许可以官网为准。

## 整合输入

`Meta_dbs_merge` 列出的准备文件：

- KEGG：`kegg_pathway_data.csv`
- STRING：`string_link.txt`、`string_physical_links.txt`
- Reactome：`reactome_metadata.tsv`
- BioGRID：`biogrid_all_data.tsv`

标准化、整合和网络存储三节没有写完，不能从这份笔记推出合并主键或去重规则。

## 待核实

- STRING 物种数、分数阈值上的边数，以及 BioGRID 4.4.233 的文献数，都是笔记中的统计，不是当前在线值。
- STRING「发布于 2021 年」与常用的 v12 时间线可能不一致。

## 相关

- [KEGG 通路数据库](./kegg-pathway-database.md)
- [本地化项目地图](./bioinformatics-local-data-project.md)
- [MOC](../MOC.md)
