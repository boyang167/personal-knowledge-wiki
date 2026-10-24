<h1 align="center">BioGRID Tables 详情</h1>

<p align="center">
    编写作者：wu_jiannan /
    编写时间：2024.05.21
</p>

### 1. 数据统计

| 表名               | 行数       |
| ------------------ | ---------- |
| t_biogrid_all_data | 2,679,882* |

*注：与原文本文件有差异，待确认

### 2. 数据入库
#### pg入库

t_biogrid_all_data：

| 字段                               | 注释                                                                                                                                                                                                                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| BioGRID Interaction ID             | 相互作用ID，唯一的标识符                                                                                                                                                                                                                                                       |
| Entrez Gene Interactor A           | Interactor A 对应的 Entrez-Gene 数据库中的标识符，如果没有，则为 "-"                                                                                                                                                                                                           |
| Entrez Gene Interactor B           | 同上                                                                                                                                                                                                                                                                           |
| BioGRID ID Interactor A            | Interactor A 对应的 BioGRID 数据库中的标识符                                                                                                                                                                                                                                   |
| BioGRID ID Interactor B            | 同上                                                                                                                                                                                                                                                                           |
| Systematic Name Interactor A       | Interactor A 的系统名称，如果没有，则为 "-"                                                                                                                                                                                                                                    |
| Systematic Name Interactor B       | 同上                                                                                                                                                                                                                                                                           |
| Official Symbol Interactor A       | Interactor A 的常见基因名/官方编码名，如果没有，则为 "-"                                                                                                                                                                                                                       |
| Official Symbol Interactor B       | 同上                                                                                                                                                                                                                                                                           |
| Synonyms Interactor A              | 别名，用 "&vert;" 分隔， 如果没有，则为 "-"                                                                                                                                                                                                                                    |
| Synonyms Interactor B              | 同上                                                                                                                                                                                                                                                                           |
| Experimental System                | <a href="BioGrid_investigation.md#experimental-evidence-name">实验证据名称</a>                                                                                                                                                                                                 |
| Experimental System Type           | 实验证据类型                                                                                                                                                                                                                                                                   |
| Author                             | 出版物的第一作者姓氏，后面也可能有附加信息，如Stephenson A (2005)                                                                                                                                                                                                              |
| Publication Source                 | 出版物来源， 格式为"SOURCE:ID"                                                                                                                                                                                                                                                 |
| Organism ID Interactor A           | Interactor A 的 NCBI Taxonomy ID                                                                                                                                                                                                                                               |
| Organism ID Interactor B           | 同上                                                                                                                                                                                                                                                                           |
| Throughput                         | 高通量、低通量或两者（以"&vert;" 分隔）                                                                                                                                                                                                                                        |
| Score                              | 原始出版物记录的正值或负值，表示P值、置信度评分、SGA评分等，如果没有，则为"-"                                                                                                                                                                                                  |
| Modification                       | 对于任何生物化学活性实验，该字段将填充相关的翻译后修饰，如果没有，则为"-"                                                                                                                                                                                                      |
| Qualifications                     | 相互作用的额外纯文本信息，用 "&vert;" 分隔，如果没有，则为"-"                                                                                                                                                                                                                  |
| Tags                               | 相互作用其他分类，用 "&vert;" 分隔，如果没有，则为"-"                                                                                                                                                                                                                          |
| Source Database                    | 提供该相互作用的数据库的名称                                                                                                                                                                                                                                                   |
| SWISS-PROT Accessions Interactor A | 一个或多个匹配的 Swiss-Prot accession，用 "&vert;" 分隔，如果没有，则为"-"                                                                                                                                                                                                     |
| SWISS-PROT Accessions Interactor B | 同上                                                                                                                                                                                                                                                                           |
| TREMBL Accessions Interactor A     | 一个或多个匹配的 TREMBL accession，用 "&vert;" 分隔，如果没有，则为"-"                                                                                                                                                                                                         |
| TREMBL Accessions Interactor B     | 同上                                                                                                                                                                                                                                                                           |
| REFSEQ Accessions Interactor A     | 一个或多个匹配的 REFSEQ accession，用 "&vert;" 分隔，如果没有，则为"-"                                                                                                                                                                                                         |
| REFSEQ Accessions Interactor B     | 同上                                                                                                                                                                                                                                                                           |
| Ontology Term IDs                  | 本体术语ID，用 "&vert;" 分隔，如果没有，则为"-"                                                                                                                                                                                                                                |
| Ontology Term Names                | 本体术语名称，用 "&vert;" 分隔，如果没有，则为"-"                                                                                                                                                                                                                              |
| Ontology Term Categories           | 本体术语类别，用 "&vert;" 分隔，如果没有，则为"-"                                                                                                                                                                                                                              |
| Ontology Term Qualifier IDs        | 如果有任何附加的限定术语与 `"Ontology Term IDs"` 中指定的术语相关联，这些限定术语 ID 将会在此列中列出，用"&vert;"分隔。单个术语可能会与多个限定术语相关联，在这种情况下，每个限定术语将用 "^" 分隔。例如：APO:0000006^APO:0000009 &vert;-&vert; APO:0000010。如果没有，则为"-" |
| Ontology Term Qualifier Names      | 本体术语限定符名称                                                                                                                                                                                                                                                             |
| Ontology Term Types                | 本体术语其他类别                                                                                                                                                                                                                                                               |
| Organism Name Interactor A         | 物种名称                                                                                                                                                                                                                                                                       |
| Organism Name Interactor B         | 同上                                                                                                                                                                                                                                                                           |

#### Nebula入库

[Network](BioGRID_investigation.md#五-network)