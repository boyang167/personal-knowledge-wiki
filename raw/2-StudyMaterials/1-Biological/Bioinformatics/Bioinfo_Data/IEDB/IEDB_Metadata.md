# IEDB Metadata

## 1. Tables

Table Name | Number of Rows | Number of Columns
--- | --- | ---
t_assay_finder_bcell_ancestry | 523 | 5
t_chain | 424656 | 16
t_reference_linking | 25 | 4
t_mhc_bind | 815717 | 12
t_distinct_chain | 234642 | 16
t_organism | 9158 | 5
t_mhc_allele_restriction | 22689 | 25
t_distinct_receptor_receptor_grp | 213497 | 3
t_molecule_finder_prot_ancestry | 899842 | 5
t_assay_type | 464 | 7
t_geoloc_finder_ancestry | 893 | 3
t_disease_finder_ancestry | 57363 | 3
t_tcell_receptor | 244517 | 2
t_journal | 2742 | 4
t_bcell_receptor | 18546 | 2
t_molecule_finder_nonp_ancestry | 53120 | 5
t_source | 3140000 | 13
t_organism_names | 32627 | 3
t_epitope | 2228034 | 14
t_distinct_receptor | 213497 | 5
t_bcell | 1404831 | 78
t_reference | 24849 | 3
t_geolocation | 217 | 3
t_object | 5872684 | 23
t_reference_category_assoc | 24846 | 2
t_submission | 428 | 8
t_receptor_group | 193663 | 5
t_curated_epitope | 3812144 | 13
t_organism_finder_host_ancestry | 4320 | 5
t_assay_finder_elution_ancestry | 320 | 5
t_disease | 3579 | 5
t_organism_finder_src_ancestry | 35745 | 6
t_mhc_elution | 3987940 | 44
t_complex | 6970 | 43
t_tcell | 536239 | 97
t_allele_finder_ancestry | 143746 | 5
t_reference_category | 201 | 4
t_epitope_object | 3812144 | 4
t_curated_receptor | 223288 | 19
t_article | 24421 | 20
t_assay_finder_tcell_ancestry | 1861 | 5



## 2. Columns

### t_assay_finder_bcell_ancestry
Column Name | Data Type | Description
--- | --- | ---
c_node_id | integer | 
c_assay_type_id | numeric | 
c_obi_id | text | 
c_child_assay_type_id | numeric | 
c_child_obi_id | text | 
### t_chain
Column Name | Data Type | Description
--- | --- | ---
c_chain_id | integer | 
c_species | numeric | 
c_chain_type | text | 
c_v_dom_seq | text | 
c_v_gene | text | 
c_d_gene | text | 
c_j_gene | text | 
c_cdr1_seq | text | 
c_cdr1_start | numeric | 
c_cdr1_end | numeric | 
c_cdr2_seq | text | 
c_cdr2_start | numeric | 
c_cdr2_end | numeric | 
c_cdr3_seq | text | 
c_cdr3_start | numeric | 
c_cdr3_end | numeric | 
### t_reference_linking
Column Name | Data Type | Description
--- | --- | ---
c_reference_id | integer | 
c_ref_reference_id | integer | 
c_comments | text | 
c_title | text | 
### t_mhc_bind
Column Name | Data Type | Description
--- | --- | ---
c_mhc_bind_id | integer | 
c_reference_id | integer | 
c_curated_epitope_id | integer | 
c_as_location | text | 
c_as_type_id | integer | 
c_as_char_value | text | 
c_as_num_value | text | 
c_as_inequality | text | 
c_as_comments | text | 
c_mhc_allele_restriction_id | integer | 
c_mhc_allele_name | text | 
c_complex_id | text | 
### t_distinct_chain
Column Name | Data Type | Description
--- | --- | ---
c_distinct_chain_id | integer | 
c_species | numeric | 
c_chain_type | text | 
c_v_dom_seq | text | 
c_v_gene | text | 
c_d_gene | text | 
c_j_gene | text | 
c_cdr1_start | numeric | 
c_cdr1_end | numeric | 
c_cdr2_start | numeric | 
c_cdr2_end | numeric | 
c_cdr3_start | numeric | 
c_cdr3_end | numeric | 
c_cdr1_seq | text | 
c_cdr2_seq | text | 
c_cdr3_seq | text | 
### t_organism
Column Name | Data Type | Description
--- | --- | ---
c_organism_id | integer | 
c_parent_tax_id | integer | 
c_active_node | text | 
c_path | text | 
c_rank | text | 
### t_mhc_allele_restriction
Column Name | Data Type | Description
--- | --- | ---
c_mhc_allele_restriction_id | integer | 
c_displayed_restriction | text | 
c_synonyms | text | 
c_includes | text | 
c_restriction_level | text | 
c_organism | text | 
c_organism_ncbi_tax_id | integer | 
c_class | text | 
c_haplotype | text | 
c_locus | text | 
c_serotype | text | 
c_molecule | text | 
c_chain_i_name | text | 
c_chain_ii_name | text | 
c_chain_i_locus | text | 
c_chain_i_mutation | text | 
c_chain_ii_locus | text | 
c_chain_ii_mutation | text | 
c_chain_i_source_id | text | 
c_chain_ii_source_id | text | 
c_iri | text | 
c_chain_i_accession | text | 
c_chain_ii_accession | text | 
c_chain_i_mro_id | text | 
c_chain_ii_mro_id | text | 
### t_distinct_receptor_receptor_grp
Column Name | Data Type | Description
--- | --- | ---
c_receptor_group_id | integer | 
c_distinct_receptor_id | integer | 
c_match_code | text | 
### t_molecule_finder_prot_ancestry
Column Name | Data Type | Description
--- | --- | ---
c_node_id | integer | 
c_source_id | text | 
c_obi_id | text | 
c_child_source_id | text | 
c_child_obi_id | text | 
### t_assay_type
Column Name | Data Type | Description
--- | --- | ---
c_assay_type_id | integer | 
c_category | text | 
c_assay_type | text | 
c_response | text | 
c_units | text | 
c_obi_id | text | 
c_class | text | 
### t_geoloc_finder_ancestry
Column Name | Data Type | Description
--- | --- | ---
c_node_id | integer | 
c_obi_id | text | 
c_child_obi_id | text | 
### t_disease_finder_ancestry
Column Name | Data Type | Description
--- | --- | ---
c_node_id | integer | 
c_obi_id | text | 
c_child_obi_id | text | 
### t_tcell_receptor
Column Name | Data Type | Description
--- | --- | ---
c_curated_receptor_id | integer | 
c_tcell_id | integer | 
### t_journal
Column Name | Data Type | Description
--- | --- | ---
c_journal_id | integer | 
c_journal_title | text | 
c_journal_issn | text | 
c_medline_ta | text | 
### t_bcell_receptor
Column Name | Data Type | Description
--- | --- | ---
c_curated_receptor_id | integer | 
c_bcell_id | integer | 
### t_molecule_finder_nonp_ancestry
Column Name | Data Type | Description
--- | --- | ---
c_node_id | integer | 
c_source_id | text | 
c_obi_id | text | 
c_child_source_id | text | 
c_child_obi_id | text | 
### t_source
Column Name | Data Type | Description
--- | --- | ---
c_source_id | integer | 
c_accession | text | 
c_database | text | 
c_name | text | 
c_aliases | text | 
c_chemical_type | text | 
c_source_date | text | 
c_sequence | text | 
c_smiles_structure | text | 
c_synonyms | text | 
c_organism_id | text | 
c_organism_name | text | 
c_smiles_image | text | 
### t_organism_names
Column Name | Data Type | Description
--- | --- | ---
c_organism_id | integer | 
c_name_txt | text | 
c_name_class | text | 
### t_epitope
Column Name | Data Type | Description
--- | --- | ---
c_epitope_id | integer | 
c_description | text | 
c_linear_peptide_seq | text | 
c_linear_peptide_modified_seq | text | 
c_linear_peptide_modification | text | 
c_non_aa_source_id | text | 
c_disc_source_id | text | 
c_disc_region | text | 
c_disc_modification | text | 
c_mc_region | text | 
c_mc_mol1_source_id | text | 
c_mc_mol1_modification | text | 
c_mc_mol2_source_id | text | 
c_mc_mol2_modification | text | 
### t_distinct_receptor
Column Name | Data Type | Description
--- | --- | ---
c_distinct_receptor_id | integer | 
c_distinct_chain1_id | numeric | 
c_distinct_chain2_id | numeric | 
c_receptor_type | text | 
c_species | numeric | 
### t_bcell
Column Name | Data Type | Description
--- | --- | ---
c_bcell_id | integer | 
c_reference_id | integer | 
c_curated_epitope_id | integer | 
c_as_location | text | 
c_as_type_id | integer | 
c_as_char_value | text | 
c_as_num_value | numeric | 
c_as_inequality | text | 
c_as_num_subjects | numeric | 
c_as_num_responded | numeric | 
c_as_response_frequency | numeric | 
c_as_immunization_comments | text | 
c_as_comments | text | 
c_as_ant_conformation | text | 
c_h_organism_id | integer | 
c_h_gaz_id | text | 
c_h_sex | text | 
c_h_age | text | 
c_h_mhc_types_present | text | 
c_iv1_process_type | text | 
c_iv1_adjuvants | text | 
c_iv1_route | text | 
c_iv1_dose_schedule | text | 
c_iv1_disease_id | numeric | 
c_iv1_disease_stage | text | 
c_iv1_imm_type | text | 
c_iv1_imm_ref_name | text | 
c_iv1_imm_object_id | numeric | 
c_iv1_imm_ev | text | 
c_iv1_con_object_id | numeric | 
c_iv2_process_type | text | 
c_iv2_adjuvants | text | 
c_iv2_route | text | 
c_iv2_dose_schedule | text | 
c_iv2_disease_id | numeric | 
c_iv2_disease_stage | text | 
c_iv2_imm_type | text | 
c_iv2_imm_ref_name | text | 
c_iv2_imm_object_id | numeric | 
c_iv2_imm_ev | text | 
c_iv2_con_object_id | numeric | 
c_ab_name | text | 
c_ab_type | text | 
c_ab_materials_assayed | text | 
c_ab_immunoglobulin_domain | text | 
c_ab_c1_mol_type | text | 
c_ab_c2_mol_type | text | 
c_adt_iv_process_type | text | 
c_adt_iv_adjuvants | text | 
c_adt_iv_route | text | 
c_adt_iv_dose_schedule | text | 
c_adt_iv_disease_id | numeric | 
c_adt_iv_disease_stage | text | 
c_adt_iv_imm_type | text | 
c_adt_iv_imm_ref_name | text | 
c_adt_iv_imm_object_id | numeric | 
c_adt_iv_imm_ev | text | 
c_adt_iv_con_object_id | numeric | 
c_adt_ab_name | text | 
c_adt_ab_type | text | 
c_adt_ab_materials_assayed | text | 
c_adt_ab_immunoglobulin_domain | text | 
c_adt_ab_c1_mol_type | text | 
c_adt_ab_c2_mol_type | text | 
c_adt_h_organism_id | numeric | 
c_adt_h_gaz_id | text | 
c_adt_h_age | text | 
c_adt_h_sex | text | 
c_adt_h_mhc_types_present | text | 
c_adt_comments | text | 
c_ant_type | text | 
c_ant_ref_name | text | 
c_ant_object_id | integer | 
c_ant_ev | text | 
c_ant_con_object_id | numeric | 
c_complex_id | numeric | 
c_ab_object_id | numeric | 
c_adt_ab_object_id | numeric | 
### t_reference
Column Name | Data Type | Description
--- | --- | ---
c_reference_id | integer | 
c_reference_type | text | 
c_curation_keywords | text | 
### t_geolocation
Column Name | Data Type | Description
--- | --- | ---
c_gaz_id | text | 
c_display_name | text | 
c_secondary_names | text | 
### t_object
Column Name | Data Type | Description
--- | --- | ---
c_object_id | integer | 
c_reference_id | integer | 
c_object_type | text | 
c_object_sub_type | text | 
c_object_description | text | 
c_derivative_type | text | 
c_organism_id | text | 
c_organism2_id | text | 
c_region | text | 
c_starting_position | text | 
c_ending_position | text | 
c_cell_name | text | 
c_cell_type | text | 
c_tissue_type | text | 
c_origin | text | 
c_mol1_seq | text | 
c_mol1_modified_seq | text | 
c_mol1_modification | text | 
c_mol1_source_id | text | 
c_mol2_modified_seq | text | 
c_mol2_modification | text | 
c_mol2_source_id | text | 
c_mult_chain_mol_name | text | 
### t_reference_category_assoc
Column Name | Data Type | Description
--- | --- | ---
c_reference_id | integer | 
c_ref_category_id | integer | 
### t_submission
Column Name | Data Type | Description
--- | --- | ---
c_submission_id | integer | 
c_reference_id | integer | 
c_submitter_name | text | 
c_submission_date | date | 
c_submission_authors | text | 
c_submission_affiliations | text | 
c_submission_title | text | 
c_submission_abstract | text | 
### t_receptor_group
Column Name | Data Type | Description
--- | --- | ---
c_receptor_group_id | integer | 
c_receptor_type | text | 
c_species | text | 
c_chain1_cdr3_seq | text | 
c_chain2_cdr3_seq | text | 
### t_curated_epitope
Column Name | Data Type | Description
--- | --- | ---
c_curated_epitope_id | integer | 
c_reference_id | integer | 
c_e_name | text | 
c_e_location | text | 
c_e_region_domain_flag | text | 
c_e_comments | text | 
c_e_object_id | integer | 
c_related_object_id | numeric | 
c_related_object_type | text | 
c_e_ev | text | 
c_e_ref_start | numeric | 
c_e_ref_end | numeric | 
c_e_ref_region | text | 
### t_organism_finder_host_ancestry
Column Name | Data Type | Description
--- | --- | ---
c_node_id | integer | 
c_org_id | integer | 
c_obi_id | text | 
c_child_org_id | integer | 
c_child_obi_id | text | 
### t_assay_finder_elution_ancestry
Column Name | Data Type | Description
--- | --- | ---
c_node_id | integer | 
c_assay_type_id | numeric | 
c_obi_id | text | 
c_child_assay_type_id | numeric | 
c_child_obi_id | text | 
### t_disease
Column Name | Data Type | Description
--- | --- | ---
c_disease_id | integer | 
c_disease_name | text | 
c_synonyms | text | 
c_accession | text | 
c_disease_source | text | 
### t_organism_finder_src_ancestry
Column Name | Data Type | Description
--- | --- | ---
c_node_id | integer | 
c_org_id | integer | 
c_obi_id | text | 
c_child_org_id | integer | 
c_child_obi_id | text | 
c_child_obi_species_obi | text | 
### t_mhc_elution
Column Name | Data Type | Description
--- | --- | ---
c_mhc_elution_id | integer | 
c_reference_id | integer | 
c_curated_epitope_id | integer | 
c_as_location | text | 
c_as_type_id | integer | 
c_as_char_value | text | 
c_as_num_value | text | 
c_as_inequality | text | 
c_as_num_subjects | text | 
c_as_num_responded | text | 
c_as_response_frequency | text | 
c_as_immunization_comments | text | 
c_as_comments | text | 
c_h_organism_id | integer | 
c_h_gaz_id | text | 
c_h_sex | text | 
c_h_age | text | 
c_h_mhc_types_present | text | 
c_iv1_process_type | text | 
c_iv1_adjuvants | text | 
c_iv1_route | text | 
c_iv1_dose_schedule | text | 
c_iv1_disease_id | text | 
c_iv1_disease_stage | text | 
c_iv1_imm_type | text | 
c_iv1_imm_ref_name | text | 
c_iv1_imm_object_id | text | 
c_iv1_imm_ev | text | 
c_iv1_con_object_id | text | 
c_ivt_process_type | text | 
c_ivt_imm_type | text | 
c_ivt_imm_ref_name | text | 
c_ivt_imm_object_id | text | 
c_ivt_imm_ev | text | 
c_ivt_con_object_id | text | 
c_mhc_allele_restriction_id | integer | 
c_mhc_allele_name | text | 
c_mhc_allele_ev | text | 
c_ant_type | text | 
c_ant_ref_name | text | 
c_ant_object_id | integer | 
c_apc_cell_type | text | 
c_apc_tissue_type | text | 
c_apc_origin | text | 
### t_complex
Column Name | Data Type | Description
--- | --- | ---
c_complex_id | integer | 
c_reference_id | integer | 
c_atom_pairs | text | 
c_pdb_id | text | 
c_pdb_cell_contact_area | text | 
c_e_contact_area | text | 
c_e_viewer_status | boolean | 
c_ab_c1_pdb_chain | text | 
c_ab_c2_pdb_chain | text | 
c_mhc_c1_pdb_chain | text | 
c_mhc_c2_pdb_chain | text | 
c_tcr_c1_pdb_chain | text | 
c_tcr_c2_pdb_chain | text | 
c_ant_pdb_chain | text | 
c_e_pdb_chain | text | 
c_e_residues | text | 
c_ab_ant_residues | text | 
c_e_mhc_residues | text | 
c_e_tcr_residues | text | 
c_mhc_e_residues | text | 
c_mhc_tcr_residues | text | 
c_tcr_e_residues | text | 
c_tcr_mhc_residues | text | 
c_calc_atom_pairs | text | 
c_calc_e_contact_area | text | 
c_calc_cell_contact_area | text | 
c_calc_e_residues | text | 
c_calc_ab_ant_residues | text | 
c_calc_e_mhc_residues | text | 
c_calc_e_tcr_residues | text | 
c_calc_mhc_e_residues | text | 
c_calc_mhc_tcr_residues | text | 
c_calc_tcr_e_residues | text | 
c_calc_tcr_mhc_residues | text | 
c_comments | text | 
c_complex_type | text | 
c_type_flag | text | 
c_c1_type | text | 
c_c2_type | text | 
c_mhc_chain1 | text | 
c_mhc_chain2 | text | 
c_modified_date | text | 
c_created_date | text | 
### t_tcell
Column Name | Data Type | Description
--- | --- | ---
c_tcell_id | integer | 
c_reference_id | integer | 
c_curated_epitope_id | integer | 
c_as_location | text | 
c_as_type_id | integer | 
c_as_char_value | text | 
c_as_num_value | text | 
c_as_inequality | text | 
c_as_num_subjects | text | 
c_as_num_responded | text | 
c_as_response_frequency | text | 
c_as_immunization_comments | text | 
c_as_comments | text | 
c_h_organism_id | integer | 
c_h_gaz_id | text | 
c_h_sex | text | 
c_h_age | text | 
c_h_mhc_types_present | text | 
c_tcr_name | text | 
c_tcr_c1_mol_type | text | 
c_tcr_c2_mol_type | text | 
c_iv1_process_type | text | 
c_iv1_adjuvants | text | 
c_iv1_route | text | 
c_iv1_dose_schedule | text | 
c_iv1_disease_id | text | 
c_iv1_disease_stage | text | 
c_iv1_imm_type | text | 
c_iv1_imm_ref_name | text | 
c_iv1_imm_object_id | text | 
c_iv1_imm_ev | text | 
c_iv1_con_object_id | text | 
c_iv2_process_type | text | 
c_iv2_adjuvants | text | 
c_iv2_route | text | 
c_iv2_dose_schedule | text | 
c_iv2_disease_id | text | 
c_iv2_disease_stage | text | 
c_iv2_imm_type | text | 
c_iv2_imm_ref_name | text | 
c_iv2_imm_object_id | text | 
c_iv2_imm_ev | text | 
c_iv2_con_object_id | text | 
c_ivt_process_type | text | 
c_ivt_responder_cell_type | text | 
c_ivt_stimulator_cell_type | text | 
c_ivt_imm_type | text | 
c_ivt_imm_ref_name | text | 
c_ivt_imm_object_id | text | 
c_ivt_imm_ev | text | 
c_ivt_con_object_id | text | 
c_adt_iv_process_type | text | 
c_adt_iv_adjuvants | text | 
c_adt_iv_route | text | 
c_adt_iv_dose_schedule | text | 
c_adt_iv_disease_id | text | 
c_adt_iv_disease_stage | text | 
c_adt_iv_imm_type | text | 
c_adt_iv_imm_ref_name | text | 
c_adt_iv_imm_object_id | text | 
c_adt_iv_imm_ev | text | 
c_adt_iv_con_object_id | text | 
c_adt_tcr_name | text | 
c_adt_tcr_organism_id | text | 
c_adt_tcr_c1_mol_type | text | 
c_adt_tcr_c2_mol_type | text | 
c_adt_h_organism_id | text | 
c_adt_h_gaz_id | text | 
c_adt_h_age | text | 
c_adt_h_sex | text | 
c_adt_h_mhc_types_present | text | 
c_adt_effector_cell_type | text | 
c_adt_effector_tissue_type | text | 
c_adt_effector_origin | text | 
c_adt_comments | text | 
c_effector_cell_type | text | 
c_effector_tissue_type | text | 
c_effector_origin | text | 
c_mhc_allele_restriction_id | text | 
c_mhc_allele_name | text | 
c_mhc_allele_ev | text | 
c_mhc_autologous | text | 
c_apc_cell_type | text | 
c_apc_tissue_type | text | 
c_apc_origin | text | 
c_apc_h_organism_id | text | 
c_apc_h_age | text | 
c_apc_h_sex | text | 
c_apc_h_mhc_types_present | text | 
c_ant_type | text | 
c_ant_ref_name | text | 
c_ant_object_id | integer | 
c_ant_ev | text | 
c_ant_con_object_id | text | 
c_complex_id | text | 
c_tcr_object_id | text | 
c_adt_tcr_object_id | text | 
### t_allele_finder_ancestry
Column Name | Data Type | Description
--- | --- | ---
c_node_id | integer | 
c_iedb_mhc_id | integer | 
c_obi_id | text | 
c_child_iedb_mhc_id | integer | 
c_child_obi_id | text | 
### t_reference_category
Column Name | Data Type | Description
--- | --- | ---
c_ref_category_id | integer | 
c_category_name | text | 
c_priority | text | 
c_sort_order | text | 
### t_epitope_object
Column Name | Data Type | Description
--- | --- | ---
c_epitope_id | integer | 
c_object_id | integer | 
c_source_antigen_accession | text | 
c_source_organism_org_id | text | 
### t_curated_receptor
Column Name | Data Type | Description
--- | --- | ---
c_curated_receptor_id | integer | 
c_distinct_receptor_id | integer | 
c_ref_name | text | 
c_ref_synonyms | text | 
c_rr_id | text | 
c_comments | text | 
c_receptor_type | text | 
c_chain1_id_cur | numeric | 
c_chain1_id_calc | numeric | 
c_chain1_nt_acc | text | 
c_chain1_nt_seq | text | 
c_chain1_pro_acc | text | 
c_chain1_pro_seq | text | 
c_chain2_id_cur | numeric | 
c_chain2_id_calc | numeric | 
c_chain2_nt_acc | text | 
c_chain2_nt_seq | text | 
c_chain2_pro_acc | text | 
c_chain2_pro_seq | text | 
### t_article
Column Name | Data Type | Description
--- | --- | ---
c_article_id | integer | 
c_reference_id | integer | 
c_journal_id | integer | 
c_journal_volume | text | 
c_journal_issue | text | 
c_article_date | integer | 
c_article_pages | text | 
c_article_title | text | 
c_article_authors | text | 
c_article_abstract | text | 
c_article_affiliations | text | 
c_article_chemical_list | text | 
c_article_mesh_headings_list | text | 
c_medline_date | text | 
c_comments | text | 
c_pubmed_id | integer | 
c_pmc_id | text | 
c_preprint_url | text | 
c_modified_date | text | 
c_created_date | text | 
### t_assay_finder_tcell_ancestry
Column Name | Data Type | Description
--- | --- | ---
c_node_id | integer | 
c_assay_type_id | numeric | 
c_obi_id | text | 
c_child_assay_type_id | numeric | 
c_child_obi_id | text | 
