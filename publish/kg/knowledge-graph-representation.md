---
title: 知识图谱中的实体链接与 RDF 表示
summary: 区分实体、提及和歧义，并记录 RDF、RDFS、OWL 在笔记里的分工
tags: [kg, rdf, owl, entity-linking]
status: reviewed
updated: 2026-10-24
sources:
  - path: wiki/kg/knowledge-graph-representation.md
    note: 对外发布副本，原始资料路径不对外
---

# 知识图谱中的实体链接与 RDF 表示

## 结论摘要

- 实体链接是把文本里的 mention 接到图谱中的实体。同一实体可以有多种说法，同一个说法也可以指向不同实体。
- 关系写成 `<实体, 关系, 实体>`，属性写成 `<实体, 属性, 属性值>`。
- RDF 是三元组数据模型。RDFS 用预定义词汇描述类和属性。OWL 进一步把数据属性和对象属性分开。

## 提及和歧义

- mention variation：一个实体有多个称呼，例如同一人物的不同名号。
- entity ambiguity：一个称呼对应多个实体，例如同名的不同人物。
- 链接要同时处理这两种情况，不能把字符串相等当成实体相同。

## RDF、RDFS、OWL

| 层 | 作用 |
|----|------|
| RDF | 资源描述框架。主语可以是 IRI 或空白节点，谓语必须是 IRI，宾语三者都可以。序列化包括 N-Triples 和 Turtle |
| RDFS | 用 `rdfs:Class`、`rdf:Property` 定义类和边。`rdfs:domain` 表示属性属于哪一类，`rdfs:range` 表示取值类型。不区分数据属性和对象属性 |
| OWL | 用 `owl:DatatypeProperty` 和 `owl:ObjectProperty` 把“属性值”和“实体到实体的关系”分开 |

RDFS 同时有模式层词汇和数据层实例。`rdfs:Class`、`rdfs:Property`、`rdfs:Literal` 放在模式层。

## 待核实

- 实体消歧和知识存储没有在本页展开。
- 笔记中的 `rdfs:domian` 拼写应按 `rdfs:domain` 理解。

## 相关

- [图表示学习](/knowledge/ml/graph-representation-learning/)
- [MOC](/knowledge/)
