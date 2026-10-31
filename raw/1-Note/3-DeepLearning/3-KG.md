# AI 综合笔记

知识图谱、多模态与大模型路线图等。计算机视觉见 [`8-ComputerVision.md`](./8-ComputerVision.md)。生成模型见 [`7-GenerateModel.md`](./7-GenerateModel.md)。强化学习见 [`6-ReinforcementLearning.md`](./6-ReinforcementLearning.md)。
## 目录

- [知识图谱](#知识图谱)
- [时间序列](#时间序列)
- [多模态](#多模态)
- [大模型（学习路线图）](#大模型学习路线图)
- [参考资料](#参考资料)

---

## 知识图谱

### 核心概念

| 概念 | 说明 |
| --- | --- |
| Entity | 知识库中的实体 |
| Mention | 文本中对实体的提及 |
| Entity Linking | 将 mention 链接到 KG 中的 entity |
| Mention Variation | 同一 entity 多种表述，如「唐僧 / 唐三藏 / 玄奘」 |
| Entity Ambiguity | 同一 mention 对应多个 entity，如「迈克尔·乔丹」 |

**三元组**：`<实体, 关系, 实体>`；**属性**：`<实体, 属性, 属性值>`。



<img src="../img/image-20230326101826622.png" alt="image-20230326101826622" style="zoom: 25%;" />



![image-20230326102027835](../img/image-20230326102027835-1716637414166.png)

![image-20230326102050147](../img/image-20230326102050147-1716637414167.png)

![image-20230326102240844](../img/image-20230326102240844-1716637414168.png)

![image-20230326102331070](../img/image-20230326102331070-1716637414168.png)



![image-20230326102537368](../img/image-20230326102537368-1716637414168.png)

![image-20230326102557064](../img/image-20230326102557064-1716637414168.png)

![image-20230326102618179](../img/image-20230326102618179-1716637414168.png)

![image-20230326102649495](../img/image-20230326102649495-1716637414168.png)



![image-20230326102703489](../img/image-20230326102703489-1716637414168.png)

![image-20230326102739298](../img/image-20230326102739298-1716637414168.png)

![image-20230326102804926](../img/image-20230326102804926-1716637414168.png)

### 知识表示（RDF / RDFS / OWL）

```text
知识图谱基础之 RDF、RDFS 与 OWL
    Subject 可以是IRI或者Blank NodePredicate必须是IRIObject三种都可以
RDF : Resource Description Framework 
	N-Triples
	Turtle
	
Resource Description Framework Schema: RDFS 

RDFS/OWL本质上是一些预定义词汇（vocabulary）构成的集合，用于对RDF进行类似的类定义及其属性的定义。
### 这里我们用词汇rdfs:Class定义了“人”和“地点”这两个类。
:Person rdf:type rdfs:Class.
:Place rdf:type rdfs:Class.

### rdfs当中不区分数据属性和对象属性，词汇rdf:Property定义了属性，即RDF的“边”。
:chineseName rdf:type rdf:Property;
        rdfs:domain :Person;
        rdfs:range xsd:string .

rdfs:Class 
rdfs:domian   用于表示该属性属于哪个类别。
rdfs:range 用于描述该属性的取值类型。
rdfs:subClassof
rdfs:subProperty
rdfs:type


RDFS ： top level 
模式层：
rdfs:Class rdfs:Property rdfs:Literal 
define : vocabulary  
数据层：
data :



Web Ontology Language(owl):
### owl区分数据属性和对象属性（对象属性表示实体和实体之间的关系）。词汇owl:DatatypeProperty定义了数据属性，owl:ObjectProperty定义了对象属性。
property graph:

owl: 
owl:class owl:ObjectProperty owl:DatatypeProperty rdfs: Literal 


描述属性特征的词汇：
owl : TranstiveProperty 属性具有传递性质。
owl:  SymmetricProperty 属性具有对称性。
owl: FunctionalProperty 属性取值唯一性
本体映射词汇：
ontology mapping 
owl:equivalentClass 表示某个类和另一个类是相同的
owl:equivalentProperty 表示某个属性和另一个属性是相同的
owl:sameAs 表示两个实体是同一个实体



```

![image-20230326103055046](../img/image-20230326103055046-1716637414168.png)

![image-20230326103123099](../img/image-20230326103123099-1716637414168.png)

![image-20230326103139925](../img/image-20230326103139925-1716637414168.png)

![image-20230326103211221](../img/image-20230326103211221-1716637414169.png)



![image-20230326103232319](../img/image-20230326103232319-1716637414168.png)

![image-20230326103810411](../img/image-20230326103810411.png)



![image-20230326103830310](../img/image-20230326103830310-1716637414169.png)

![image-20230326104012149](../img/image-20230326104012149-1716637414169.png)



![image-20230326104236820](../img/image-20230326104236820-1716637414169.png)



![image-20230326104315197](../img/image-20230326104315197-1716637414169.png)





![image-20230326104445916](../img/image-20230326104445916-1716637414169.png)



![image-20230326104742210](../img/image-20230326104742210-1716637414169.png)



![image-20230326104811800](../img/image-20230326104811800-1716637414169.png)

![image-20230326105003883](../img/image-20230326105003883-1716637414169.png)



![image-20230326105356487](../img/image-20230326105356487-1716637414169.png)

![image-20230326105711516](../img/image-20230326105711516.png)

![image-20230326105730279](../img/image-20230326105730279.png)

![image-20230326112042100](../img/image-20230326112042100-1716637414169.png)



![image-20230326112338886](../img/image-20230326112338886-1716637414169.png)

![image-20230326112523930](../img/image-20230326112523930-1716637414169.png)

![image-20230326112543623](../img/image-20230326112543623-1716637414169.png)

![image-20230326112601279](../img/image-20230326112601279.png)

![image-20230326112731809](../img/image-20230326112731809-1716637414170.png)

![image-20230327210723428](../img/image-20230327210723428-1716637414170.png)

![image-20230327210859902](../img/image-20230327210859902-1716637414170.png)

![image-20230327210932687](../img/image-20230327210932687-1716637414170.png)

![image-20230327211013102](../img/image-20230327211013102-1716637414170.png)



![image-20230327211055288](../img/image-20230327211055288-1716637414170.png)

![image-20230327211930587](../img/image-20230327211930587-1716637414170.png)

![image-20230327211949168](../img/image-20230327211949168-1716637414170.png)



![image-20230327212310660](../img/image-20230327212310660-1716637414170.png)

![image-20230327212433266](../img/image-20230327212433266-1716637414170.png)

![image-20230327212511927](../img/image-20230327212511927-1716637414170.png)

![image-20230327212554566](../img/image-20230327212554566-1716637414170.png)

![image-20230327212739828](../img/image-20230327212739828-1716637414170.png)

![image-20230327212938855](../img/image-20230327212938855-1716637414170.png)

![image-20230327212954010](../img/image-20230327212954010-1716637414170.png)

![image-20230327213058205](../img/image-20230327213058205-1716637414170.png)

![image-20230327213145706](../img/image-20230327213145706-1716637414170.png)

![image-20230327213233565](../img/image-20230327213233565-1716637414170.png)

![image-20230327213342075](../img/image-20230327213342075-1716637414171.png)

![image-20230327213519880](../img/image-20230327213519880-1716637414171.png)

![image-20230327213655866](../img/image-20230327213655866-1716637414171.png)

![image-20230327214106721](../img/image-20230327214106721.png)







### 实体消歧

![image-20230329200649460](../img/image-20230329200649460-1716637414171.png)

![image-20230329200725099](../img/image-20230329200725099-1716637414171.png)

![image-20230329200842233](../img/image-20230329200842233-1716637414171.png)

![image-20230329201011725](../img/image-20230329201011725-1716637414171.png)

![image-20230329201108376](../img/image-20230329201108376-1716637414171.png)



![image-20230329201120886](../img/image-20230329201120886-1716637414171.png)

![image-20230329201315823](../img/image-20230329201315823-1716637414171.png)



![image-20230329201448127](../img/image-20230329201448127-1716637414171.png)

![image-20230329201551942](../img/image-20230329201551942-1716637414171.png)

![image-20230329201702831](../img/image-20230329201702831-1716637414171.png)



### 知识存储和检索

![image-20230329202010731](../img/image-20230329202010731-1716637414171.png)



![image-20230329202206858](../img/image-20230329202206858-1716637414171.png)



![image-20230329202734595](../img/image-20230329202734595-1716637414171.png)



![image-20230329202819066](../img/image-20230329202819066-1716637414171.png)



![image-20230329203059958](../img/image-20230329203059958-1716637414171.png)



**参考**：B 站 KG 系列、 [KBQA-for-Diagnosis](https://github.com/wangle1218/KBQA-for-Diagnosis)、PointNet 相关视频（原笔记链接）。



---

## 时间序列

~~~
https://www.bilibili.com/video/BV1F441187xt?spm_id_from=333.337.search-card.all.click
https://github.com/dragen1860/TensorFlow-2.x-Tutorials

https://developer.huawei.com/consumer/cn/forum/topic/0202744487054880144?fid=0101592429757310384
~~~



---

## 多模态

MultiModal Machine Learning（MMML）：

多模态表示学习（Representation）

模态转化 Translation

对齐：  Alignment

多模态融合：  Fusion

协同学习（Co-learning）




![image-20210609104647608](../img/image-20210609104647608.png)

![image-20210609104719752](../img/image-20210609104719752.png)

![image-20210609104744097](../img/image-20210609104744097.png)

![image-20210609104807316](../img/image-20210609104807316.png)

![image-20210609104840560](../img/image-20210609104840560.png)

![image-20210609104855714](../img/image-20210609104855714.png)

![image-20210609104909805](../img/image-20210609104909805.png)

![image-20210609104927517](../img/image-20210609104927517.png)

![image-20210609104953058](../img/image-20210609104953058.png)

![image-20210609105022628](../img/image-20210609105022628.png)

---

## 大模型（学习路线图）

- 第一章 概览与前置任务

  -  tokenizer训练

     - tokenizer原理与算法:BPE，ByteBPE, wordpiece,unilm,sentence-piece

     - tokenizer训练：sentence-piece

  -  position encoding方案

     - Alibi

     - RoPE

     - [综述：利用位置编码实现长度外推 (qq.com)](https://mp.weixin.qq.com/s/h6Ug2ttJSN5W2qmAC8Id5A)![img](https://api2.mubu.com/v3/document_image/61415017-c42c-48a1-84ef-b67f44c27cd7-8142555.jpg)

  -  注意力机制与transformer架构

     - 典型的自注意力机制
       - ![img](https://api2.mubu.com/v3/document_image/dbf02412-8f54-4220-95f8-54a0d161f387-8142555.jpg)

     - 其他注意力机制
       - Mamba,H3,Hyena,RetNet,RWKV,Linear attention, Sparse attention

     - 典型的transformer架构

       - decoder-only

       - encoder-only

       - encoder-decoder

- 第二章 训练

  - 预训练

    - lm训练配置

      - 正则化方法

      - 激活函数

      - 优化器

  - SFT训练

  - 强化学习

    - Police-Based

    - Value-Based

    - Actor-Critic

  - RLHF训练

  - 其他指令对齐训练

  - 分布式并行训练技术

    - 模型并行

      - tensor parellelism

      - 序列并行

      - pipeline parellelism
        - GPipe,1F1B, interleaved 1F1B

    - 数据并行
      - DP,DDP,FSDP,ZeRO

  - MoE

  - PEFT训练

    - Adapter类

    - Prompt类

    - LoRA类

  - 上下文扩展技术

    - window attention

    - 注意力缩放

    - streaming-llm

    - RoPE改进

    - Alibi

- 第三章 推理

  - 压缩

    - 剪枝

    - 量化

      - 校准量化

        - GPTQ

        - AWQ

        - SmoothQuant

        - SpQR

      - 非校准量化

        - LLM.int8

        - ZeroQuant

  - 显存优化技术

    - pagedattention

    - quantized kv cache

    - mqa/gqa

    - flash-attention

    - flash-attention-v2

    - flash-attention-decoding

  - 调度优化技术

    - dynamic batching

    - async serving

    - continuous/interative-level batching

    - sarathi/fastgen

  - 请求优化技术

    - 网络通信优化

    - 响应模式优化

  - 采样及解码加速

    - speculative decoding

    - specinfer

    - medusa

    - blockwise parallel decoding

    - SOT-parallel decoding

  - 推理中的模型并行策略
    - TP,PP

  - 算子融合及其他优化:no padding, 高性能算子...

- 第四章 应用

  - RAG

    - RAG的基本组件

      - DocLoader

      - TextSplitter

      - 向量数据库
        - 索引：NSW,NSG,HNSW,DiskAnn,LSH,IVF

      - embedding模型

    - RAG增强训练

      - self-rag

      - Chain-of-Note

    - RAG优化

      - NL2Cypher

      - NL2SQL

      - 文本检索

      - embedding训练

      - reranker

  - Agent

    - Agent基本组件

      - Planning

      - Reflection

      - Memory

      - Tool Use

    - Agent对齐微调

      - Toolformer

      - TALM

      - Chain of Hindsight

      - Algorthm Distillation

    - Agent框架

      - ReAct

      - Relfexion

  - Prompt Engineering
    - CoT,ToT,GoT

![在这里插入图片描述](../img/fe4358f50efc4839801562b690b32cff.png)









## 参考资料

- [ML2022-Spring](https://github.com/virginiakm1988/ML2022-Spring)
- [科学空间：扩散模型等](https://kexue.fm/archives/5253)
- [CSDN 笔记](https://blog.csdn.net/weixin_42491648/article/details/132384913)
- [Code-LMs](https://github.com/VHellendoorn/Code-LMs)
