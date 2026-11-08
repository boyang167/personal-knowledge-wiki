# 蛋白纯化实验笔记（PS / 下游实操）
## 目录

- [术语速查](#术语速查)
- [浓缩与换液](#浓缩与换液)
- [内毒素与柱层析总览](#内毒素与柱层析总览)
- [SDS-PAGE 跑胶](#sds-page-跑胶)
- [AKTA 亲和层析通用流程](#akta-亲和层析通用流程)
- [填料与缓冲液配方](#填料与缓冲液配方)
- [QC 与缓冲液体系](#qc-与缓冲液体系)
- [试剂与抗体形式](#试剂与抗体形式)
- [业务平台与 LDMS 角色](#业务平台与-ldms-角色)
- [其他链接与资源](#其他链接与资源)

---

## 术语速查

| 缩写 | 含义 |
|------|------|
| **kDa** | 千道尔顿；蛋白分子量常用单位（原子量按原子个数求和） |
| **MWCO** | Molecular Weight Cut Off，超滤膜**截留分子量** |
| **MW** | 分子量 |
| **pI** | 等电点 |
| **EC** | 消光系数（NanoDrop 280 相关） |
| **conc** | 浓度，常用 mg/ml |
| **vol** | 体积，ml |
| **step yield** | 步骤回收率 |
| **gly / cly** | 糖基化 |
| **Endotoxin level** | 内毒素，EU/mg |
| **FT** | flow through，流穿 |
| **loading** | 上样（上清 / 发酵液） |
| **elution** | 洗脱 |
| **FC / FV / Fab** | 恒定区 / 可变区 / 含抗原结合片段（笔记中「Fab：抗原区」按实验语境保留） |

---

## 浓缩与换液

### 超滤浓缩管（实验室小规模）

**作用**：浓缩蛋白体积、**更换缓冲液**（透析式洗脱）。

**材料**：待浓缩蛋白液、浓缩管、缓冲液、离心机。

| 步骤 | 要点 |
|------|------|
| 选型 | 截留分子量为目标蛋白 MW 的约 **1/2**（如 10 ml/30 kDa、15 ml/30 kDa、50 ml/30 kDa 等规格） |
| 润湿膜 | 缓冲液或无菌水，离心 2 min，**3000–4000 rpm** |
| 浓缩 | 加样，离心约 10 min；**轻吹打**避免局部过浓 |
| 换液 | 加等体积缓冲液，重复浓缩；循环至目标浓度 |
| 收样 | 取出浓缩液，缓冲液冲洗膜；**废液测蛋白含量**算废弃率 |

**注意**：离心中观察是否**沉淀堵膜**；若沉淀需追溯原因（pH、盐、温度、浓度）。

### UFDF（膜包，中试 / 生产尺度）

- 膜包保存：浸泡在 **0.1 M NaOH** 中。
- 典型流程：
  1. **0.5 M NaOH** 清洗、消毒膜包 **0.5–1 h**。
  2. 完整性测试、水通量测试。
  3. 平衡液平衡。
  4. 进口 / 回流管置于蛋白池，穿透端接废液；先浓缩至目标浓度，开启补液端，**换液 ≥6 倍体积**；穿透端 pH、电导与 **Formulation buffer** 一致即停。
  5. 样品泵回蛋白容器；**100–150 ml** Formulation buffer 冲洗膜包提高回收。
  6. **500 ml–1 L** Formulation buffer 及时冲洗，**防止膜包干涸**。

---

## 内毒素与柱层析总览

### 内毒素（凝胶法背景）

内毒素为革兰氏阴性菌细胞壁**脂多糖**，须菌体破裂或人工破菌后才释放。

### 柱层析原理

将混合物分成多份小体积，使目标蛋白在部分流分中**相对浓缩**。

| 类型 | 英文 |
|------|------|
| 亲和层析 | Affinity (AC) |
| 离子交换 | IEX |
| 疏水层析 | HIC |
| 体积排阻 | SEC |

表达质粒可在 **N 端 / C 端**（少数在已知柔性环）加**亲和标签**便于纯化。

**缓冲液参考**：[Labome 蛋白纯化方法](http://www.labome.cn/method/Protein-Purification.html)

**亲和层析概念**：配基共价固定于载体，利用生物大分子与配基的**可逆、结构识别**结合。[亲和层析简介（尊宝生物）](http://www.zoonbio.com/protein/protein-purification-affinity.html)

---

## SDS-PAGE 跑胶

### 目的与上样量

- 上样量约 **2–3 μg**。
- 体积估算：`2 / c(待测样浓度) = v`（μl）。

### 还原（R）与非还原（NR）

| 试剂 | 作用 |
|------|------|
| **IAM**（碘乙酰胺）2 μl | NR：**保护剂**，烷基化防再氧化 |
| **DTT** 2 μl，**95 °C 5 min** | R：**还原剂**，打开二硫键 → 重链 / 轻链分开 |
| **Loading** 5 μl × 4 | 上样 |
| **Marker** 5 μl | 分子量标准 |

### 电泳条件（实验室记录）

- Running buffer：**400 ml** = 380 ml 水 + 20 ml 浓缩液。
- **180 V，400 mA，40 min**（笔录用 180 U / 400 A 表述，实操以仪器面板为准）。
- 胶：撕下封条、拔梳子；跑完后**染色、拍照、存档**。
- 样品总体积约 **16 μl**（water + sample 约 10 μl 体系等，按 SOP 微调）。

**注意上样量**与 NR/R 处理一致；AKTA 等可粗估样品浓度。

---

## AKTA 亲和层析通用流程

### 柱 / 仪器消毒（笔记）

| 对象 | 条件 |
|------|------|
| 柱子 | **0.5 M NaOH** 约 30 min |
| 仪器与管路 | **1 M NaOH** 约 30 min |

### 标准步骤（Basic steps）

```text
1. Choose volume（选柱体积与填料载量）
2. Rinse
3. Sanitization
4. Equilibration（Eq，pH / 电导）
5. Wash
6. Elution
7. Rinse
8. Strip
9. Rinse
```

---

## 填料与缓冲液配方

### MabSelect Sure（MSS，Protein A）

- **原理**：Protein A 亲和，结合多数 **IgG**（人源 / 哺乳动物 IgG1–IgG4 等）；不同洗脱条件洗下 mAb；耐 **0.1–0.5 M NaOH**。
- **场景**：细胞上清纯化单抗；**Fc 融合蛋白**亦可用亲和思路。

**平衡与洗涤（ID: AC EQ）**

| Buffer | 配方 |
|--------|------|
| **A1** | 25 mM Tris-HCl，150 mM NaCl，5 mM EDTA，**pH 7.5** |
| **A2** | A1 + 0.05% (V/V) Triton X-114 + 0.05% Triton X-100，**pH 7.5**（114 控内毒素；X-100 助溶、保护蛋白） |

**洗脱与中和**

| 上样量 | Elution | 中和 |
|--------|---------|------|
| **< 2 g** | 50 mM Na-citrate，150 mM NaCl，**pH 3.0** | 1 M Arginine，400 mM Succinic acid，**pH 9.0** |
| **> 2 g** | 0.1 M HAc | 1 M Tris，**pH 9.0** |

**Strip**：**1 M HAc**（强酸，洗脱强结合杂质）。

**MSS 步骤摘要**

```text
A1 中和（电导约 16–17，pH 7.5）→ loading → A1 → A2 → A1
→ Elution（按蛋白量选配方）→ A1 → 0.5 M NaOH 5 min → A1
```

### Ni Excel（His 标签）

笔记仅列项，具体操作补 SOP。

### Protein A / G / L / A·B

| 蛋白 | 结合位点 |
|------|----------|
| **Protein A、G** | 抗体重链 **Fc** |
| **Protein L** | **Fab** 轻链可变区 |

### Poros XS（阳离子 CEX）

- **低盐上样，高盐洗脱**；载量约 **25 mg/ml**。
- **Buffer A**：20 mM NaAc-HAc，50 mM NaCl，**pH 5.5**（稀释降低电导）。
- **Buffer B**：20 mM NaAc-HAc，1 M NaCl，**pH 5.5**。
- 步骤：A 平衡 → 上样 → A → B 洗脱 → A → **0.5 M NaOH** 消毒 → A。

### Capto Q Impres（阴离子 AEX）

- 载量 **20–25 mg/ml**。
- **A**：20 mM Tris，50 mM NaCl，**pH 8.5**。
- **B**：20 mM Tris，1 M NaCl，**pH 8.5**。
- 样品用 **20 mM Tris pH 8.5** 稀释。

### Capto MMC（多模式）

- **Buffer A / B**（笔记两式相同，实操以 Cytiva 批记录为准）：  
  0.01 M MES + 0.01 M HEPES + 0.01 M TAPS + 0.01 M CHS，**pH 6.0**。

### HIC / SEC

笔记仅标题；体积排阻在「分子筛选」语境常与 **SEC**、脱盐 / 聚合体分析相关（见 QC）。

---

## QC 与缓冲液体系

### 纯化常见问题

- **聚集 / 沉淀**（浓缩、换液、pH、盐浓度、界面剪切）。

### NanoDrop

- 蛋白 **A280**；输入 **EC**（消光系数）。
- **Blank**：水 → 合上盖再测。
- 测 **3 次**取平均，剔除异常点。

### 其他分析

| 方法 | 用途 |
|------|------|
| **SEC-HPLC** | 聚合体、片段、分子量分布 |
| **MS** | 分子量、修饰确认 |
| **SDS-PAGE** | 纯度、还原 / 非还原条带 |

### 常用缓冲液类型

磷酸、**MOPS**、**HEPES**、**Tris** 等。

### 添加剂（保存与稳定）

| 类型 | 举例 | 作用 |
|------|------|------|
| 缓冲液 | Tris 等 | 稳定 pH，防变性 |
| 还原剂 | **BME、DTT、TCEP（Tris 体系）** | 防氧化 |
| 蛋白酶抑制剂 | cocktail | 防内源性蛋白酶降解 |
| 金属螯合剂 | **EDTA、EGTA** | 螯合 Mg²⁺，抑制金属蛋白酶 |
| 离子稳定剂 | 盐、多元醇等 | 增溶 |

**操作温度**：纯化多在 **4 °C** 进行。表达体系选择会影响下游纯化难度。

---

## 试剂与抗体形式

| 名词 | 说明 |
|------|------|
| **sdAb** | 单域抗体 single-domain antibody |
| **mAb** | 单克隆抗体 |
| **scFv** | 单链可变区片段 |
| **HCAb** | 重链抗体 |
| **Signal peptide** | 信号肽 |
| **免疫原性** | 制剂与开发需评估 |

**序列资源**

- [IMGT](http://www.imgt.org/) — 免疫球蛋白种系与注释。
- [IgBLAST](http://www.ncbi.nlm.nih.gov/igblast/) — NCBI 抗体序列比对。

---

## 业务平台与 LDMS 角色

### 平台与工艺路线（公司笔记）

| 平台 | 路线示例 |
|------|----------|
| **E.coli** | — |
| **Wuxian Express** | DNA prep → Expression → Purification / QC |
| **Wuxian Transient** | DNA prep → pool → 细胞表达 → Fed-batch → Purification / QC |
| 简化 | Expression → Purification / QC |

### LDMS 流程与角色（PS 收获）

- **收获**：表达 → 发酵液；**WBP 号**由客户分子号生成。
- **Function Sponsor (FS)**：建项、指派 FL、归档 / 冻结。
- **Function Leader (FL)**：配流程、节点权限（Edit / View / Witness）、审核数据、归档 / 冻结任务。
- **Common User (CU)**：按节点录入实验。
- **BU Admin**：模板、权限、报告输出等问题对接。


---

## 其他链接与资源

| 主题 | 链接 |
|------|------|
| 亲和层析 | [zoonbio](http://www.zoonbio.com/protein/protein-purification-affinity.html) |
| 博客园相关 | [yinzhengjie](https://www.cnblogs.com/yinzhengjie/p/14124623.html) |
| DeepPhase | [github.com/cheneyyu/DeepPhase](https://github.com/cheneyyu/DeepPhase) |
| 单域抗体（汉斯） | [hanspub 综述](https://image.hanspub.org/html/2-1050014_15852.htm#txtF7) |
| Rosetta 在线 | [rosie.rosettacommons.org](http://rosie.rosettacommons.org) |
| 实验室 mAb 制备与纯化进展 | 文献题录「实验室水平单克隆抗体制备方法及相应纯化策略的研究进展」 |
| 抗登革 h1A1D 构建纯化 | 课题笔记（原文标题保留） |

![工作记录附图](./image/2-Work-Record/1682477234582.png)  
*若图无法显示，请将原图置于 `Protein/image/2-Work-Record/` 下。*

---

## 附录 · 原日志索引（可选检索）

| 日期 | 主题 |
|------|------|
| 2023/2/13 | 分子筛选、纯化方法概览 |
| 2023/2/14 | 浓缩管、UFDF、内毒素、四种柱层析、标签 |
| 2023/2/15 | SDS-PAGE、亲和层析、MWCO |
| 2023/2/16–17 | 跑胶、电泳细节 |
| 2023/2/28 | Biosuite、BIKG |
| 2023/3/1 | BIKG、CKG 阅读 |
| 2023/3/7 | AC 组分 / 工艺 |
| 2023/3/8 | SDS-PAGE 详参、MSS / IEX 填料与步骤 |
