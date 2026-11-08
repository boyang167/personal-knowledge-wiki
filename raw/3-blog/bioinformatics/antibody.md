---
title: 抗体与重组蛋白：基础笔记与资源索引
description: 抗体结构、等电点与亲和力要点，重组表达质控清单，以及学习资料、专利爬取与知识图谱链接汇总。
category: 生物信息
date: 2026-11-08
readTime: 8 分钟
icon: 🧬
featured: false
draft: true
---

> 个人学习索引：原始碎片笔记已按主题归并。深度学习抗体综述另见本站 [deep-learning-antibodies-review.md](./deep-learning-antibodies-review.md)。

## 1. 入门路径

| 资源 | 链接 |
|------|------|
| 生信零基础（曾新美） | [biotrainee 生信基础](http://www.biotrainee.com/jmzeng/book/basic/) |

---

## 2. 抗体结构基础

| 符号 | 含义 |
|------|------|
| **H** | 重链（Heavy chain） |
| **L** | 轻链（Light chain） |
| **V** | 可变区（Variable region） |
| **C** | 恒定区（Constant region） |

- 哺乳动物体内抗体 **5 种同种型**：**IgG、IgM、IgA、IgD、IgE**。
- **抗体药物**常通过 **Fab** 段的 **CDR**（互补决定区）识别、结合抗原。

### 2.1 延伸阅读（结构与功能）

| 主题 | 链接 |
|------|------|
| Cell Signaling 抗体入门 | [Antibody Essentials Part 1](https://blog.cellsignal.cn/antibody-essentials-part-1-antibody-basics) |
| NCBI Bookshelf | [Immunobiology — Antibodies](https://www.ncbi.nlm.nih.gov/books/NBK26848/) |
| 英国免疫学会 · 抗体速览 | [Bitesized Immunology: Antibodies](https://www.immunology.org/public-information/bitesized-immunology/antibodies) |
| BU · Antibodies 101 | [Antibodies 101](https://www.bu.edu/research/articles/antibodies-101/) |
| 制备与使用（赛默飞中文） | [如何制备和使用抗体](https://www.thermofisher.com/cn/zh/home/life-science/antibodies/antibodies-learning-center/antibodies-resource-library/antibodies-news/how-to-make-and-use-antibodies.html) |
| 疫苗与抗体（Nature 新闻） | [Nature 相关报道](https://www.nature.com/articles/d41586-020-03109-7) |
| AI + 抗体深度学习综述笔记 | [华为云社区](https://bbs.huaweicloud.com/blogs/339190) → 本站 [综述导读](./deep-learning-antibodies-review.md) |

---

## 3. 蛋白化学：等电点（pI）

**等电点（isoelectric point, pI）**：在给定条件下蛋白质**净电荷为零**时的 pH。此时正负电荷平衡，蛋白整体不带电。

- pI 由序列中各氨基酸的 **pKa** 与排列决定。
- 在 pI 附近：溶解度、电泳行为、偶联与制剂稳定性等都会明显变化。
- 实验与计算：常用各残基 pKa 估算 pI；用于**分离、纯化、表征**（离子交换、pI 沉淀等）。

---

## 4. 抗体亲和力

**亲和力**：抗原**结合位点（paratope）**与**表位（epitope）**之间互作强度。

- **结合常数 $K_a$**：平衡时复合物量；也可直观理解为结合快慢与解离难易。
- **高 $K_a$（高亲和）**：更短时间结合更多抗原，复合物更稳定。
- **低 $K_a$（低亲和）**：结合弱、易解离。

（药物与检测场景里也常讨论 **$K_d$**；$K_d = 1/K_a$，单位与实验测定方法需与文献一致。）

---

## 5. 重组蛋白表达：方案与质控

### 5.1 确定待表达方案（检查清单）

```text
蛋白分析 → 载体构建 → 表达与纯化 → 验证与质控
```

| 阶段 | 关注点 |
|------|--------|
| **蛋白分析（in silico）** | 疏水性、信号肽、免疫原性 |
| **载体构建** | 密码子优化、标签选择、表达载体选型 |
| **表达** | 表达条件、细胞系 / 宿主 |
| **纯化与定量** | 收率、纯度、浓度 |
| **验证** | 大小符合预期（SDS-PAGE / WB）；**具备预期活性** |

### 5.2 纯化参考

- 科学网博文：[蛋白纯化相关笔记](https://blog.sciencenet.cn/blog-3506747-1351379.html)

---

## 6. 知识图谱（概念）

- 达观数据：[知识图谱简介](https://www.datagrand.com/blog/knowledge-map.html)（与抗体业务无直接耦合，作 NLP/知识工程背景参考。）

---

## 7. 专利数据爬取（GitHub 工具索引）

爬取与使用专利数据须遵守各站点 **ToS、版权与合规**要求；以下仅作技术调研链接汇总。

| 项目 | 语言 / 特点 | 仓库 |
|------|-------------|------|
| **Patent2Net** | 欧盟资助；EP、USPTO、WIPO 等 | [github.com/Patent2Net](https://github.com/Patent2Net) |
| **patentcrawler** | Python；Google Patents、USPTO、EP、WIPO | [PatentSight/patentcrawler](https://github.com/PatentSight/patentcrawler) |
| **PatZilla** | Java；爬取 + 分析可视化 | [PatZilla/PatZilla](https://github.com/PatZilla/PatZilla) · [ip-tools/patzilla](https://github.com/ip-tools/patzilla) |
| **patentparser** | Python；解析为结构化可读格式 | [QuicksandTeam/patentparser](https://github.com/QuicksandTeam/patentparser) |
| **USPTO-PatFT-Web-Crawler** | USPTO PatFT | [mattwang44/USPTO-PatFT-Web-Crawler](https://github.com/mattwang44/USPTO-PatFT-Web-Crawler) |
| **Google-Patents-Scraper** | Google Patents | [wenyalintw/Google-Patents-Scraper](https://github.com/wenyalintw/Google-Patents-Scraper) |
| **patent-crawler** | 通用爬虫示例 | [anvaari/patent-crawler](https://github.com/anvaari/patent-crawler) |
