---
title: 抗体、纳米抗体与免疫表位数据库
summary: 对比 IMGT、SAbDab、Thera-SAbDab、INDI、ADCdb、IEDB 与 DOTAD 的对象和获取边界，供抗体设计与免疫原性查询选型
tags: [biological, antibody, immunology, nanobody, adc]
status: reviewed
updated: 2026-10-24
sources:
  - path: wiki/biological/antibody-immunology-databases.md
    note: 对外发布副本，原始资料路径不对外
---

# 抗体、纳米抗体与免疫表位数据库

## 结论摘要

- 序列参考、实验结构、治疗性抗体、纳米抗体、ADC 和免疫表位是不同对象，不能用一个库互相替代。
- IMGT 用 IMGT-ONTOLOGY 统一免疫遗传学命名；抗体注释优先用 GENE-DB 的参考序列，结构用 2D/3Dstructure-DB。
- SAbDab 收 PDB 中的抗体结构并做重轻链配对；Thera-SAbDab 在此之上对齐 WHO 治疗性抗体和纳米抗体，并找可变区相似结构。
- INDI 把专利、GenBank、PDB、NGS 和手工筛选的纳米抗体（VHH / 单域抗体）放到同一检索入口。
- IEDB 按实验类型拆成 MHC 洗脱配体、MHC 结合、T 细胞和 B 细胞，文献通过 reference 关联。

## 选型

| 库 | 核心对象 | 使用时注意 |
|----|----------|------------|
| IMGT | IG/TR 序列、基因、结构、单抗 | LIGM-DB、GENE-DB 可下 FASTA/flat-file；PRIMER-DB 与部分结构需要额外抓取。CLL-DB 需注册。MHC 数据在 IPD |
| SAbDab | PDB 抗体结构与序列 | 提供 Chothia 与 IMGT 编号；调研记录为每周更新，批量文件需在搜索页手工下载 |
| Thera-SAbDab | 治疗性抗体 / 纳米抗体及其近似结构 | 数据来自 SAbDab，按可变区序列找相似或相同结构 |
| INDI | 纳米抗体序列与文本元数据 | 五渠道：专利、GenBank、结构、NGS、手工筛选。专利序列要连同专利题录，否则无法按靶点检索 |
| ADCdb | 抗体药物偶联物 | 拆成 ADC、抗体、payload、linker、antigen 及活性/适应症。调研时网页批量下载失效，文件来自作者 |
| IEDB | 免疫表位 | 洗脱配体含抗原肽–MHC–疾病–宿主；结合实验信息更少；部分 T/B 数据带复合物结构 |
| DOTAD | 治疗性抗体可开发性 | 序列、临床、治疗属性与文献中的实验指标，含实测和部分预测 |
| Tabs | 治疗性抗体商业库 | 同一分子在临床前、临床和上市阶段名称会变，记录会汇总别名；无法证明是同一分子时拆成两条并加注释。wiki 不记录账号 |

IMGT 当时判断需要的子集是：带氨基酸序列的 GENE-DB、MHC、PRIMER-DB，以及 2D/3D 结构库。GENE-DB 与 MHC 走下载页，引物和结构需要爬取。

## 待核实

- 调研里的条目数（如 IMGT 基因数、ADCdb 的 6572 条、INDI 的千万级序列）都是写作时的快照。
- SAbDab 调研中的「最后更新时间」和下载是否仍需手工操作，以官网为准。
- Tabs 无公开文献可核对其覆盖范围，商业统计不要外推成学术库规模。

## 相关

- 本地化项目地图
- [MOC](/knowledge/)
