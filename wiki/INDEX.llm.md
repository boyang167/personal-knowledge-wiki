# Wiki LLM Index

自动生成，请勿手改。运行 `python scripts/build_llm_index.py` 更新。

**Generated:** 2026-10-24 11:17 UTC

Agent 用法：先读本表定位路径，再打开对应 markdown 全文。

| path | title | status | summary | tags |
|------|-------|--------|---------|------|
| big-data/data-platform-architecture.md | 数据平台架构演进（Lambda / Kappa / 湖仓一体） | draft | 对比 Lambda、Kappa 与湖仓一体架构的短板及 Table/列式/序列化存储格式选型要点 | big-data, lakehouse, lambda, kappa, architecture |
| big-data/flink-stream-processing.md | Apache Flink 流处理核心概念与作业模型 | draft | 梳理 Flink 的批流统一、状态计算、时间语义、窗口、Checkpoint、算子链与部署模式，作为学习和设计实时作业的速查页 | big-data, flink, stream-processing, state, checkpoint |
| biological/antibody-immunology-databases.md | 抗体、纳米抗体与免疫表位数据库 | draft | 对比 IMGT、SAbDab、Thera-SAbDab、INDI、ADCdb、IEDB 与 DOTAD 的对象和获取边界，供抗体设计与免疫原性查询选型 | biological, antibody, immunology, nanobody, adc |
| biological/bioinformatics-data-landscape.md | 生物信息学数据资源总览与蛋白数据整合线索 | draft | 按数据类型和使用场景整理 GenBank、UniParc、JGI、MGnify 等资源，辅助设计可持续更新的蛋白与基因数据库 | biological, bioinformatics, protein, genome, database |
| biological/bioinformatics-local-data-project.md | 生物药公开数据本地化项目地图 | draft | 按用途归纳 Bioinfo_Data 要本地化的公开库，并指向各类调研页；统计数字与入库进度以 raw 快照为准 | biological, bioinformatics, data-platform, catalog |
| biological/cmc-project-roadmap.md | 抗体药物 CMC 项目阶段与 IND 活动路线 | draft | 按项目启动、细胞系与工艺开发、GMP 生产、稳定性和申报收尾整理原始 CMC 笔记中的阶段结构 | biological, cmc, antibody, drug-development, ind |
| biological/drug-and-target-databases.md | 药物、靶点与获批数据库 | draft | 说明 ChEMBL、DGIdb、TTD、Drugs@FDA 与 CAS 的对象差异，以及本地药物查询要拼出的字段 | biological, drug, target, chembl, fda |
| biological/human-annotation-and-expression.md | 人类基因注释、GenBank 发布与蛋白质图谱 | draft | 说明 MANE 代表转录本、GenBank 三类记录与双月发布，以及 HPA 按生物学问题拆开的 12 个部分 | biological, genome, mane, genbank, hpa |
| biological/interaction-and-pathway-databases.md | 蛋白质互作与代谢通路数据库 | draft | 对比 STRING、BioGRID、Reactome、MetaCyc 与 KEGG 的证据类型，并记录代谢网络整合时要准备的四份源表 | biological, pathway, ppi, string, reactome, metacyc |
| biological/kegg-pathway-database.md | KEGG 通路数据库调研要点 | uncertain | 说明 KEGG 的 PATHWAY、KO、GENES、COMPOUND 等数据组织方式、通路编号和常见应用边界 | biological, bioinformatics, kegg, pathway, genomics |
| biological/literature-terminology-and-patents.md | 文献、医学术语与专利序列 | draft | 区分 PubMed 引文、PMC 全文、UMLS 概念标识，以及 EMBL 专利核酸和专利蛋白序列的入库取舍 | biological, pubmed, umls, patent, literature |
| biological/protein-domains-structures-enzymes.md | 蛋白质结构域、结构、酶家族与非典型氨基酸 | draft | 归纳 Pfam、AlphaFold、CAZy、iNClusive 与 SPSED 各自回答的问题，以及序列或结构要从哪里补齐 | biological, protein, pfam, alphafold, cazy, enzyme |
| database/mongodb-source.md | MongoDB 基础资料索引 | draft | 数据库目录目前只有一份 MongoDB 基础 PDF，尚未从正文提炼 | database, mongodb |
| infrastructure/container-platform-sources.md | 容器、Kubernetes 与持续集成资料索引 | draft | 列出基础设施目录中的 Docker、Kubernetes 和 Jenkins PDF，供按需打开，尚未从正文提炼 | infrastructure, docker, kubernetes, jenkins |
| kg/knowledge-graph-representation.md | 知识图谱中的实体链接与 RDF 表示 | draft | 区分实体、提及和歧义，并记录 RDF、RDFS、OWL 在笔记里的分工 | kg, rdf, owl, entity-linking |
| kg/knowledge-graph-source.md | 知识图谱资料索引 | draft | 知识图谱目录目前只有第 1 章概述 PDF，尚未从正文提炼 | kg, knowledge-graph |
| ml/computer-vision-models.md | 视觉模型笔记索引 | draft | 按笔记标题列出 CNN、经典视觉模型和检测模型，并保留 AlexNet 与文本卷积的几条原文要点 | ml, vision, cnn, transformer |
| ml/deep-learning-building-blocks.md | 深度学习网络构件 | draft | 整理全连接层、激活函数和两类优化器的选用边界，作为网络配置备忘 | ml, deep-learning, activation, optimizer |
| ml/deep-learning-source-index.md | 深度学习与推荐系统资料索引 | draft | 按文件名列出推荐系统课件章节和本地论文 PDF，正文仍在 raw，尚未逐篇提炼 | ml, deep-learning, recommendation, papers |
| ml/generative-models.md | 自编码器、VAE、GAN 与扩散模型 | draft | 按笔记区分重构式自编码器、变分自编码器和对抗训练，并记录扩散过程与 FID 的用途 | ml, generative, vae, gan, diffusion |
| ml/graph-representation-learning.md | 图表示学习方法索引 | draft | 按个人笔记的小节顺序，把图嵌入、图神经网络和动态图方法列成索引 | ml, graph, gnn, embedding |
| ml/llm-function-calling-and-mcp.md | Function calling 与 MCP | draft | 说明笔记里 Function calling 和 MCP 的差别，以及 Host、Client、Server 的调用顺序 | ml, llm, mcp, function-calling |
| ml/machine-learning-map.md | 机器学习项目流程与算法地图 | draft | 按个人笔记整理监督学习、无监督学习、偏差方差和类别不平衡的选型提纲 | ml, supervised, unsupervised, bias-variance |
| ml/mcmc-sampling.md | MCMC、M-H 与 Gibbs 采样 | draft | 记录马尔可夫链平稳分布、M-H 采样的两个缺点，以及 Gibbs 采样适用的条件 | ml, mcmc, gibbs, sampling |
| ml/nlp-representation-and-pretrained-models.md | NLP 表示学习与预训练模型 | draft | 对比计数共现和直接预测的词向量，并记录注意力、Transformer 与 BERT 系模型在笔记中的分工 | ml, nlp, transformer, bert, word-embedding |
| ml/personal-notes-map.md | 个人学习笔记地图 | draft | 说明 raw/1-Note 里数学、机器学习、深度学习和 LLM 笔记各自覆盖什么，并链到已提炼的 wiki 页 | ml, notes, map |
| ml/pytorch-reinforcement-learning-notes.md | PyTorch 强化学习示例目录 | draft | 按本地教程仓库的章节顺序整理从 Q-learning 到 Actor-Critic 的算法台阶，便于按目录回读代码 | ml, reinforcement-learning, pytorch, dqn |
| ml/reinforcement-learning-concepts.md | 强化学习的基本划分 | draft | 用状态、动作、策略和奖赏整理笔记中的 Model-free/Model-based、价值/策略、在线/离线划分 | ml, reinforcement-learning, q-learning, policy |
| opensource/ants-go-worker-pool.md | ants Go 协程池使用与运行模型 | draft | 提炼 ants 协程池的基本使用、容量管理、任务提交和生命周期操作，便于阅读源码或快速接入 | opensource, golang, goroutine, worker-pool, ants |
| programming/java-and-spring-sources.md | Java 与 Spring 资料索引 | draft | 编程语言目录只有 Java 与 Spring 两份 PDF，尚未从正文提炼 | programming, java, spring |
| tech/tech-talk-catalog.md | 技术分享题目索引 | draft | 把 raw 中技术分享 README 的题目收成主题索引，具体提纲仍回 raw 阅读 | tech, talks, distributed-systems, golang |

**Total pages:** 31
