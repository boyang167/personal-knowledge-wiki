---
title: 药物、靶点与获批数据库
summary: 说明 ChEMBL、DGIdb、TTD、Drugs@FDA 与 CAS 的对象差异，以及本地药物查询要拼出的字段
tags: [biological, drug, target, chembl, fda]
status: reviewed
updated: 2026-10-24
sources:
  - path: wiki/biological/drug-and-target-databases.md
    note: 对外发布副本，原始资料路径不对外
---

# 药物、靶点与获批数据库

## 结论摘要

- ChEMBL 是手工整理的类药生物活性分子库，核心是化合物–实验–靶点，而不是获批名单。
- DGIdb 汇总人类药物–基因相互作用，并给基因打「潜在可药靶」类别；它不提供特定突变的可药性。
- TTD 以治疗靶点为中心，挂疾病、通路和对应药物，并交叉引用其他库。
- Drugs@FDA 是美国上市产品与审评文件，不是在研管线，也不覆盖疫苗、细胞基因治疗和膳食补充剂等排除项。
- 本地药物查询用名称（优先有效成分名）把商品名、阶段、化学标识、序列和 ADA 等信息拼成一张结果。

## 各库边界

| 库 | 回答的问题 | 关键约定 |
|----|------------|----------|
| ChEMBL | 某分子对某靶点有什么实验活性 | 活性分结合、功能、ADME、毒性、理化、未分类。confidence score 0–9：单蛋白高分，细胞系等非分子靶点为 1，同源映射可为 8。parent 与 variant 共用 ChEMBL ID，variant 另有 variant_id。同一蛋白的 isoform 映射到同一 UniProt accession，差异写在 assay 描述 |
| DGIdb | 某人类基因和哪些药物有相互作用、是否像可药靶 | 来源包括 DrugBank、PharmGKB、ChEMBL 等。相互作用可归成抑制或激活。interaction score 依赖已知互作数量和文献量，库更新后分数会变。基因类别部分来自预测，收紧来源可降低假阳性 |
| TTD | 已知或在研治疗靶点、药物和生物标志物 | 调研快照约 4298 个靶点（多数有序列）和约 4.3 万个药物。部分品牌名缺失，可与 Drugs@FDA 对照。下载包当时缺少文献表 |
| Drugs@FDA | 1938 年以来 FDA 批准的人用药品和部分治疗性生物制品 | 含品牌药、仿制药、部分生物制品和生物类似药，以及部分 OTC。每周二更新数据文件。不含疫苗、血液制品、细胞与基因治疗、无申请号的 OTC 专论药品、膳食补充剂和未获美国上市许可的产品 |
| CAS | 化学物质的登记号 | 最多 10 位，三段：2–7 位、两位、一位校验。用来消除别名，不携带生物活性 |

## 化学标识（来自 TTD 笔记）

- PubChem SID 是各提交方的物质记录；同一结构被多方提交会有多个 SID。
- PubChem CID 是标准化成同一化学结构后的化合物号，一个 CID 可汇总多个 SID。
- SMILES 是线性结构式，同一结构可有多种写法；canonical SMILES 才尽量一一对应。
- InChI 按层描述结构，标准 InChI 与结构一一对应。InChIKey 是定长哈希，由 InChI 可算出 Key，反向必须查表。

## 本地药物查询要拼的字段

输入是药物名称：商品名、有效成分名或研发代号，笔记建议优先用有效成分名。

输出包括：商品名、研发公司、最高阶段、ATC、药物类型（笔记里用 FDA 申请类型粗分生物药/化学药）、CAS、PDB、化学信息（canonical SMILES、标准 InChI、InChIKey）、重链/轻链类型、生物药序列与 Chothia CDR、生物药描述、ADA 发生率及文献。多值字段是表，不是单行字符串。

## 待核实

- ChEMBL、DGIdb、TTD 笔记中的版本和条目数（如 DGIdb v5.0.6、TTD 2024-01-10）是入库当时的快照。
- 用申请类型 ANDA/NDA/BLA 划分化学药和生物药是查询笔记里的规则，不是法规定义的完整标准。

## 相关

- 本地化项目地图
- [文献与术语](/knowledge/biological/literature-terminology-and-patents/)
- [MOC](/knowledge/)
