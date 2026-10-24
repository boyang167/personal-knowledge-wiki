# Metadata
*部分描述包含单位以及实验条件*
## clinical_trials_metadata
|                       | description         |
|-----------------------|---------------------|
| c_inn                 | 国际非药品专利名称   |
| c_application         | 应用（诊断/治疗）         |
| c_clinical_indication | 临床适应症 |
| c_development_status  | 开发阶段  |
## sequence_metadata
|       | description |
|-------|-------------|
| c_id  | ID          |
| c_inn | INN         |
| c_vh  | VH          |
| c_vl  | VL          |
## therapeutic_metadata  
|                      | description        |
|----------------------|--------------------|
| c_id                 | ID                 |
| c_inn                | INN                |
| c_format             | 抗体类型             |
| c_hc_class           | 重链亚型           |
| c_lc_type            | 轻链类型（K/L）          |
| c_highest_clin_trial | 临床阶段 |
| c_target             | 靶点             |
| c_species            | 物种            |
| c_pdb                | PDB                |
| c_pdb_reference      | PDB_reference      |
| c_adas_rate          | ADAs_rate          |
| c_adas_reference     | ADAs_reference     |
## tools_integration_metadata
|             | description |
|-------------|-------------|
| c_name      | Name        |
| c_year      | Year        |
| c_model     | Model       |
| c_url       | URL         |
| c_reference | Reference   |
## experimental_data_Avery_metadata
|                 | dtype   | description   |
|-----------------|---------|---------------|
| c_name          | text    | Name          |
| c_cl_ml_hr_kg_8 | decimal | vivo clearance |
| c_dna_8         | decimal | DNA elisa       |
| c_insulin_8     | decimal | Insulin elisa     |
| c_acsins_8      | text    | ACSINS      |
| c_fcrn_rt_8     | text    | FcRn 柱上的保留时间 |
| c_fcrn_pw_8     | text    | FcRn 峰宽    |
## experimental_data_Bailly_metadata
|               | dtype   | description |
|---------------|---------|-------------|
| c_full_name   | text    | Full Name   |
| c_hic_pred_15 | decimal | HIC.pred |
## experimental_data_Chung_metadata
|                            | dtype   | description              |
|----------------------------|---------|--------------------------|
| c_name                     | text    | Name                     |
| c_cl_ml_d_kg_7             | decimal | Cl.Ml.D.Kg 清除率          |
| c_trans_mdck_hfcrn_ng_ml_7 | decimal | Trans.MDCK.hFcRn.ng.mL |
| c_trans_mdck_ng_ml_7       | text    | Trans.MDCK.ng.mL      |
| c_mdck_mfi_7               | text    | MDCK.MFI               |
| c_mdck_hfcrn_mfi_7         | text    | MDCK.hFcRn.MFI         |
| c_fcrn_kd_ph6_7            | text    | FcRn.Kd.pH6           |
| c_bv_elisa_7               | text    | BV.ELISA              |
## experimental_data_Fekete_metadata
|          | dtype   | description |
|----------|---------|-------------|
| c_name   | text    | Name        |
| c_hic_16 | decimal | HIC      |                                
## experimental_data_Goulet_metadata
|                       | dtype   | description         |
|-----------------------|---------|---------------------|
| c_name                | text    | Name                |
| c_cl_ml_d_kg_9        | decimal | CL.ml.d.kg          |
| c_half_life_9         | decimal | 半衰期            |
| c_fcrn_ka_ph6_9       | decimal | FcRn.ka.pH6       |
| c_fcrn_kd_ph6_9       | decimal | FcRn.kd.pH6       |
| c_fcrn_response_ph7_9 | decimal | FcRn.Response.pH7 |
| c_dh_9                | decimal | ΔH unfold的焓变能     |
| c_tm_9                | decimal | Tm               |
| c_dcp_9               | decimal | ΔCP unfold的热容变化             |
## experimental_data_Grinshpun_metadata
|                 | dtype   | description   |
|-----------------|---------|---------------|
| c_name          | text    | Name          |
| c_cl_ml_d_kg_12 | decimal | CL.mL.d.kg 清除率 |
## experimental_data_Hebditch_metadata
|                 | dtype   | description   |
|-----------------|---------|---------------|
| c_full_name     | text    | Full Name     |
| c_accstab_pred  | decimal | ACCSTAB.pred  |
| c_acsins_pred   | decimal | ACSINS.pred   |
| c_bvpelisa_pred | decimal | BVPELISA.pred |
| c_cic_pred      | decimal | CIC.pred      |
| c_csibli_pred   | decimal | CSIBLI.pred   |
| c_dsf_pred      | decimal | DSF.pred      |
| c_elisa_pred    | decimal | ELISA.pred    |
| c_hek_pred      | decimal | HEK.pred      |
| c_hic_pred      | decimal | HIC.pred      |
| c_psr_pred      | decimal | PSR.pred      |
| c_sgac_pred     | decimal | SGAC.pred     |
| c_smac_pred     | decimal | SMAC.pred     |
## experimental_data_Hu_metadata
|               | dtype   | description |
|---------------|---------|-------------|
| c_name        | text    | Name        |
| c_cl_ml_day_4 | decimal | CL.ml.day |
## experimental_data_Jain_metadata
|                 | dtype   | description   |
|-----------------|---------|---------------|
| c_name          | text    | Name          |
| c_tm_negated_   | decimal | Tm(Negated)   |
| c_as            | decimal | AS            |
| c_sgac_negated_ | decimal | SGAC(Negated) |
| c_hic           | decimal | HIC           |
| c_smac          | decimal | SMAC          |
| c_psr           | decimal | PSR           |
| c_acsins        | decimal | ACSINS        |
| c_cic           | decimal | CIC           |
| c_csi           | decimal | CSI           |
| c_elisa         | decimal | ELISA         |
| c_bvp           | decimal | BVP  ELISA与杆状病毒颗粒的结合    |
| c_dnp           | text    | DNP  ELISA 中与 2,4-二硝基苯酚的结合         |
## experimental_data_Kelly_metadata
|              | dtype   | description |
|--------------|---------|-------------|
| c_name       | text    | Name        |
| c_hsp90_10   | decimal | Hsp90含量，交叉相互作用指标    |
| c_smp_10     | decimal | solubilized membrane protein含量，交叉相互作用指标  |
| c_scp_10     | decimal | soluble cytosolic protein含量，交叉相互作用指标      |
| c_hsp70_10   | decimal | Hsp70含量，交叉相互作用指标    |
| c_trigger_10 | decimal | trigger factor  |
## experimental_data_Kraft_metadata
|                 | dtype   | description   |
|-----------------|---------|---------------|
| c_name          | text    | Name          |
| c_fcrn_rel_rt_3 | decimal | FcRn.Rel.RT FcRn 柱上的保留时间 |
| c_hep_rt_3      | text    | Hep.RT      |
## experimental_data_Lai_metadata
|                  | dtype   | description    |
|------------------|---------|----------------|
| c_name           | text    | Name           |
| c_ph6_agg_rate_5 | decimal | pH6.Agg.Rate |
## experimental_data_Lecerf_metadata
|                | dtype   | description  |
|----------------|---------|--------------|
| c_name         | text    | Name         |
| c_fe_fviii_2   | decimal | Fe.FVIII   |
| c_fe_c3_2      | decimal | Fe.C3      |
| c_fe_lysm_2    | decimal | Fe.LysM    |
| c_heme_fviii_2 | text    | Heme.FVIII |
| c_heme_c3_2    | text    | Heme.C3    |
| c_heme_lysm_2  | text    | Heme.LysM  |
| c_heme_2       | text    | Heme ELISA 中与血红素的结合     |
| c_fa_2         | text    | FA ELISA 中与叶酸的结合       |
## experimental_data_link_metadata
|           | dtype | description |
|-----------|-------|-------------|
| c_name    | text  | name        |
| c_pmid    | text  | PMID        |
| c_address | text  | address     |
## experimental_data_Makowski_metadata
|         | dtype   | description |
|---------|---------|-------------|
| c_name  | text    | Name        |
| c_smp_6 | decimal | SMP soluble membrane protein处理得到PSP分数，非特异性相互作用指标       |
| c_scp_6 | decimal | SCP soluble cytosolic proteins处理得到PSP分数       |
| c_ova_6 | decimal | OVA ovalbumin处理得到PSP分数      |
| c_hsa_6 | decimal | HSA human serum albumin处理得到PSP分数      |

## 检测项目
|测定|描述|
|:----|:----|
|ACCSTAB|蛋白质稳定性预测指数|
|ACSINS|自相互作用|
|AS|通过 SEC% 单体测量加速稳定性|
|CIC|交叉相互作用色谱法|
|CL|清除率|
|CSI|自相互作用|
|CSIBLI|生物层干涉测量法克隆自相互作用|
|DSF|差示扫描荧光法，蛋白质热稳定性指标|
|ELISA|酶联免疫吸附测定，灵敏度和特异性指标|
|FcRn|新生儿Fc受体|
|Fe+2 *|暴露于亚铁离子后获得 * 的结合|
|HEK|HEK细胞表达滴度|
|Heme *|接触血红素后获得 * 的结合|
|Hep RT|肝素柱上的保留时间|
|HIC|疏水相互作用色谱保留时间|
|MDCK|Madin–Darby canine kidney细胞系|
|PSR|交叉相互作用指标|
|SGAC-SINS|自相互作用指标|
|SMAC|立式单层吸附色谱，特异性相互作用指标|
|Tm|熔点温度，热稳定性指标|
