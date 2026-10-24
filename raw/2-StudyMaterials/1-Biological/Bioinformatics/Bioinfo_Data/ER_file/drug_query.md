# 药物信息查询整合

-   修改日期：2024-06-17

## 已整合的数据库

| 数据库名称        | 数据内容                                                      | 侧重方向                                                                                  | 完成人     |
|--------------|-----------------------------------------------------------|---------------------------------------------------------------------------------------|---------|
| Drugs@FDA    | FDA批准的供人类使用的药物信息                                          | 药物获批状态，FDA文件（url）                                                                     | Xintian |
| TTD          | Therapeutic Target Database                               | 药物靶点综合信息                                                                              | Xintian |
| DGIdb        | drug–gene interaction database                            | 药物靶基因                                                                                 | Xintian |
| ChEMBL       | database of bioactive molecules with drug-like properties | 药物实验数据（ADME, binding, functional, physicochemical, toxicity），药物warning信息，专利信息，临床试验，靶点 | Xintian |
| Thera-SAbDab | therapeutic antibodies                                    | 抗体序列，抗体结构                                                                             | Jiannan |
| Tabs         | 治疗性抗体相关信息的数据库                                             | 抗体序列，抗体临床试验信息，抗体专利                                                                    | Jiannan |
| DOTAD        | 治疗性抗体数据库                                                  | 抗体可开发性                                                                                | Yixiao  |
| ADCdb        | database of antibody–drug conjugates                      | ADC药物综合信息                                                                             | Jiannan |

## 输入
-   目前支持使用药物名称查询
-   药物名称可以是：商品名，主要成分名称，研发各阶段的代号
-   推荐使用`主要成分名称`查询。

## 输出内容

><b><u>下划线和加粗</u></b>的输出内容为多行的数据框

1.   trade_name: 商品名
2.   companies：研发公司
3.   highest_status：最高研发阶段，如：Approved，Phase-3，Phase-2/3，Preregistration，Preclinical
4.   ATC_code：ATC药物系统分级分类编号
5.   drug_type：药物类型（暂根据FDA的application type确定，如为BLA则认为该药物是生物药，NDA和ANDA则认为是化学药物）及具体描述
6.   CAS_number：CAS注册数据库的注册号
7.   PDB_id：PDB编号
8.   <b><u>chemical_info</u></b>：药物化学信息，包括：c_canonical_smiles, c_standard_inchi_key, c_standard_inchi
9.   hc_type：重链类型
10.   lc_type：轻链类型
11.   <b><u>biological_sequence</u></b>：生物药序列，包括：'c_sequence_name', 'c_sequence', 'c_chothia_cdrs', 'c_lcdr1', 'c_lcdr2', 'c_lcdr3', 'c_hcdr1', 'c_hcdr2', 'c_hcdr3'
12.   biotherapeutic_description：生物药描述
13.   <b><u>ADAs_rate</u></b>：ADA(Anti-Drug Antibodies)信息，包括：c_adas_rate, c_adas_reference
14.   <u><b>FDA_docs_url</u></b>：FDA文件，包括：'c_submissionno', 'c_submissiontype', 'c_applicationdocstypedescription', 'c_applicationdocsdate', 'c_applicationdocsurl'
15.   <b><u>ChEMBL_assay</b></u>：药物的药代动力学、功能、结合、理化性质、毒性实验数据，包括：'c_description', 'c_assay_type', 'c_assay_organism', 'c_assay_strain', 'c_assay_tissue', 'c_assay_cell_type', 'c_standard_type', 'c_standard_relation', 'c_standard_value', 'c_standard_units', 'c_action_type', 'c_activity_comment', 'c_assay_subcellular_fraction', 'c_relationship_desc', 'c_confidence_score', 'c_doi', 'c_bei', 'c_sei', 'c_le', 'c_lle'
16.   <b><u>developability</b></u>：抗体可开发性信息，收录在DOTAD数据库中的已发表文献、实验数据和部分预测结果
17.   <b><u>drug_warning</b></u>：药物warning信息，包括：c_warning_type, c_warning_class, c_warning_description, c_warning_country, c_warning_year, c_ref_type, c_ref_url
18.   <b><u>product</b></u>：药物产品信息，包括：'c_drugname', 'c_activeingredient', 'c_appltype', 'c_sponsorname', 'c_form', 'c_strength', 'c_marketingstatusdescription', 'c_tecode', 'c_rld', 'c_rs'
19.   <b><u>clinical_trial</b></u>：药物临床试验信息，包括：'c_efo_term', 'c_mesh_heading', 'c_max_phase_for_ind', 'c_ref_id'
20.   <b><u>patent</b></u>：药物专利信息，包括：'c_patent_number', 'c_title', 'c_assignee', 'c_inventors', 'c_abstract', 'c_filing_date', 'c_publication_date', 'c_expire_date'
21.   <b><u>relation</b></u>：相关药物（目前只有抗体药物包含该数据，例如：tibulizumab的scFv来自ixekizumab，则ixekizumab为tibulizumab的parent），包括：'c_name', 'c_antibody0', 'c_relationship', 'c_antibody1'
22.   <b><u>target</b></u>：药物靶点（调控机制，靶点功能，binding site等），包括：'c_gene_name', 'c_concept_id', 'c_ensembl_id', 'c_uniprot_id', 'c_interaction_score', 'c_approved', 'c_immunotherapy', 'c_anti_neoplastic', 'c_categories', 'c_target_name', 'c_target_type', 'c_bioclass', 'c_moa', 'c_target_function', 'c_activity', 'c_pdb_id', 'c_ec_number', 'c_target_sequence', 'c_target_organism', 'c_target_go_terms', 'c_binding_site_name', 'c_bs_domains', 'c_bs_domain', 'c_bs_start_pos', 'c_bs_end_pos', 'c_disease_efficacy', 'c_mechanism_comment', 'c_selectivity_comment', 'c_binding_site_comment', 'c_varseq_uniprot_accession', 'c_mutation', 'c_varseq_uniprot_version', 'c_isoform', 'c_organism', 'c_varient_sequence', 'c_ref_type', 'c_mechanism_ref_url'
23.   reference：药物参考文献的pubmed_id
24.   <b><u>ADC</b></u>：ADC药物信息（DAR，payload，linker，payload与抗体连接的大致方式，实验数据等），包括：'c_drug_name', 'c_brand_name', 'c_company', 'c_adc_synonym', 'c_drug_status', 'c_dar', 'c_payload_name', 'c_payload_target', 'c_antibody_name', 'c_therapeutic_target', 'c_linker_name','c_linker_payload_combination', 'c_antibody_con_type', 'c_special_approval', 'c_chembl_id', 'c_absorption', 'c_distribution', 'c_metabolism', 'c_elimination', 'c_toxicity'

## 后续计划
1. 添加更新信息：增加每一类查询结果的数据来源+当前版本的更新时间
2. 提供完整的Uniprot编号：包括uniprot_accession/entry（如：P84085）和uniprot_id/entry_name（如：ARF5_HUMAN）
3. 建立cross-reference的target_id映射：gene_name，ensembl_id，uniprot_id和uniprot_accession，HGNC_id
4. 以靶点为查询字段查询药物数据库：
    -   整合后某一靶点的查询结果大致包括：靶点在多个数据库中的id，靶点序列，靶点功能描述，靶向药物，靶点相关疾病，`靶点间relation（整合KEGG和string中的关系）`
3. （后期）序列查询：根据序列查询相近的单抗、双抗、融合蛋白等。

## Example:
-   drug_input = 'IXEKIZUMAB'
-   output:

```
{'drug_input': 'IXEKIZUMAB',
 'trade_name': 'TALTZ',
 'companies': 'Eli Lilly;Oregon Health & Science University;Torii '
              'Pharmaceutical',
 'highest_status': 'Approved',
 'ATC_code': ['l04ac13'],
 'drug_type': 'Biologics: antibody, monoclonal antibody, whole mab, humanized '
              'mouse antibody ',
 'CAS_number': ['1143503-69-8'],
 'PDB_id': ['6nou;6nov'],
 'chemical_info': [],
 'hc_type': 'g4',
 'lc_type': 'kappa',
 'biological_sequence':            c_sequence_name                                         c_sequence  ...       c_hcdr2            c_hcdr3
0          ixekizumab LCVR  divmtqtplslsvtpgqpasiscrssrslvhsrgntylhwylqkpg...  ...          None               None
1          ixekizumab HCVR  qvqlvqsgaevkkpgssvkvsckasgysftdyhihwvrqapgqgle...  ...  52-57:npmygt  99-108:ydyftgtgvy
2   ixekizumab heavy chain  qvqlvqsgaevkkpgssvkvsckasgysftdyhihwvrqapgqgle...  ...          None               None
3   ixekizumab light chain  divmtqtplslsvtpgqpasiscrssrslvhsrgntylhwylqkpg...  ...          None               None
4              heavy_chain  QVQLVQSGAEVKKPGSSVKVSCKASGYSFTDYHIHWVRQAPGQGLE...  ...           NaN                NaN
5              light_chain  DIVMTQTPLSLSVTPGQPASISCRSSRSLVHSRGNTYLHWYLQKPG...  ...           NaN                NaN
6            heavy_chain_2                                                 na  ...           NaN                NaN
7            light_chain_2                                                 na  ...           NaN                NaN
8                       VH  QIQLVQSGSELKKPGASVKVSCKASGYTFTTAGMQWVRQAPGQGLE...  ...           NaN                NaN
9                       VL  DIQMTQSPSFLSASVGDRVTITCKASQDVSTAVAWYQQKPGQPPKL...  ...           NaN                NaN
10  Ixekizumab heavy chain  QVQLVQSGAEVKKPGSSVKVSCKASGYSFTDYHIHWVRQAPGQGLE...  ...           NaN                NaN
11  Ixekizumab light chain  DIVMTQTPLSLSVTPGQPASISCRSSRSLVHSRGNTYLHWYLQKPG...  ...           NaN                NaN

[12 rows x 9 columns],
 'biotherapeutic_description': ['ixekizumab (humanized mab)'],
 'ADAs_rate':   c_adas_rate                                   c_adas_reference
0         8.5  https://www.nature.com/articles/s41598-018-329...,
 'FDA_docs_url':     c_submissionno c_submissiontype c_applicationdocstypedescription c_applicationdocsdate                               c_applicationdocsurl
0               20       SUPPL                       Pediatric Other            1900-01-01  https://www.accessdata.fda.gov/drugsatfda_docs...
1                1       ORIG                                  Label            2016-03-23  http://www.accessdata.fda.gov/drugsatfda_docs/...
2                1       ORIG                                 Letter            2016-03-24  http://www.accessdata.fda.gov/drugsatfda_docs/...
3                1       ORIG                                 Review            2016-05-03  http://www.accessdata.fda.gov/drugsatfda_docs/...
4                1       ORIG                         Summary Review            2016-05-03  http://www.accessdata.fda.gov/drugsatfda_docs/...
5                3       SUPPL                                 Label            2017-07-05  http://www.accessdata.fda.gov/drugsatfda_docs/...
6                3       SUPPL                                Letter            2017-07-06  http://www.accessdata.fda.gov/drugsatfda_docs/...
7                4       SUPPL                                Letter            2017-12-01  http://www.accessdata.fda.gov/drugsatfda_docs/...
8                4       SUPPL                                 Label            2017-12-04  http://www.accessdata.fda.gov/drugsatfda_docs/...
9               11       SUPPL                                Letter            2018-03-20  http://www.accessdata.fda.gov/drugsatfda_docs/...
10               2       SUPPL                                 Label            2018-04-23  http://www.accessdata.fda.gov/drugsatfda_docs/...
11               2       SUPPL                                Letter            2018-04-23  http://www.accessdata.fda.gov/drugsatfda_docs/...
12               9       SUPPL                                 Label            2018-05-21  http://www.accessdata.fda.gov/drugsatfda_docs/...
13               9       SUPPL                                Letter            2018-05-21  http://www.accessdata.fda.gov/drugsatfda_docs/...
14              16       SUPPL                                Letter            2019-08-27  http://www.accessdata.fda.gov/drugsatfda_docs/...
15              16       SUPPL                                 Label            2019-09-04  http://www.accessdata.fda.gov/drugsatfda_docs/...
16              20       SUPPL                                 Label            2020-03-27  http://www.accessdata.fda.gov/drugsatfda_docs/...
17              20       SUPPL                                Letter            2020-03-27  http://www.accessdata.fda.gov/drugsatfda_docs/...
18              19       SUPPL                                 Label            2020-06-02  http://www.accessdata.fda.gov/drugsatfda_docs/...
19              19       SUPPL                                Letter            2020-06-02  http://www.accessdata.fda.gov/drugsatfda_docs/...
20              14       SUPPL                                 Label            2021-03-11  http://www.accessdata.fda.gov/drugsatfda_docs/...
21              14       SUPPL                                Letter            2021-03-11  http://www.accessdata.fda.gov/drugsatfda_docs/...
22              24       SUPPL                                 Label            2022-07-28  http://www.accessdata.fda.gov/drugsatfda_docs/...
23              24       SUPPL                                Letter            2022-07-28  https://www.accessdata.fda.gov/drugsatfda_docs...
24              24       SUPPL                      Medication Guide            2022-07-28  https://www.accessdata.fda.gov/drugsatfda_docs...
25              28       SUPPL                                Letter            2023-09-14  https://www.accessdata.fda.gov/drugsatfda_docs...
26              31       SUPPL                                Letter            2024-03-08  https://www.accessdata.fda.gov/drugsatfda_docs...
27              31       SUPPL                                 Label            2024-03-11  http://www.accessdata.fda.gov/drugsatfda_docs/...,
 'ChEMBL_assay': [],
 'developability':   avery_vivo_clearance chung_clearance goulet_clearance grinshpun_clearance  ... lecerf_fe_lysm lecerf_heme_c3 lecerf_heme_fviii lecerf_heme_lysm
0                 None             5.1             None                None  ...           None           None              None             None

[1 rows x 69 columns],
 'drug_warning': [],
 'product':   c_drugname c_activeingredient c_appltype     c_sponsorname                c_form c_strength c_marketingstatusdescription c_tecode c_rld c_rs
0      TALTZ         IXEKIZUMAB        BLA  ELI LILLY AND CO  INJECTABLE;INJECTION    80MG/ML                 Prescription     None    No  TBD,
 'clinical_trial':                    c_efo_term                     c_mesh_heading c_max_phase_for_ind                                           c_ref_id
0         psoriatic arthritis               Arthritis, Psoriatic            Approved  NCT01695239,NCT02349295,NCT02584855,NCT0315155...
1                   psoriasis                          Psoriasis            Approved  NCT01107457,NCT01474512,NCT01597245,NCT0162423...
2          psoriasis vulgaris                          Psoriasis            Approved                                        NCT04340076
3                    COVID-19  Severe Acute Respiratory Syndrome             Phase-3                                        NCT04724629
4      ankylosing spondylitis            Spondylitis, Ankylosing             Phase-3  NCT01870284,NCT02696785,NCT02696798,NCT0275735...
5        rheumatoid arthritis              Arthritis, Rheumatoid             Phase-2                NCT00966875,NCT01236118,NCT01253265
6                   stricture           Constriction, Pathologic             Phase-2                                        NCT05309616
7   major depressive disorder         Depressive Disorder, Major             Phase-2                                        NCT04979910
8    type 1 diabetes mellitus          Diabetes Mellitus, Type 1             Phase-2                                        NCT04589325
9          bullous pemphigoid                Pemphigoid, Bullous             Phase-2                                        NCT03099538
10   pityriasis rubra pilaris           Pityriasis Rubra Pilaris             Phase-2                                        NCT03485976
11                   Pyoderma                           Pyoderma             Phase-2                                        NCT03137160
12        lichen planopilaris                      Lichen Planus       Early_Phase-1                                        NCT05030415
13                        NaN                                NaN             Phase-4                                        NCT06085079
14                        NaN                                NaN             Phase-1                                        NCT04259346
15                        NaN                                NaN             Phase-4                                        NCT04083612
16                        NaN                                NaN             Phase-4                                        NCT03942042
17                        NaN                                NaN             Phase-1                                        NCT03848403,
 'patent':    c_patent_number                                            c_title  ... c_publication_date c_expire_date
0     WO2007070750                             ANTI-IL-17 ANTIBODIES   ...         2007-06-21          None
1     WO2013134052                        IL-17 ANTIBODY FORMULATION   ...         2013-09-12          None
2    US20150010573                        IL-17 ANTIBODY FORMULATION   ...         2015-01-08          None
3    US20200140537                    Treatment of Genital Psoriasis   ...         2020-05-07          None
4    US20160280781                        IL-17 ANTIBODY FORMULATION   ...         2016-09-29          None
5    US20200262911                  THERAPEUTIC ANTIBODY FORMULATION   ...         2020-08-20          None
6    US20230295290                  Treatment of Respiratory Disease   ...         2023-09-21          None
7     WO2017011260                             TREATMENT OF PRURITUS   ...         2017-01-19          None
8        US9376491  IL-17 antibody formulation and method of treat...  ...         2016-06-28          None
9    US20180057584                        IL-17 ANTIBODY FORMULATION   ...         2018-03-01          None
10    WO2019027828                  ANTI-IL-17 ANTIBODY DOSE REGIMEN   ...         2019-02-07          None
11    WO2020172002                  THERAPEUTIC ANTIBODY FORMULATION   ...         2020-08-27          None
12      US10472416  IL-17 antibody formulations and methods of tre...  ...         2019-11-12          None
13       US9845353  IL-17 antibody formulations and methods of tre...  ...         2017-12-19          None
14    WO2021211430                  TREATMENT OF RESPIRATORY DISEASE   ...         2021-10-21          None
15    WO2007070750                             ANTI-IL-17 ANTIBODIES   ...         2007-06-21          None

[16 rows x 8 columns],
 'relation':        c_name c_antibody0 c_relationship  c_antibody1
0  ixekizumab  ixekizumab         parent  tibulizumab,
 'target':   c_gene_name c_concept_id c_ensembl_id c_uniprot_id  ... c_organism  c_varient_sequence  c_ref_type                                c_mechanism_ref_url
0       IL17A    hgnc:5981         None       Q16552  ...       None                None         FDA  http://www.accessdata.fda.gov/drugsatfda_docs/...

[1 rows x 37 columns],
 'reference': [25748485,
               35187727,
               37026832,
               25355284,
               33355284,
               27039261,
               37824031,
               34600483,
               33479721,
               26072109,
               37356077,
               27887675,
               33278016,
               31488067,
               37433424,
               31874129,
               25693783,
               30360663,
               24623718,
               37400681,
               29878382,
               34310771,
               22455413,
               23515267,
               26910853,
               28917383,
               34812561,
               31184530,
               36250261,
               32316070,
               35612328,
               36967086,
               29116597,
               26842296,
               26842297,
               33602246,
               33817799,
               35089610,
               27098317,
               31254223,
               34436817,
               28903122,
               37858007,
               29751001,
               30942952,
               35674861,
               24752880,
               37434099,
               35393269,
               36181252,
               32620295,
               32293641,
               35347721,
               37481752,
               36175131,
               33964329,
               37609785,
               32200512,
               35220812,
               35661135,
               27726163,
               34050899,
               35048787,
               30650216,
               31696745,
               29803904,
               33167745,
               34320259,
               22808966,
               22808967,
               34560906,
               33276811,
               27500949,
               32814997,
               37587870,
               28551073,
               35429281,
               34106794,
               28027825,
               35170742,
               37799352,
               20131262,
               29187009,
               28792259,
               32536003,
               28074446,
               30589394,
               32557532,
               27299809,
               28600810,
               35449322,
               35638250,
               34378230],
 'ADC': []}
```