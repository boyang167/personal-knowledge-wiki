<h1 align="center">INDI — 纳米抗体数据库</h1>

[INDI 主页](https://research.naturalantibody.com/nanobodies)

简介

- Published: 08 November 2021
- 更新频率：
- DOI：https://doi.org/10.1093/nar/gkab1021

纳米抗体的小尺寸赋予了多种治疗优势（稳定性、肿瘤渗透性），2018 年纳米抗体首次获得治疗批准，巩固了这种形式的临床可行性。纳米抗体的*结构化数据*和*序列信息*将使基于纳米抗体的疗法的临床开发加速，尽管纳米抗体序列和结构数据正在被加速公开，但来源的异质性和缺乏标准化阻碍了纳米抗体信息的可靠收集。

为了有效整合当前已公开的纳米抗体的庞大数据库，*Natural Antibody* 公司创建了用于免疫信息学的纳米抗体集成数据库（*Integrated Nanobody Database for Immunoinformatics，INDI*），INDI 基于专利、GenBank、NGS 以及蛋白质结构数据库四大主要序列渠道，并人工筛选科学出版物，来搜集纳米抗体序列信息，并配备强大的纳米抗体特定序列和文本搜索，可访问超过 1100 万纳米抗体序列，有助于实现基于纳米抗体形式的药物的治疗前景。

>Integrated Nanobody Database for Immunoinformatics (INDI) curates sequences and text metadata associated with heavy-chain only antibodies, alternatively known as Nanobodies, VHH, single-domain antibodies or single-chain antibodies.

### 一. 数据库内容

1. 专利纳米抗体 - Patent Nanobodies
2. GenBank纳米抗体 - GenBank Nanobodies
3. 纳米抗体结构 - Strucures of Nanobodies
4. 下一代测序纳米抗体 - NGS Nanobodies
5. 手工筛选的纳米抗体 - Manually-curated Nanobodies

<h1 align="center"></h1>

#### 1. 专利纳米抗体

以蛋白质列表的形式收集了与专利文件相关的纳米抗体。我们通过识别抗体序列，并根据序列特征、专利文件文本和分类来评估其是否包含纳米抗体。来自专利的每个纳米抗体序列 (`patent_sequence.tsv`) 都与其原始文档的元数据 (`patent_meta.tsv`) 相关联，例如专利标题、摘要等，以便通过 metadata 进行搜索，找到与特定生物实体（例如特定靶标）相关联的序列。

>Patent Nanobodies. We collect nanobodies that are associated with patent documents in the form of protein listings. We identify the antibody sequences and on the basis of sequence features, patent document text and classification assess whether it contains Nanobodies or not. Each Nanobody sequence from patent is associated with the text metadata of the document it originated from such as patent title, abstract etc. to facilitate text-based searches for sequences associated with specific biological entities (e.g. particular targets).

#### 2. GenBank纳米抗体

GenBank是生物序列存储的主要结构化来源之一。从这些数据中，通过与抗体或纳米体相似的序列特征以及元数据的文本挖掘来识别纳米抗体。每一个GenBank纳米体序列都与其 metadata 相关联，其中包括源生物体、描述和出版物等，这有助于基于文本检索与某些生物实体（例如特定目标）相关联的纳米体序列。

>GenBank Nanobodies. GenBank is one of the primary structured sources for the deposition of biological sequences. Nanobodies from this data are identified by antibody/nanobody-like sequences features combined with text mining of the metadata of deposition. Each GenBank Nanobody sequence is associated with its source deposition document which among others includes the source organism, deposition description and source publication which facilitates text-based retrieval of Nanobody sequences associated with certain biological entities (e.g. particular targets).

#### 3. 纳米抗体结构

Protein Data Bank (PDB)是生物分子三维构象数据的主要公开来源。从PDB中识别纳米抗体序列是通过抗体-纳米抗体序列特征以及与特定链和整个PDB元数据字段挖掘来实现的。

>Structures of Nanobodies. The Protein Data Bank (PDB) is the primary public source for three dimensional conformation data on biomolecules. Nanobody sequences from the PDB are identified by the virtue of antibody-nanobody sequence features and text mining of metadata fields associated with particular chains and the entire PDB documents.

#### 4. 下一代测序纳米抗体

下一代测序现在使我们能够查询抗体序列所覆盖的巨大序列变异。我们确定了那些专门从骆驼、羊驼或驼羊中进行纳米抗体的NGS的生物项目。查询和分析这些数据集, 提供了比研究有限的可用的胚系序列更丰富的关于纳米抗体序列变异的信息。

>Next-Generation Sequencing Nanobodies. Next Generation Sequencing now allows us to query the great sequence variability covered by antibody sequences. We identify bioprojects that specifically performed NGS of Nanobodies from camels, llamas or alpacas. Querying and analyzing such datasets provides richer information on the sequence variability of Nanobodies than studying limited germline sequences available.

#### 5. 手工筛选的纳米抗体

很多时候，生物序列并未存储在诸如GenBank等标准化的数据库中，而是直接出现在科学出版物及其附属资料中。目前还没有可靠的自动方法来识别这类序列。因此，这个分类包括这样的纳米抗体序列，我们通过手工策划科学出版物来将它们添加到我们的数据库中。这些纳米抗体序列与它们来源的出版物的元数据相链接，以便通过文本进行检索。

>Manually-curated sequences. Oftentimes biological sequences are not deposited in standardized repositories such as GenBank and these can instead be directly in scientific publications and their supplementary material. There currently does not exist a reliable automatic method to identify such sequences. Therefore this category encompasses such Nanobody sequences that we add to our database on the basis of manual curation of scientific publications. Nanobody sequences here are linked to the metadata of publications that they originate from to facilitate text-based retrievals.

### 二. 搜索方式

![171715](images/171715.png)

1. **可变区序列搜索**
2. **CDR3序列搜索**
3. **文本搜索**（可以是id号，标题关键字等等）

### 三. 资源获取

可直接在 [DOWNLOAD](https://research.naturalantibody.com/nbdownload) 页面下载.

共包含以下 9 个`.tsv`文件：

- ngs_sequence.tsv
- patent_sequence.tsv
- patent_meta.tsv
- abgenbank_sequence.tsv
- abgenbank_meta.tsv
- structure_sequence.tsv
- structure_meta.tsv
- manual_sequence.tsv
- manual_meta.tsv