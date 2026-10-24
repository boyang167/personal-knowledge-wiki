<h1 align="center">Cazy — 碳水化合物活性酶数据库</h1>

[CAZy主页](http://www.cazy.org/)

简介

- Published: 1998年
- 更新频率：新的基因组出现在 GenBank 的每日发布中后不久就会定期添加
- DOI: https://10.1093/nar/gkn663

CAZy 全称为 Carbohydrate-Active enZYmes Database，碳水化合物酶相关的专业数据库，内容包括能催化碳水化合物降解、修饰、以及生物合成的相关酶系家族。

### 数据库内容

#### 1. 目前涵盖的酶类及模块

其包含五个主要分类：糖苷水解酶（Glycoside Hydrolases, GHs）、糖基转移酶（GlycosylTransferases, GTs）、多糖裂解酶（Polysaccharide Lyases, PLs）、糖酯酶（Carbohydrate Esterases, CEs）和氧化还原酶（Auxiliary Activities, AAs）。

此外，还包含与碳水化合物结合结构域（Carbohydrate-Binding Modules， CBMs）。五大分类和一个结构域下，都分别建立了多个Family。

| 名称                 | Name                         | 缩写 | 作用                            |
| -------------------- | ---------------------------- | ---- | ------------------------------- |
| 糖苷水解酶类         | Glycoside Hydrolases         | GHs  | 糖苷键的水解和/或重排           |
| 糖基转移酶类         | GlycosylTransferases         | GTs  | 糖苷键的形成                    |
| 多糖裂解酶类         | Polysaccharide Lyases        | PLs  | 糖苷键的非水解裂解              |
| 糖酯酶               | Carbohydrate Esterases       | CEs  | 水解碳水化合物的酯类            |
| 辅助模块酶类         | Auxiliary Activities         | AAs  | 与 CAZymes 协同作用的氧化还原酶 |
| 非酶类纤维素结合模块 | Carbohydrate-Binding Modules | CBMs | 与碳水化合物结合                |


#### 2. 资源获取

CAZy没有直接提供 FASTA 格式的序列数据库，而仅提供了序列的 Assenssion number，需要从 NCBI 等数据库中下载序列。

- 包含 protein_id 的 cazy_data 文件:
    
    ```linux
    wget http://www.cazy.org/IMG/cazy_data/cazy_data.zip
    ``` 
- family信息：需要爬虫