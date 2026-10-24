---
title: 知识图谱中的实体链接与 RDF 表示
summary: 区分实体、提及和歧义，并记录 RDF、RDFS、OWL 在笔记里的分工
tags: [kg, rdf, owl, entity-linking]
status: draft
updated: 2026-10-24
sources:
  - path: raw/1-Note/3-DeepLearning/3-AI.md
    note: KG 开篇的实体链接，以及 RDF、RDFS、OWL 小节
---

# 知识图谱中的实体链接与 RDF 表示

## 结论摘要

- 实体链接是把文本里的 mention 接到图谱中的实体。同一实体可以有多种说法，同一个说法也可以指向不同实体。
- 笔记用三元组表示关系 `<实体, 关系, 实体>`，用 `<实体, 属性, 属性值>` 表示属性。
- RDF 是三元组数据模型。RDFS 用预定义词汇描述类和属性。OWL 进一步把数据属性和对象属性分开。

## 提及和歧义

- mention variation：一个实体有多个称呼。笔记的例子是同一人物的不同名号。
- entity ambiguity：一个称呼对应多个实体。笔记的例子是同名的不同人物。
- 链接要同时处理这两种情况，不能把字符串相等当成实体相同。

## RDF、RDFS、OWL

| 层 | 笔记中的作用 |
|----|----------------|
| RDF | 资源描述框架。主语可以是 IRI 或空白节点，谓语必须是 IRI，宾语三者都可以。序列化包括 N-Triples 和 Turtle |
| RDFS | 用 `rdfs:Class`、`rdf:Property` 定义类和边。`rdfs:domain` 表示属性属于哪一类，`rdfs:range` 表示取值类型。不区分数据属性和对象属性 |
| OWL | 用 `owl:DatatypeProperty` 和 `owl:ObjectProperty` 把“属性值”和“实体到实体的关系”分开 |

RDFS 同时有模式层词汇和数据层实例。笔记把 `rdfs:Class`、`rdfs:Property`、`rdfs:Literal` 放在模式层。

## 待核实

- `3-AI.md` 后半还有实体消歧和知识存储，本页没有展开那些小节里的图。
- 笔记中的 `rdfs:domian` 拼写应按 `rdfs:domain` 理解。

## 相关

- [图表示学习](../ml/graph-representation-learning.md)
- [知识图谱资料索引](./knowledge-graph-source.md)
- [MOC](../MOC.md)
