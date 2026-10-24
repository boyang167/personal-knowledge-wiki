---
title: NLP 表示学习与预训练模型
summary: 对比计数共现和直接预测的词向量，并记录注意力、Transformer 与 BERT 系模型在笔记中的分工
tags: [ml, nlp, transformer, bert, word-embedding]
status: reviewed
updated: 2026-10-24
sources:
  - path: wiki/ml/nlp-representation-and-pretrained-models.md
    note: 对外发布副本，原始资料路径不对外
---

# NLP 表示学习与预训练模型

## 结论摘要

- 词向量把语义放进向量：相近词的余弦相似度高，也可以作为下游任务的特征，并在训练中继续更新。
- 计数方法（LSA、LDA、PCA）训练快、统计用得充分，但主要抓住词相似度，高频计数会过度主导。直接预测（NNLM、RNN、Skip-gram、CBOW）更能服务下游任务，但依赖大语料，统计利用率低。GloVe 想把两类好处合在一起，用共现概率的比值编码含义。
- 静态词向量处理不了一词多义。ELMo 改用上下文相关的表示。
- 注意力用 query 对一组 key-value 做加权求和，用来处理变长序列。Transformer 用多头注意力让词互相作用。BERT 在此之上做双向预训练加微调。

## 从词向量到上下文

| 方法 | 要点 |
|------|------|
| 语言模型 | 用前文预测下一个词 |
| Skip-gram | 用中心词预测窗口里的周围词 |
| CBOW | 用周围词预测中心词。加速手段包括层次 softmax 和负采样 |
| word2vec 的局限 | 一个词只有一个向量，无法区分多义词和语义/句法多个侧面 |
| ELMo | 上下文相关的词表示 |
| BPE | 子词切分 |

## 注意力与 Transformer

- CNN 易并行、擅长局部依赖，长距离要堆很多层。RNN 适合变长序列，但难并行，也不显式区分长短依赖。
- 点积注意力的输出是 value 的加权和，权重来自 query 和 key。
- 多头注意力先把 Q、K、V 映射到较低维，分别做注意力，再拼接并线性变换。
- 普通 Transformer 把文本切成等长片段，会造成上下文被切断。Transformer-XL 用片段级循环缓存前面片段的隐状态，并用相对位置编码，避免各片段的绝对位置重复。

## BERT 及后续模型

BERT 用 Transformer 在长上下文里学词表示，模式是预训练再微调。两个目标：

- MLM：约 15% 的 token 被改动。其中约 80% 换成 `[MASK]`，10% 随机换成别的 token，10% 保持原样。
- NSP：判断第二个片段是不是第一个的后文，正负样本各约一半。

笔记中的训练配置包括 Adam、GELU、dropout 0.1、序列长度 512、batch 256，数据为 BookCorpus 加英文维基。这些是笔记里的数字，不是对所有 BERT 复现的规定。

同一份笔记还点名了这些变体：ALBERT（分解嵌入、跨层共享、用句子顺序损失代替话题混杂的 NSP）、RoBERTa、SpanBERT、XLNet、BART、T5、GPT。GPT 从无标注序列的单向语言模型写起。旋转位置编码用旋转表示相对位置，而不是把绝对位置向量直接加到词向量上。

## 待核实

- 部分模型只有标题，本页不补笔记里没有写的结构细节。
- BERT 的优化器和数据规模是笔记摘录，应以原始论文为准。

## 相关

- [深度学习构件](/knowledge/ml/deep-learning-building-blocks/)
- [Function calling 与 MCP](/knowledge/ml/llm-function-calling-and-mcp/)
- [MOC](/knowledge/)
