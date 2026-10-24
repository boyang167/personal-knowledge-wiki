---
title: 文献、医学术语与专利序列
summary: 区分 PubMed 引文、PMC 全文、UMLS 概念标识，以及 EMBL 专利核酸和专利蛋白序列的入库取舍
tags: [biological, pubmed, umls, patent, literature]
status: reviewed
updated: 2026-10-24
sources:
  - path: wiki/biological/literature-terminology-and-patents.md
    note: 对外发布副本，原始资料路径不对外
---

# 文献、医学术语与专利序列

## 结论摘要

- PubMed 主要是引文和摘要。全文在 PMC 或出版商，Bookshelf 是图书和报告全文，三者不要混成一个「文献全文库」。
- UMLS 按概念而不是按字符串合并术语。稳定使用的是 CUI；大小写和标点变化会变成不同 SUI。
- 专利序列里，核酸部分笔记认为已包含在 GenBank PAT 且更新停在 2020 年，因此当时不单独下载；蛋白专利序列来自 EPO、JPO、KIPO、USPTO，当时已入库。

## PubMed

- 覆盖生物医学、健康、生命科学及相关行为、化学和生物工程文献。笔记中的规模是超过 3700 万条引文。
- MEDLINE 是最大部分，用 MeSH 索引，并带资助、遗传和化学等元数据。
- PMC 是经过挑选或按资助政策存档的全文。PubMed 记录里出现全文链接，不表示 PubMed 自己保存了全文。
- 本地更新模式是 baseline 加每日 updatefiles。解析以 NLM 的 PubMed XML DTD 为准。一条记录里常见的重复字段包括 MeSH、出版类型、化学物质、参考文献和语种。

## UMLS

三个部分：

- Metathesaurus：把多个来源词表里的同一概念连起来，保留层级、定义和关系。笔记中的 2024AA 约有 189 个来源，包括 CPT、ICD-10-CM、LOINC、MeSH、RxNorm、SNOMED CT。
- Semantic Network：语义类型及类型之间的关系。每个 Metathesaurus 概念至少有一个语义类型。
- SPECIALIST Lexicon：英语生物医学词汇和词形工具，用来生成标准化词和索引。

标识从细到粗：

| 标识 | 含义 |
|------|------|
| AUI | 某个来源词表里某次出现的原子字符串，只属于一个 CUI |
| SUI | 独特字符串。大小写、标点和字符集不同则 SUI 不同；同一字符串多义时一个 SUI 可对多个 CUI |
| LUI | 英语字符串的词形归并。一个 LUI 可对多个 CUI，一个 SUI/AUI 只对一个 LUI |
| CUI | 概念。废弃的 CUI 不会重新启用 |

关系记在 CUI 和 AUI 层，用 REL 表示宽窄等，约四分之一还有更细的 RELA（如 is_a）。词表没有穷尽所有可能关系。

## 专利序列

- 专利核酸：`ftp.ebi.ac.uk/pub/databases/embl/patent/`。笔记结论是内容已在 GenBank PAT，且当时最近更新为 2020 年，故不重复下载。
- 专利蛋白：`ftp.ebi.ac.uk/pub/databases/fastafiles/patent/`，覆盖欧、日、韩、美专利局。`.dat.gz` 为 EMBL 格式，其中也混有部分核酸。笔记未找到官方更新频率，并记录当时已全部入库。

## 待核实

- PubMed 3700 万和 UMLS 2024AA 的 189 个词表是笔记快照。
- 专利核酸「已含于 GenBank 且 2020 年后未更新」是当时的判断，重新入库前要再看 FTP 时间戳。

## 相关

- [人类基因注释与 GenBank](/knowledge/biological/human-annotation-and-expression/)
- [药物与靶点](/knowledge/biological/drug-and-target-databases/)
- [MOC](/knowledge/)
