<h1 align="center">IMGT Tables 详情</h1>

#### 一. 数据统计

| 表名                                                 | 行数   |
| ---------------------------------------------------- | ------ |
| t_imgt_2d_structure_chain_details                    | 2,343  |
| t_imgt_2d_structure_domain_details                   | 7,061  |
| t_imgt_3d_structure_chain_details                    | 1,097  |
| t_imgt_3d_structure_domain_details                   | 1,484  |
| t_imgt_genedb_genelist                               | 11,179 |
| t_imgt_genedb_sequence_AA_WithoutGaps_F_ORF_inframeP | 14,860 |
| t_imgt_mabdb_company                                 | 2,590  |
| t_imgt_mabdb_entries                                 | 1,489  |
| t_imgt_mhcdb_hla_allele_list                         | 38,909 |
| t_imgt_mhcdb_hla_allele_status                       | 38,909 |
| t_imgt_mhcdb_hla_cds_seq                             | 43,471 |
| t_imgt_mhcdb_hla_dna_seq                             | 21,139 |
| t_imgt_mhcdb_hla_prot_seq                            | 43,270 |


#### 二. ER 图

#### 三. Tables

1. t_imgt_2d_structure_chain_details  
   
   | 字段名                    | 注释   | 数据类型 |
   | ------------------------- | ------ | -------- |
   | c_pdbcode                 | PDBid  | numeric  |
   | c_chain_id                | 链id   | text     |
   | c_chain_length            | 链长度 | numeric  |
   | c_imgt_chain_description  | 链描述 | text     |
   | c_chain_sequence          | 序列   | text     |
   | c_n_d                     |        | text     |
   | c_hinge_region            |        | text     |
   | c_chs                     |        | text     |
   | c_linker                  |        | text     |
   | c_a_domain                |        | text     |
   | c_contact_analysis        |        | text     |
   | c_chainamino_acidsequence |        | text     |
   | c_remarks                 |        | text     |

   t_imgt_3d_structure_chain_details

    | 字段名                   | 注释 | 数据类型 |
    | ------------------------ | ---- | -------- |
    | c_pdbcode                |      | text     |
    | c_chain_id               |      | text     |
    | c_chain_length           |      | numeric  |
    | c_imgt_chain_description |      | text     |
    | c_chain_sequence         |      | text     |
    | c_remarks                |      | text     |
    | c_sheet_composition      |      | text     |
    | c_n_d                    |      | text     |
    | c_linker                 |      | text     |
    | c_hinge_region           |      | text     |
    | c_chs                    |      | text     |

2. t_imgt_2d_structure_domain_details / t_imgt_3d_structure_domain_details

    | 字段名            | 注释 | 数据类型 |
    | ----------------- | ---- | -------- |
    | c_chain_id        |      | text     |
    | c_domain          |      | text     |
    | c_start           |      | text     |
    | c_end             |      | numeric  |
    | c_gene_and_allele |      | text     |
	
3. t_imgt_genedb_genelist

    | 字段名                                          | 注释         | 数据类型 |
    | ----------------------------------------------- | ------------ | -------- |
    | c_species                                       | 物种         | text     |
    | c_imgt_gene_db (`需修改字段名为gene_name`)      | 基因名       | text     |
    | c_gene_functionality                            | 基因功能     | text     |
    | c_imgt_and_hgnc_gene_definition                 | 基因定义     | text     |
    | c_number_of_alleles                             | 等位基因数量 | numeric  |
    | c_chromosome                                    | 染色体       | text     |
    | c_chromosomal_localization                      | 染色体位置   | text     |
    | c_imgt_ligm_db_reference_sequence_for_allele_01 |              | text     |
    | c_ncbi_gene                                     | ncbi 基因号  | text     |

4. t_imgt_genedb_sequence_AA_WithoutGaps_F_ORF_inframeP

    | 字段名                                                                   | 注释                   | 数据类型 | 备注                                                                                                                                         |
    | ------------------------------------------------------------------------ | ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
    | accession_number                                                         | accession号            | text     | 对应IMGT/LIGM-DB数据库                                                                                                                       |
    | imgt_gene_and_allele_name                                                | imgt基因名和等位基因名 | text     |                                                                                                                                              |
    | species                                                                  | 物种                   | text     |                                                                                                                                              |
    | imgt_allele_functionality                                                | 等位基因功能           | text     |
    | region_name                                                              | 区域名                 | text     |
    | start_and_end_positions                                                  | 起始和终止位置         | text     | in the IMGT/LIGM-DB accession number(s)                                                                                                      | `拆`? |
    | number_of_nucleotides                                                    | nt数量                 | text     | in the IMGT/LIGM-DB accession number(s)                                                                                                      |
    | codon_start_or_nr_for_non_coding_labels                                  |                        | text     | 'NR'指 not relevant                                                                                                                          |
    | number_of_nucleotides_added_in_5_prime_end                               |                        | text     | number of nucleotides (nt) added in 5' compared to the corresponding label extracted from IMGT/LIGM-DB                                       |
    | number_of_nucleotides_added_or_removed_in_3_prime_end                    |                        | text     | compared to the corresponding label extracted from IMGT/LIGM-DB                                                                              |
    | number_of_added_deleted_and_or_substituted_nucleotides_or_not_scorrected |                        | text     | number of added, deleted, and/or substituted nucleotides to correct sequencing errors, or 'not corrected' if non corrected sequencing errors |
    | number_of_amino_acids                                                    |                        | text     | this field indicates that the sequence is in amino acids                                                                                     |
    | nt_or_aa_add_imgt_gaps                                                   | 碱基数量加gap数量      | text     | number of characters in the sequence                                                                                                         |
    | partial                                                                  |
    | reverse_complementary                                                    | 反向互补               | text     |
    | sequence                                                                 | 序列                   | text     |


5. t_imgt_mabdb_company
   
   | 字段名                              | 注释 | 数据类型 |
   | ----------------------------------- | ---- | -------- |
   | c_company                           |      | text     |
   | c_expression_system                 |      | text     |
   | c_application                       |      | text     |
   | c_clinical_domain                   |      | text     |
   | c_mechanism_of_action               |      | text     |
   | c_clinical_indication               |      | text     |
   | c_development_status                |      | text     |
   | c_regulatory_agency_status_and_year |      | text     |
   | c_imgt_mab_db_id                    |      | numeric  |

6. t_imgt_mabdb_entries

    | 字段名                                | 注释     | 数据类型 |
    | ------------------------------------- | -------- | -------- |
    | c_imgt_mab_db_id                      |          | numeric  |
    | c_inn                                 |          | text     |
    | c_inn_number                          |          | numeric  |
    | c_inn_prop__list                      |          | text     |
    | c_inn_rec__list                       |          | text     |
    | c_common_name                         |          | text     |
    | c_proprietary_name                    |          | text     |
    | c_species                             |          | text     |
    | c_imgt_receptor_type                  |          | text     |
    | c_receptor_identification             |          | text     |
    | c_radiolabelled___conjugated___fused  |          | text     |
    | c_imgt_2dstructure_db                 |          | numeric  |
    | c_imgt_3dstructure_db                 |          | text     |
    | c_specificity_target_name_and_species |          | text     |
    | c_development_technology              |          | text     |
    | c_origin_clone_species                |          | text     |
    | c_origin_clone_name                   |          | text     |
    | c_clinical_trials                     |          | text     |
    | c_authority_decisions                 |          | text     |
    | c_external_links                      |          | text     |
    | c_biosimilars                         |          | text     |
    | c_imgt_notes                          |          | text     |
    | c_imgt_citations                      |          | text     |
    | c_imgt_references                     |          | text     |
    | c_effects                             |          | text     |
    | c_partners                            |          | text     |
    | c_description                         | 描述     | text     |
    | c_references                          | 参考文献 | text     |

7. t_imgt_mhcdb_hla_allele_list

    | 字段名     | 注释       | 数据类型 |
    | ---------- | ---------- | -------- |
    | c_alleleid | 等位基因id | text     |
    | c_allele   | 等位基因   | text     |

8. t_imgt_mhcdb_hla_allele_status
   
    | 字段名      | 注释     | 数据类型 |
    | ----------- | -------- | -------- |
    | c_allele    | 等位基因 | text     |
    | c_cells     |          | numeric  |
    | c_groups    |          | numeric  |
    | c_confirmed |          | text     |
    | c_start     | 开始位置 | numeric  |
    | c_end       | 终止位置 | numeric  |
    | c_partial   |          | text     |
    | c_type      | 类型     | text     |

9.  t_imgt_mhcdb_hla_cds_seq / t_imgt_mhcdb_hla_dna_seq /       t_imgt_mhcdb_hla_prot_seq

    | 字段名     | 注释       | 数据类型 |
    | ---------- | ---------- | -------- |
    | c_alleleid | 等位基因id | text     |
    | c_allele   | 等位基因   | text     |
    | c_length   | 长度       | text     |
    | c_sequence | 序列       | text     |
  