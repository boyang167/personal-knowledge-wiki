<h1 align="center">ADCdb Tables 详情</h1>

#### 一. 数据统计

| 表格                | 数量   |
| ------------------- | ------ |
| t_adc_activity      | 9,214  |
| t_adc_general       | 6,514  |
| t_adc_indication    | 11,000 |
| t_antibody_activity | 161    |
| t_antibody_general  | 1,157  |
| t_linker_general    | 493    |
| t_payload_activity  | 17,363 |
| t_payload_general   | 446    |
| t_reference         | 5,990  |
| t_`antigen`_general | 336    |

#### 二. ER 图

![]()

#### 三. Tables

1. `adc_general`

    | 字段名                       | 注释                   | 数据类型 | 备注                                                                                                                                                                                                    |
    | ---------------------------- | ---------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `c_drug_id`                  | ADC id                 | text     | 爬虫新增                                                                                                                                                                                                |
    | `c_drug_id_old`              | ADC 旧id               | text     | `旧id，不可作为关键搜索词`                                                                                                                                                                              |
    | c_drug_name                  | ADC名称                | text     | 与 website 的 'ADC Name' 一致                                                                                                                                                                           |
    | c_brand_name                 | 药品名称               | text     |
    | c_adc_synonym                | ADC别称                | text     | 与 website 的 'Synonyms' 一致                                                                                                                                                                           |
    | c_company                    | 公司                   | text     | 与 website 的 'Organization' 一致                                                                                                                                                                       |
    | c_drug_status                | 药物状态               | text     |
    | c_drug_status_rank           | 药物状态等级           | numeric  | 如：1代表已批准；8代表研究中                                                                                                                                                                            |
    | c_dar                        | 抗体药物比             | text     | Drug-to-Antibody Ratio，是ADC药物独特的重要质量属性,它代表抗体偶联小分子毒性药物的平均数量,较低的DAR会降低ADC的效力,但过高的DAR又会影响ADC分析的药代动力学和毒性，普遍认为dar在2-4之间是ADC药物的最优选 |
    | c_structure_yes              | 是否有结构             | numeric  | 0：无；1：有                                                                                                                                                                                            |
    | c_structure_yes_old          |                        | text     | B0119 `不懂`                                                                                                                                                                                            |
    | `c_antibody_id`              | 抗体id                 | text     |                                                                                                                                                                                                         |
    | `c_payload_id`               | 载体id                 | text     |                                                                                                                                                                                                         |
    | `c_antigen_id`               | 抗原id                 | text     |                                                                                                                                                                                                         |
    | `c_linker_id`                | 链id                   | text     |                                                                                                                                                                                                         |
    | c_linker_payload_combination | 偶联物类型             | text     | `在 website 中对应的是'Combination Type'`                                                                                                                                                               |
    | c_antibody_con_type          | 结合方式               | text     | `在 website 中对应的是'Conjugate Type'`                                                                                                                                                                 |
    | c_absorption                 | 药物吸收               | text     | 给药部位进入血液循环的过程                                                                                                                                                                              |
    | c_distribution               | 药物分布               | text     | 吸收入血液的药物随血液循环到达机体组织、器官的过程                                                                                                                                                      |
    | c_metabolism                 | 药物代谢               | text     | 药物在体内的生物化学转化过程                                                                                                                                                                            |
    | c_elimination                | 药物消除               | text     | 药物的生物转化和排泄                                                                                                                                                                                    |
    | c_toxicity                   | 药物毒性               | text     | 药物在细胞、组织或整个机体上造成伤害或有害影响                                                                                                                                                          |
    | c_puchem_sid                 | Puchem 数据库 SID      | text     | SID表示物质                                                                                                                                                                                             |
    | c_drugbank_id                | DrugBank 数据库药品 id | text     |                                                                                                                                                                                                         |
    | c_drugmap_id                 | DrugMAP 数据库         | text     |                                                                                                                                                                                                         |
    | c_ttd_id                     | TTD 数据库             | text     |                                                                                                                                                                                                         |
    | c_dresis_id                  | DRESIS 数据库          | text     |                                                                                                                                                                                                         |
    | c_intede_id                  | INTEDE 数据库          | text     |                                                                                                                                                                                                         |
    | c_chebi_id                   | ChEBI 数据库           | text     |                                                                                                                                                                                                         |
    | c_adc_rank                   |                        | numeric  | `没查到`； 0 1 2 3                                                                                                                                                                                      |
    | c_drug_name_show             |                        | text     | ?                                                                                                                                                                                                       |
    | c_drug_status_link           |                        | text     | ?                                                                                                                                                                                                       |
    | c_drug_status_rank_link      |                        | numeric  | ?                                                                                                                                                                                                       |
    | c_con_yes                    |                        | text     | ？                                                                                                                                                                                                      |
    | c_special_approval           | 特别审批               | text     | 如FDA                                                                                                                                                                                                   |
    | c_puchem_cid                 | Puchem 数据库          | text     | CID表示化合物                                                                                                                                                                                           |  |
    | c_ref_id                     | 参考文献               | text     |
    | c_ref_id_slt                 |                        |          |                                                                                                                                                                                                         |
    | c_ref_id_full                |                        |          |                                                                                                                                                                                                         |
    
    <!-- | ~~synonym~~         |              |          | 与 adc_synonym 重复，已删                                                                                                                                                                               |
    | ~~antibody_id_c~~            |                        |          | antibody_general表中的数据                                                                                                                                                                              |
    | ~~antibody_name~~            |                        |          | antibody_general表中的数据                                                                                                                                                                              |
    | ~~antibody_name_show~~       |                        |          | antibody_general表中的数据                                                                                                                                                                              |
    | ~~payload_id_c~~             |                        |          | payload_general表中的数据                                                                                                                                                                               |
    | ~~payload_target_id~~        |                        |          | payload_general表中的数据                                                                                                                                                                               |
    | ~~payload_target~~           | 治疗靶点               |          | payload_general表中的数据，`在 website 中对应的是'Therapeutic Target'`                                                                                                                                  |
    | ~~payload_name~~             |                        |          | payload_general表中的数据                                                                                                                                                                               |
    | ~~therapeutic_target_id_c~~  |                        |          | antigen_general表中的数据                                                                                                                                                                               |
    | ~~therapeutic_target~~    |                        |          | antigen_general表中的数据                                                                                                                                                                               |
    | ~~linker_id_c~~              |                        |          | linker_general表中的数据                                                                                                                                                                                |
    | ~~linker_name~~              |                        |          | linker_general表中的数据                                                                                                                                                                                |
                                                                                                                                                                                                                   -->

2. `adc_activity`

    | 字段名                            | 注释         | 数据类型 | 备注               |
    | --------------------------------- | ------------ | -------- | ------------------ |
    | rank                              |              | text     | id                 |
    | drug_id_o                         |              | text     |
    | `drug_id_old`                     | 药物旧id     | text     |
    | adc_activity_level                | 药物活性水平 | text     |
    | adc_level_type                    | 药物水平类型 | numeric  |
    | method_description                | 方法描述     | text     |
    | animal_model                      | 动物模型     | text     | 人类疾病的动物模型 |
    | antigen_expression                | 抗原表达     | text     |
    | patients_enrolled                 | 患者记录     | text     |
    | administration_dosage             | 药物剂量     | text     |
    | efficacy_type_old                 | 功效类型     | text     |
    | efficacy_type                     | 功效类型     | text     |
    | efficacy_symbols                  |              |          |
    | if_dot                            |              | numeric  |
    | efficacy_value                    | 功效值       | text     |
    | efficacy_value_d                  |              | text     |
    | efficacy_unit                     | 功效单位     | text     |
    | clinical_trial_identification     | 临床试验id   | text     |
    | adverse_event                     | 不良事件     | text     |
    | clinical_trial_identification_url | 链接         | text     |
    | clinical_trial_description        | 临床描述     | text     |
    | clinical_trial_status             | 临床试验阶段 | text     |
    | primary_endpoint                  | 主要目标     | text     |
    | other_endpoints                   | 其他目标     | text     |
    | ref_id                            | 参考id       | text     |
    | cell_id                           | 细胞id       | text     |
    | adc_cell_disease                  | 疾病         | text     |
    | adc_cell_access                   |              | text     |
    | adc_cell_name                     | 名称         | text     |
    | cell_name_old                     |              | text     |
    | ref_id_old                        |              | text     |

3. `antibody_general`

    | 字段名                                                       | 注释                                               | 数据类型 |
    | ------------------------------------------------------------ | -------------------------------------------------- | -------- |
    | antibody_id_c                                                |                                                    | text     |
    | `antibody_id`                                                | 抗体id                                             | text     |
    | `antibody_id_old `                                           | 抗体旧id                                           | text     |
    | drug_status                                                  |                                                    |
    | antibody_subtype                                             | 抗体亚型                                           | text     |
    | sequence_count                                               |                                                    | numeric  |
    | antibody_heavy_chain_variable_domain_vh                      | 抗体重链可变结构域序列                             | text     |
    | antibody_heavy_chain_constant_domain_ch1                     | 抗体重链恒定结构域序列                             | text     |
    | antibody_heavy_chain_constant_domain_ch2                     | 抗体重链恒定结构域序列                             | text     |
    | antibody_heavy_chain_constant_domain_ch3                     | 抗体重链恒定结构域序列                             | text     |
    | antibody_heavy_chain_hinge_region                            | 抗体重链铰链区                                     | text     |
    | antibody_heavy_chain_complementarity_determining_region_cdr1 | 抗体重链互补决定区                                 | text     |
    | antibody_heavy_chain_complementarity_determining_region_cdr2 | 抗体重链互补决定区                                 | text     |
    | antibody_heavy_chain_complementarity_determining_region_cdr3 | 抗体重链互补决定区                                 | text     |
    | antibody_light_chain_variable_domain_vl                      | 抗体轻链可变结构域                                 | text     |
    | heavy_chain_sequence                                         | 重链序列                                           | text     |
    | light_chain_sequence                                         | 轻链序列                                           | text     |
    | antibody_light_chain_constant_domain_cl                      | 抗体轻链恒定结构域                                 | text     |
    | antibody_light_chain_complementarity_determining_region_cdr1 | 抗体轻链互补决定区                                 | text     |
    | antibody_light_chain_complementarity_determining_region_cdr2 | 抗体轻链互补决定区                                 | text     |
    | antibody_light_chain_complementarity_determining_region_cdr3 | 抗体轻链互补决定区                                 | text     |
    | company                                                      | 公司，与 website 的 'Organization' 一致            | text     |
    | brand_name                                                   |
    | approval_date                                                | 批准日期                                           | text     |
    | indication                                                   | 适应症，又叫指征，指药物等方法适合运用的范围、标准 | text     |
    | antibody_name_show                                           |
    | antibody_name                                                | 抗体名称                                           | text     |
    | ab_rank                                                      |                                                    | text     |
    | antibody_synonym                                             | 抗体别称                                           | text     |
    | `antigen_id`                                                 | 抗原id                                             | text     |
    | antibody_type                                                | 抗体类型                                           | text     |
    | chembl_id                                                    | ChEMBL数据库 id                                    | text     |
    | imgt_mab_db_id                                               | IMGT/mAB 数据库 ID                                 | text     |
    | pdb_id                                                       | PDB 数据库                                         | text     |
    | drugbank_id                                                  | DrugBank 数据库                                    | text     |
    | drug_central_id                                              | DrugCentral 数据库                                 | text     |

4. `antibody_activity`

    | 字段名                         | 注释             | 数据类型 | 备注 |
    | ------------------------------ | ---------------- | -------- | ---- |
    | atbacc_id                      | 抗体活性id       | text     | 猜测 |
    | antibody_id                    | 抗体id           | text     |
    | antibody_function              | 抗体功能         | text     |
    | antibody_antigen_binding_assay | 抗体抗原结合测定 | text     |
    | cell_id                        | 细胞id           | text     |
    | adc_cell_name                  | ADC结合细胞名称  | text     |
    | adc_cell_access                |                  | text     |
    | efficacy_type                  | 药物效力衡量类型 | text     |

5. `payload_general`

    | 字段名                    | 注释                               | 数据类型 | 备注                                                                                                                                                                                                            |
    | ------------------------- | ---------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | payload_id_c              |
    | `payload_id`              |
    | `payload_id_old`          |
    | payload_target_id         |
    | palyload_target_name      |
    | payload_name              |
    | structure_png             | 结构图                             | text     |
    | structure_3d_sdf          | 3d结构文件                         | text     |
    | structure_2d_sdf          | 2d结构文件                         | bool     |
    | isosmiles                 | Isomeric SMILES                    | text     |
    | canonicalsmiles           | Canonical SMILES                   | text     |
    | mw                        | 分子量                             | text     |
    | mf                        | 化学式                             | text     |
    | polararea                 | 极性表面积                         | text     | Topological Polar Surface Area, the surface sum over polar atoms in the molecule                                                                                                                                |
    | complexity                | 复杂度                             | text     | The complexity rating of a compound is a rough estimate of how complicated a structure is, seen from both the point of view of the elements contained and the displayed structural features including symmetry. |
    | xlogp                     | 疏水参数计算参考值                 | text     | xlogp is the octanol-water partition coefficient, which is used to measure the hydrophilicity or hydrophobicity of a molecule.                                                                                  |
    | heavycnt                  | 该化合物中重原子（非氢原子）的数量 | text     | Heavy Atom Count, The number of heavy atoms (non-hydrogen atoms) in this compound.                                                                                                                              |
    | hbonddonor                | 氢键供体的数量                     | text     | Hydrogen Bond Donor Count, The number of hydrogen bond donors in this molecule.                                                                                                                                 |
    | hbondacc                  | 氢键受体的数量                     | text     | Hydrogen Bond Acceptor Count, The number of hydrogen bond acceptors in this molecule.                                                                                                                           |
    | rotbonds                  | 可旋转键的数量                     | text     | Rotatable Bond Count, The number of rotatable bond in this molecule, which is any single-order non-ring bond                                                                                                    |
    | inchi                     | InChI                              | text     |
    | inchikey                  | InChIKey                           | text     |
    | pubchem_cid               | PubChem CID                        | text     |
    | payload_name_show         |
    | synonym                   |
    | payload_target_uniprot_id |
    | payload_rank              |
    | iupacname                 | IUPAC Name                         | text     |

6. `payload_activity`

    | 字段名             | 注释 | 数据类型 | 备注 |
    | ------------------ | ---- | -------- | ---- |
    | molecule_chembl_id |
    | dupref             |
    | payload_id_0       |
    | payload_id_c       |
    | efficacy_type_old  |
    | payload_acc_id     |
    | ref_id_before      |
    | ref_id             |
    | `payload_id_old`   |
    | payload_name       |
    | ref_id_old         |
    | target             |
    | payload_type       |
    | efficacy_type      |
    | efficacy_symbols   |
    | ic50_value         |
    | ic50_unit          |
    | cell_id            |
    | adc_cell_disease   |
    | adc_cell_name      |
    | adc_cell_access    |
    | cell_name          |

7. `linker_general`

    | 字段名           | 注释                               | 数据类型 | 备注                                                                                                                                                                                                            |
    | ---------------- | ---------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | linker_id_c      |                                    | text     |
    | linker_id        | 交联剂id                           | text     |
    | linker_id_old    | 交联剂旧id                         | text     |
    | structure_png    | 结构图                             | text     |
    | structure_3d_sdf | 3d结构文件                         | text     |
    | structure_2d_sdf | 2d结构文件                         | bool     |
    | linker_rank      |                                    | text     |
    | linker_name      | 交联剂名称                         | text     |
    | linker_name_show | 交联剂                             | text     |
    | linker           | 交联剂                             | text     |
    | pubchem_cid      | PubChem CID                        | text     |
    | linker_type      | 交联剂类型                         | text     |
    | cleavable        | 可裂解                             | text     |
    | cmpdname         | 化合物名称                         | text     |
    | cmpdsynonym      | 化合物别称                         | text     |
    | mw               | 分子量                             | text     |
    | mf               | 化学式                             | text     |
    | polararea        | 极性表面积                         | text     | Topological Polar Surface Area, the surface sum over polar atoms in the molecule                                                                                                                                |
    | complexity       | 复杂度                             | text     | The complexity rating of a compound is a rough estimate of how complicated a structure is, seen from both the point of view of the elements contained and the displayed structural features including symmetry. |
    | xlogp            | 疏水参数计算参考值                 | text     | xlogp is the octanol-water partition coefficient, which is used to measure the hydrophilicity or hydrophobicity of a molecule.                                                                                  |
    | heavycnt         | 该化合物中重原子（非氢原子）的数量 | text     | Heavy Atom Count, The number of heavy atoms (non-hydrogen atoms) in this compound.                                                                                                                              |
    | hbonddonor       | 氢键供体的数量                     | text     | Hydrogen Bond Donor Count, The number of hydrogen bond donors in this molecule.                                                                                                                                 |
    | hbondacc         | 氢键受体的数量                     | text     | Hydrogen Bond Acceptor Count, The number of hydrogen bond acceptors in this molecule.                                                                                                                           |
    | rotbonds         | 可旋转键的数量                     | text     | Rotatable Bond Count, The number of rotatable bond in this molecule, which is any single-order non-ring bond                                                                                                    |
    | inchi            | InChI                              | text     |
    | isosmiles        | Isomeric SMILES                    | text     |
    | canonicalsmiles  | Canonical SMILES                   | text     |
    | inchikey         | InChIKey                           | text     |
    | iupacname        | IUPAC Name                         | text     |
    | ref_raw          | DOI                                | text     |
    | ref_id           | 参考文献id                         | text     |

8. `antigen_general` ~~target_general~~

    | 字段名                                   | 注释          | 数据类型 | 备注  |
    | ---------------------------------------- | ------------- | -------- | ----- |
    | ~~therapeutic_target_id_c~~ antigen_id_c |               | text     |
    | ~~therapeutic_target_id~~ antigen_id     | 抗原id        | text     |
    | ~~target_name~~ antigen_name             | 抗原名称      | text     |
    | tissue_express                           |               | text     |
    | pro_num                                  | 蛋白数量      | numeric  | 1/2/3 |
    | uniprot_id                               | UniProt id    | text     |       |
    | protein_name                             | 蛋白名称      | text     |
    | gene_name                                | 基因名称      | text     |
    | synonym                                  | 别名          | text     |
    | synonym1                                 | 别名          | text     |
    | synonym2                                 | 别名          | text     |
    | synonym3                                 | 别名          | text     |
    | sequence1                                | 序列          | text     |
    | sequence2                                | 序列          | text     |
    | sequence3                                | 序列          | text     |
    | gene_id                                  | 基因id        | text     |
    | family1                                  | 家族          | text     |
    | family2                                  | 家族          | text     |
    | family3                                  | 家族          | text     |
    | function1                                | 功能          | text     |
    | function2                                | 功能          | text     |
    | function3                                | 功能          | text     |
    | uniprot_entry                            | Uniprot Entry | text     |
    | hgnc_id                                  | HGNC ID       | text     |       |
    | kegg_id                                  | KEGG ID       | text     |       |

9. `adc_indication`

    | 字段名                | 注释             | 数据类型 |
    | --------------------- | ---------------- | -------- |
    | drug_id_old           | id               | text     |
    | indication_name       | 适应症名称       | text     |
    | indication_merge      | 适应症名称+ICD11 | text     |
    | indication_name_old   | 旧称             | text     |
    | indication_status     | 适应症状态       | text     |
    | indication_phase_num  | 临床试验阶段     | numeric  |
    | indication_status_old |                  | text     |
    | showornot             | show or not      | bool     |
    | icd_11                | 国际疾病分类     | text     |

10. `reference`

    | 字段名  | 注释         | 数据类型 | 备注                   |
    | ------- | ------------ | -------- | ---------------------- |
    | ref_id  | 参考文献id   | text     |
    | rf_name | 参考文献名称 | text     |
    | url     | 链接         | text     |
    | pmid    | 文献编号     | text     | PMID，PubMed唯一标识码 |