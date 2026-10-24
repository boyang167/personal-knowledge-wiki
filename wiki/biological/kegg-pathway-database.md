---
title: KEGG 通路数据库调研要点
summary: 说明 KEGG 的 PATHWAY、KO、GENES、COMPOUND 等数据组织方式、通路编号和常见应用边界
tags: [biological, bioinformatics, kegg, pathway, genomics]
status: uncertain
updated: 2026-10-24
sources:
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/KEGG/KEGG-PATHWAY调研文档.md
    note: KEGG 数据组织、map 与物种通路、KO/EC 说明、通路分类和 2024-05-30 统计快照
---

# KEGG 通路数据库调研要点

## 结论摘要

- KEGG 不只是通路图，还组织了 KO、基因、化合物、反应、模块和 BRITE 等系统信息。
- `map` 通常表示参考通路，物种前缀通路（如原文示例中的 `mmu`）用于具体物种映射；两者用途不同。
- KO（KEGG Orthology）是把不同物种中的同源功能归并到功能组的重要索引，可用于从基因注释连接到通路。
- 原始文档中的数量是 2024-05-30 的统计快照，页面因此标记为 `uncertain`，不能直接当作当前在线规模。

## 数据对象

| 对象 | 作用 |
|------|------|
| PATHWAY | 参考和物种特异的通路图 |
| BRITE | 功能层级与分类体系 |
| MODULE | 功能模块和反应模块 |
| KO | KEGG Orthology 功能组 |
| GENES / GENOME | 物种基因与基因组信息 |
| COMPOUND | 代谢物及其他化学物质 |
| REACTION | 生化反应 |

## 编号与映射

- 通路编号通常由数字部分标识，例如糖酵解参考通路 `00010`。
- `map00010` 表示参考通路；带物种前缀的编号表示该物种对应的通路视图。
- KO 编号以 `K` 开头。将基因映射到 KO 后，可以进一步连接到 PATHWAY、MODULE 等功能层级。
- EC 编号用于酶的系统分类，形式为 `EC x.x.x.x`；它描述酶催化反应的类别与层级。

## 常见应用

1. 基因功能注释与 KO 映射。
2. 代谢通路富集和通路完整性分析。
3. 代谢模型构建所需的反应、化合物和通路关联。
4. 结合物种前缀通路查看特定物种的基因分布。

## 数据工程注意事项

- 设计入库模型时，应区分参考通路、物种通路、KO、基因和反应，避免把图展示层当成唯一事实表。
- 通路更新会改变数量和关联关系，批处理时应保存下载日期、版本或抓取批次。
- KEGG 的访问、下载和再分发条件需要按当前官方规则确认。

## 待核实

- 本页不复述历史统计作为当前数据；在线数量、更新频率、许可和下载接口都需要访问官方页面复核。

## 相关页面

- [蛋白质互作与代谢通路数据库](./interaction-and-pathway-databases.md)
- [生物信息学数据资源总览](./bioinformatics-data-landscape.md)
- [MOC](../MOC.md)
