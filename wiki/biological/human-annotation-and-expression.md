---
title: 人类基因注释、GenBank 发布与蛋白质图谱
summary: 说明 MANE 代表转录本、GenBank 三类记录与双月发布，以及 HPA 按生物学问题拆开的 12 个部分
tags: [biological, genome, mane, genbank, hpa]
status: draft
updated: 2026-10-24
sources:
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/MANE_db/mane.md
    note: MANE Select、Plus Clinical 与选择流程
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/Genbank/Genbank调研.md
    note: Release 更新文件、traditional、WGS/TSA/TLS 与 genome
  - path: raw/2-StudyMaterials/1-Biological/Bioinformatics/Bioinfo_Data/HPA/调研文档.md
    note: 十二个组成和版本 13 的覆盖描述
---

# 人类基因注释、GenBank 发布与蛋白质图谱

## 结论摘要

- MANE 为人类蛋白编码基因选一条 RefSeq 与 Ensembl/GENCODE 外显子完全一致、并贴合 GRCh38 的代表转录本，两个标识可以互换。
- GenBank 不能当成单一 flatfile：传统记录、WGS/TSA/TLS 集合和 genome 组装要分开解析；发布大约每两个月一次，增量看 changed、deleted、new。
- HPA 把组织、单细胞、病理、血液、亚细胞、细胞系和结构等分成独立部分，RNA 与蛋白覆盖程度不同。

序列主库与去重模型见 [蛋白与基因数据总览](./bioinformatics-data-landscape.md)。本页只补发布单位和人类注释。

## MANE

- MANE Select：每个蛋白编码基因一条转录本，用作临床报告、浏览器默认和比较基因组的起点。由计算初选加人工复核。
- MANE Plus Clinical：在 Select 覆盖不了公共资源里致病或可能致病变异时，为该基因额外保留转录本。
- 选择时先由 NCBI 与 EMBL-EBI 各自挑 select transcript，再找剪接结构和 CDS 都相同的配对。5' 端用 CAGE 簇定常用 TSS，3' 端用 polyA-seq 簇定末端；笔记中的窗口是 50 bp，常用位点取簇内靠近端点且计数达到最大计数至少 50% 的位置。
- 笔记记录的 1.0 覆盖约 99% 的人类蛋白编码基因。文件按 release 放在 NCBI RefSeq FTP，同时提供 Ensembl 标识和 RefSeq 标识的 GTF/GFF。

## GenBank 发布

- 笔记下载的是 Release 259.0（2023-12-15）。相对上一版的变动列表：`gbchg.txt.gz`、`gbdel.txt.gz`、`gbnew.txt.gz`。
- Traditional records 是常见 flatfile，头部加序列条目；当时规模约 2.5 亿条，以 release notes 为准。
- Set-based（WGS/TSA/TLS）和 Genome 是另一套组织，解析器不能只按传统 flatfile 写。
- Accession 与 taxon_id 的细节在调研附录，入库时要保留，不能只存序列。

## Human Protein Atlas

笔记描述的 12 个部分：组织、脑、单细胞类型、组织细胞类型、病理、疾病血液、免疫细胞、血液蛋白、亚细胞、细胞系、结构（实验和预测结构、抗原位点、群体与临床变异）、相互作用。

版本 13 的说法是：99.9% 的 RNA 数据和 83% 预测人类基因的蛋白数据，图像超过 1100 万。病理部分覆盖约 20 种常见癌症的免疫组化。这些比例是该版本文案，不是永久覆盖率。

## 待核实

- Release 259 与 HPA 版本 13 之后的发布策略、文件名和覆盖率需要对照 NCBI 与 HPA 当前说明。
- MANE 笔记写了 release 1–11、13 与 track 12 的路径差异，新版本目录要以 FTP 实况为准。

## 相关

- [蛋白与基因数据总览](./bioinformatics-data-landscape.md)
- [文献、术语与专利序列](./literature-terminology-and-patents.md)
- [MOC](../MOC.md)
