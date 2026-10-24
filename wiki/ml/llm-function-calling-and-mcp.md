---
title: Function calling 与 MCP
summary: 说明笔记里 Function calling 和 MCP 的差别，以及 Host、Client、Server 的调用顺序
tags: [ml, llm, mcp, function-calling]
status: draft
updated: 2026-10-24
sources:
  - path: raw/1-Note/3-DeepLearning/llm.md
    note: Function calling 的局限，以及 MCP 架构和 client 工作流
---

# Function calling 与 MCP

## 结论摘要

- 笔记认为只靠 Function calling 把模型和 API 绑死，Agent 开发门槛高，很多时候只能在现成平台里搭。
- MCP 是模型和外部工具、数据源之间的协议层，目标是换模型和换工具时不必各写一套对接。笔记用 USB-C 作类比。
- 架构是客户端-服务器。Host 里的 Client 与 Server 一对一连接。Server 再访问本地或远程资源。
- Client 先拿工具列表，连同用户问题和工具描述交给模型；模型决定是否调用；调用结果回到模型后再生成回复。

## 角色

| 角色 | 笔记中的定义 |
|------|----------------|
| Host | 发起请求的 LLM 应用，例如桌面助手或 IDE |
| Client | 跑在 Host 里，与一个 Server 保持连接 |
| Server | 向 Client 提供上下文、工具和 prompt |
| Local Resources | Server 可以安全读取的本机文件或数据库 |
| Remote Resources | Server 通过 API 访问的远程资源 |

## 一次调用

1. Client 从 Server 取得可用工具。
2. 把用户查询和工具描述通过 function calling 发给模型。
3. 模型决定用不用工具、用哪一个。
4. 需要工具时，Client 经 Server 执行。
5. 工具结果回到模型。
6. 模型生成自然语言回复并展示给用户。

## 待核实

- 笔记没有写协议的消息格式和版本，图示仍在 `llm.md` 引用的图片里。

## 相关

- [NLP 表示与预训练模型](./nlp-representation-and-pretrained-models.md)
- [个人学习笔记地图](./personal-notes-map.md)
- [MOC](../MOC.md)
