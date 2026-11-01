> 抗体 **Alemtuzumab** 计算机（in silico）可开发性评估提纲。与 CMC 工艺笔记 [protein.md](protein.md) 互补；术语见 [Bio Business summary.md](../Bio%20Business%20summary.md)。  
> 原文档名保留 `molecule_anlysis`（analysis 拼写）；若后续补图，统一放 `../../img/`。

# Alemtuzumab — In Silico 评估

## 目录

- [Sequence liability（序列风险位点）](#sequence-liability序列风险位点)
- [CDR hotspots](#cdr-hotspots)
- [Free cysteine（游离半胱氨酸）](#free-cysteine游离半胱氨酸)
- [Post-translational modification（PTM）](#post-translational-modificationptm)
- [Structure diagram](#structure-diagram)
- [Molecular properties](#molecular-properties)
- [Sequence validation](#sequence-validation)
- [Disulfide bond](#disulfide-bond)
- [Fc mutation](#fc-mutation)
- [Aggregation risk](#aggregation-risk)
- [Amino acid usage frequency](#amino-acid-usage-frequency)
- [Immunogenicity & humanization](#immunogenicity--humanization)

| 图例（序列图着色） | 含义 |
| --- | --- |
| 蓝色字体 | 氧化（Met / Trp 等） |
| 红色字体 | 异构化（Asp 等） |
| 绿色字体 | 脱酰胺（Asn） |

---

## Sequence liability（序列风险位点）

序列图展示 **可变区 / 恒定区** 注释及 **liability 位点**；潜在 **翻译后修饰（PTM）** 以不同颜色标出（见上表）。

## CDR hotspots

CDR 区域潜在修饰热点汇总（表），常见类型包括：

- **Asn 脱酰胺**（deamidation）  
- **Asp 异构化**（isomerization）  
- **Met / Trp 氧化**（oxidation）  

上述位点可能影响抗体 **稳定性** 与 **功能**，需在 developability 与 CMC 中跟踪。

## Free cysteine（游离半胱氨酸）

- 检查序列中是否存在 **未参与二硫键** 的 Cys，评估氧化、聚集与质量属性风险。  
- （待补：具体位点、预测工具与结论。）

## Post-translational modification（PTM）

- 除 CDR hotspot 外，恒定区及铰链区 PTM 风险（糖基化、C 端赖氨酸剪切、N 端焦谷氨酸化等按项目填写）。  
- （待补：预测结果与实验验证计划。）

## Structure diagram

- 结构示意图：结构域划分、二硫键连接、CDR 环区位置。  
- （待补：`../../img/` 插图。）

## Molecular properties

- 分子量、等电点（pI）、疏水性、电荷分布等 **in silico** 指标。  
- （待补：数值表或工具输出。）

## Sequence validation

- 序列与参考标准 / 专利 / 细胞系表达载体 **一致性** 核对（VH/VL、信号肽、标签等）。  
- （待补：比对结论。）

## Disulfide bond

- 理论二硫键配对（链间 / 链内）与 **free thiol** 风险。  
- （待补：配对图或列表。）

## Fc mutation

- Fc 区突变或工程化位点（如 silencing、半衰期、效应功能）及 **免疫原性 / 稳定性** 影响。  
- （待补：突变列表与 rationale。）

## Aggregation risk

- 序列与结构 based 的 **聚集倾向**（疏水 patch、电荷不对称、CDR 修饰等）。  
- （待补：预测分数与缓解策略。）

## Amino acid usage frequency

- 与人类抗体库或同种系 **氨基酸使用频率** 对比，辅助人源化与免疫原性评估。  
- （待补：统计图或表。）

## Immunogenicity & humanization

- T 细胞表位、MHC-II 结合等 **免疫原性** 预测；人源化策略与保留 CDR 原则。  
- （待补：人源化前后对比与推荐序列。）
