---
title: 蛋白质结构域、结构、酶家族与非典型氨基酸
summary: 归纳 Pfam、AlphaFold、CAZy、iNClusive 与 SPSED 各自回答的问题，以及序列或结构要从哪里补齐
tags: [biological, protein, pfam, alphafold, cazy, enzyme]
status: reviewed
updated: 2026-10-24
sources:
  - path: wiki/biological/protein-domains-structures-enzymes.md
    note: 对外发布副本，原始资料路径不对外
---

# 蛋白质结构域、结构、酶家族与非典型氨基酸

## 结论摘要

- Pfam 用比对和 HMM 描述结构域与家族，现在由 InterPro 托管；它回答「有哪些域」，不替代全长序列库。
- AlphaFold DB 按 UniProt 提供预测结构。pLDDT 写在 mmCIF/PDB 的 B 因子字段里，数值越高越好，低于 50 的坐标不应按折叠来解释。
- CAZy 分类碳水化合物活性酶和结合模块，批量序列不直接给 FASTA，要用 accession 回 NCBI 取序列。
- iNClusive 收集非标准氨基酸及其来源和功能，序列文件需要额外抓取再填回表。
- SPSED 的一行是「某靶蛋白 + 某信号肽」的分泌产量，不是通用信号肽预测模型。

## Pfam

笔记中的组织单位：

- Domain：结构单元。
- Family：序列相似且功能相关的一组蛋白，是基本分类。
- Clan：相关家族的更高层集合。
- 条目类型还包括 Repeat（重复单元，不一定是完整功能域）。

用途是按家族或结构域找蛋白、看一个蛋白里有哪些域，以及这些家族出现在哪些物种。笔记记录 InterPro 约 8 周更新一次，并写明 Pfam 37.0（2024-04-24）及当时的家族规模，这些数字是快照。

## AlphaFold DB

- 覆盖 UniProt 中的大量预测结构，另有人类蛋白质组和笔记所称 47 个全球健康相关物种的蛋白质组可单独下载。
- `accession_ids.csv` 给出 UniProt 登录号、残基起止和 AlphaFold 标识（如 `AF-A8H2R3-F1`）。
- `model_v4.cif` 是带元数据的坐标；`model_v4.pdb` 用 B 因子存残基置信度。
- pLDDT：>90 适合结合位点等高精度用途；70–90 通常主干可靠；50–70 要谨慎；<50 常呈带状，不要解释成稳定三维结构。

治疗性抗体可开发性见 [抗体与免疫库](/knowledge/biological/antibody-immunology-databases/) 中的 DOTAD，不在本页重复。

## CAZy

五类酶加一类结合模块：糖苷水解酶 GH、糖基转移酶 GT、多糖裂解酶 PL、糖酯酶 CE、辅助氧化还原酶 AA，以及碳水化合物结合模块 CBM。各类下面再分 family。基因组进入 GenBank 每日发布后会陆续补入。序列要通过 accession 到 NCBI 获取；family 信息笔记认为需要爬取。

## iNClusive 与 SPSED

- iNClusive 记录非 20 种标准氨基酸：名称、结构、来源（突变、翻译后修饰、生物合成等）、对蛋白功能的影响和文献。笔记写明数据来自 600 多篇文献的人工整理，标称每六个月更新但作者未必做到。
- SPSED 从实验文献收集分泌效率。笔记中的版本含 20 个实验、1025 条记录，并按表达宿主（多种芽孢杆菌、谷氨酸棒杆菌、植物乳杆菌、解脂耶氏酵母）和靶蛋白分类。

## 待核实

- Pfam 家族数、AlphaFold「超过 2 亿」和「47 个物种」、CAZy 的 DOI 书写、SPSED 条目数都来自调研原文，使用前核对当前版本。
- CAZy 笔记里的 DOI 字符串缺少常规 `doi.org` 前缀，引用时以期刊页面为准。

## 相关

- [蛋白与基因数据总览](/knowledge/biological/bioinformatics-data-landscape/)
- 本地化项目地图
- [MOC](/knowledge/)
