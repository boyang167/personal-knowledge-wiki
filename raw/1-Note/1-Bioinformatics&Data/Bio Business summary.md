> # 生物制药研发流程术语（Business Summary）

## 目录

- [流程总览](#流程总览)
- [术语对照表](#术语对照表)
- [阶段说明](#阶段说明)
  - [分子克隆与测序](#1-分子克隆与测序)
  - [细胞操作与池（Pool）培养](#2-细胞操作与池pool培养)
  - [收获与小试纯化](#3-收获与小试纯化)
  - [细胞库、澄清与层析纯化](#4-细胞库澄清与层析纯化)
  - [制剂筛选与可开发性](#5-制剂筛选与可开发性)
  - [克隆开发、MCB 与工艺锁定](#6-克隆开发mcb-与工艺锁定)
  - [中试与 GMP 生产](#7-中试与-gmp-生产)
- [上游 vs 下游](#上游-vs-下游)

---

## 流程总览

典型生物药从分子到商业化生产，可粗分为以下链路（各公司内部命名略有差异）：

```text
分子需求 → 序列分析 / 密码子优化 → 质粒设计构建 → 引物设计/合成 → PCR / 连接 / 转化 / 菌落筛选
    → 质粒制备、HTP 测序 → 转染 → Pool 恢复 / 传代 / 补料分批 → 收获 → 小规模纯化 → 报告与讨论
    → 克隆开发 / 筛选 / 稳定性 → MCB → 上游工艺锁定 → 下游开发 / 锁定 → 制剂与 DP 工艺锁定
    → 非 GMP 中试 → GMP 生产；并行：pH/缓冲液、赋形剂与表面活性剂筛选、Developability、Tech Transfer
```

---

## 术语对照表

| 英文（常见写法） | 中文 | 备注 |
| --- | --- | --- |
| Molecule request(s) | 分子需求 | 按项目目标确定 DNA/RNA/蛋白或小分子等 |
| Sequence analysis | 序列分析 | ORF、元件、同源比对、蛋白结构域等 |
| Codon optimization | 密码子优化 | 适配宿主密码子偏好以提高表达 |
| Plasmid construction (design) | 质粒构建（设计） | 载体骨架、插入位点、启动子/标记等 |
| Primer design / arrangement / synthesis | 引物设计 / 排列 / 合成 | PCR、测序等；排列多指实验编排 |
| PCR | 聚合酶链式反应 | 变性–退火–延伸循环扩增 |
| Ligation | 连接 | 连接酶连接插入片段与载体 |
| Transformation | 转化 | 外源 DNA 导入细菌等宿主 |
| Colony screening | 菌落筛选 | 抗性、蓝白斑、菌落 PCR、酶切等 |
| HTP sequencing (NGS) | 高通量测序 | 相对 Sanger 的大规模并行测序 |
| Bacterial culture | 细菌培养 | LB 等培养基，质粒扩增常用 |
| Plasmid preparation | 质粒制备 | 碱裂解等，得较纯质粒 |
| Sequencing reporting | 测序报告 | 原始数据、Q 值、比对、变异等 |
| Transfection | 转染 | 外源核酸导入真核细胞 |
| Pool recovery | 池恢复 | 操作后让细胞群恢复至正常状态 |
| Pool passage | 池传代 | 细胞密度过高时分瓶续培 |
| Pool fed-batch | 池补料分批 | 分批补营养以延长生长、提高产量 |
| Harvest | 收获 | 自培养/发酵体系分离细胞或产物 |
| Small-scale purification | 小规模纯化 | 研发阶段柱层析、沉淀等 |
| Pool results / reporting / discussion | 池结果 / 报告 / 讨论 | 生长、表达、纯度、转染效率等 |
| Cryopreservation | 冷冻保存 | 常 −196°C 液氮；DMSO 等保护剂 |
| Cell recovery | 细胞复苏 | 快速解冻、去保护剂、恢复培养 |
| Passage / culture | 传代 / 培养 | 贴壁或悬浮；DMEM、RPMI 等 |
| Clarification | 澄清 | 离心、过滤去大颗粒与碎片 |
| Affinity chromatography | 亲和层析 | 抗原–抗体、标签蛋白等特异性捕获 |
| Depth filtration | 深度过滤 | 原文 *inter-depth filtration* 多指此项 |
| 1st / 2nd chromatography | 第一 / 第二次层析 | 如 IEX 后再 SEC 等组合 |
| UF/DF (Ultrafiltration / Diafiltration) | 超滤 / 透析（换液） | 浓缩大分子、脱盐换缓冲液 |
| Aliquot | 分装 | 样品等分便于平行实验 |
| DS freezing / thaw | 双链冷冻 / 解冻 | DS = double-stranded；或指下游冷冻 |
| Developability | 可开发性 | 技术、成本、监管等综合评估 |
| pH & buffer screening | pH 与缓冲液筛选 | 反应/产物稳定性条件 |
| Excipient & surfactant screening | 赋形剂与表面活性剂筛选 | 制剂性能与稳定性 |
| Tech transfer protocol | 技术转移协议 | 研发→生产或跨部门转移规范 |
| Molecule construction | 分子构建 | 表达盒、蛋白改造、小分子合成等 |
| Pool development | 池开发 | 转染/筛选后的细胞或分子集合 |
| Material generation | 材料生成 | 细胞、上清、DNA/蛋白等中间体 |
| Clone development / selection | 克隆开发 / 筛选 | 单克隆扩增与高产/稳定株挑选 |
| Clone stability study | 克隆稳定性研究 | 传代后表达、遗传一致性 |
| MCB creation | 主细胞库建立 | Master Cell Bank，生产细胞源头 |
| Downstream development | 下游开发 | 捕获、纯化、除病毒、制剂前处理 |
| Upstream / downstream process lock | 上 / 下游工艺锁定 | 参数与 SOP 固定，保证批间一致 |
| Drug product formulation & process lock | 制剂与 DP 工艺锁定 | 剂型、辅料、包装与生产步骤 |
| Non-GMP pilot production | 非 GMP 中试 | 工艺调试，不用于上市销售 |
| GMP production | GMP 生产 | 符合药品生产质量管理规范 |

---

## 阶段说明

以下各节每个术语只保留**一段**说明，已合并原文中重复出现的「一、二、翻译、解释」等多处内容。

### 1. 分子克隆与测序

**Molecule request** — 根据实验或项目目标明确所需核酸/蛋白等；可来自提取、合成或订购。

**Sequence analysis** — 对 DNA/RNA：ORF、启动子/增强子、比对与同源性；对蛋白：结构域与结构预测。

**Codon optimization** — 按宿主（如原核表达真核基因）替换偏性密码子，提升翻译通量。

**Plasmid construction** — 酶切载体与插入片段，连接酶连接得重组质粒；设计阶段需定骨架、调控元件与筛选标记。

**Primer design → synthesis** — 控制长度、GC、Tm、二聚体与特异性；合成由商业服务完成。

**PCR → ligation → transformation → colony screening** — 扩增目的片段 → 克隆入载体 → 导入宿主 → 抗生素/标记/PCR/酶切确认正确克隆。

**HTP sequencing (NGS)** — 大规模并行测序，用于基因组、转录组、质粒验证等；**sequencing reporting** 汇总质量与变异。

**Bacterial culture & plasmid preparation** — 扩增含质粒的菌体；碱裂解等法制备质粒用于后续转染、测序或酶切。

### 2. 细胞操作与池（Pool）培养

**Transfection** — 脂质体、电转、病毒载体等将 DNA/RNA 导入真核细胞，用于表达或功能研究。

**Pool recovery / pool passage** — 转染或应激后恢复培养；密度过高时稀释传代。**Pool fed-batch** 在培养过程中分批补料，延长指数期、提高滴度。

### 3. 收获与小试纯化

**Harvest** — 离心、过滤等自培养液获得细胞或上清产物。

**Small-scale purification** — 实验室规模 IEX、亲和、SEC、沉淀等，为放大工艺提供依据。

**Pool results / reporting / discussion** — 汇总生长曲线、滴度、纯度、转染效率；讨论偏差与下一步优化。

### 4. 细胞库、澄清与层析纯化

**Cryopreservation & cell recovery** — 含保护剂（如 DMSO）慢冻/液氮保存；使用时快速解冻、洗涤去保护剂。

**Culture & passage** — 维持细胞系；注意传代次数对表型的影响。

**Clarification** — 收获液初步去细胞碎片与颗粒，减轻后续柱压与堵膜。

**Affinity chromatography** — 利用特异性相互作用捕获目标蛋白，再洗脱。

**Depth filtration** — 多层滤材去除微粒与部分胶体，介于粗滤与超滤之间。

**1st / 2nd chromatography** — 按电荷、疏水、尺寸等分步提纯；常见 IEX + SEC 组合。

**UF/DF** — 超滤浓缩蛋白；透析或 diafiltration 换缓冲液、脱盐。

**Aliquot；DS freezing / thaw** — 样品分装；双链核酸或中间体冷冻/解冻需注意避免反复冻融降解。

### 5. 制剂筛选与可开发性

**Developability** — 评估分子与工艺是否值得进入临床与商业化（表达、稳定性、免疫原性、成本、法规路径等）。

**pH & buffer screening；excipient & surfactant screening** — 为反应或成品找到稳定 pH/缓冲体系及合适辅料与表面活性剂。

**Result (discussion)；tech transfer protocol** — 记录筛选结论；技术转移协议规定设备、物料、验证与 QC 要求。

### 6. 克隆开发、MCB 与工艺锁定

**Molecule construction；pool development；material generation** — 构建表达单元或分子库；形成可筛选的 cell/molecule pool；产出用于下游的中间材料。

**Clone development → selection → stability study** — 有限稀释或单克隆扩增；选高产、稳定、符合法规的株；长期传代验证表达与遗传稳定。

**MCB creation** — 从合格工作细胞库放大前，建立主细胞库并全面检定（纯度、身份、无外来因子等）。

**Downstream development** — 开发捕获、精纯、除病毒、浓缩与除菌过滤等步骤。

**Upstream / downstream process lock** — 在验证完成后固定培养/发酵与纯化参数，进入 routine 生产。

**Drug product formulation & process lock** — 固定剂型（如液体制剂、冻干）、辅料、灌装与包装工艺。

### 7. 中试与 GMP 生产

**Non-GMP pilot production** — 在小规模或中试车间验证放大，产品多用于内部分析与工艺改进，不上市。

**GMP production** — 在质量体系下批量生产，全程记录与放行检验，供临床或商业供应。

---

## 上游 vs 下游

| | 上游（Upstream） | 下游（Downstream） |
| --- | --- | --- |
| **范围** | 细胞/微生物培养、发酵；基因克隆、载体、转染/转化；扩增获得表达产物 | 自培养物分离纯化目标分子；除杂质、病毒；UF/DF；制剂与灌装 |
| **目标** | 足够生物量与高表达滴度；稳定、可重复的 living factory | 高纯度、符合药用标准的 DS/DP；正确剂型与包装 |
| **典型单元** | 培养基、反应器、补料策略、过程控制（pH、DO、温度） | 澄清、层析、过滤、除病毒、制剂、冻干、灯检等 |

两者通过 **process lock** 与 **tech transfer** 衔接；**MCB** 与 **clone stability** 是上游长期一致性的基础，**Developability** 与辅料筛选则贯穿 CMC 与制剂开发。
