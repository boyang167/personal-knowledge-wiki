## 1 normal_tissue

| Unnamed: 0    | dtype | description |
|:--------------|:------|:------------|
| c_gene        | text  | Gene        |
| c_gene_name   | text  | Gene name   |
| c_tissue      | text  | Tissue      |
| c_cell_type   | text  | Cell type   |
| c_level       | text  | Level       |
| c_reliability | text  | Reliability |


## 2 pathology

| Unnamed: 0                   | dtype   | description                |
|:-----------------------------|:--------|:---------------------------|
| c_gene                       | text    | Gene                       |
| c_gene_name                  | text    | Gene name                  |
| c_cancer                     | text    | Cancer                     |
| c_high                       | decimal | High                       |
| c_medium                     | decimal | Medium                     |
| c_low                        | decimal | Low                        |
| c_not_detected               | decimal | Not detected               |
| c_prognostic___favorable     | decimal | prognostic - favorable     |
| c_unprognostic___favorable   | decimal | unprognostic - favorable   |
| c_prognostic___unfavorable   | decimal | prognostic - unfavorable   |
| c_unprognostic___unfavorable | decimal | unprognostic - unfavorable |


## 3 subcellular_location

| Unnamed: 0                        | dtype   | description                     |
|:----------------------------------|:--------|:--------------------------------|
| c_gene                            | text    | Gene                            |
| c_gene_name                       | text    | Gene name                       |
| c_reliability                     | text    | Reliability                     |
| c_main_location                   | text    | Main location                   |
| c_additional_location             | text    | Additional location             |
| c_extracellular_location          | text    | Extracellular location          |
| c_enhanced                        | text    | Enhanced                        |
| c_supported                       | text    | Supported                       |
| c_approved                        | text    | Approved                        |
| c_uncertain                       | text    | Uncertain                       |
| c_single_cell_variation_intensity | text    | Single-cell variation intensity |
| c_single_cell_variation_spatial   | text    | Single-cell variation spatial   |
| c_cell_cycle_dependency           | text    | Cell cycle dependency           |
| c_go_id                           | text    | GO id                           |


## 4 rna_tissue_consensus

| Unnamed: 0   | dtype   | description   |
|:-------------|:--------|:--------------|
| c_gene       | text    | Gene          |
| c_gene_name  | text    | Gene name     |
| c_tissue     | text    | Tissue        |
| c_ntpm       | decimal | nTPM          |


## 5 rna_tissue_hpa

| Unnamed: 0   | dtype   | description   |
|:-------------|:--------|:--------------|
| c_gene       | text    | Gene          |
| c_gene_name  | text    | Gene name     |
| c_tissue     | text    | Tissue        |
| c_tpm        | decimal | TPM           |
| c_ptpm       | decimal | pTPM          |
| c_ntpm       | decimal | nTPM          |


## 5.5 rna_tissue_hpa_description

| Unnamed: 0   | dtype   | description   |
|:-------------|:--------|:--------------|
| c_tissue     | text    | Tissue        |
| c_tissue_group | text    | Tissue group  |
| c_organ      | text    | Organ         |


## 6 rna_brain_hpa

| Unnamed: 0   | dtype   | description   |
|:-------------|:--------|:--------------|
| c_gene       | text    | Gene          |
| c_gene_name  | text    | Gene name     |
| c_subregion  | text    | Subregion     |
| c_tpm        | decimal | TPM           |
| c_ptpm       | decimal | pTPM          |
| c_ntpm       | decimal | nTPM          |


## 7 rna_pfc_brain_hpa

| Unnamed: 0   | dtype   | description   |
|:-------------|:--------|:--------------|
| c_gene       | text    | Gene          |
| c_gene_name  | text    | Gene name     |
| c_subregion  | text    | Subregion     |
| c_tpm        | decimal | TPM           |
| c_ptpm       | decimal | pTPM          |
| c_ntpm       | decimal | nTPM          |


## 8 rna_tissue_gtex

| Unnamed: 0   | dtype   | description   |
|:-------------|:--------|:--------------|
| c_gene       | text    | Gene          |
| c_gene_name  | text    | Gene name     |
| c_tissue     | text    | Tissue        |
| c_tpm        | decimal | TPM           |
| c_ptpm       | decimal | pTPM          |
| c_ntpm       | decimal | nTPM          |


## 9 rna_tissue_fantom

| Unnamed: 0   | dtype   | description   |
|:-------------|:--------|:--------------|
| c_gene       | text    | Gene          |
| c_gene_name  | text    | Gene name     |
| c_tissue     | text    | Tissue        |
| c_tpm        | decimal | TPM           |
| c_stpm       | decimal | sTPM          |
| c_ntpm       | decimal | nTPM          |


## 10 rna_single_cell_type

| Unnamed: 0   | dtype   | description   |
|:-------------|:--------|:--------------|
| c_gene       | text    | Gene          |
| c_gene_name  | text    | Gene name     |
| c_cell_type  | text    | Cell type     |
| c_ntpm       | decimal | nTPM          |

## 11 rna_single_cell_type_tissue
| Unnamed: 0        | dtype   | description     |
|:------------------|:--------|:----------------|
|c_gene	|text	|Gene|
|c_gene_name	|text|	Gene name|
|c_tissue	|text|	Tissue|
|c_cluster	|text|	Cluster|
|c_cell_type	|text|	Cell type|
|c_read_count	|decimal|	Read count|
|c_ntpm	|decimal|	nTPM|

## 11.5 rna_single_cell_cluster_description

| Unnamed: 0        | dtype   | description     |
|:------------------|:--------|:----------------|
| c_tissue          | text    | Tissue          |
| c_cluster         | text    | Cluster         |
| c_cell_type       | text    | Cell type       |
| c_cell_type_group | text    | Cell type group |
| c_cell_count      | decimal | Cell count      |


## 13 rna_brain_gtex

| Unnamed: 0     | dtype   | description   |
|:---------------|:--------|:--------------|
| c_gene         | text    | Gene          |
| c_gene_name    | text    | Gene name     |
| c_brain_region | text    | Brain region  |
| c_tpm          | decimal | TPM           |
| c_ptpm         | decimal | pTPM          |
| c_ntpm         | decimal | nTPM          |


## 14 rna_brain_fantom

| Unnamed: 0     | dtype   | description   |
|:---------------|:--------|:--------------|
| c_gene         | text    | Gene          |
| c_gene_name    | text    | Gene name     |
| c_brain_region | text    | Brain region  |
| c_tpm          | decimal | TPM           |
| c_stpm         | decimal | sTPM          |
| c_ntpm         | decimal | nTPM          |


## 15 rna_pig_brain_hpa

| Unnamed: 0     | dtype   | description   |
|:---------------|:--------|:--------------|
| c_gene         | text    | Gene          |
| c_gene_name    | text    | Gene name     |
| c_brain_region | text    | Brain region  |
| c_tpm          | decimal | TPM           |
| c_ptpm         | decimal | pTPM          |
| c_ntpm         | decimal |



## 16 rna_pig_brain_sample_hpa

| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
| c_enssscg_id  | text    | ENSSSCG_ID    |
| c_main_region | text    | Main_region   |
| c_subregion   | text    | Subregion     |
| c_animal      | text    | Animal        |
| c_tpm         | decimal | TPM           |
| c_ptpm        | decimal | pTPM          |
| c_ntpm        | decimal | nTPM          |

## 17 rna_mouse_brain_hpa

| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
|c_gene	|text|	Gene|
|c_gene_name|	text|	Gene name|
|c_brain_region|	text|	Brain region|
|c_tpm	|decimal|	TPM|
|c_ptpm	|decimal|	pTPM|
|c_ntpm	|decimal|	nTPM|

## 18 rna_mouse_brain_sample_hpa

| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
| c_ensmusg_id  | text    | ENSMUSG_ID    |
| c_main_region | text    | Main_region   |
| c_subregion   | text    | Subregion     |
| c_animal      | text    | Animal        |
| c_tpm         | decimal | TPM           |
| c_ptpm        | decimal | pTPM          |
| c_ntpm        | decimal | nTPM          |


## 18 rna_mouse_brain_mouse_sample

| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
| c_ensmusg_id  | text    | ENSMUSG ID    |
| c_main_region | text    | Main region   |
| c_subregion   | text    | Subregion     |
| c_animal      | text    | Animal        |
| c_tpm         | decimal | TPM           |
| c_ptpm        | decimal | pTPM          |

## 19 rna_mouse_brain_allen
| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
|c_gene	|text|	Gene|
|c_gene_name|	text|	Gene name|
|c_brain_region	|text|	Brain region|
|c_expression_energy|	decimal	|Expression energy|

## 20 rna_immune_cell

| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
|c_gene	|text|Gene|
|c_gene_name|	text|	Gene name|
|c_immune_cell|	text|	Immune cell|
|c_tpm	|decimal|	TPM|
|c_ptpm	|decimal|	pTPM|
|c_ntpm|	decimal|	nTPM|


## 21 rna_immune_cell_sample

| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
| c_sample_id   | decimal | Sample ID     |
| c_donor       | text    | Donor         |
| c_immune_cell | text    | Immune cell   |
| c_ensg_id     | text    | ENSG ID       |
| c_gene_name   | text    | Gene name     |
| c_tpm         | decimal | TPM           |
| c_ptpm        | decimal | pTPM          |
| c_ntpm        | decimal | nTPM          |

## 22 rna_immune_cell_monaco
| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
|c_gene|	text|	Gene|
|c_gene_name|	text|	Gene name|
|c_immune_cell|	text|	Immune cell|
|c_tpm|	decimal|	TPM|
|c_ptpm|	decimal|	pTPM|

## 23 rna_immune_cell_schmiedel
| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
|c_gene	|text|	Gene|
|c_gene_name|	text|	Gene name|
|c_immune_cell|	text|	Immune cell|
|c_tpm	|decimal|	TPM|

## 24 rna_celline_cancer
| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
|c_gene	|text|	Gene|
|c_gene_name|	text|	Gene name|
|c_cancer|	text|	Cancer|
|c_tpm	|decimal|	TPM|
|c_ptpm	|decimal|	pTPM|
|c_ntpm	|decimal|	nTPM|

## 25 rna_celline
| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
|c_gene	|text|	Gene|
|c_gene_name|	text|	Gene name|
|c_cell_line|	text|	Cell line|
|c_tpm|	decimal|	TPM|
|c_ptpm|	decimal	|pTPM|
|c_ntpm	|decimal|	nTPM|

## 26 ran_cancer_sample
| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
|c_gene|	text|	Gene|
|c_sample	|text|	Sample|
|c_cancer|	text|	Cancer|
|c_fpkm	|decimal|	FPKM|

## 27 transcript_rna_pigbrain

| Unnamed: 0                             | dtype   | description                          |
|:---------------------------------------|:--------|:-------------------------------------|
| c_ensgid                               | text    | ensgid                               |
| c_enstid                               | text    | enstid                               |
| c_tpm_amygdala_1052                    | decimal | TPM.amygdala.1052                    |
| c_est_counts_amygdala_1052             | decimal | est_counts.amygdala.1052             |
| c_tpm_amygdala_1086                    | decimal | TPM.amygdala.1086                    |
| c_est_counts_amygdala_1086             | decimal | est_counts.amygdala.1086             |
| c_tpm_amygdala_1122                    | decimal | TPM.amygdala.1122                    |
| c_est_counts_amygdala_1122             | decimal | est_counts.amygdala.1122             |
| c_tpm_amygdala_1159                    | decimal | TPM.amygdala.1159                    |
| c_est_counts_amygdala_1159             | decimal | est_counts.amygdala.1159             |
| c_tpm_caudate_1064                     | decimal | TPM.caudate.1064                     |
| c_est_counts_caudate_1064              | decimal | est_counts.caudate.1064              |
| c_tpm_caudate_1099                     | decimal | TPM.caudate.1099                     |
| c_est_counts_caudate_1099              | decimal | est_counts.caudate.1099              |
| c_tpm_caudate_1135                     | decimal | TPM.caudate.1135                     |
| c_est_counts_caudate_1135              | decimal | est_counts.caudate.1135              |
| c_tpm_caudate_1172                     | decimal | TPM.caudate.1172                     |
| c_est_counts_caudate_1172              | decimal | est_counts.caudate.1172              |
| c_tpm_cerebellum_1062                  | decimal | TPM.cerebellum.1062                  |
| c_est_counts_cerebellum_1062           | decimal | est_counts.cerebellum.1062           |
| c_tpm_cerebellum_1097                  | decimal | TPM.cerebellum.1097                  |
| c_est_counts_cerebellum_1097           | decimal | est_counts.cerebellum.1097           |
| c_tpm_cerebellum_1133                  | decimal | TPM.cerebellum.1133                  |
| c_est_counts_cerebellum_1133           | decimal | est_counts.cerebellum.1133           |
| c_tpm_cerebellum_1170                  | decimal | TPM.cerebellum.1170                  |
| c_est_counts_cerebellum_1170           | decimal | est_counts.cerebellum.1170           |
| c_tpm_choroid_plexus_1063              | decimal | TPM.choroid plexus.1063              |
| c_est_counts_choroid_plexus_1063       | decimal | est_counts.choroid plexus.1063       |
| c_tpm_choroid_plexus_1098              | decimal | TPM.choroid plexus.1098              |
| c_est_counts_choroid_plexus_1098       | decimal | est_counts.choroid plexus.1098       |
| c_tpm_choroid_plexus_1134              | decimal | TPM.choroid plexus.1134              |
| c_est_counts_choroid_plexus_1134       | decimal | est_counts.choroid plexus.1134       |
| c_tpm_choroid_plexus_1171              | decimal | TPM.choroid plexus.1171              |
| c_est_counts_choroid_plexus_1171       | decimal | est_counts.choroid plexus.1171       |
| c_tpm_cingulate_cortex_1053            | decimal | TPM.cingulate cortex.1053            |
| c_est_counts_cingulate_cortex_1053     | decimal | est_counts.cingulate cortex.1053     |
| c_tpm_cingulate_cortex_1087            | decimal | TPM.cingulate cortex.1087            |
| c_est_counts_cingulate_cortex_1087     | decimal | est_counts.cingulate cortex.1087     |
| c_tpm_cingulate_cortex_1123            | decimal | TPM.cingulate cortex.1123            |
| c_est_counts_cingulate_cortex_1123     | decimal | est_counts.cingulate cortex.1123     |
| c_tpm_cingulate_cortex_1160            | decimal | TPM.cingulate cortex.1160            |
| c_est_counts_cingulate_cortex_1160     | decimal | est_counts.cingulate cortex.1160     |
| c_tpm_cornea_1066                      | decimal | TPM.cornea.1066                      |
| c_est_counts_cornea_1066               | decimal | est_counts.cornea.1066               |
| c_tpm_cornea_1101                      | decimal | TPM.cornea.1101                      |
| c_est_counts_cornea_1101               | decimal | est_counts.cornea.1101               |
| c_tpm_cornea_1137                      | decimal | TPM.cornea.1137                      |
| c_est_counts_cornea_1137               | decimal | est_counts.cornea.1137               |
| c_tpm_cornea_1174                      | decimal | TPM.cornea.1174                      |
| c_est_counts_cornea_1174               | decimal | est_counts.cornea.1174               |
| c_tpm_corpus_callosum_1061             | decimal | TPM.corpus callosum.1061             |
| c_est_counts_corpus_callosum_1061      | decimal | est_counts.corpus callosum.1061      |
| c_tpm_corpus_callosum_1096             | decimal | TPM.corpus callosum.1096             |
| c_est_counts_corpus_callosum_1096      | decimal | est_counts.corpus callosum.1096      |
| c_tpm_corpus_callosum_1132             | decimal | TPM.corpus callosum.1132             |
| c_est_counts_corpus_callosum_1132      | decimal | est_counts.corpus callosum.1132      |
| c_tpm_corpus_callosum_1169             | decimal | TPM.corpus callosum.1169             |
| c_est_counts_corpus_callosum_1169      | decimal | est_counts.corpus callosum.1169      |
| c_tpm_dorsal_hippocampus__1069         | decimal | TPM.dorsal hippocampus .1069         |
| c_est_counts_dorsal_hippocampus__1069  | decimal | est_counts.dorsal hippocampus .1069  |
| c_tpm_dorsal_hippocampus__1104         | decimal | TPM.dorsal hippocampus .1104         |
| c_est_counts_dorsal_hippocampus__1104  | decimal | est_counts.dorsal hippocampus .1104  |
| c_tpm_dorsal_hippocampus__1140         | decimal | TPM.dorsal hippocampus .1140         |
| c_est_counts_dorsal_hippocampus__1140  | decimal | est_counts.dorsal hippocampus .1140  |
| c_tpm_dorsal_hippocampus__1177         | decimal | TPM.dorsal hippocampus .1177         |
| c_est_counts_dorsal_hippocampus__1177  | decimal | est_counts.dorsal hippocampus .1177  |
| c_tpm_dorsal_spinal_cord_1079          | decimal | TPM.dorsal spinal cord.1079          |
| c_est_counts_dorsal_spinal_cord_1079   | decimal | est_counts.dorsal spinal cord.1079   |
| c_tpm_dorsal_spinal_cord_1115          | decimal | TPM.dorsal spinal cord.1115          |
| c_est_counts_dorsal_spinal_cord_1115   | decimal | est_counts.dorsal spinal cord.1115   |
| c_tpm_dorsal_spinal_cord_1152          | decimal | TPM.dorsal spinal cord.1152          |
| c_est_counts_dorsal_spinal_cord_1152   | decimal | est_counts.dorsal spinal cord.1152   |
| c_tpm_dorsal_spinal_cord_1188          | decimal | TPM.dorsal spinal cord.1188          |
| c_est_counts_dorsal_spinal_cord_1188   | decimal | est_counts.dorsal spinal cord.1188   |
| c_tpm_dura_mater_1065                  | decimal | TPM.dura mater.1065                  |
| c_est_counts_dura_mater_1065           | decimal | est_counts.dura mater.1065           |
| c_tpm_dura_mater_1100                  | decimal | TPM.dura mater.1100                  |
| c_est_counts_dura_mater_1100           | decimal | est_counts.dura mater.1100           |
| c_tpm_dura_mater_1136                  | decimal | TPM.dura mater.1136                  |
| c_est_counts_dura_mater_1136           | decimal | est_counts.dura mater.1136           |
| c_tpm_dura_mater_1173                  | decimal | TPM.dura mater.1173                  |
| c_est_counts_dura_mater_1173           | decimal | est_counts.dura mater.1173           |
| c_tpm_entorhinal_cortex_1054           | decimal | TPM.entorhinal cortex.1054           |
| c_est_counts_entorhinal_cortex_1054    | decimal | est_counts.entorhinal cortex.1054    |
| c_tpm_entorhinal_cortex_1088           | decimal | TPM.entorhinal cortex.1088           |
| c_est_counts_entorhinal_cortex_1088    | decimal | est_counts.entorhinal cortex.1088    |
| c_tpm_entorhinal_cortex_1124           | decimal | TPM.entorhinal cortex.1124           |
| c_est_counts_entorhinal_cortex_1124    | decimal | est_counts.entorhinal cortex.1124    |
| c_tpm_entorhinal_cortex_1161           | decimal | TPM.entorhinal cortex.1161           |
| c_est_counts_entorhinal_cortex_1161    | decimal | est_counts.entorhinal cortex.1161    |
| c_tpm_hypothalamus_1071                | decimal | TPM.hypothalamus.1071                |
| c_est_counts_hypothalamus_1071         | decimal | est_counts.hypothalamus.1071         |
| c_tpm_hypothalamus_1106                | decimal | TPM.hypothalamus.1106                |
| c_est_counts_hypothalamus_1106         | decimal | est_counts.hypothalamus.1106         |
| c_tpm_hypothalamus_1142                | decimal | TPM.hypothalamus.1142                |
| c_est_counts_hypothalamus_1142         | decimal | est_counts.hypothalamus.1142         |
| c_tpm_hypothalamus_1179                | decimal | TPM.hypothalamus.1179                |
| c_est_counts_hypothalamus_1179         | decimal | est_counts.hypothalamus.1179         |
| c_tpm_insular_cortex_1055              | decimal | TPM.insular cortex.1055              |
| c_est_counts_insular_cortex_1055       | decimal | est_counts.insular cortex.1055       |
| c_tpm_insular_cortex_1089              | decimal | TPM.insular cortex.1089              |
| c_est_counts_insular_cortex_1089       | decimal | est_counts.insular cortex.1089       |
| c_tpm_insular_cortex_1125              | decimal | TPM.insular cortex.1125              |
| c_est_counts_insular_cortex_1125       | decimal | est_counts.insular cortex.1125       |
| c_tpm_insular_cortex_1162              | decimal | TPM.insular cortex.1162              |
| c_est_counts_insular_cortex_1162       | decimal | est_counts.insular cortex.1162       |
| c_tpm_lens_1067                        | decimal | TPM.lens.1067                        |
| c_est_counts_lens_1067                 | decimal | est_counts.lens.1067                 |
| c_tpm_lens_1102                        | decimal | TPM.lens.1102                        |
| c_est_counts_lens_1102                 | decimal | est_counts.lens.1102                 |
| c_tpm_lens_1138                        | decimal | TPM.lens.1138                        |
| c_est_counts_lens_1138                 | decimal | est_counts.lens.1138                 |
| c_tpm_lens_1175                        | decimal | TPM.lens.1175                        |
| c_est_counts_lens_1175                 | decimal | est_counts.lens.1175                 |
| c_tpm_medulla_oblongata_1072           | decimal | TPM.medulla oblongata.1072           |
| c_est_counts_medulla_oblongata_1072    | decimal | est_counts.medulla oblongata.1072    |
| c_tpm_medulla_oblongata_1107           | decimal | TPM.medulla oblongata.1107           |
| c_est_counts_medulla_oblongata_1107    | decimal | est_counts.medulla oblongata.1107    |
| c_tpm_medulla_oblongata_1143           | decimal | TPM.medulla oblongata.1143           |
| c_est_counts_medulla_oblongata_1143    | decimal | est_counts.medulla oblongata.1143    |
| c_tpm_medulla_oblongata_1180           | decimal | TPM.medulla oblongata.1180           |
| c_est_counts_medulla_oblongata_1180    | decimal | est_counts.medulla oblongata.1180    |
| c_tpm_midbrain_1073                    | decimal | TPM.midbrain.1073                    |
| c_est_counts_midbrain_1073             | decimal | est_counts.midbrain.1073             |
| c_tpm_midbrain_1108                    | decimal | TPM.midbrain.1108                    |
| c_est_counts_midbrain_1108             | decimal | est_counts.midbrain.1108             |
| c_tpm_midbrain_1144                    | decimal | TPM.midbrain.1144                    |
| c_est_counts_midbrain_1144             | decimal | est_counts.midbrain.1144             |
| c_tpm_midbrain_1181                    | decimal | TPM.midbrain.1181                    |
| c_est_counts_midbrain_1181             | decimal | est_counts.midbrain.1181             |
| c_tpm_motor_cortex_1056                | decimal | TPM.motor cortex.1056                |
| c_est_counts_motor_cortex_1056         | decimal | est_counts.motor cortex.1056         |
| c_tpm_motor_cortex_1090                | decimal | TPM.motor cortex.1090                |
| c_est_counts_motor_cortex_1090         | decimal | est_counts.motor cortex.1090         |
| c_tpm_motor_cortex_1126                | decimal | TPM.motor cortex.1126                |
| c_est_counts_motor_cortex_1126         | decimal | est_counts.motor cortex.1126         |
| c_tpm_motor_cortex_1163                | decimal | TPM.motor cortex.1163                |
| c_est_counts_motor_cortex_1163         | decimal | est_counts.motor cortex.1163         |
| c_tpm_occipital_cortex_1057            | decimal | TPM.occipital cortex.1057            |
| c_est_counts_occipital_cortex_1057     | decimal | est_counts.occipital cortex.1057     |
| c_tpm_occipital_cortex_1091            | decimal | TPM.occipital cortex.1091            |
| c_est_counts_occipital_cortex_1091     | decimal | est_counts.occipital cortex.1091     |
| c_tpm_occipital_cortex_1127            | decimal | TPM.occipital cortex.1127            |
| c_est_counts_occipital_cortex_1127     | decimal | est_counts.occipital cortex.1127     |
| c_tpm_occipital_cortex_1164            | decimal | TPM.occipital cortex.1164            |
| c_est_counts_occipital_cortex_1164     | decimal | est_counts.occipital cortex.1164     |
| c_tpm_olfactory_bulb_1074              | decimal | TPM.olfactory bulb.1074              |
| c_est_counts_olfactory_bulb_1074       | decimal | est_counts.olfactory bulb.1074       |
| c_tpm_olfactory_bulb_1109              | decimal | TPM.olfactory bulb.1109              |
| c_est_counts_olfactory_bulb_1109       | decimal | est_counts.olfactory bulb.1109       |
| c_tpm_olfactory_bulb_1195              | decimal | TPM.olfactory bulb.1195              |
| c_est_counts_olfactory_bulb_1195       | decimal | est_counts.olfactory bulb.1195       |
| c_tpm_olfactory_bulb_1145              | decimal | TPM.olfactory bulb.1145              |
| c_est_counts_olfactory_bulb_1145       | decimal | est_counts.olfactory bulb.1145       |
| c_tpm_olfactory_bulb_1182              | decimal | TPM.olfactory bulb.1182              |
| c_est_counts_olfactory_bulb_1182       | decimal | est_counts.olfactory bulb.1182       |
| c_tpm_periaqueductal_gray_1110         | decimal | TPM.periaqueductal gray.1110         |
| c_est_counts_periaqueductal_gray_1110  | decimal | est_counts.periaqueductal gray.1110  |
| c_tpm_periaqueductal_gray_1146         | decimal | TPM.periaqueductal gray.1146         |
| c_est_counts_periaqueductal_gray_1146  | decimal | est_counts.periaqueductal gray.1146  |
| c_tpm_periaqueductal_gray_1183         | decimal | TPM.periaqueductal gray.1183         |
| c_est_counts_periaqueductal_gray_1183  | decimal | est_counts.periaqueductal gray.1183  |
| c_tpm_pineal_gland_1147                | decimal | TPM.pineal gland.1147                |
| c_est_counts_pineal_gland_1147         | decimal | est_counts.pineal gland.1147         |
| c_tpm_pituitary_gland_1075             | decimal | TPM.pituitary gland.1075             |
| c_est_counts_pituitary_gland_1075      | decimal | est_counts.pituitary gland.1075      |
| c_tpm_pituitary_gland_1111             | decimal | TPM.pituitary gland.1111             |
| c_est_counts_pituitary_gland_1111      | decimal | est_counts.pituitary gland.1111      |
| c_tpm_pituitary_gland_1148             | decimal | TPM.pituitary gland.1148             |
| c_est_counts_pituitary_gland_1148      | decimal | est_counts.pituitary gland.1148      |
| c_tpm_pituitary_gland_1184             | decimal | TPM.pituitary gland.1184             |
| c_est_counts_pituitary_gland_1184      | decimal | est_counts.pituitary gland.1184      |
| c_tpm_pons_1076                        | decimal | TPM.pons.1076                        |
| c_est_counts_pons_1076                 | decimal | est_counts.pons.1076                 |
| c_tpm_pons_1112                        | decimal | TPM.pons.1112                        |
| c_est_counts_pons_1112                 | decimal | est_counts.pons.1112                 |
| c_tpm_pons_1149                        | decimal | TPM.pons.1149                        |
| c_est_counts_pons_1149                 | decimal | est_counts.pons.1149                 |
| c_tpm_pons_1185                        | decimal | TPM.pons.1185                        |
| c_est_counts_pons_1185                 | decimal | est_counts.pons.1185                 |
| c_tpm_prefrontal_cortex_1058           | decimal | TPM.prefrontal cortex.1058           |
| c_est_counts_prefrontal_cortex_1058    | decimal | est_counts.prefrontal cortex.1058    |
| c_tpm_prefrontal_cortex_1092           | decimal | TPM.prefrontal cortex.1092           |
| c_est_counts_prefrontal_cortex_1092    | decimal | est_counts.prefrontal cortex.1092    |
| c_tpm_prefrontal_cortex_1128           | decimal | TPM.prefrontal cortex.1128           |
| c_est_counts_prefrontal_cortex_1128    | decimal | est_counts.prefrontal cortex.1128    |
| c_tpm_prefrontal_cortex_1165           | decimal | TPM.prefrontal cortex.1165           |
| c_est_counts_prefrontal_cortex_1165    | decimal | est_counts.prefrontal cortex.1165    |
| c_tpm_putamen_1077                     | decimal | TPM.putamen.1077                     |
| c_est_counts_putamen_1077              | decimal | est_counts.putamen.1077              |
| c_tpm_putamen_1113                     | decimal | TPM.putamen.1113                     |
| c_est_counts_putamen_1113              | decimal | est_counts.putamen.1113              |
| c_tpm_putamen_1150                     | decimal | TPM.putamen.1150                     |
| c_est_counts_putamen_1150              | decimal | est_counts.putamen.1150              |
| c_tpm_putamen_1186                     | decimal | TPM.putamen.1186                     |
| c_est_counts_putamen_1186              | decimal | est_counts.putamen.1186              |
| c_tpm_retina_1068                      | decimal | TPM.retina.1068                      |
| c_est_counts_retina_1068               | decimal | est_counts.retina.1068               |
| c_tpm_retina_1103                      | decimal | TPM.retina.1103                      |
| c_est_counts_retina_1103               | decimal | est_counts.retina.1103               |
| c_tpm_retina_1139                      | decimal | TPM.retina.1139                      |
| c_est_counts_retina_1139               | decimal | est_counts.retina.1139               |
| c_tpm_retina_1176                      | decimal | TPM.retina.1176                      |
| c_est_counts_retina_1176               | decimal | est_counts.retina.1176               |
| c_tpm_retrosplenial_cortex_1059        | decimal | TPM.retrosplenial cortex.1059        |
| c_est_counts_retrosplenial_cortex_1059 | decimal | est_counts.retrosplenial cortex.1059 |
| c_tpm_retrosplenial_cortex_1093        | decimal | TPM.retrosplenial cortex.1093        |
| c_est_counts_retrosplenial_cortex_1093 | decimal | est_counts.retrosplenial cortex.1093 |
| c_tpm_retrosplenial_cortex_1129        | decimal | TPM.retrosplenial cortex.1129        |
| c_est_counts_retrosplenial_cortex_1129 | decimal | est_counts.retrosplenial cortex.1129 |
| c_tpm_retrosplenial_cortex_1166        | decimal | TPM.retrosplenial cortex.1166        |
| c_est_counts_retrosplenial_cortex_1166 | decimal | est_counts.retrosplenial cortex.1166 |
| c_tpm_septum_1081                      | decimal | TPM.septum.1081                      |
| c_est_counts_septum_1081               | decimal | est_counts.septum.1081               |
| c_tpm_septum_1117                      | decimal | TPM.septum.1117                      |
| c_est_counts_septum_1117               | decimal | est_counts.septum.1117               |
| c_tpm_septum_1154                      | decimal | TPM.septum.1154                      |
| c_est_counts_septum_1154               | decimal | est_counts.septum.1154               |
| c_tpm_septum_1190                      | decimal | TPM.septum.1190                      |
| c_est_counts_septum_1190               | decimal | est_counts.septum.1190               |
| c_tpm_somatosensory_cortex_1094        | decimal | TPM.somatosensory cortex.1094        |
| c_est_counts_somatosensory_cortex_1094 | decimal | est_counts.somatosensory cortex.1094 |
| c_tpm_somatosensory_cortex_1130        | decimal | TPM.somatosensory cortex.1130        |
| c_est_counts_somatosensory_cortex_1130 | decimal | est_counts.somatosensory cortex.1130 |
| c_tpm_somatosensory_cortex_1167        | decimal | TPM.somatosensory cortex.1167        |
| c_est_counts_somatosensory_cortex_1167 | decimal | est_counts.somatosensory cortex.1167 |
| c_tpm_subiculum_1083                   | decimal | TPM.subiculum.1083                   |
| c_est_counts_subiculum_1083            | decimal | est_counts.subiculum.1083            |
| c_tpm_subiculum_1119                   | decimal | TPM.subiculum.1119                   |
| c_est_counts_subiculum_1119            | decimal | est_counts.subiculum.1119            |
| c_tpm_subiculum_1156                   | decimal | TPM.subiculum.1156                   |
| c_est_counts_subiculum_1156            | decimal | est_counts.subiculum.1156            |
| c_tpm_subiculum_1192                   | decimal | TPM.subiculum.1192                   |
| c_est_counts_subiculum_1192            | decimal | est_counts.subiculum.1192            |
| c_tpm_substantia_nigra_1082            | decimal | TPM.substantia nigra.1082            |
| c_est_counts_substantia_nigra_1082     | decimal | est_counts.substantia nigra.1082     |
| c_tpm_substantia_nigra_1118            | decimal | TPM.substantia nigra.1118            |
| c_est_counts_substantia_nigra_1118     | decimal | est_counts.substantia nigra.1118     |
| c_tpm_substantia_nigra_1155            | decimal | TPM.substantia nigra.1155            |
| c_est_counts_substantia_nigra_1155     | decimal | est_counts.substantia nigra.1155     |
| c_tpm_substantia_nigra_1191            | decimal | TPM.substantia nigra.1191            |
| c_est_counts_substantia_nigra_1191     | decimal | est_counts.substantia nigra.1191     |
| c_tpm_superior_colliculi_1078          | decimal | TPM.superior colliculi.1078          |
| c_est_counts_superior_colliculi_1078   | decimal | est_counts.superior colliculi.1078   |
| c_tpm_superior_colliculi_1114          | decimal | TPM.superior colliculi.1114          |
| c_est_counts_superior_colliculi_1114   | decimal | est_counts.superior colliculi.1114   |
| c_tpm_superior_colliculi_1151          | decimal | TPM.superior colliculi.1151          |
| c_est_counts_superior_colliculi_1151   | decimal | est_counts.superior colliculi.1151   |
| c_tpm_superior_colliculi_1187          | decimal | TPM.superior colliculi.1187          |
| c_est_counts_superior_colliculi_1187   | decimal | est_counts.superior colliculi.1187   |
| c_tpm_temporal_cortex_1060             | decimal | TPM.temporal cortex.1060             |
| c_est_counts_temporal_cortex_1060      | decimal | est_counts.temporal cortex.1060      |
| c_tpm_temporal_cortex_1095             | decimal | TPM.temporal cortex.1095             |
| c_est_counts_temporal_cortex_1095      | decimal | est_counts.temporal cortex.1095      |
| c_tpm_temporal_cortex_1131             | decimal | TPM.temporal cortex.1131             |
| c_est_counts_temporal_cortex_1131      | decimal | est_counts.temporal cortex.1131      |
| c_tpm_temporal_cortex_1168             | decimal | TPM.temporal cortex.1168             |
| c_est_counts_temporal_cortex_1168      | decimal | est_counts.temporal cortex.1168      |
| c_tpm_thalamus_1084                    | decimal | TPM.thalamus.1084                    |
| c_est_counts_thalamus_1084             | decimal | est_counts.thalamus.1084             |
| c_tpm_thalamus_1120                    | decimal | TPM.thalamus.1120                    |
| c_est_counts_thalamus_1120             | decimal | est_counts.thalamus.1120             |
| c_tpm_thalamus_1157                    | decimal | TPM.thalamus.1157                    |
| c_est_counts_thalamus_1157             | decimal | est_counts.thalamus.1157             |
| c_tpm_thalamus_1193                    | decimal | TPM.thalamus.1193                    |
| c_est_counts_thalamus_1193             | decimal | est_counts.thalamus.1193             |
| c_tpm_ventral_hippocampus__1070        | decimal | TPM.ventral hippocampus .1070        |
| c_est_counts_ventral_hippocampus__1070 | decimal | est_counts.ventral hippocampus .1070 |
| c_tpm_ventral_hippocampus__1105        | decimal | TPM.ventral hippocampus .1105        |
| c_est_counts_ventral_hippocampus__1105 | decimal | est_counts.ventral hippocampus .1105 |
| c_tpm_ventral_hippocampus__1141        | decimal | TPM.ventral hippocampus .1141        |
| c_est_counts_ventral_hippocampus__1141 | decimal | est_counts.ventral hippocampus .1141 |
| c_tpm_ventral_hippocampus__1178        | decimal | TPM.ventral hippocampus .1178        |
| c_est_counts_ventral_hippocampus__1178 | decimal | est_counts.ventral hippocampus .1178 |
| c_tpm_ventral_pallidum_1085            | decimal | TPM.ventral pallidum.1085            |
| c_est_counts_ventral_pallidum_1085     | decimal | est_counts.ventral pallidum.1085     |
| c_tpm_ventral_pallidum_1121            | decimal | TPM.ventral pallidum.1121            |
| c_est_counts_ventral_pallidum_1121     | decimal | est_counts.ventral pallidum.1121     |
| c_tpm_ventral_pallidum_1158            | decimal | TPM.ventral pallidum.1158            |
| c_est_counts_ventral_pallidum_1158     | decimal | est_counts.ventral pallidum.1158     |
| c_tpm_ventral_pallidum_1194            | decimal | TPM.ventral pallidum.1194            |
| c_est_counts_ventral_pallidum_1194     | decimal | est_counts.ventral pallidum.1194     |
| c_tpm_ventral_spinal_cord_1080         | decimal | TPM.ventral spinal cord.1080         |
| c_est_counts_ventral_spinal_cord_1080  | decimal | est_counts.ventral spinal cord.1080  |
| c_tpm_ventral_spinal_cord_1116         | decimal | TPM.ventral spinal cord.1116         |
| c_est_counts_ventral_spinal_cord_1116  | decimal | est_counts.ventral spinal cord.1116  |
| c_tpm_ventral_spinal_cord_1153         | decimal | TPM.ventral spinal cord.1153         |
| c_est_counts_ventral_spinal_cord_1153  | decimal | est_counts.ventral spinal cord.1153  |
| c_tpm_ventral_spinal_cord_1189         | decimal | TPM.ventral spinal cord.1189         |
| c_est_counts_ventral_spinal_cord_1189  | decimal | est_counts.ventral spinal cord.1189  |


## 27 rna_pigbrain_pig_sample

| Unnamed: 0    | dtype   | description   |
|:--------------|:--------|:--------------|
| c_ensmusg_id  | text    | ENSMUSG ID    |
| c_main_region | text    | Main region   |
| c_subregion   | text    | Subregion     |
| c_animal      | text    | Animal        |
| c_tpm         | decimal | TPM           |
| c_ptpm        | decimal | pTPM          |

## 27 transcript_rna_tissue
| Unnamed: 0                          | dtype   | description                       |
|:------------------------------------|:--------|:----------------------------------|
| c_ensgid                            | text    | ensgid                            |
| c_enstid                            | text    | enstid                            |
| c_tpm_adipose_tissue_86             | decimal | TPM.adipose tissue.86             |
| c_est_counts_adipose_tissue_86      | decimal | est_counts.adipose tissue.86      |
| c_tpm_adipose_tissue_137            | decimal | TPM.adipose tissue.137            |
| c_est_counts_adipose_tissue_137     | decimal | est_counts.adipose tissue.137     |
| c_tpm_adipose_tissue_115            | decimal | TPM.adipose tissue.115            |
| c_est_counts_adipose_tissue_115     | decimal | est_counts.adipose tissue.115     |
| c_tpm_adipose_tissue_329            | decimal | TPM.adipose tissue.329            |
| c_est_counts_adipose_tissue_329     | decimal | est_counts.adipose tissue.329     |
| c_tpm_adipose_tissue_331            | decimal | TPM.adipose tissue.331            |
| c_est_counts_adipose_tissue_331     | decimal | est_counts.adipose tissue.331     |
| c_tpm_adrenal_gland_87              | decimal | TPM.adrenal gland.87              |
| c_est_counts_adrenal_gland_87       | decimal | est_counts.adrenal gland.87       |
| c_tpm_adrenal_gland_88              | decimal | TPM.adrenal gland.88              |
| c_est_counts_adrenal_gland_88       | decimal | est_counts.adrenal gland.88       |
| c_tpm_adrenal_gland_89              | decimal | TPM.adrenal gland.89              |
| c_est_counts_adrenal_gland_89       | decimal | est_counts.adrenal gland.89       |
| c_tpm_appendix_92                   | decimal | TPM.appendix.92                   |
| c_est_counts_appendix_92            | decimal | est_counts.appendix.92            |
| c_tpm_appendix_93                   | decimal | TPM.appendix.93                   |
| c_est_counts_appendix_93            | decimal | est_counts.appendix.93            |
| c_tpm_appendix_94                   | decimal | TPM.appendix.94                   |
| c_est_counts_appendix_94            | decimal | est_counts.appendix.94            |
| c_tpm_bone_marrow_97                | decimal | TPM.bone marrow.97                |
| c_est_counts_bone_marrow_97         | decimal | est_counts.bone marrow.97         |
| c_tpm_bone_marrow_98                | decimal | TPM.bone marrow.98                |
| c_est_counts_bone_marrow_98         | decimal | est_counts.bone marrow.98         |
| c_tpm_bone_marrow_99                | decimal | TPM.bone marrow.99                |
| c_est_counts_bone_marrow_99         | decimal | est_counts.bone marrow.99         |
| c_tpm_bone_marrow_100               | decimal | TPM.bone marrow.100               |
| c_est_counts_bone_marrow_100        | decimal | est_counts.bone marrow.100        |
| c_tpm_breast_390                    | decimal | TPM.breast.390                    |
| c_est_counts_breast_390             | decimal | est_counts.breast.390             |
| c_tpm_breast_405                    | decimal | TPM.breast.405                    |
| c_est_counts_breast_405             | decimal | est_counts.breast.405             |
| c_tpm_breast_373                    | decimal | TPM.breast.373                    |
| c_est_counts_breast_373             | decimal | est_counts.breast.373             |
| c_tpm_breast_410                    | decimal | TPM.breast.410                    |
| c_est_counts_breast_410             | decimal | est_counts.breast.410             |
| c_tpm_cerebral_cortex_105           | decimal | TPM.cerebral cortex.105           |
| c_est_counts_cerebral_cortex_105    | decimal | est_counts.cerebral cortex.105    |
| c_tpm_cerebral_cortex_106           | decimal | TPM.cerebral cortex.106           |
| c_est_counts_cerebral_cortex_106    | decimal | est_counts.cerebral cortex.106    |
| c_tpm_cerebral_cortex_48            | decimal | TPM.cerebral cortex.48            |
| c_est_counts_cerebral_cortex_48     | decimal | est_counts.cerebral cortex.48     |
| c_tpm_cervix_383                    | decimal | TPM.cervix.383                    |
| c_est_counts_cervix_383             | decimal | est_counts.cervix.383             |
| c_tpm_cervix_374                    | decimal | TPM.cervix.374                    |
| c_est_counts_cervix_374             | decimal | est_counts.cervix.374             |
| c_tpm_choroid_plexus_3667           | decimal | TPM.choroid plexus.3667           |
| c_est_counts_choroid_plexus_3667    | decimal | est_counts.choroid plexus.3667    |
| c_tpm_choroid_plexus_3666           | decimal | TPM.choroid plexus.3666           |
| c_est_counts_choroid_plexus_3666    | decimal | est_counts.choroid plexus.3666    |
| c_tpm_colon_67                      | decimal | TPM.colon.67                      |
| c_est_counts_colon_67               | decimal | est_counts.colon.67               |
| c_tpm_colon_76                      | decimal | TPM.colon.76                      |
| c_est_counts_colon_76               | decimal | est_counts.colon.76               |
| c_tpm_colon_68                      | decimal | TPM.colon.68                      |
| c_est_counts_colon_68               | decimal | est_counts.colon.68               |
| c_tpm_colon_69                      | decimal | TPM.colon.69                      |
| c_est_counts_colon_69               | decimal | est_counts.colon.69               |
| c_tpm_colon_70                      | decimal | TPM.colon.70                      |
| c_est_counts_colon_70               | decimal | est_counts.colon.70               |
| c_tpm_colon_299                     | decimal | TPM.colon.299                     |
| c_est_counts_colon_299              | decimal | est_counts.colon.299              |
| c_tpm_colon_300                     | decimal | TPM.colon.300                     |
| c_est_counts_colon_300              | decimal | est_counts.colon.300              |
| c_tpm_colon_391                     | decimal | TPM.colon.391                     |
| c_est_counts_colon_391              | decimal | est_counts.colon.391              |
| c_tpm_colon_384                     | decimal | TPM.colon.384                     |
| c_est_counts_colon_384              | decimal | est_counts.colon.384              |
| c_tpm_colon_381                     | decimal | TPM.colon.381                     |
| c_est_counts_colon_381              | decimal | est_counts.colon.381              |
| c_tpm_colon_368                     | decimal | TPM.colon.368                     |
| c_est_counts_colon_368              | decimal | est_counts.colon.368              |
| c_tpm_colon_403                     | decimal | TPM.colon.403                     |
| c_est_counts_colon_403              | decimal | est_counts.colon.403              |
| c_tpm_colon_389                     | decimal | TPM.colon.389                     |
| c_est_counts_colon_389              | decimal | est_counts.colon.389              |
| c_tpm_duodenum_120                  | decimal | TPM.duodenum.120                  |
| c_est_counts_duodenum_120           | decimal | est_counts.duodenum.120           |
| c_tpm_duodenum_121                  | decimal | TPM.duodenum.121                  |
| c_est_counts_duodenum_121           | decimal | est_counts.duodenum.121           |
| c_tpm_endometrium_113               | decimal | TPM.endometrium.113               |
| c_est_counts_endometrium_113        | decimal | est_counts.endometrium.113        |
| c_tpm_endometrium_114               | decimal | TPM.endometrium.114               |
| c_est_counts_endometrium_114        | decimal | est_counts.endometrium.114        |
| c_tpm_endometrium_268               | decimal | TPM.endometrium.268               |
| c_est_counts_endometrium_268        | decimal | est_counts.endometrium.268        |
| c_tpm_endometrium_297               | decimal | TPM.endometrium.297               |
| c_est_counts_endometrium_297        | decimal | est_counts.endometrium.297        |
| c_tpm_endometrium_301               | decimal | TPM.endometrium.301               |
| c_est_counts_endometrium_301        | decimal | est_counts.endometrium.301        |
| c_tpm_epididymis_407                | decimal | TPM.epididymis.407                |
| c_est_counts_epididymis_407         | decimal | est_counts.epididymis.407         |
| c_tpm_esophagus_130                 | decimal | TPM.esophagus.130                 |
| c_est_counts_esophagus_130          | decimal | est_counts.esophagus.130          |
| c_tpm_esophagus_131                 | decimal | TPM.esophagus.131                 |
| c_est_counts_esophagus_131          | decimal | est_counts.esophagus.131          |
| c_tpm_esophagus_132                 | decimal | TPM.esophagus.132                 |
| c_est_counts_esophagus_132          | decimal | est_counts.esophagus.132          |
| c_tpm_fallopian_tube_136            | decimal | TPM.fallopian tube.136            |
| c_est_counts_fallopian_tube_136     | decimal | est_counts.fallopian tube.136     |
| c_tpm_fallopian_tube_304            | decimal | TPM.fallopian tube.304            |
| c_est_counts_fallopian_tube_304     | decimal | est_counts.fallopian tube.304     |
| c_tpm_fallopian_tube_305            | decimal | TPM.fallopian tube.305            |
| c_est_counts_fallopian_tube_305     | decimal | est_counts.fallopian tube.305     |
| c_tpm_fallopian_tube_306            | decimal | TPM.fallopian tube.306            |
| c_est_counts_fallopian_tube_306     | decimal | est_counts.fallopian tube.306     |
| c_tpm_fallopian_tube_307            | decimal | TPM.fallopian tube.307            |
| c_est_counts_fallopian_tube_307     | decimal | est_counts.fallopian tube.307     |
| c_tpm_gallbladder_140               | decimal | TPM.gallbladder.140               |
| c_est_counts_gallbladder_140        | decimal | est_counts.gallbladder.140        |
| c_tpm_gallbladder_141               | decimal | TPM.gallbladder.141               |
| c_est_counts_gallbladder_141        | decimal | est_counts.gallbladder.141        |
| c_tpm_gallbladder_142               | decimal | TPM.gallbladder.142               |
| c_est_counts_gallbladder_142        | decimal | est_counts.gallbladder.142        |
| c_tpm_heart_muscle_149              | decimal | TPM.heart muscle.149              |
| c_est_counts_heart_muscle_149       | decimal | est_counts.heart muscle.149       |
| c_tpm_heart_muscle_150              | decimal | TPM.heart muscle.150              |
| c_est_counts_heart_muscle_150       | decimal | est_counts.heart muscle.150       |
| c_tpm_heart_muscle_151              | decimal | TPM.heart muscle.151              |
| c_est_counts_heart_muscle_151       | decimal | est_counts.heart muscle.151       |
| c_tpm_heart_muscle_152              | decimal | TPM.heart muscle.152              |
| c_est_counts_heart_muscle_152       | decimal | est_counts.heart muscle.152       |
| c_tpm_kidney_57                     | decimal | TPM.kidney.57                     |
| c_est_counts_kidney_57              | decimal | est_counts.kidney.57              |
| c_tpm_kidney_58                     | decimal | TPM.kidney.58                     |
| c_est_counts_kidney_58              | decimal | est_counts.kidney.58              |
| c_tpm_kidney_358                    | decimal | TPM.kidney.358                    |
| c_est_counts_kidney_358             | decimal | est_counts.kidney.358             |
| c_tpm_kidney_414                    | decimal | TPM.kidney.414                    |
| c_est_counts_kidney_414             | decimal | est_counts.kidney.414             |
| c_tpm_kidney_377                    | decimal | TPM.kidney.377                    |
| c_est_counts_kidney_377             | decimal | est_counts.kidney.377             |
| c_tpm_kidney_380                    | decimal | TPM.kidney.380                    |
| c_est_counts_kidney_380             | decimal | est_counts.kidney.380             |
| c_tpm_kidney_394                    | decimal | TPM.kidney.394                    |
| c_est_counts_kidney_394             | decimal | est_counts.kidney.394             |
| c_tpm_kidney_55                     | decimal | TPM.kidney.55                     |
| c_est_counts_kidney_55              | decimal | est_counts.kidney.55              |
| c_tpm_kidney_56                     | decimal | TPM.kidney.56                     |
| c_est_counts_kidney_56              | decimal | est_counts.kidney.56              |
| c_tpm_liver_21                      | decimal | TPM.liver.21                      |
| c_est_counts_liver_21               | decimal | est_counts.liver.21               |
| c_tpm_liver_23                      | decimal | TPM.liver.23                      |
| c_est_counts_liver_23               | decimal | est_counts.liver.23               |
| c_tpm_liver_24                      | decimal | TPM.liver.24                      |
| c_est_counts_liver_24               | decimal | est_counts.liver.24               |
| c_tpm_liver_350                     | decimal | TPM.liver.350                     |
| c_est_counts_liver_350              | decimal | est_counts.liver.350              |
| c_tpm_liver_351                     | decimal | TPM.liver.351                     |
| c_est_counts_liver_351              | decimal | est_counts.liver.351              |
| c_tpm_liver_352                     | decimal | TPM.liver.352                     |
| c_est_counts_liver_352              | decimal | est_counts.liver.352              |
| c_tpm_liver_353                     | decimal | TPM.liver.353                     |
| c_est_counts_liver_353              | decimal | est_counts.liver.353              |
| c_tpm_liver_396                     | decimal | TPM.liver.396                     |
| c_est_counts_liver_396              | decimal | est_counts.liver.396              |
| c_tpm_liver_367                     | decimal | TPM.liver.367                     |
| c_est_counts_liver_367              | decimal | est_counts.liver.367              |
| c_tpm_liver_359                     | decimal | TPM.liver.359                     |
| c_est_counts_liver_359              | decimal | est_counts.liver.359              |
| c_tpm_lung_166                      | decimal | TPM.lung.166                      |
| c_est_counts_lung_166               | decimal | est_counts.lung.166               |
| c_tpm_lung_167                      | decimal | TPM.lung.167                      |
| c_est_counts_lung_167               | decimal | est_counts.lung.167               |
| c_tpm_lung_168                      | decimal | TPM.lung.168                      |
| c_est_counts_lung_168               | decimal | est_counts.lung.168               |
| c_tpm_lung_379                      | decimal | TPM.lung.379                      |
| c_est_counts_lung_379               | decimal | est_counts.lung.379               |
| c_tpm_lung_376                      | decimal | TPM.lung.376                      |
| c_est_counts_lung_376               | decimal | est_counts.lung.376               |
| c_tpm_lung_406                      | decimal | TPM.lung.406                      |
| c_est_counts_lung_406               | decimal | est_counts.lung.406               |
| c_tpm_lung_387                      | decimal | TPM.lung.387                      |
| c_est_counts_lung_387               | decimal | est_counts.lung.387               |
| c_tpm_lung_164                      | decimal | TPM.lung.164                      |
| c_est_counts_lung_164               | decimal | est_counts.lung.164               |
| c_tpm_lung_165                      | decimal | TPM.lung.165                      |
| c_est_counts_lung_165               | decimal | est_counts.lung.165               |
| c_tpm_lymph_node_173                | decimal | TPM.lymph node.173                |
| c_est_counts_lymph_node_173         | decimal | est_counts.lymph node.173         |
| c_tpm_lymph_node_174                | decimal | TPM.lymph node.174                |
| c_est_counts_lymph_node_174         | decimal | est_counts.lymph node.174         |
| c_tpm_lymph_node_175                | decimal | TPM.lymph node.175                |
| c_est_counts_lymph_node_175         | decimal | est_counts.lymph node.175         |
| c_tpm_lymph_node_176                | decimal | TPM.lymph node.176                |
| c_est_counts_lymph_node_176         | decimal | est_counts.lymph node.176         |
| c_tpm_lymph_node_177                | decimal | TPM.lymph node.177                |
| c_est_counts_lymph_node_177         | decimal | est_counts.lymph node.177         |
| c_tpm_ovary_3662                    | decimal | TPM.ovary.3662                    |
| c_est_counts_ovary_3662             | decimal | est_counts.ovary.3662             |
| c_tpm_ovary_3663                    | decimal | TPM.ovary.3663                    |
| c_est_counts_ovary_3663             | decimal | est_counts.ovary.3663             |
| c_tpm_ovary_3664                    | decimal | TPM.ovary.3664                    |
| c_est_counts_ovary_3664             | decimal | est_counts.ovary.3664             |
| c_tpm_ovary_3665                    | decimal | TPM.ovary.3665                    |
| c_est_counts_ovary_3665             | decimal | est_counts.ovary.3665             |
| c_tpm_ovary_192                     | decimal | TPM.ovary.192                     |
| c_est_counts_ovary_192              | decimal | est_counts.ovary.192              |
| c_tpm_ovary_193                     | decimal | TPM.ovary.193                     |
| c_est_counts_ovary_193              | decimal | est_counts.ovary.193              |
| c_tpm_ovary_308                     | decimal | TPM.ovary.308                     |
| c_est_counts_ovary_308              | decimal | est_counts.ovary.308              |
| c_tpm_pancreas_194                  | decimal | TPM.pancreas.194                  |
| c_est_counts_pancreas_194           | decimal | est_counts.pancreas.194           |
| c_tpm_pancreas_195                  | decimal | TPM.pancreas.195                  |
| c_est_counts_pancreas_195           | decimal | est_counts.pancreas.195           |
| c_tpm_parathyroid_gland_393         | decimal | TPM.parathyroid gland.393         |
| c_est_counts_parathyroid_gland_393  | decimal | est_counts.parathyroid gland.393  |
| c_tpm_parathyroid_gland_1600        | decimal | TPM.parathyroid gland.1600        |
| c_est_counts_parathyroid_gland_1600 | decimal | est_counts.parathyroid gland.1600 |
| c_tpm_parathyroid_gland_1601        | decimal | TPM.parathyroid gland.1601        |
| c_est_counts_parathyroid_gland_1601 | decimal | est_counts.parathyroid gland.1601 |
| c_tpm_placenta_202                  | decimal | TPM.placenta.202                  |
| c_est_counts_placenta_202           | decimal | est_counts.placenta.202           |
| c_tpm_placenta_203                  | decimal | TPM.placenta.203                  |
| c_est_counts_placenta_203           | decimal | est_counts.placenta.203           |
| c_tpm_placenta_204                  | decimal | TPM.placenta.204                  |
| c_est_counts_placenta_204           | decimal | est_counts.placenta.204           |
| c_tpm_placenta_398                  | decimal | TPM.placenta.398                  |
| c_est_counts_placenta_398           | decimal | est_counts.placenta.398           |
| c_tpm_placenta_375                  | decimal | TPM.placenta.375                  |
| c_est_counts_placenta_375           | decimal | est_counts.placenta.375           |
| c_tpm_placenta_413                  | decimal | TPM.placenta.413                  |
| c_est_counts_placenta_413           | decimal | est_counts.placenta.413           |
| c_tpm_placenta_385                  | decimal | TPM.placenta.385                  |
| c_est_counts_placenta_385           | decimal | est_counts.placenta.385           |
| c_tpm_placenta_200                  | decimal | TPM.placenta.200                  |
| c_est_counts_placenta_200           | decimal | est_counts.placenta.200           |
| c_tpm_prostate_59                   | decimal | TPM.prostate.59                   |
| c_est_counts_prostate_59            | decimal | est_counts.prostate.59            |
| c_tpm_prostate_205                  | decimal | TPM.prostate.205                  |
| c_est_counts_prostate_205           | decimal | est_counts.prostate.205           |
| c_tpm_prostate_206                  | decimal | TPM.prostate.206                  |
| c_est_counts_prostate_206           | decimal | est_counts.prostate.206           |
| c_tpm_prostate_207                  | decimal | TPM.prostate.207                  |
| c_est_counts_prostate_207           | decimal | est_counts.prostate.207           |
| c_tpm_prostate_365                  | decimal | TPM.prostate.365                  |
| c_est_counts_prostate_365           | decimal | est_counts.prostate.365           |
| c_tpm_prostate_364                  | decimal | TPM.prostate.364                  |
| c_est_counts_prostate_364           | decimal | est_counts.prostate.364           |
| c_tpm_prostate_412                  | decimal | TPM.prostate.412                  |
| c_est_counts_prostate_412           | decimal | est_counts.prostate.412           |
| c_tpm_prostate_388                  | decimal | TPM.prostate.388                  |
| c_est_counts_prostate_388           | decimal | est_counts.prostate.388           |
| c_tpm_prostate_361                  | decimal | TPM.prostate.361                  |
| c_est_counts_prostate_361           | decimal | est_counts.prostate.361           |
| c_tpm_rectum_333                    | decimal | TPM.rectum.333                    |
| c_est_counts_rectum_333             | decimal | est_counts.rectum.333             |
| c_tpm_rectum_334                    | decimal | TPM.rectum.334                    |
| c_est_counts_rectum_334             | decimal | est_counts.rectum.334             |
| c_tpm_rectum_335                    | decimal | TPM.rectum.335                    |
| c_est_counts_rectum_335             | decimal | est_counts.rectum.335             |
| c_tpm_rectum_338                    | decimal | TPM.rectum.338                    |
| c_est_counts_rectum_338             | decimal | est_counts.rectum.338             |
| c_tpm_salivary_gland_216            | decimal | TPM.salivary gland.216            |
| c_est_counts_salivary_gland_216     | decimal | est_counts.salivary gland.216     |
| c_tpm_salivary_gland_217            | decimal | TPM.salivary gland.217            |
| c_est_counts_salivary_gland_217     | decimal | est_counts.salivary gland.217     |
| c_tpm_salivary_gland_218            | decimal | TPM.salivary gland.218            |
| c_est_counts_salivary_gland_218     | decimal | est_counts.salivary gland.218     |
| c_tpm_seminal_vesicle_404           | decimal | TPM.seminal vesicle.404           |
| c_est_counts_seminal_vesicle_404    | decimal | est_counts.seminal vesicle.404    |
| c_tpm_seminal_vesicle_386           | decimal | TPM.seminal vesicle.386           |
| c_est_counts_seminal_vesicle_386    | decimal | est_counts.seminal vesicle.386    |
| c_tpm_seminal_vesicle_409           | decimal | TPM.seminal vesicle.409           |
| c_est_counts_seminal_vesicle_409    | decimal | est_counts.seminal vesicle.409    |
| c_tpm_skeletal_muscle_339           | decimal | TPM.skeletal muscle.339           |
| c_est_counts_skeletal_muscle_339    | decimal | est_counts.skeletal muscle.339    |
| c_tpm_skeletal_muscle_340           | decimal | TPM.skeletal muscle.340           |
| c_est_counts_skeletal_muscle_340    | decimal | est_counts.skeletal muscle.340    |
| c_tpm_skeletal_muscle_341           | decimal | TPM.skeletal muscle.341           |
| c_est_counts_skeletal_muscle_341    | decimal | est_counts.skeletal muscle.341    |
| c_tpm_skeletal_muscle_342           | decimal | TPM.skeletal muscle.342           |
| c_est_counts_skeletal_muscle_342    | decimal | est_counts.skeletal muscle.342    |
| c_tpm_skeletal_muscle_343           | decimal | TPM.skeletal muscle.343           |
| c_est_counts_skeletal_muscle_343    | decimal | est_counts.skeletal muscle.343    |
| c_tpm_skin_227                      | decimal | TPM.skin.227                      |
| c_est_counts_skin_227               | decimal | est_counts.skin.227               |
| c_tpm_skin_225                      | decimal | TPM.skin.225                      |
| c_est_counts_skin_225               | decimal | est_counts.skin.225               |
| c_tpm_skin_226                      | decimal | TPM.skin.226                      |
| c_est_counts_skin_226               | decimal | est_counts.skin.226               |
| c_tpm_small_intestine_232           | decimal | TPM.small intestine.232           |
| c_est_counts_small_intestine_232    | decimal | est_counts.small intestine.232    |
| c_tpm_small_intestine_233           | decimal | TPM.small intestine.233           |
| c_est_counts_small_intestine_233    | decimal | est_counts.small intestine.233    |
| c_tpm_small_intestine_234           | decimal | TPM.small intestine.234           |
| c_est_counts_small_intestine_234    | decimal | est_counts.small intestine.234    |
| c_tpm_small_intestine_235           | decimal | TPM.small intestine.235           |
| c_est_counts_small_intestine_235    | decimal | est_counts.small intestine.235    |
| c_tpm_smooth_muscle_298             | decimal | TPM.smooth muscle.298             |
| c_est_counts_smooth_muscle_298      | decimal | est_counts.smooth muscle.298      |
| c_tpm_smooth_muscle_302             | decimal | TPM.smooth muscle.302             |
| c_est_counts_smooth_muscle_302      | decimal | est_counts.smooth muscle.302      |
| c_tpm_smooth_muscle_330             | decimal | TPM.smooth muscle.330             |
| c_est_counts_smooth_muscle_330      | decimal | est_counts.smooth muscle.330      |
| c_tpm_spleen_378                    | decimal | TPM.spleen.378                    |
| c_est_counts_spleen_378             | decimal | est_counts.spleen.378             |
| c_tpm_spleen_236                    | decimal | TPM.spleen.236                    |
| c_est_counts_spleen_236             | decimal | est_counts.spleen.236             |
| c_tpm_spleen_237                    | decimal | TPM.spleen.237                    |
| c_est_counts_spleen_237             | decimal | est_counts.spleen.237             |
| c_tpm_spleen_238                    | decimal | TPM.spleen.238                    |
| c_est_counts_spleen_238             | decimal | est_counts.spleen.238             |
| c_tpm_spleen_239                    | decimal | TPM.spleen.239                    |
| c_est_counts_spleen_239             | decimal | est_counts.spleen.239             |
| c_tpm_stomach_61                    | decimal | TPM.stomach.61                    |
| c_est_counts_stomach_61             | decimal | est_counts.stomach.61             |
| c_tpm_stomach_369                   | decimal | TPM.stomach.369                   |
| c_est_counts_stomach_369            | decimal | est_counts.stomach.369            |
| c_tpm_stomach_240                   | decimal | TPM.stomach.240                   |
| c_est_counts_stomach_240            | decimal | est_counts.stomach.240            |
| c_tpm_stomach_241                   | decimal | TPM.stomach.241                   |
| c_est_counts_stomach_241            | decimal | est_counts.stomach.241            |
| c_tpm_testis_244                    | decimal | TPM.testis.244                    |
| c_est_counts_testis_244             | decimal | est_counts.testis.244             |
| c_tpm_testis_278                    | decimal | TPM.testis.278                    |
| c_est_counts_testis_278             | decimal | est_counts.testis.278             |
| c_tpm_testis_279                    | decimal | TPM.testis.279                    |
| c_est_counts_testis_279             | decimal | est_counts.testis.279             |
| c_tpm_testis_280                    | decimal | TPM.testis.280                    |
| c_est_counts_testis_280             | decimal | est_counts.testis.280             |
| c_tpm_testis_281                    | decimal | TPM.testis.281                    |
| c_est_counts_testis_281             | decimal | est_counts.testis.281             |
| c_tpm_testis_282                    | decimal | TPM.testis.282                    |
| c_est_counts_testis_282             | decimal | est_counts.testis.282             |
| c_tpm_testis_283                    | decimal | TPM.testis.283                    |
| c_est_counts_testis_283             | decimal | est_counts.testis.283             |
| c_tpm_testis_349                    | decimal | TPM.testis.349                    |
| c_est_counts_testis_349             | decimal | est_counts.testis.349             |
| c_tpm_testis_371                    | decimal | TPM.testis.371                    |
| c_est_counts_testis_371             | decimal | est_counts.testis.371             |
| c_tpm_testis_354                    | decimal | TPM.testis.354                    |
| c_est_counts_testis_354             | decimal | est_counts.testis.354             |
| c_tpm_thymus_1599                   | decimal | TPM.thymus.1599                   |
| c_est_counts_thymus_1599            | decimal | est_counts.thymus.1599            |
| c_tpm_thymus_1602                   | decimal | TPM.thymus.1602                   |
| c_est_counts_thymus_1602            | decimal | est_counts.thymus.1602            |
| c_tpm_thymus_1603                   | decimal | TPM.thymus.1603                   |
| c_est_counts_thymus_1603            | decimal | est_counts.thymus.1603            |
| c_tpm_thyroid_gland_249             | decimal | TPM.thyroid gland.249             |
| c_est_counts_thyroid_gland_249      | decimal | est_counts.thyroid gland.249      |
| c_tpm_thyroid_gland_250             | decimal | TPM.thyroid gland.250             |
| c_est_counts_thyroid_gland_250      | decimal | est_counts.thyroid gland.250      |
| c_tpm_thyroid_gland_251             | decimal | TPM.thyroid gland.251             |
| c_est_counts_thyroid_gland_251      | decimal | est_counts.thyroid gland.251      |
| c_tpm_thyroid_gland_252             | decimal | TPM.thyroid gland.252             |
| c_est_counts_thyroid_gland_252      | decimal | est_counts.thyroid gland.252      |
| c_tpm_thyroid_gland_363             | decimal | TPM.thyroid gland.363             |
| c_est_counts_thyroid_gland_363      | decimal | est_counts.thyroid gland.363      |
| c_tpm_tongue_1604                   | decimal | TPM.tongue.1604                   |
| c_est_counts_tongue_1604            | decimal | est_counts.tongue.1604            |
| c_tpm_tonsil_295                    | decimal | TPM.tonsil.295                    |
| c_est_counts_tonsil_295             | decimal | est_counts.tonsil.295             |
| c_tpm_tonsil_309                    | decimal | TPM.tonsil.309                    |
| c_est_counts_tonsil_309             | decimal | est_counts.tonsil.309             |
| c_tpm_tonsil_315                    | decimal | TPM.tonsil.315                    |
| c_est_counts_tonsil_315             | decimal | est_counts.tonsil.315             |
| c_tpm_tonsil_318                    | decimal | TPM.tonsil.318                    |
| c_est_counts_tonsil_318             | decimal | est_counts.tonsil.318             |
| c_tpm_tonsil_320                    | decimal | TPM.tonsil.320                    |
| c_est_counts_tonsil_320             | decimal | est_counts.tonsil.320             |
| c_tpm_urinary_bladder_264           | decimal | TPM.urinary bladder.264           |
| c_est_counts_urinary_bladder_264    | decimal | est_counts.urinary bladder.264    |
| c_tpm_urinary_bladder_265           | decimal | TPM.urinary bladder.265           |
| c_est_counts_urinary_bladder_265    | decimal | est_counts.urinary bladder.265    |
| c_tpm_urinary_bladder_1597          | decimal | TPM.urinary bladder.1597          |
| c_est_counts_urinary_bladder_1597   | decimal | est_counts.urinary bladder.1597   |
| c_tpm_urinary_bladder_1598          | decimal | TPM.urinary bladder.1598          |
| c_est_counts_urinary_bladder_1598   | decimal | est_counts.urinary bladder.1598   |

## 27 transcript_rna_gtexretina

| Unnamed: 0               | dtype   | description            |
|:-------------------------|:--------|:-----------------------|
| c_ensgid                 | text    | ensgid                 |
| c_enstid                 | text    | enstid                 |
| c_tpm_retina_1660        | decimal | TPM.retina.1660        |
| c_est_counts_retina_1660 | decimal | est_counts.retina.1660 |
| c_tpm_retina_1661        | decimal | TPM.retina.1661        |
| c_est_counts_retina_1661 | decimal | est_counts.retina.1661 |
| c_tpm_retina_1662        | decimal | TPM.retina.1662        |
| c_est_counts_retina_1662 | decimal | est_counts.retina.1662 |
| c_tpm_retina_1663        | decimal | TPM.retina.1663        |
| c_est_counts_retina_1663 | decimal | est_counts.retina.1663 |
| c_tpm_retina_1664        | decimal | TPM.retina.1664        |
| c_est_counts_retina_1664 | decimal | est_counts.retina.1664 |
| c_tpm_retina_1665        | decimal | TPM.retina.1665        |
| c_est_counts_retina_1665 | decimal | est_counts.retina.1665 |
| c_tpm_retina_1666        | decimal | TPM.retina.1666        |
| c_est_counts_retina_1666 | decimal | est_counts.retina.1666 |
| c_tpm_retina_1667        | decimal | TPM.retina.1667        |
| c_est_counts_retina_1667 | decimal | est_counts.retina.1667 |
| c_tpm_retina_1668        | decimal | TPM.retina.1668        |
| c_est_counts_retina_1668 | decimal | est_counts.retina.1668 |
| c_tpm_retina_1669        | decimal | TPM.retina.1669        |
| c_est_counts_retina_1669 | decimal | est_counts.retina.1669 |
| c_tpm_retina_1670        | decimal | TPM.retina.1670        |
| c_est_counts_retina_1670 | decimal | est_counts.retina.1670 |
| c_tpm_retina_1671        | decimal | TPM.retina.1671        |
| c_est_counts_retina_1671 | decimal | est_counts.retina.1671 |
| c_tpm_retina_1672        | decimal | TPM.retina.1672        |
| c_est_counts_retina_1672 | decimal | est_counts.retina.1672 |
| c_tpm_retina_1673        | decimal | TPM.retina.1673        |
| c_est_counts_retina_1673 | decimal | est_counts.retina.1673 |
| c_tpm_retina_1650        | decimal | TPM.retina.1650        |
| c_est_counts_retina_1650 | decimal | est_counts.retina.1650 |
| c_tpm_retina_1674        | decimal | TPM.retina.1674        |
| c_est_counts_retina_1674 | decimal | est_counts.retina.1674 |
| c_tpm_retina_1675        | decimal | TPM.retina.1675        |
| c_est_counts_retina_1675 | decimal | est_counts.retina.1675 |
| c_tpm_retina_1676        | decimal | TPM.retina.1676        |
| c_est_counts_retina_1676 | decimal | est_counts.retina.1676 |
| c_tpm_retina_1651        | decimal | TPM.retina.1651        |
| c_est_counts_retina_1651 | decimal | est_counts.retina.1651 |
| c_tpm_retina_1677        | decimal | TPM.retina.1677        |
| c_est_counts_retina_1677 | decimal | est_counts.retina.1677 |
| c_tpm_retina_1646        | decimal | TPM.retina.1646        |
| c_est_counts_retina_1646 | decimal | est_counts.retina.1646 |
| c_tpm_retina_1678        | decimal | TPM.retina.1678        |
| c_est_counts_retina_1678 | decimal | est_counts.retina.1678 |
| c_tpm_retina_1679        | decimal | TPM.retina.1679        |
| c_est_counts_retina_1679 | decimal | est_counts.retina.1679 |
| c_tpm_retina_1680        | decimal | TPM.retina.1680        |
| c_est_counts_retina_1680 | decimal | est_counts.retina.1680 |
| c_tpm_retina_1681        | decimal | TPM.retina.1681        |
| c_est_counts_retina_1681 | decimal | est_counts.retina.1681 |
| c_tpm_retina_1682        | decimal | TPM.retina.1682        |
| c_est_counts_retina_1682 | decimal | est_counts.retina.1682 |
| c_tpm_retina_1683        | decimal | TPM.retina.1683        |
| c_est_counts_retina_1683 | decimal | est_counts.retina.1683 |
| c_tpm_retina_1684        | decimal | TPM.retina.1684        |
| c_est_counts_retina_1684 | decimal | est_counts.retina.1684 |
| c_tpm_retina_1685        | decimal | TPM.retina.1685        |
| c_est_counts_retina_1685 | decimal | est_counts.retina.1685 |
| c_tpm_retina_1686        | decimal | TPM.retina.1686        |
| c_est_counts_retina_1686 | decimal | est_counts.retina.1686 |
| c_tpm_retina_1687        | decimal | TPM.retina.1687        |
| c_est_counts_retina_1687 | decimal | est_counts.retina.1687 |
| c_tpm_retina_1688        | decimal | TPM.retina.1688        |
| c_est_counts_retina_1688 | decimal | est_counts.retina.1688 |
| c_tpm_retina_1689        | decimal | TPM.retina.1689        |
| c_est_counts_retina_1689 | decimal | est_counts.retina.1689 |
| c_tpm_retina_1690        | decimal | TPM.retina.1690        |
| c_est_counts_retina_1690 | decimal | est_counts.retina.1690 |
| c_tpm_retina_1691        | decimal | TPM.retina.1691        |
| c_est_counts_retina_1691 | decimal | est_counts.retina.1691 |
| c_tpm_retina_1692        | decimal | TPM.retina.1692        |
| c_est_counts_retina_1692 | decimal | est_counts.retina.1692 |
| c_tpm_retina_1693        | decimal | TPM.retina.1693        |
| c_est_counts_retina_1693 | decimal | est_counts.retina.1693 |
| c_tpm_retina_1694        | decimal | TPM.retina.1694        |
| c_est_counts_retina_1694 | decimal | est_counts.retina.1694 |
| c_tpm_retina_1695        | decimal | TPM.retina.1695        |
| c_est_counts_retina_1695 | decimal | est_counts.retina.1695 |
| c_tpm_retina_1696        | decimal | TPM.retina.1696        |
| c_est_counts_retina_1696 | decimal | est_counts.retina.1696 |
| c_tpm_retina_1697        | decimal | TPM.retina.1697        |
| c_est_counts_retina_1697 | decimal | est_counts.retina.1697 |
| c_tpm_retina_1698        | decimal | TPM.retina.1698        |
| c_est_counts_retina_1698 | decimal | est_counts.retina.1698 |
| c_tpm_retina_1699        | decimal | TPM.retina.1699        |
| c_est_counts_retina_1699 | decimal | est_counts.retina.1699 |
| c_tpm_retina_1700        | decimal | TPM.retina.1700        |
| c_est_counts_retina_1700 | decimal | est_counts.retina.1700 |
| c_tpm_retina_1701        | decimal | TPM.retina.1701        |
| c_est_counts_retina_1701 | decimal | est_counts.retina.1701 |
| c_tpm_retina_1702        | decimal | TPM.retina.1702        |
| c_est_counts_retina_1702 | decimal | est_counts.retina.1702 |
| c_tpm_retina_1703        | decimal | TPM.retina.1703        |
| c_est_counts_retina_1703 | decimal | est_counts.retina.1703 |
| c_tpm_retina_1704        | decimal | TPM.retina.1704        |
| c_est_counts_retina_1704 | decimal | est_counts.retina.1704 |
| c_tpm_retina_1652        | decimal | TPM.retina.1652        |
| c_est_counts_retina_1652 | decimal | est_counts.retina.1652 |
| c_tpm_retina_1705        | decimal | TPM.retina.1705        |
| c_est_counts_retina_1705 | decimal | est_counts.retina.1705 |
| c_tpm_retina_1706        | decimal | TPM.retina.1706        |
| c_est_counts_retina_1706 | decimal | est_counts.retina.1706 |
| c_tpm_retina_1707        | decimal | TPM.retina.1707        |
| c_est_counts_retina_1707 | decimal | est_counts.retina.1707 |
| c_tpm_retina_1708        | decimal | TPM.retina.1708        |
| c_est_counts_retina_1708 | decimal | est_counts.retina.1708 |
| c_tpm_retina_1709        | decimal | TPM.retina.1709        |
| c_est_counts_retina_1709 | decimal | est_counts.retina.1709 |
| c_tpm_retina_1710        | decimal | TPM.retina.1710        |
| c_est_counts_retina_1710 | decimal | est_counts.retina.1710 |
| c_tpm_retina_1711        | decimal | TPM.retina.1711        |
| c_est_counts_retina_1711 | decimal | est_counts.retina.1711 |
| c_tpm_retina_1712        | decimal | TPM.retina.1712        |
| c_est_counts_retina_1712 | decimal | est_counts.retina.1712 |
| c_tpm_retina_1653        | decimal | TPM.retina.1653        |
| c_est_counts_retina_1653 | decimal | est_counts.retina.1653 |
| c_tpm_retina_1713        | decimal | TPM.retina.1713        |
| c_est_counts_retina_1713 | decimal | est_counts.retina.1713 |
| c_tpm_retina_1714        | decimal | TPM.retina.1714        |
| c_est_counts_retina_1714 | decimal | est_counts.retina.1714 |
| c_tpm_retina_1715        | decimal | TPM.retina.1715        |
| c_est_counts_retina_1715 | decimal | est_counts.retina.1715 |
| c_tpm_retina_1716        | decimal | TPM.retina.1716        |
| c_est_counts_retina_1716 | decimal | est_counts.retina.1716 |
| c_tpm_retina_1717        | decimal | TPM.retina.1717        |
| c_est_counts_retina_1717 | decimal | est_counts.retina.1717 |
| c_tpm_retina_1718        | decimal | TPM.retina.1718        |
| c_est_counts_retina_1718 | decimal | est_counts.retina.1718 |
| c_tpm_retina_1719        | decimal | TPM.retina.1719        |
| c_est_counts_retina_1719 | decimal | est_counts.retina.1719 |
| c_tpm_retina_1720        | decimal | TPM.retina.1720        |
| c_est_counts_retina_1720 | decimal | est_counts.retina.1720 |
| c_tpm_retina_1721        | decimal | TPM.retina.1721        |
| c_est_counts_retina_1721 | decimal | est_counts.retina.1721 |
| c_tpm_retina_1722        | decimal | TPM.retina.1722        |
| c_est_counts_retina_1722 | decimal | est_counts.retina.1722 |
| c_tpm_retina_1723        | decimal | TPM.retina.1723        |
| c_est_counts_retina_1723 | decimal | est_counts.retina.1723 |
| c_tpm_retina_1724        | decimal | TPM.retina.1724        |
| c_est_counts_retina_1724 | decimal | est_counts.retina.1724 |
| c_tpm_retina_1725        | decimal | TPM.retina.1725        |
| c_est_counts_retina_1725 | decimal | est_counts.retina.1725 |
| c_tpm_retina_1726        | decimal | TPM.retina.1726        |
| c_est_counts_retina_1726 | decimal | est_counts.retina.1726 |
| c_tpm_retina_1727        | decimal | TPM.retina.1727        |
| c_est_counts_retina_1727 | decimal | est_counts.retina.1727 |
| c_tpm_retina_1728        | decimal | TPM.retina.1728        |
| c_est_counts_retina_1728 | decimal | est_counts.retina.1728 |
| c_tpm_retina_1647        | decimal | TPM.retina.1647        |
| c_est_counts_retina_1647 | decimal | est_counts.retina.1647 |
| c_tpm_retina_1729        | decimal | TPM.retina.1729        |
| c_est_counts_retina_1729 | decimal | est_counts.retina.1729 |
| c_tpm_retina_1730        | decimal | TPM.retina.1730        |
| c_est_counts_retina_1730 | decimal | est_counts.retina.1730 |
| c_tpm_retina_1731        | decimal | TPM.retina.1731        |
| c_est_counts_retina_1731 | decimal | est_counts.retina.1731 |
| c_tpm_retina_1654        | decimal | TPM.retina.1654        |
| c_est_counts_retina_1654 | decimal | est_counts.retina.1654 |
| c_tpm_retina_1732        | decimal | TPM.retina.1732        |
| c_est_counts_retina_1732 | decimal | est_counts.retina.1732 |
| c_tpm_retina_1733        | decimal | TPM.retina.1733        |
| c_est_counts_retina_1733 | decimal | est_counts.retina.1733 |
| c_tpm_retina_1734        | decimal | TPM.retina.1734        |
| c_est_counts_retina_1734 | decimal | est_counts.retina.1734 |
| c_tpm_retina_1655        | decimal | TPM.retina.1655        |
| c_est_counts_retina_1655 | decimal | est_counts.retina.1655 |
| c_tpm_retina_1735        | decimal | TPM.retina.1735        |
| c_est_counts_retina_1735 | decimal | est_counts.retina.1735 |
| c_tpm_retina_1656        | decimal | TPM.retina.1656        |
| c_est_counts_retina_1656 | decimal | est_counts.retina.1656 |
| c_tpm_retina_1736        | decimal | TPM.retina.1736        |
| c_est_counts_retina_1736 | decimal | est_counts.retina.1736 |
| c_tpm_retina_1737        | decimal | TPM.retina.1737        |
| c_est_counts_retina_1737 | decimal | est_counts.retina.1737 |
| c_tpm_retina_1738        | decimal | TPM.retina.1738        |
| c_est_counts_retina_1738 | decimal | est_counts.retina.1738 |
| c_tpm_retina_1739        | decimal | TPM.retina.1739        |
| c_est_counts_retina_1739 | decimal | est_counts.retina.1739 |
| c_tpm_retina_1740        | decimal | TPM.retina.1740        |
| c_est_counts_retina_1740 | decimal | est_counts.retina.1740 |
| c_tpm_retina_1741        | decimal | TPM.retina.1741        |
| c_est_counts_retina_1741 | decimal | est_counts.retina.1741 |
| c_tpm_retina_1742        | decimal | TPM.retina.1742        |
| c_est_counts_retina_1742 | decimal | est_counts.retina.1742 |
| c_tpm_retina_1743        | decimal | TPM.retina.1743        |
| c_est_counts_retina_1743 | decimal | est_counts.retina.1743 |
| c_tpm_retina_1744        | decimal | TPM.retina.1744        |
| c_est_counts_retina_1744 | decimal | est_counts.retina.1744 |
| c_tpm_retina_1745        | decimal | TPM.retina.1745        |
| c_est_counts_retina_1745 | decimal | est_counts.retina.1745 |
| c_tpm_retina_1746        | decimal | TPM.retina.1746        |
| c_est_counts_retina_1746 | decimal | est_counts.retina.1746 |
| c_tpm_retina_1747        | decimal | TPM.retina.1747        |
| c_est_counts_retina_1747 | decimal | est_counts.retina.1747 |
| c_tpm_retina_1748        | decimal | TPM.retina.1748        |
| c_est_counts_retina_1748 | decimal | est_counts.retina.1748 |
| c_tpm_retina_1749        | decimal | TPM.retina.1749        |
| c_est_counts_retina_1749 | decimal | est_counts.retina.1749 |
| c_tpm_retina_1750        | decimal | TPM.retina.1750        |
| c_est_counts_retina_1750 | decimal | est_counts.retina.1750 |
| c_tpm_retina_1648        | decimal | TPM.retina.1648        |
| c_est_counts_retina_1648 | decimal | est_counts.retina.1648 |
| c_tpm_retina_1657        | decimal | TPM.retina.1657        |
| c_est_counts_retina_1657 | decimal | est_counts.retina.1657 |
| c_tpm_retina_1658        | decimal | TPM.retina.1658        |
| c_est_counts_retina_1658 | decimal | est_counts.retina.1658 |
| c_tpm_retina_1649        | decimal | TPM.retina.1649        |
| c_est_counts_retina_1649 | decimal | est_counts.retina.1649 |
| c_tpm_retina_1659        | decimal | TPM.retina.1659        |
| c_est_counts_retina_1659 | decimal | est_counts.retina.1659 |


## 27 transcript_rna_brain

| Unnamed: 0                                                                        | dtype   | description                                                                     |
|:----------------------------------------------------------------------------------|:--------|:--------------------------------------------------------------------------------|
| c_ensgid                                                                          | text    | ensgid                                                                          |
| c_enstid                                                                          | text    | enstid                                                                          |
| c_tpm_amygdala_2514                                                               | decimal | TPM.amygdala.2514                                                               |
| c_est_counts_amygdala_2514                                                        | decimal | est_counts.amygdala.2514                                                        |
| c_tpm_amygdala_1987                                                               | decimal | TPM.amygdala.1987                                                               |
| c_est_counts_amygdala_1987                                                        | decimal | est_counts.amygdala.1987                                                        |
| c_tpm_amygdala_2517                                                               | decimal | TPM.amygdala.2517                                                               |
| c_est_counts_amygdala_2517                                                        | decimal | est_counts.amygdala.2517                                                        |
| c_tpm_amygdala_2695                                                               | decimal | TPM.amygdala.2695                                                               |
| c_est_counts_amygdala_2695                                                        | decimal | est_counts.amygdala.2695                                                        |
| c_tpm_amygdala_2814                                                               | decimal | TPM.amygdala.2814                                                               |
| c_est_counts_amygdala_2814                                                        | decimal | est_counts.amygdala.2814                                                        |
| c_tpm_angular_gyrus_2260                                                          | decimal | TPM.angular gyrus.2260                                                          |
| c_est_counts_angular_gyrus_2260                                                   | decimal | est_counts.angular gyrus.2260                                                   |
| c_tpm_angular_gyrus_2722                                                          | decimal | TPM.angular gyrus.2722                                                          |
| c_est_counts_angular_gyrus_2722                                                   | decimal | est_counts.angular gyrus.2722                                                   |
| c_tpm_angular_gyrus_2103                                                          | decimal | TPM.angular gyrus.2103                                                          |
| c_est_counts_angular_gyrus_2103                                                   | decimal | est_counts.angular gyrus.2103                                                   |
| c_tpm_angular_gyrus_2265                                                          | decimal | TPM.angular gyrus.2265                                                          |
| c_est_counts_angular_gyrus_2265                                                   | decimal | est_counts.angular gyrus.2265                                                   |
| c_tpm_angular_gyrus_2602                                                          | decimal | TPM.angular gyrus.2602                                                          |
| c_est_counts_angular_gyrus_2602                                                   | decimal | est_counts.angular gyrus.2602                                                   |
| c_tpm_angular_gyrus_2221                                                          | decimal | TPM.angular gyrus.2221                                                          |
| c_est_counts_angular_gyrus_2221                                                   | decimal | est_counts.angular gyrus.2221                                                   |
| c_tpm_angular_gyrus_1790                                                          | decimal | TPM.angular gyrus.1790                                                          |
| c_est_counts_angular_gyrus_1790                                                   | decimal | est_counts.angular gyrus.1790                                                   |
| c_tpm_angular_gyrus_1866                                                          | decimal | TPM.angular gyrus.1866                                                          |
| c_est_counts_angular_gyrus_1866                                                   | decimal | est_counts.angular gyrus.1866                                                   |
| c_tpm_angular_gyrus__white_matter__1920                                           | decimal | TPM.angular gyrus (white matter).1920                                           |
| c_est_counts_angular_gyrus__white_matter__1920                                    | decimal | est_counts.angular gyrus (white matter).1920                                    |
| c_tpm_anterior_cingulate_cortex__supragenual_dorsal_2472                          | decimal | TPM.anterior cingulate cortex, supragenual-dorsal.2472                          |
| c_est_counts_anterior_cingulate_cortex__supragenual_dorsal_2472                   | decimal | est_counts.anterior cingulate cortex, supragenual-dorsal.2472                   |
| c_tpm_anterior_cingulate_cortex__supragenual_dorsal_2547                          | decimal | TPM.anterior cingulate cortex, supragenual-dorsal.2547                          |
| c_est_counts_anterior_cingulate_cortex__supragenual_dorsal_2547                   | decimal | est_counts.anterior cingulate cortex, supragenual-dorsal.2547                   |
| c_tpm_anterior_cingulate_cortex__supragenual_dorsal_2342                          | decimal | TPM.anterior cingulate cortex, supragenual-dorsal.2342                          |
| c_est_counts_anterior_cingulate_cortex__supragenual_dorsal_2342                   | decimal | est_counts.anterior cingulate cortex, supragenual-dorsal.2342                   |
| c_tpm_anterior_cingulate_cortex__supragenual_dorsal_1896                          | decimal | TPM.anterior cingulate cortex, supragenual-dorsal.1896                          |
| c_est_counts_anterior_cingulate_cortex__supragenual_dorsal_1896                   | decimal | est_counts.anterior cingulate cortex, supragenual-dorsal.1896                   |
| c_tpm_anterior_cingulate_cortex__supragenual_dorsal_2478                          | decimal | TPM.anterior cingulate cortex, supragenual-dorsal.2478                          |
| c_est_counts_anterior_cingulate_cortex__supragenual_dorsal_2478                   | decimal | est_counts.anterior cingulate cortex, supragenual-dorsal.2478                   |
| c_tpm_anterior_cingulate_cortex__supragenual_ventral_2538                         | decimal | TPM.anterior cingulate cortex, supragenual-ventral.2538                         |
| c_est_counts_anterior_cingulate_cortex__supragenual_ventral_2538                  | decimal | est_counts.anterior cingulate cortex, supragenual-ventral.2538                  |
| c_tpm_anterior_cingulate_cortex__supragenual_ventral_1761                         | decimal | TPM.anterior cingulate cortex, supragenual-ventral.1761                         |
| c_est_counts_anterior_cingulate_cortex__supragenual_ventral_1761                  | decimal | est_counts.anterior cingulate cortex, supragenual-ventral.1761                  |
| c_tpm_anterior_cingulate_cortex__supragenual_ventral_1755                         | decimal | TPM.anterior cingulate cortex, supragenual-ventral.1755                         |
| c_est_counts_anterior_cingulate_cortex__supragenual_ventral_1755                  | decimal | est_counts.anterior cingulate cortex, supragenual-ventral.1755                  |
| c_tpm_anterior_cingulate_cortex__supragenual_ventral_1950                         | decimal | TPM.anterior cingulate cortex, supragenual-ventral.1950                         |
| c_est_counts_anterior_cingulate_cortex__supragenual_ventral_1950                  | decimal | est_counts.anterior cingulate cortex, supragenual-ventral.1950                  |
| c_tpm_anterior_cingulate_cortex__supragenual_ventral_2479                         | decimal | TPM.anterior cingulate cortex, supragenual-ventral.2479                         |
| c_est_counts_anterior_cingulate_cortex__supragenual_ventral_2479                  | decimal | est_counts.anterior cingulate cortex, supragenual-ventral.2479                  |
| c_tpm_anterior_cochlear_nucleus__ventral_2090                                     | decimal | TPM.anterior cochlear nucleus, ventral.2090                                     |
| c_est_counts_anterior_cochlear_nucleus__ventral_2090                              | decimal | est_counts.anterior cochlear nucleus, ventral.2090                              |
| c_tpm_anterior_cochlear_nucleus__ventral_2188                                     | decimal | TPM.anterior cochlear nucleus, ventral.2188                                     |
| c_est_counts_anterior_cochlear_nucleus__ventral_2188                              | decimal | est_counts.anterior cochlear nucleus, ventral.2188                              |
| c_tpm_anterior_cochlear_nucleus__ventral_2301                                     | decimal | TPM.anterior cochlear nucleus, ventral.2301                                     |
| c_est_counts_anterior_cochlear_nucleus__ventral_2301                              | decimal | est_counts.anterior cochlear nucleus, ventral.2301                              |
| c_tpm_anterior_cochlear_nucleus__ventral_1984                                     | decimal | TPM.anterior cochlear nucleus, ventral.1984                                     |
| c_est_counts_anterior_cochlear_nucleus__ventral_1984                              | decimal | est_counts.anterior cochlear nucleus, ventral.1984                              |
| c_tpm_anterior_funiculus__white_matter__2819                                      | decimal | TPM.anterior funiculus (white matter).2819                                      |
| c_est_counts_anterior_funiculus__white_matter__2819                               | decimal | est_counts.anterior funiculus (white matter).2819                               |
| c_tpm_anterior_funiculus__white_matter__2818                                      | decimal | TPM.anterior funiculus (white matter).2818                                      |
| c_est_counts_anterior_funiculus__white_matter__2818                               | decimal | est_counts.anterior funiculus (white matter).2818                               |
| c_tpm_anterior_funiculus__white_matter__2734                                      | decimal | TPM.anterior funiculus (white matter).2734                                      |
| c_est_counts_anterior_funiculus__white_matter__2734                               | decimal | est_counts.anterior funiculus (white matter).2734                               |
| c_tpm_anterior_funiculus__white_matter__2193                                      | decimal | TPM.anterior funiculus (white matter).2193                                      |
| c_est_counts_anterior_funiculus__white_matter__2193                               | decimal | est_counts.anterior funiculus (white matter).2193                               |
| c_tpm_anterior_insular_cortex__dorsal_2670                                        | decimal | TPM.anterior insular cortex, dorsal.2670                                        |
| c_est_counts_anterior_insular_cortex__dorsal_2670                                 | decimal | est_counts.anterior insular cortex, dorsal.2670                                 |
| c_tpm_anterior_insular_cortex__dorsal_2235                                        | decimal | TPM.anterior insular cortex, dorsal.2235                                        |
| c_est_counts_anterior_insular_cortex__dorsal_2235                                 | decimal | est_counts.anterior insular cortex, dorsal.2235                                 |
| c_tpm_anterior_insular_cortex__dorsal_2506                                        | decimal | TPM.anterior insular cortex, dorsal.2506                                        |
| c_est_counts_anterior_insular_cortex__dorsal_2506                                 | decimal | est_counts.anterior insular cortex, dorsal.2506                                 |
| c_tpm_anterior_insular_cortex__dorsal_2001                                        | decimal | TPM.anterior insular cortex, dorsal.2001                                        |
| c_est_counts_anterior_insular_cortex__dorsal_2001                                 | decimal | est_counts.anterior insular cortex, dorsal.2001                                 |
| c_tpm_anterior_insular_cortex__ventral_2757                                       | decimal | TPM.anterior insular cortex, ventral.2757                                       |
| c_est_counts_anterior_insular_cortex__ventral_2757                                | decimal | est_counts.anterior insular cortex, ventral.2757                                |
| c_tpm_anterior_insular_cortex__ventral_2596                                       | decimal | TPM.anterior insular cortex, ventral.2596                                       |
| c_est_counts_anterior_insular_cortex__ventral_2596                                | decimal | est_counts.anterior insular cortex, ventral.2596                                |
| c_tpm_anterior_insular_cortex__ventral_1925                                       | decimal | TPM.anterior insular cortex, ventral.1925                                       |
| c_est_counts_anterior_insular_cortex__ventral_1925                                | decimal | est_counts.anterior insular cortex, ventral.1925                                |
| c_tpm_anterior_insular_cortex__ventral_2507                                       | decimal | TPM.anterior insular cortex, ventral.2507                                       |
| c_est_counts_anterior_insular_cortex__ventral_2507                                | decimal | est_counts.anterior insular cortex, ventral.2507                                |
| c_tpm_anterior_insular_cortex__ventral_2262                                       | decimal | TPM.anterior insular cortex, ventral.2262                                       |
| c_est_counts_anterior_insular_cortex__ventral_2262                                | decimal | est_counts.anterior insular cortex, ventral.2262                                |
| c_tpm_anterior_insular_cortex__ventral_1852                                       | decimal | TPM.anterior insular cortex, ventral.1852                                       |
| c_est_counts_anterior_insular_cortex__ventral_1852                                | decimal | est_counts.anterior insular cortex, ventral.1852                                |
| c_tpm_anterior_thalamic_nucleus__ventral_2032                                     | decimal | TPM.anterior thalamic nucleus, ventral.2032                                     |
| c_est_counts_anterior_thalamic_nucleus__ventral_2032                              | decimal | est_counts.anterior thalamic nucleus, ventral.2032                              |
| c_tpm_anterior_thalamic_nucleus__ventral_2497                                     | decimal | TPM.anterior thalamic nucleus, ventral.2497                                     |
| c_est_counts_anterior_thalamic_nucleus__ventral_2497                              | decimal | est_counts.anterior thalamic nucleus, ventral.2497                              |
| c_tpm_anterior_thalamic_nucleus__ventral_2396                                     | decimal | TPM.anterior thalamic nucleus, ventral.2396                                     |
| c_est_counts_anterior_thalamic_nucleus__ventral_2396                              | decimal | est_counts.anterior thalamic nucleus, ventral.2396                              |
| c_tpm_arcuate_nucleus_1961                                                        | decimal | TPM.arcuate nucleus.1961                                                        |
| c_est_counts_arcuate_nucleus_1961                                                 | decimal | est_counts.arcuate nucleus.1961                                                 |
| c_tpm_arcuate_nucleus_2226                                                        | decimal | TPM.arcuate nucleus.2226                                                        |
| c_est_counts_arcuate_nucleus_2226                                                 | decimal | est_counts.arcuate nucleus.2226                                                 |
| c_tpm_area_parastriata__inferior_1758                                             | decimal | TPM.area parastriata, inferior.1758                                             |
| c_est_counts_area_parastriata__inferior_1758                                      | decimal | est_counts.area parastriata, inferior.1758                                      |
| c_tpm_area_parastriata__inferior_2268                                             | decimal | TPM.area parastriata, inferior.2268                                             |
| c_est_counts_area_parastriata__inferior_2268                                      | decimal | est_counts.area parastriata, inferior.2268                                      |
| c_tpm_area_parastriata__inferior_2234                                             | decimal | TPM.area parastriata, inferior.2234                                             |
| c_est_counts_area_parastriata__inferior_2234                                      | decimal | est_counts.area parastriata, inferior.2234                                      |
| c_tpm_area_parastriata__inferior_2421                                             | decimal | TPM.area parastriata, inferior.2421                                             |
| c_est_counts_area_parastriata__inferior_2421                                      | decimal | est_counts.area parastriata, inferior.2421                                      |
| c_tpm_area_parastriata__inferior_2509                                             | decimal | TPM.area parastriata, inferior.2509                                             |
| c_est_counts_area_parastriata__inferior_2509                                      | decimal | est_counts.area parastriata, inferior.2509                                      |
| c_tpm_area_parastriata__inferior_1760                                             | decimal | TPM.area parastriata, inferior.1760                                             |
| c_est_counts_area_parastriata__inferior_1760                                      | decimal | est_counts.area parastriata, inferior.1760                                      |
| c_tpm_area_parastriata__inferior_1789                                             | decimal | TPM.area parastriata, inferior.1789                                             |
| c_est_counts_area_parastriata__inferior_1789                                      | decimal | est_counts.area parastriata, inferior.1789                                      |
| c_tpm_area_parastriata__parietal_2233                                             | decimal | TPM.area parastriata, parietal.2233                                             |
| c_est_counts_area_parastriata__parietal_2233                                      | decimal | est_counts.area parastriata, parietal.2233                                      |
| c_tpm_area_parastriata__parietal_2420                                             | decimal | TPM.area parastriata, parietal.2420                                             |
| c_est_counts_area_parastriata__parietal_2420                                      | decimal | est_counts.area parastriata, parietal.2420                                      |
| c_tpm_area_parastriata__parietal_2236                                             | decimal | TPM.area parastriata, parietal.2236                                             |
| c_est_counts_area_parastriata__parietal_2236                                      | decimal | est_counts.area parastriata, parietal.2236                                      |
| c_tpm_area_parastriata__parietal_2680                                             | decimal | TPM.area parastriata, parietal.2680                                             |
| c_est_counts_area_parastriata__parietal_2680                                      | decimal | est_counts.area parastriata, parietal.2680                                      |
| c_tpm_area_parastriata__parietal_1785                                             | decimal | TPM.area parastriata, parietal.1785                                             |
| c_est_counts_area_parastriata__parietal_1785                                      | decimal | est_counts.area parastriata, parietal.1785                                      |
| c_tpm_area_parastriata__superior_2435                                             | decimal | TPM.area parastriata, superior.2435                                             |
| c_est_counts_area_parastriata__superior_2435                                      | decimal | est_counts.area parastriata, superior.2435                                      |
| c_tpm_area_parastriata__superior_2419                                             | decimal | TPM.area parastriata, superior.2419                                             |
| c_est_counts_area_parastriata__superior_2419                                      | decimal | est_counts.area parastriata, superior.2419                                      |
| c_tpm_area_parastriata__superior_1773                                             | decimal | TPM.area parastriata, superior.1773                                             |
| c_est_counts_area_parastriata__superior_1773                                      | decimal | est_counts.area parastriata, superior.1773                                      |
| c_tpm_area_parastriata__superior_2604                                             | decimal | TPM.area parastriata, superior.2604                                             |
| c_est_counts_area_parastriata__superior_2604                                      | decimal | est_counts.area parastriata, superior.2604                                      |
| c_tpm_area_parastriata__superior_2684                                             | decimal | TPM.area parastriata, superior.2684                                             |
| c_est_counts_area_parastriata__superior_2684                                      | decimal | est_counts.area parastriata, superior.2684                                      |
| c_tpm_area_parastriata__superior_2881                                             | decimal | TPM.area parastriata, superior.2881                                             |
| c_est_counts_area_parastriata__superior_2881                                      | decimal | est_counts.area parastriata, superior.2881                                      |
| c_tpm_area_parastriata__temporal_2267                                             | decimal | TPM.area parastriata, temporal.2267                                             |
| c_est_counts_area_parastriata__temporal_2267                                      | decimal | est_counts.area parastriata, temporal.2267                                      |
| c_tpm_area_parastriata__temporal_2471                                             | decimal | TPM.area parastriata, temporal.2471                                             |
| c_est_counts_area_parastriata__temporal_2471                                      | decimal | est_counts.area parastriata, temporal.2471                                      |
| c_tpm_area_parastriata__temporal_2681                                             | decimal | TPM.area parastriata, temporal.2681                                             |
| c_est_counts_area_parastriata__temporal_2681                                      | decimal | est_counts.area parastriata, temporal.2681                                      |
| c_tpm_area_parastriata__temporal_2424                                             | decimal | TPM.area parastriata, temporal.2424                                             |
| c_est_counts_area_parastriata__temporal_2424                                      | decimal | est_counts.area parastriata, temporal.2424                                      |
| c_tpm_area_parastriata__temporal_1804                                             | decimal | TPM.area parastriata, temporal.1804                                             |
| c_est_counts_area_parastriata__temporal_1804                                      | decimal | est_counts.area parastriata, temporal.1804                                      |
| c_tpm_area_postrema_2799                                                          | decimal | TPM.area postrema.2799                                                          |
| c_est_counts_area_postrema_2799                                                   | decimal | est_counts.area postrema.2799                                                   |
| c_tpm_area_postrema_2306                                                          | decimal | TPM.area postrema.2306                                                          |
| c_est_counts_area_postrema_2306                                                   | decimal | est_counts.area postrema.2306                                                   |
| c_tpm_area_postrema_2054                                                          | decimal | TPM.area postrema.2054                                                          |
| c_est_counts_area_postrema_2054                                                   | decimal | est_counts.area postrema.2054                                                   |
| c_tpm_area_striata_1753                                                           | decimal | TPM.area striata.1753                                                           |
| c_est_counts_area_striata_1753                                                    | decimal | est_counts.area striata.1753                                                    |
| c_tpm_area_striata_2417                                                           | decimal | TPM.area striata.2417                                                           |
| c_est_counts_area_striata_2417                                                    | decimal | est_counts.area striata.2417                                                    |
| c_tpm_area_striata_2002                                                           | decimal | TPM.area striata.2002                                                           |
| c_est_counts_area_striata_2002                                                    | decimal | est_counts.area striata.2002                                                    |
| c_tpm_area_striata_2427                                                           | decimal | TPM.area striata.2427                                                           |
| c_est_counts_area_striata_2427                                                    | decimal | est_counts.area striata.2427                                                    |
| c_tpm_area_striata_2679                                                           | decimal | TPM.area striata.2679                                                           |
| c_est_counts_area_striata_2679                                                    | decimal | est_counts.area striata.2679                                                    |
| c_tpm_area_striata_1884                                                           | decimal | TPM.area striata.1884                                                           |
| c_est_counts_area_striata_1884                                                    | decimal | est_counts.area striata.1884                                                    |
| c_tpm_area_striata__white_matter__2258                                            | decimal | TPM.area striata (white matter).2258                                            |
| c_est_counts_area_striata__white_matter__2258                                     | decimal | est_counts.area striata (white matter).2258                                     |
| c_tpm_basal_amygdala_2110                                                         | decimal | TPM.basal amygdala.2110                                                         |
| c_est_counts_basal_amygdala_2110                                                  | decimal | est_counts.basal amygdala.2110                                                  |
| c_tpm_basal_amygdala_2609                                                         | decimal | TPM.basal amygdala.2609                                                         |
| c_est_counts_basal_amygdala_2609                                                  | decimal | est_counts.basal amygdala.2609                                                  |
| c_tpm_basal_amygdala_2243                                                         | decimal | TPM.basal amygdala.2243                                                         |
| c_est_counts_basal_amygdala_2243                                                  | decimal | est_counts.basal amygdala.2243                                                  |
| c_tpm_basal_amygdala_2685                                                         | decimal | TPM.basal amygdala.2685                                                         |
| c_est_counts_basal_amygdala_2685                                                  | decimal | est_counts.basal amygdala.2685                                                  |
| c_tpm_basal_amygdala_2827                                                         | decimal | TPM.basal amygdala.2827                                                         |
| c_est_counts_basal_amygdala_2827                                                  | decimal | est_counts.basal amygdala.2827                                                  |
| c_tpm_basal_amygdala_1955                                                         | decimal | TPM.basal amygdala.1955                                                         |
| c_est_counts_basal_amygdala_1955                                                  | decimal | est_counts.basal amygdala.1955                                                  |
| c_tpm_caudate_nucleus_2846                                                        | decimal | TPM.caudate nucleus.2846                                                        |
| c_est_counts_caudate_nucleus_2846                                                 | decimal | est_counts.caudate nucleus.2846                                                 |
| c_tpm_caudate_nucleus_2290                                                        | decimal | TPM.caudate nucleus.2290                                                        |
| c_est_counts_caudate_nucleus_2290                                                 | decimal | est_counts.caudate nucleus.2290                                                 |
| c_tpm_caudate_nucleus_2289                                                        | decimal | TPM.caudate nucleus.2289                                                        |
| c_est_counts_caudate_nucleus_2289                                                 | decimal | est_counts.caudate nucleus.2289                                                 |
| c_tpm_caudate_nucleus_1854                                                        | decimal | TPM.caudate nucleus.1854                                                        |
| c_est_counts_caudate_nucleus_1854                                                 | decimal | est_counts.caudate nucleus.1854                                                 |
| c_tpm_caudate_nucleus_2288                                                        | decimal | TPM.caudate nucleus.2288                                                        |
| c_est_counts_caudate_nucleus_2288                                                 | decimal | est_counts.caudate nucleus.2288                                                 |
| c_tpm_caudate_nucleus_2481                                                        | decimal | TPM.caudate nucleus.2481                                                        |
| c_est_counts_caudate_nucleus_2481                                                 | decimal | est_counts.caudate nucleus.2481                                                 |
| c_tpm_caudate_nucleus_1857                                                        | decimal | TPM.caudate nucleus.1857                                                        |
| c_est_counts_caudate_nucleus_1857                                                 | decimal | est_counts.caudate nucleus.1857                                                 |
| c_tpm_caudate_nucleus_1781                                                        | decimal | TPM.caudate nucleus.1781                                                        |
| c_est_counts_caudate_nucleus_1781                                                 | decimal | est_counts.caudate nucleus.1781                                                 |
| c_tpm_central_amygdala_2239                                                       | decimal | TPM.central amygdala.2239                                                       |
| c_est_counts_central_amygdala_2239                                                | decimal | est_counts.central amygdala.2239                                                |
| c_tpm_central_amygdala_2515                                                       | decimal | TPM.central amygdala.2515                                                       |
| c_est_counts_central_amygdala_2515                                                | decimal | est_counts.central amygdala.2515                                                |
| c_tpm_central_amygdala_2701                                                       | decimal | TPM.central amygdala.2701                                                       |
| c_est_counts_central_amygdala_2701                                                | decimal | est_counts.central amygdala.2701                                                |
| c_tpm_central_amygdala_2826                                                       | decimal | TPM.central amygdala.2826                                                       |
| c_est_counts_central_amygdala_2826                                                | decimal | est_counts.central amygdala.2826                                                |
| c_tpm_central_amygdala_1905                                                       | decimal | TPM.central amygdala.1905                                                       |
| c_est_counts_central_amygdala_1905                                                | decimal | est_counts.central amygdala.1905                                                |
| c_tpm_centromedial_thalamic_nucleus_2279                                          | decimal | TPM.centromedial thalamic nucleus.2279                                          |
| c_est_counts_centromedial_thalamic_nucleus_2279                                   | decimal | est_counts.centromedial thalamic nucleus.2279                                   |
| c_tpm_centromedial_thalamic_nucleus_2401                                          | decimal | TPM.centromedial thalamic nucleus.2401                                          |
| c_est_counts_centromedial_thalamic_nucleus_2401                                   | decimal | est_counts.centromedial thalamic nucleus.2401                                   |
| c_tpm_cerebellar_cortex_1768                                                      | decimal | TPM.cerebellar cortex.1768                                                      |
| c_est_counts_cerebellar_cortex_1768                                               | decimal | est_counts.cerebellar cortex.1768                                               |
| c_tpm_cerebellar_cortex_2006                                                      | decimal | TPM.cerebellar cortex.2006                                                      |
| c_est_counts_cerebellar_cortex_2006                                               | decimal | est_counts.cerebellar cortex.2006                                               |
| c_tpm_cerebellar_cortex_1774                                                      | decimal | TPM.cerebellar cortex.1774                                                      |
| c_est_counts_cerebellar_cortex_1774                                               | decimal | est_counts.cerebellar cortex.1774                                               |
| c_tpm_cerebellar_cortex_2055                                                      | decimal | TPM.cerebellar cortex.2055                                                      |
| c_est_counts_cerebellar_cortex_2055                                               | decimal | est_counts.cerebellar cortex.2055                                               |
| c_tpm_cerebellar_cortex_2101                                                      | decimal | TPM.cerebellar cortex.2101                                                      |
| c_est_counts_cerebellar_cortex_2101                                               | decimal | est_counts.cerebellar cortex.2101                                               |
| c_tpm_cerebellar_cortex_2003                                                      | decimal | TPM.cerebellar cortex.2003                                                      |
| c_est_counts_cerebellar_cortex_2003                                               | decimal | est_counts.cerebellar cortex.2003                                               |
| c_tpm_cerebellar_cortex_1769                                                      | decimal | TPM.cerebellar cortex.1769                                                      |
| c_est_counts_cerebellar_cortex_1769                                               | decimal | est_counts.cerebellar cortex.1769                                               |
| c_tpm_cerebellar_cortex_1788                                                      | decimal | TPM.cerebellar cortex.1788                                                      |
| c_est_counts_cerebellar_cortex_1788                                               | decimal | est_counts.cerebellar cortex.1788                                               |
| c_tpm_cerebellar_nuclei_2783                                                      | decimal | TPM.cerebellar nuclei.2783                                                      |
| c_est_counts_cerebellar_nuclei_2783                                               | decimal | est_counts.cerebellar nuclei.2783                                               |
| c_tpm_cerebellar_nuclei_2175                                                      | decimal | TPM.cerebellar nuclei.2175                                                      |
| c_est_counts_cerebellar_nuclei_2175                                               | decimal | est_counts.cerebellar nuclei.2175                                               |
| c_tpm_cerebellar_nuclei_2005                                                      | decimal | TPM.cerebellar nuclei.2005                                                      |
| c_est_counts_cerebellar_nuclei_2005                                               | decimal | est_counts.cerebellar nuclei.2005                                               |
| c_tpm_cerebellar_nuclei_1966                                                      | decimal | TPM.cerebellar nuclei.1966                                                      |
| c_est_counts_cerebellar_nuclei_1966                                               | decimal | est_counts.cerebellar nuclei.1966                                               |
| c_tpm_cerebellar_nuclei_2318                                                      | decimal | TPM.cerebellar nuclei.2318                                                      |
| c_est_counts_cerebellar_nuclei_2318                                               | decimal | est_counts.cerebellar nuclei.2318                                               |
| c_tpm_cerebellar_nuclei_2177                                                      | decimal | TPM.cerebellar nuclei.2177                                                      |
| c_est_counts_cerebellar_nuclei_2177                                               | decimal | est_counts.cerebellar nuclei.2177                                               |
| c_tpm_cerebellar_nuclei_2882                                                      | decimal | TPM.cerebellar nuclei.2882                                                      |
| c_est_counts_cerebellar_nuclei_2882                                               | decimal | est_counts.cerebellar nuclei.2882                                               |
| c_tpm_cerebellar_nuclei_1879                                                      | decimal | TPM.cerebellar nuclei.1879                                                      |
| c_est_counts_cerebellar_nuclei_1879                                               | decimal | est_counts.cerebellar nuclei.1879                                               |
| c_tpm_cerebellar_nuclei_1871                                                      | decimal | TPM.cerebellar nuclei.1871                                                      |
| c_est_counts_cerebellar_nuclei_1871                                               | decimal | est_counts.cerebellar nuclei.1871                                               |
| c_tpm_cerebellar_white_matter_2174                                                | decimal | TPM.cerebellar white matter.2174                                                |
| c_est_counts_cerebellar_white_matter_2174                                         | decimal | est_counts.cerebellar white matter.2174                                         |
| c_tpm_cerebellar_white_matter_1864                                                | decimal | TPM.cerebellar white matter.1864                                                |
| c_est_counts_cerebellar_white_matter_1864                                         | decimal | est_counts.cerebellar white matter.1864                                         |
| c_tpm_cerebellar_white_matter_1931                                                | decimal | TPM.cerebellar white matter.1931                                                |
| c_est_counts_cerebellar_white_matter_1931                                         | decimal | est_counts.cerebellar white matter.1931                                         |
| c_tpm_cerebellar_white_matter_2105                                                | decimal | TPM.cerebellar white matter.2105                                                |
| c_est_counts_cerebellar_white_matter_2105                                         | decimal | est_counts.cerebellar white matter.2105                                         |
| c_tpm_cerebellar_white_matter_2773                                                | decimal | TPM.cerebellar white matter.2773                                                |
| c_est_counts_cerebellar_white_matter_2773                                         | decimal | est_counts.cerebellar white matter.2773                                         |
| c_tpm_cerebellar_white_matter_1837                                                | decimal | TPM.cerebellar white matter.1837                                                |
| c_est_counts_cerebellar_white_matter_1837                                         | decimal | est_counts.cerebellar white matter.1837                                         |
| c_tpm_cervical_spinal_cord__central_gray_2816                                     | decimal | TPM.cervical spinal cord, central gray.2816                                     |
| c_est_counts_cervical_spinal_cord__central_gray_2816                              | decimal | est_counts.cervical spinal cord, central gray.2816                              |
| c_tpm_cervical_spinal_cord__central_gray_2194                                     | decimal | TPM.cervical spinal cord, central gray.2194                                     |
| c_est_counts_cervical_spinal_cord__central_gray_2194                              | decimal | est_counts.cervical spinal cord, central gray.2194                              |
| c_tpm_cervical_spinal_cord__central_gray_1981                                     | decimal | TPM.cervical spinal cord, central gray.1981                                     |
| c_est_counts_cervical_spinal_cord__central_gray_1981                              | decimal | est_counts.cervical spinal cord, central gray.1981                              |
| c_tpm_cervical_spinal_cord__central_gray_2565                                     | decimal | TPM.cervical spinal cord, central gray.2565                                     |
| c_est_counts_cervical_spinal_cord__central_gray_2565                              | decimal | est_counts.cervical spinal cord, central gray.2565                              |
| c_tpm_cervical_spinal_cord__central_gray_2048                                     | decimal | TPM.cervical spinal cord, central gray.2048                                     |
| c_est_counts_cervical_spinal_cord__central_gray_2048                              | decimal | est_counts.cervical spinal cord, central gray.2048                              |
| c_tpm_cervical_spinal_cord__dorsal_horn_2069                                      | decimal | TPM.cervical spinal cord, dorsal horn.2069                                      |
| c_est_counts_cervical_spinal_cord__dorsal_horn_2069                               | decimal | est_counts.cervical spinal cord, dorsal horn.2069                               |
| c_tpm_cervical_spinal_cord__dorsal_horn_2173                                      | decimal | TPM.cervical spinal cord, dorsal horn.2173                                      |
| c_est_counts_cervical_spinal_cord__dorsal_horn_2173                               | decimal | est_counts.cervical spinal cord, dorsal horn.2173                               |
| c_tpm_cervical_spinal_cord__dorsal_horn_2721                                      | decimal | TPM.cervical spinal cord, dorsal horn.2721                                      |
| c_est_counts_cervical_spinal_cord__dorsal_horn_2721                               | decimal | est_counts.cervical spinal cord, dorsal horn.2721                               |
| c_tpm_cervical_spinal_cord__dorsal_horn_2297                                      | decimal | TPM.cervical spinal cord, dorsal horn.2297                                      |
| c_est_counts_cervical_spinal_cord__dorsal_horn_2297                               | decimal | est_counts.cervical spinal cord, dorsal horn.2297                               |
| c_tpm_cervical_spinal_cord__dorsal_horn_2296                                      | decimal | TPM.cervical spinal cord, dorsal horn.2296                                      |
| c_est_counts_cervical_spinal_cord__dorsal_horn_2296                               | decimal | est_counts.cervical spinal cord, dorsal horn.2296                               |
| c_tpm_cervical_spinal_cord__dorsal_horn_1877                                      | decimal | TPM.cervical spinal cord, dorsal horn.1877                                      |
| c_est_counts_cervical_spinal_cord__dorsal_horn_1877                               | decimal | est_counts.cervical spinal cord, dorsal horn.1877                               |
| c_tpm_cervical_spinal_cord__ventral_horn_2820                                     | decimal | TPM.cervical spinal cord, ventral horn.2820                                     |
| c_est_counts_cervical_spinal_cord__ventral_horn_2820                              | decimal | est_counts.cervical spinal cord, ventral horn.2820                              |
| c_tpm_cervical_spinal_cord__ventral_horn_2098                                     | decimal | TPM.cervical spinal cord, ventral horn.2098                                     |
| c_est_counts_cervical_spinal_cord__ventral_horn_2098                              | decimal | est_counts.cervical spinal cord, ventral horn.2098                              |
| c_tpm_cervical_spinal_cord__ventral_horn_2809                                     | decimal | TPM.cervical spinal cord, ventral horn.2809                                     |
| c_est_counts_cervical_spinal_cord__ventral_horn_2809                              | decimal | est_counts.cervical spinal cord, ventral horn.2809                              |
| c_tpm_cervical_spinal_cord__ventral_horn_2480                                     | decimal | TPM.cervical spinal cord, ventral horn.2480                                     |
| c_est_counts_cervical_spinal_cord__ventral_horn_2480                              | decimal | est_counts.cervical spinal cord, ventral horn.2480                              |
| c_tpm_cervical_spinal_cord__ventral_horn_2295                                     | decimal | TPM.cervical spinal cord, ventral horn.2295                                     |
| c_est_counts_cervical_spinal_cord__ventral_horn_2295                              | decimal | est_counts.cervical spinal cord, ventral horn.2295                              |
| c_tpm_cervical_spinal_cord__ventral_horn_2068                                     | decimal | TPM.cervical spinal cord, ventral horn.2068                                     |
| c_est_counts_cervical_spinal_cord__ventral_horn_2068                              | decimal | est_counts.cervical spinal cord, ventral horn.2068                              |
| c_tpm_choroid_plexus_2504                                                         | decimal | TPM.choroid plexus.2504                                                         |
| c_est_counts_choroid_plexus_2504                                                  | decimal | est_counts.choroid plexus.2504                                                  |
| c_tpm_choroid_plexus_2766                                                         | decimal | TPM.choroid plexus.2766                                                         |
| c_est_counts_choroid_plexus_2766                                                  | decimal | est_counts.choroid plexus.2766                                                  |
| c_tpm_choroid_plexus_2425                                                         | decimal | TPM.choroid plexus.2425                                                         |
| c_est_counts_choroid_plexus_2425                                                  | decimal | est_counts.choroid plexus.2425                                                  |
| c_tpm_choroid_plexus_2505                                                         | decimal | TPM.choroid plexus.2505                                                         |
| c_est_counts_choroid_plexus_2505                                                  | decimal | est_counts.choroid plexus.2505                                                  |
| c_tpm_claustrum_2196                                                              | decimal | TPM.claustrum.2196                                                              |
| c_est_counts_claustrum_2196                                                       | decimal | est_counts.claustrum.2196                                                       |
| c_tpm_claustrum_2645                                                              | decimal | TPM.claustrum.2645                                                              |
| c_est_counts_claustrum_2645                                                       | decimal | est_counts.claustrum.2645                                                       |
| c_tpm_claustrum_2568                                                              | decimal | TPM.claustrum.2568                                                              |
| c_est_counts_claustrum_2568                                                       | decimal | est_counts.claustrum.2568                                                       |
| c_tpm_claustrum_2198                                                              | decimal | TPM.claustrum.2198                                                              |
| c_est_counts_claustrum_2198                                                       | decimal | est_counts.claustrum.2198                                                       |
| c_tpm_claustrum_2491                                                              | decimal | TPM.claustrum.2491                                                              |
| c_est_counts_claustrum_2491                                                       | decimal | est_counts.claustrum.2491                                                       |
| c_tpm_claustrum_2284                                                              | decimal | TPM.claustrum.2284                                                              |
| c_est_counts_claustrum_2284                                                       | decimal | est_counts.claustrum.2284                                                       |
| c_tpm_claustrum_2392                                                              | decimal | TPM.claustrum.2392                                                              |
| c_est_counts_claustrum_2392                                                       | decimal | est_counts.claustrum.2392                                                       |
| c_tpm_claustrum_2292                                                              | decimal | TPM.claustrum.2292                                                              |
| c_est_counts_claustrum_2292                                                       | decimal | est_counts.claustrum.2292                                                       |
| c_tpm_claustrum_1956                                                              | decimal | TPM.claustrum.1956                                                              |
| c_est_counts_claustrum_1956                                                       | decimal | est_counts.claustrum.1956                                                       |
| c_tpm_corpus_callosum__genu__white_matter__1934                                   | decimal | TPM.corpus callosum, genu (white matter).1934                                   |
| c_est_counts_corpus_callosum__genu__white_matter__1934                            | decimal | est_counts.corpus callosum, genu (white matter).1934                            |
| c_tpm_corpus_callosum__genu__white_matter__2771                                   | decimal | TPM.corpus callosum, genu (white matter).2771                                   |
| c_est_counts_corpus_callosum__genu__white_matter__2771                            | decimal | est_counts.corpus callosum, genu (white matter).2771                            |
| c_tpm_corpus_callosum__genu__white_matter__1849                                   | decimal | TPM.corpus callosum, genu (white matter).1849                                   |
| c_est_counts_corpus_callosum__genu__white_matter__1849                            | decimal | est_counts.corpus callosum, genu (white matter).1849                            |
| c_tpm_corpus_callosum__genu__white_matter__1885                                   | decimal | TPM.corpus callosum, genu (white matter).1885                                   |
| c_est_counts_corpus_callosum__genu__white_matter__1885                            | decimal | est_counts.corpus callosum, genu (white matter).1885                            |
| c_tpm_corpus_callosum__genu__white_matter__1886                                   | decimal | TPM.corpus callosum, genu (white matter).1886                                   |
| c_est_counts_corpus_callosum__genu__white_matter__1886                            | decimal | est_counts.corpus callosum, genu (white matter).1886                            |
| c_tpm_corpus_callosum__genu__white_matter__1887                                   | decimal | TPM.corpus callosum, genu (white matter).1887                                   |
| c_est_counts_corpus_callosum__genu__white_matter__1887                            | decimal | est_counts.corpus callosum, genu (white matter).1887                            |
| c_tpm_corpus_callosum__splenium__white_matter__2104                               | decimal | TPM.corpus callosum, splenium (white matter).2104                               |
| c_est_counts_corpus_callosum__splenium__white_matter__2104                        | decimal | est_counts.corpus callosum, splenium (white matter).2104                        |
| c_tpm_corpus_callosum__splenium__white_matter__2238                               | decimal | TPM.corpus callosum, splenium (white matter).2238                               |
| c_est_counts_corpus_callosum__splenium__white_matter__2238                        | decimal | est_counts.corpus callosum, splenium (white matter).2238                        |
| c_tpm_corpus_callosum__splenium__white_matter__2847                               | decimal | TPM.corpus callosum, splenium (white matter).2847                               |
| c_est_counts_corpus_callosum__splenium__white_matter__2847                        | decimal | est_counts.corpus callosum, splenium (white matter).2847                        |
| c_tpm_corpus_callosum__splenium__white_matter__1946                               | decimal | TPM.corpus callosum, splenium (white matter).1946                               |
| c_est_counts_corpus_callosum__splenium__white_matter__1946                        | decimal | est_counts.corpus callosum, splenium (white matter).1946                        |
| c_tpm_corticomedial_amygdala_2829                                                 | decimal | TPM.corticomedial amygdala.2829                                                 |
| c_est_counts_corticomedial_amygdala_2829                                          | decimal | est_counts.corticomedial amygdala.2829                                          |
| c_tpm_corticomedial_amygdala_2428                                                 | decimal | TPM.corticomedial amygdala.2428                                                 |
| c_est_counts_corticomedial_amygdala_2428                                          | decimal | est_counts.corticomedial amygdala.2428                                          |
| c_tpm_corticomedial_amygdala_2242                                                 | decimal | TPM.corticomedial amygdala.2242                                                 |
| c_est_counts_corticomedial_amygdala_2242                                          | decimal | est_counts.corticomedial amygdala.2242                                          |
| c_tpm_corticomedial_amygdala_2429                                                 | decimal | TPM.corticomedial amygdala.2429                                                 |
| c_est_counts_corticomedial_amygdala_2429                                          | decimal | est_counts.corticomedial amygdala.2429                                          |
| c_tpm_corticomedial_amygdala_2535                                                 | decimal | TPM.corticomedial amygdala.2535                                                 |
| c_est_counts_corticomedial_amygdala_2535                                          | decimal | est_counts.corticomedial amygdala.2535                                          |
| c_tpm_corticomedial_amygdala_2240                                                 | decimal | TPM.corticomedial amygdala.2240                                                 |
| c_est_counts_corticomedial_amygdala_2240                                          | decimal | est_counts.corticomedial amygdala.2240                                          |
| c_tpm_cuneiform_nucleus_1870                                                      | decimal | TPM.cuneiform nucleus.1870                                                      |
| c_est_counts_cuneiform_nucleus_1870                                               | decimal | est_counts.cuneiform nucleus.1870                                               |
| c_tpm_cuneiform_nucleus_2828                                                      | decimal | TPM.cuneiform nucleus.2828                                                      |
| c_est_counts_cuneiform_nucleus_2828                                               | decimal | est_counts.cuneiform nucleus.2828                                               |
| c_tpm_cuneiform_nucleus_1827                                                      | decimal | TPM.cuneiform nucleus.1827                                                      |
| c_est_counts_cuneiform_nucleus_1827                                               | decimal | est_counts.cuneiform nucleus.1827                                               |
| c_tpm_cuneiform_nucleus_1833                                                      | decimal | TPM.cuneiform nucleus.1833                                                      |
| c_est_counts_cuneiform_nucleus_1833                                               | decimal | est_counts.cuneiform nucleus.1833                                               |
| c_tpm_cuneiform_nucleus_2019                                                      | decimal | TPM.cuneiform nucleus.2019                                                      |
| c_est_counts_cuneiform_nucleus_2019                                               | decimal | est_counts.cuneiform nucleus.2019                                               |
| c_tpm_cuneiform_nucleus_2411                                                      | decimal | TPM.cuneiform nucleus.2411                                                      |
| c_est_counts_cuneiform_nucleus_2411                                               | decimal | est_counts.cuneiform nucleus.2411                                               |
| c_tpm_cuneiform_nucleus_2586                                                      | decimal | TPM.cuneiform nucleus.2586                                                      |
| c_est_counts_cuneiform_nucleus_2586                                               | decimal | est_counts.cuneiform nucleus.2586                                               |
| c_tpm_cuneiform_nucleus_2666                                                      | decimal | TPM.cuneiform nucleus.2666                                                      |
| c_est_counts_cuneiform_nucleus_2666                                               | decimal | est_counts.cuneiform nucleus.2666                                               |
| c_tpm_cuneiform_nucleus_2219                                                      | decimal | TPM.cuneiform nucleus.2219                                                      |
| c_est_counts_cuneiform_nucleus_2219                                               | decimal | est_counts.cuneiform nucleus.2219                                               |
| c_tpm_cuneiform_nucleus_1830                                                      | decimal | TPM.cuneiform nucleus.1830                                                      |
| c_est_counts_cuneiform_nucleus_1830                                               | decimal | est_counts.cuneiform nucleus.1830                                               |
| c_tpm_dentate_gyrus_1927                                                          | decimal | TPM.dentate gyrus.1927                                                          |
| c_est_counts_dentate_gyrus_1927                                                   | decimal | est_counts.dentate gyrus.1927                                                   |
| c_tpm_dentate_gyrus_2528                                                          | decimal | TPM.dentate gyrus.2528                                                          |
| c_est_counts_dentate_gyrus_2528                                                   | decimal | est_counts.dentate gyrus.2528                                                   |
| c_tpm_dentate_gyrus_2530                                                          | decimal | TPM.dentate gyrus.2530                                                          |
| c_est_counts_dentate_gyrus_2530                                                   | decimal | est_counts.dentate gyrus.2530                                                   |
| c_tpm_dentate_gyrus_2246                                                          | decimal | TPM.dentate gyrus.2246                                                          |
| c_est_counts_dentate_gyrus_2246                                                   | decimal | est_counts.dentate gyrus.2246                                                   |
| c_tpm_dentate_gyrus_2531                                                          | decimal | TPM.dentate gyrus.2531                                                          |
| c_est_counts_dentate_gyrus_2531                                                   | decimal | est_counts.dentate gyrus.2531                                                   |
| c_tpm_dentate_gyrus_2010                                                          | decimal | TPM.dentate gyrus.2010                                                          |
| c_est_counts_dentate_gyrus_2010                                                   | decimal | est_counts.dentate gyrus.2010                                                   |
| c_tpm_dorsal_cochlear_nucleus_2370                                                | decimal | TPM.dorsal cochlear nucleus.2370                                                |
| c_est_counts_dorsal_cochlear_nucleus_2370                                         | decimal | est_counts.dorsal cochlear nucleus.2370                                         |
| c_tpm_dorsal_cochlear_nucleus_2378                                                | decimal | TPM.dorsal cochlear nucleus.2378                                                |
| c_est_counts_dorsal_cochlear_nucleus_2378                                         | decimal | est_counts.dorsal cochlear nucleus.2378                                         |
| c_tpm_dorsal_cochlear_nucleus_2187                                                | decimal | TPM.dorsal cochlear nucleus.2187                                                |
| c_est_counts_dorsal_cochlear_nucleus_2187                                         | decimal | est_counts.dorsal cochlear nucleus.2187                                         |
| c_tpm_dorsal_cochlear_nucleus_2802                                                | decimal | TPM.dorsal cochlear nucleus.2802                                                |
| c_est_counts_dorsal_cochlear_nucleus_2802                                         | decimal | est_counts.dorsal cochlear nucleus.2802                                         |
| c_tpm_dorsal_cochlear_nucleus_2058                                                | decimal | TPM.dorsal cochlear nucleus.2058                                                |
| c_est_counts_dorsal_cochlear_nucleus_2058                                         | decimal | est_counts.dorsal cochlear nucleus.2058                                         |
| c_tpm_dorsal_funiculus__white_matter__2817                                        | decimal | TPM.dorsal funiculus (white matter).2817                                        |
| c_est_counts_dorsal_funiculus__white_matter__2817                                 | decimal | est_counts.dorsal funiculus (white matter).2817                                 |
| c_tpm_dorsal_funiculus__white_matter__2064                                        | decimal | TPM.dorsal funiculus (white matter).2064                                        |
| c_est_counts_dorsal_funiculus__white_matter__2064                                 | decimal | est_counts.dorsal funiculus (white matter).2064                                 |
| c_tpm_dorsal_funiculus__white_matter__2810                                        | decimal | TPM.dorsal funiculus (white matter).2810                                        |
| c_est_counts_dorsal_funiculus__white_matter__2810                                 | decimal | est_counts.dorsal funiculus (white matter).2810                                 |
| c_tpm_dorsal_funiculus__white_matter__2128                                        | decimal | TPM.dorsal funiculus (white matter).2128                                        |
| c_est_counts_dorsal_funiculus__white_matter__2128                                 | decimal | est_counts.dorsal funiculus (white matter).2128                                 |
| c_tpm_dorsal_funiculus__white_matter__2812                                        | decimal | TPM.dorsal funiculus (white matter).2812                                        |
| c_est_counts_dorsal_funiculus__white_matter__2812                                 | decimal | est_counts.dorsal funiculus (white matter).2812                                 |
| c_tpm_dorsal_medullary_reticular_nucleus_2373                                     | decimal | TPM.dorsal medullary reticular nucleus.2373                                     |
| c_est_counts_dorsal_medullary_reticular_nucleus_2373                              | decimal | est_counts.dorsal medullary reticular nucleus.2373                              |
| c_tpm_dorsal_medullary_reticular_nucleus_2040                                     | decimal | TPM.dorsal medullary reticular nucleus.2040                                     |
| c_est_counts_dorsal_medullary_reticular_nucleus_2040                              | decimal | est_counts.dorsal medullary reticular nucleus.2040                              |
| c_tpm_dorsal_medullary_reticular_nucleus_2088                                     | decimal | TPM.dorsal medullary reticular nucleus.2088                                     |
| c_est_counts_dorsal_medullary_reticular_nucleus_2088                              | decimal | est_counts.dorsal medullary reticular nucleus.2088                              |
| c_tpm_dorsal_motor_vagal_complex_2813                                             | decimal | TPM.dorsal motor vagal complex.2813                                             |
| c_est_counts_dorsal_motor_vagal_complex_2813                                      | decimal | est_counts.dorsal motor vagal complex.2813                                      |
| c_tpm_dorsal_motor_vagal_complex_2797                                             | decimal | TPM.dorsal motor vagal complex.2797                                             |
| c_est_counts_dorsal_motor_vagal_complex_2797                                      | decimal | est_counts.dorsal motor vagal complex.2797                                      |
| c_tpm_dorsal_motor_vagal_complex_2133                                             | decimal | TPM.dorsal motor vagal complex.2133                                             |
| c_est_counts_dorsal_motor_vagal_complex_2133                                      | decimal | est_counts.dorsal motor vagal complex.2133                                      |
| c_tpm_dorsal_motor_vagal_complex_2643                                             | decimal | TPM.dorsal motor vagal complex.2643                                             |
| c_est_counts_dorsal_motor_vagal_complex_2643                                      | decimal | est_counts.dorsal motor vagal complex.2643                                      |
| c_tpm_dorsal_motor_vagal_complex_2807                                             | decimal | TPM.dorsal motor vagal complex.2807                                             |
| c_est_counts_dorsal_motor_vagal_complex_2807                                      | decimal | est_counts.dorsal motor vagal complex.2807                                      |
| c_tpm_dorsal_motor_vagal_complex_2185                                             | decimal | TPM.dorsal motor vagal complex.2185                                             |
| c_est_counts_dorsal_motor_vagal_complex_2185                                      | decimal | est_counts.dorsal motor vagal complex.2185                                      |
| c_tpm_dorsal_motor_vagal_complex_2844                                             | decimal | TPM.dorsal motor vagal complex.2844                                             |
| c_est_counts_dorsal_motor_vagal_complex_2844                                      | decimal | est_counts.dorsal motor vagal complex.2844                                      |
| c_tpm_dorsal_motor_vagal_complex_2000                                             | decimal | TPM.dorsal motor vagal complex.2000                                             |
| c_est_counts_dorsal_motor_vagal_complex_2000                                      | decimal | est_counts.dorsal motor vagal complex.2000                                      |
| c_tpm_dorsal_raphe_nucleus_2016                                                   | decimal | TPM.dorsal raphe nucleus.2016                                                   |
| c_est_counts_dorsal_raphe_nucleus_2016                                            | decimal | est_counts.dorsal raphe nucleus.2016                                            |
| c_tpm_dorsal_raphe_nucleus_2047                                                   | decimal | TPM.dorsal raphe nucleus.2047                                                   |
| c_est_counts_dorsal_raphe_nucleus_2047                                            | decimal | est_counts.dorsal raphe nucleus.2047                                            |
| c_tpm_dorsal_raphe_nucleus_1828                                                   | decimal | TPM.dorsal raphe nucleus.1828                                                   |
| c_est_counts_dorsal_raphe_nucleus_1828                                            | decimal | est_counts.dorsal raphe nucleus.1828                                            |
| c_tpm_dorsal_raphe_nucleus_2298                                                   | decimal | TPM.dorsal raphe nucleus.2298                                                   |
| c_est_counts_dorsal_raphe_nucleus_2298                                            | decimal | est_counts.dorsal raphe nucleus.2298                                            |
| c_tpm_dorsal_raphe_nucleus_2750                                                   | decimal | TPM.dorsal raphe nucleus.2750                                                   |
| c_est_counts_dorsal_raphe_nucleus_2750                                            | decimal | est_counts.dorsal raphe nucleus.2750                                            |
| c_tpm_dorsal_tegmental_nucleus_2358                                               | decimal | TPM.dorsal tegmental nucleus.2358                                               |
| c_est_counts_dorsal_tegmental_nucleus_2358                                        | decimal | est_counts.dorsal tegmental nucleus.2358                                        |
| c_tpm_dorsal_tegmental_nucleus_2083                                               | decimal | TPM.dorsal tegmental nucleus.2083                                               |
| c_est_counts_dorsal_tegmental_nucleus_2083                                        | decimal | est_counts.dorsal tegmental nucleus.2083                                        |
| c_tpm_dorsal_tegmental_nucleus_2326                                               | decimal | TPM.dorsal tegmental nucleus.2326                                               |
| c_est_counts_dorsal_tegmental_nucleus_2326                                        | decimal | est_counts.dorsal tegmental nucleus.2326                                        |
| c_tpm_dorsal_tegmental_nucleus_1936                                               | decimal | TPM.dorsal tegmental nucleus.1936                                               |
| c_est_counts_dorsal_tegmental_nucleus_1936                                        | decimal | est_counts.dorsal tegmental nucleus.1936                                        |
| c_tpm_dorsolateral_tegmental_area_2337                                            | decimal | TPM.dorsolateral tegmental area.2337                                            |
| c_est_counts_dorsolateral_tegmental_area_2337                                     | decimal | est_counts.dorsolateral tegmental area.2337                                     |
| c_tpm_dorsolateral_tegmental_area_2654                                            | decimal | TPM.dorsolateral tegmental area.2654                                            |
| c_est_counts_dorsolateral_tegmental_area_2654                                     | decimal | est_counts.dorsolateral tegmental area.2654                                     |
| c_tpm_dorsolateral_tegmental_area_2360                                            | decimal | TPM.dorsolateral tegmental area.2360                                            |
| c_est_counts_dorsolateral_tegmental_area_2360                                     | decimal | est_counts.dorsolateral tegmental area.2360                                     |
| c_tpm_dorsolateral_tegmental_area_2751                                            | decimal | TPM.dorsolateral tegmental area.2751                                            |
| c_est_counts_dorsolateral_tegmental_area_2751                                     | decimal | est_counts.dorsolateral tegmental area.2751                                     |
| c_tpm_dorsolateral_tegmental_area_2141                                            | decimal | TPM.dorsolateral tegmental area.2141                                            |
| c_est_counts_dorsolateral_tegmental_area_2141                                     | decimal | est_counts.dorsolateral tegmental area.2141                                     |
| c_tpm_dorsomedial_nucleus_2017                                                    | decimal | TPM.dorsomedial nucleus.2017                                                    |
| c_est_counts_dorsomedial_nucleus_2017                                             | decimal | est_counts.dorsomedial nucleus.2017                                             |
| c_tpm_dorsomedial_nucleus_2041                                                    | decimal | TPM.dorsomedial nucleus.2041                                                    |
| c_est_counts_dorsomedial_nucleus_2041                                             | decimal | est_counts.dorsomedial nucleus.2041                                             |
| c_tpm_dorsomedial_nucleus_1989                                                    | decimal | TPM.dorsomedial nucleus.1989                                                    |
| c_est_counts_dorsomedial_nucleus_1989                                             | decimal | est_counts.dorsomedial nucleus.1989                                             |
| c_tpm_entorhinal_gyrus_2764                                                       | decimal | TPM.entorhinal gyrus.2764                                                       |
| c_est_counts_entorhinal_gyrus_2764                                                | decimal | est_counts.entorhinal gyrus.2764                                                |
| c_tpm_entorhinal_gyrus_2686                                                       | decimal | TPM.entorhinal gyrus.2686                                                       |
| c_est_counts_entorhinal_gyrus_2686                                                | decimal | est_counts.entorhinal gyrus.2686                                                |
| c_tpm_entorhinal_gyrus_2117                                                       | decimal | TPM.entorhinal gyrus.2117                                                       |
| c_est_counts_entorhinal_gyrus_2117                                                | decimal | est_counts.entorhinal gyrus.2117                                                |
| c_tpm_entorhinal_gyrus_2613                                                       | decimal | TPM.entorhinal gyrus.2613                                                       |
| c_est_counts_entorhinal_gyrus_2613                                                | decimal | est_counts.entorhinal gyrus.2613                                                |
| c_tpm_entorhinal_gyrus_1938                                                       | decimal | TPM.entorhinal gyrus.1938                                                       |
| c_est_counts_entorhinal_gyrus_1938                                                | decimal | est_counts.entorhinal gyrus.1938                                                |
| c_tpm_entorhinal_gyrus_1787                                                       | decimal | TPM.entorhinal gyrus.1787                                                       |
| c_est_counts_entorhinal_gyrus_1787                                                | decimal | est_counts.entorhinal gyrus.1787                                                |
| c_tpm_flocculonodular_lobe_2004                                                   | decimal | TPM.flocculonodular lobe.2004                                                   |
| c_est_counts_flocculonodular_lobe_2004                                            | decimal | est_counts.flocculonodular lobe.2004                                            |
| c_tpm_flocculonodular_lobe_1771                                                   | decimal | TPM.flocculonodular lobe.1771                                                   |
| c_est_counts_flocculonodular_lobe_1771                                            | decimal | est_counts.flocculonodular lobe.1771                                            |
| c_tpm_flocculonodular_lobe_2176                                                   | decimal | TPM.flocculonodular lobe.2176                                                   |
| c_est_counts_flocculonodular_lobe_2176                                            | decimal | est_counts.flocculonodular lobe.2176                                            |
| c_tpm_flocculonodular_lobe_1835                                                   | decimal | TPM.flocculonodular lobe.1835                                                   |
| c_est_counts_flocculonodular_lobe_1835                                            | decimal | est_counts.flocculonodular lobe.1835                                            |
| c_tpm_flocculonodular_lobe_1767                                                   | decimal | TPM.flocculonodular lobe.1767                                                   |
| c_est_counts_flocculonodular_lobe_1767                                            | decimal | est_counts.flocculonodular lobe.1767                                            |
| c_tpm_flocculonodular_lobe_1765                                                   | decimal | TPM.flocculonodular lobe.1765                                                   |
| c_est_counts_flocculonodular_lobe_1765                                            | decimal | est_counts.flocculonodular lobe.1765                                            |
| c_tpm_flocculonodular_lobe_1792                                                   | decimal | TPM.flocculonodular lobe.1792                                                   |
| c_est_counts_flocculonodular_lobe_1792                                            | decimal | est_counts.flocculonodular lobe.1792                                            |
| c_tpm_frontal_eye_field_2147                                                      | decimal | TPM.frontal eye field.2147                                                      |
| c_est_counts_frontal_eye_field_2147                                               | decimal | est_counts.frontal eye field.2147                                               |
| c_tpm_frontal_eye_field_2441                                                      | decimal | TPM.frontal eye field.2441                                                      |
| c_est_counts_frontal_eye_field_2441                                               | decimal | est_counts.frontal eye field.2441                                               |
| c_tpm_frontal_eye_field_2543                                                      | decimal | TPM.frontal eye field.2543                                                      |
| c_est_counts_frontal_eye_field_2543                                               | decimal | est_counts.frontal eye field.2543                                               |
| c_tpm_frontal_eye_field_2761                                                      | decimal | TPM.frontal eye field.2761                                                      |
| c_est_counts_frontal_eye_field_2761                                               | decimal | est_counts.frontal eye field.2761                                               |
| c_tpm_frontal_operculum_2030                                                      | decimal | TPM.frontal operculum.2030                                                      |
| c_est_counts_frontal_operculum_2030                                               | decimal | est_counts.frontal operculum.2030                                               |
| c_tpm_frontal_operculum_2348                                                      | decimal | TPM.frontal operculum.2348                                                      |
| c_est_counts_frontal_operculum_2348                                               | decimal | est_counts.frontal operculum.2348                                               |
| c_tpm_frontal_operculum_2781                                                      | decimal | TPM.frontal operculum.2781                                                      |
| c_est_counts_frontal_operculum_2781                                               | decimal | est_counts.frontal operculum.2781                                               |
| c_tpm_fusiform_gyrus_2433                                                         | decimal | TPM.fusiform gyrus.2433                                                         |
| c_est_counts_fusiform_gyrus_2433                                                  | decimal | est_counts.fusiform gyrus.2433                                                  |
| c_tpm_fusiform_gyrus_2112                                                         | decimal | TPM.fusiform gyrus.2112                                                         |
| c_est_counts_fusiform_gyrus_2112                                                  | decimal | est_counts.fusiform gyrus.2112                                                  |
| c_tpm_fusiform_gyrus_2431                                                         | decimal | TPM.fusiform gyrus.2431                                                         |
| c_est_counts_fusiform_gyrus_2431                                                  | decimal | est_counts.fusiform gyrus.2431                                                  |
| c_tpm_fusiform_gyrus_2074                                                         | decimal | TPM.fusiform gyrus.2074                                                         |
| c_est_counts_fusiform_gyrus_2074                                                  | decimal | est_counts.fusiform gyrus.2074                                                  |
| c_tpm_fusiform_gyrus_2617                                                         | decimal | TPM.fusiform gyrus.2617                                                         |
| c_est_counts_fusiform_gyrus_2617                                                  | decimal | est_counts.fusiform gyrus.2617                                                  |
| c_tpm_fusiform_gyrus_2784                                                         | decimal | TPM.fusiform gyrus.2784                                                         |
| c_est_counts_fusiform_gyrus_2784                                                  | decimal | est_counts.fusiform gyrus.2784                                                  |
| c_tpm_fusiform_gyrus_1807                                                         | decimal | TPM.fusiform gyrus.1807                                                         |
| c_est_counts_fusiform_gyrus_1807                                                  | decimal | est_counts.fusiform gyrus.1807                                                  |
| c_tpm_gigantocellular_reticular_nuclei__medullary_2314                            | decimal | TPM.gigantocellular reticular nuclei, medullary.2314                            |
| c_est_counts_gigantocellular_reticular_nuclei__medullary_2314                     | decimal | est_counts.gigantocellular reticular nuclei, medullary.2314                     |
| c_tpm_gigantocellular_reticular_nuclei__medullary_2310                            | decimal | TPM.gigantocellular reticular nuclei, medullary.2310                            |
| c_est_counts_gigantocellular_reticular_nuclei__medullary_2310                     | decimal | est_counts.gigantocellular reticular nuclei, medullary.2310                     |
| c_tpm_gigantocellular_reticular_nuclei__medullary_2387                            | decimal | TPM.gigantocellular reticular nuclei, medullary.2387                            |
| c_est_counts_gigantocellular_reticular_nuclei__medullary_2387                     | decimal | est_counts.gigantocellular reticular nuclei, medullary.2387                     |
| c_tpm_gigantocellular_reticular_nuclei__medullary_2462                            | decimal | TPM.gigantocellular reticular nuclei, medullary.2462                            |
| c_est_counts_gigantocellular_reticular_nuclei__medullary_2462                     | decimal | est_counts.gigantocellular reticular nuclei, medullary.2462                     |
| c_tpm_gigantocellular_reticular_nuclei__medullary_1876                            | decimal | TPM.gigantocellular reticular nuclei, medullary.1876                            |
| c_est_counts_gigantocellular_reticular_nuclei__medullary_1876                     | decimal | est_counts.gigantocellular reticular nuclei, medullary.1876                     |
| c_tpm_gigantocellular_reticular_nuclei__medullary_2022                            | decimal | TPM.gigantocellular reticular nuclei, medullary.2022                            |
| c_est_counts_gigantocellular_reticular_nuclei__medullary_2022                     | decimal | est_counts.gigantocellular reticular nuclei, medullary.2022                     |
| c_tpm_gigantocellular_reticular_nuclei__pars_2336                                 | decimal | TPM.gigantocellular reticular nuclei, pars.2336                                 |
| c_est_counts_gigantocellular_reticular_nuclei__pars_2336                          | decimal | est_counts.gigantocellular reticular nuclei, pars.2336                          |
| c_tpm_gigantocellular_reticular_nuclei__pars_2330                                 | decimal | TPM.gigantocellular reticular nuclei, pars.2330                                 |
| c_est_counts_gigantocellular_reticular_nuclei__pars_2330                          | decimal | est_counts.gigantocellular reticular nuclei, pars.2330                          |
| c_tpm_gigantocellular_reticular_nuclei__pars_2706                                 | decimal | TPM.gigantocellular reticular nuclei, pars.2706                                 |
| c_est_counts_gigantocellular_reticular_nuclei__pars_2706                          | decimal | est_counts.gigantocellular reticular nuclei, pars.2706                          |
| c_tpm_gigantocellular_reticular_nuclei__pars_2084                                 | decimal | TPM.gigantocellular reticular nuclei, pars.2084                                 |
| c_est_counts_gigantocellular_reticular_nuclei__pars_2084                          | decimal | est_counts.gigantocellular reticular nuclei, pars.2084                          |
| c_tpm_gigantocellular_reticular_nuclei__pars_2168                                 | decimal | TPM.gigantocellular reticular nuclei, pars.2168                                 |
| c_est_counts_gigantocellular_reticular_nuclei__pars_2168                          | decimal | est_counts.gigantocellular reticular nuclei, pars.2168                          |
| c_tpm_globus_pallidus__externus_2772                                              | decimal | TPM.globus pallidus, externus.2772                                              |
| c_est_counts_globus_pallidus__externus_2772                                       | decimal | est_counts.globus pallidus, externus.2772                                       |
| c_tpm_globus_pallidus__externus_2567                                              | decimal | TPM.globus pallidus, externus.2567                                              |
| c_est_counts_globus_pallidus__externus_2567                                       | decimal | est_counts.globus pallidus, externus.2567                                       |
| c_tpm_globus_pallidus__externus_2646                                              | decimal | TPM.globus pallidus, externus.2646                                              |
| c_est_counts_globus_pallidus__externus_2646                                       | decimal | est_counts.globus pallidus, externus.2646                                       |
| c_tpm_globus_pallidus__externus_1996                                              | decimal | TPM.globus pallidus, externus.1996                                              |
| c_est_counts_globus_pallidus__externus_1996                                       | decimal | est_counts.globus pallidus, externus.1996                                       |
| c_tpm_globus_pallidus__externus_2395                                              | decimal | TPM.globus pallidus, externus.2395                                              |
| c_est_counts_globus_pallidus__externus_2395                                       | decimal | est_counts.globus pallidus, externus.2395                                       |
| c_tpm_globus_pallidus__internus_2566                                              | decimal | TPM.globus pallidus, internus.2566                                              |
| c_est_counts_globus_pallidus__internus_2566                                       | decimal | est_counts.globus pallidus, internus.2566                                       |
| c_tpm_globus_pallidus__internus_2037                                              | decimal | TPM.globus pallidus, internus.2037                                              |
| c_est_counts_globus_pallidus__internus_2037                                       | decimal | est_counts.globus pallidus, internus.2037                                       |
| c_tpm_globus_pallidus__internus_2287                                              | decimal | TPM.globus pallidus, internus.2287                                              |
| c_est_counts_globus_pallidus__internus_2287                                       | decimal | est_counts.globus pallidus, internus.2287                                       |
| c_tpm_globus_pallidus__internus_2778                                              | decimal | TPM.globus pallidus, internus.2778                                              |
| c_est_counts_globus_pallidus__internus_2778                                       | decimal | est_counts.globus pallidus, internus.2778                                       |
| c_tpm_globus_pallidus__internus_2483                                              | decimal | TPM.globus pallidus, internus.2483                                              |
| c_est_counts_globus_pallidus__internus_2483                                       | decimal | est_counts.globus pallidus, internus.2483                                       |
| c_tpm_globus_pallidus__internus_2111                                              | decimal | TPM.globus pallidus, internus.2111                                              |
| c_est_counts_globus_pallidus__internus_2111                                       | decimal | est_counts.globus pallidus, internus.2111                                       |
| c_tpm_globus_pallidus__internus_1818                                              | decimal | TPM.globus pallidus, internus.1818                                              |
| c_est_counts_globus_pallidus__internus_1818                                       | decimal | est_counts.globus pallidus, internus.1818                                       |
| c_tpm_habenula_2252                                                               | decimal | TPM.habenula.2252                                                               |
| c_est_counts_habenula_2252                                                        | decimal | est_counts.habenula.2252                                                        |
| c_tpm_habenula_2276                                                               | decimal | TPM.habenula.2276                                                               |
| c_est_counts_habenula_2276                                                        | decimal | est_counts.habenula.2276                                                        |
| c_tpm_habenula_2203                                                               | decimal | TPM.habenula.2203                                                               |
| c_est_counts_habenula_2203                                                        | decimal | est_counts.habenula.2203                                                        |
| c_tpm_habenula_1957                                                               | decimal | TPM.habenula.1957                                                               |
| c_est_counts_habenula_1957                                                        | decimal | est_counts.habenula.1957                                                        |
| c_tpm_hippocampus_1898                                                            | decimal | TPM.hippocampus.1898                                                            |
| c_est_counts_hippocampus_1898                                                     | decimal | est_counts.hippocampus.1898                                                     |
| c_tpm_hippocampus_2148                                                            | decimal | TPM.hippocampus.2148                                                            |
| c_est_counts_hippocampus_2148                                                     | decimal | est_counts.hippocampus.2148                                                     |
| c_tpm_hippocampus_2529                                                            | decimal | TPM.hippocampus.2529                                                            |
| c_est_counts_hippocampus_2529                                                     | decimal | est_counts.hippocampus.2529                                                     |
| c_tpm_hippocampus_1911                                                            | decimal | TPM.hippocampus.1911                                                            |
| c_est_counts_hippocampus_1911                                                     | decimal | est_counts.hippocampus.1911                                                     |
| c_tpm_hippocampus_2621                                                            | decimal | TPM.hippocampus.2621                                                            |
| c_est_counts_hippocampus_2621                                                     | decimal | est_counts.hippocampus.2621                                                     |
| c_tpm_hippocampus_1855                                                            | decimal | TPM.hippocampus.1855                                                            |
| c_est_counts_hippocampus_1855                                                     | decimal | est_counts.hippocampus.1855                                                     |
| c_tpm_hippocampus__ca1_2749                                                       | decimal | TPM.hippocampus, CA1.2749                                                       |
| c_est_counts_hippocampus__ca1_2749                                                | decimal | est_counts.hippocampus, CA1.2749                                                |
| c_tpm_hippocampus__ca1_2082                                                       | decimal | TPM.hippocampus, CA1.2082                                                       |
| c_est_counts_hippocampus__ca1_2082                                                | decimal | est_counts.hippocampus, CA1.2082                                                |
| c_tpm_hippocampus__ca1_2527                                                       | decimal | TPM.hippocampus, CA1.2527                                                       |
| c_est_counts_hippocampus__ca1_2527                                                | decimal | est_counts.hippocampus, CA1.2527                                                |
| c_tpm_hippocampus__ca1_1873                                                       | decimal | TPM.hippocampus, CA1.1873                                                       |
| c_est_counts_hippocampus__ca1_1873                                                | decimal | est_counts.hippocampus, CA1.1873                                                |
| c_tpm_hippocampus__ca1_2045                                                       | decimal | TPM.hippocampus, CA1.2045                                                       |
| c_est_counts_hippocampus__ca1_2045                                                | decimal | est_counts.hippocampus, CA1.2045                                                |
| c_tpm_hippocampus__ca2_1963                                                       | decimal | TPM.hippocampus, CA2.1963                                                       |
| c_est_counts_hippocampus__ca2_1963                                                | decimal | est_counts.hippocampus, CA2.1963                                                |
| c_tpm_hippocampus__ca2_2113                                                       | decimal | TPM.hippocampus, CA2.2113                                                       |
| c_est_counts_hippocampus__ca2_2113                                                | decimal | est_counts.hippocampus, CA2.2113                                                |
| c_tpm_hippocampus__ca2_2249                                                       | decimal | TPM.hippocampus, CA2.2249                                                       |
| c_est_counts_hippocampus__ca2_2249                                                | decimal | est_counts.hippocampus, CA2.2249                                                |
| c_tpm_hippocampus__ca2_2437                                                       | decimal | TPM.hippocampus, CA2.2437                                                       |
| c_est_counts_hippocampus__ca2_2437                                                | decimal | est_counts.hippocampus, CA2.2437                                                |
| c_tpm_hippocampus__ca2_1940                                                       | decimal | TPM.hippocampus, CA2.1940                                                       |
| c_est_counts_hippocampus__ca2_1940                                                | decimal | est_counts.hippocampus, CA2.1940                                                |
| c_tpm_hippocampus__ca2_1892                                                       | decimal | TPM.hippocampus, CA2.1892                                                       |
| c_est_counts_hippocampus__ca2_1892                                                | decimal | est_counts.hippocampus, CA2.1892                                                |
| c_tpm_hippocampus__ca3_2137                                                       | decimal | TPM.hippocampus, CA3.2137                                                       |
| c_est_counts_hippocampus__ca3_2137                                                | decimal | est_counts.hippocampus, CA3.2137                                                |
| c_tpm_hippocampus__ca3_2436                                                       | decimal | TPM.hippocampus, CA3.2436                                                       |
| c_est_counts_hippocampus__ca3_2436                                                | decimal | est_counts.hippocampus, CA3.2436                                                |
| c_tpm_hippocampus__ca3_2620                                                       | decimal | TPM.hippocampus, CA3.2620                                                       |
| c_est_counts_hippocampus__ca3_2620                                                | decimal | est_counts.hippocampus, CA3.2620                                                |
| c_tpm_hippocampus__ca3_1891                                                       | decimal | TPM.hippocampus, CA3.1891                                                       |
| c_est_counts_hippocampus__ca3_1891                                                | decimal | est_counts.hippocampus, CA3.1891                                                |
| c_tpm_hippocampus__ca3_2861                                                       | decimal | TPM.hippocampus, CA3.2861                                                       |
| c_est_counts_hippocampus__ca3_2861                                                | decimal | est_counts.hippocampus, CA3.2861                                                |
| c_tpm_hippocampus__ca3_1867                                                       | decimal | TPM.hippocampus, CA3.1867                                                       |
| c_est_counts_hippocampus__ca3_1867                                                | decimal | est_counts.hippocampus, CA3.1867                                                |
| c_tpm_inferior_colliculus_1848                                                    | decimal | TPM.inferior colliculus.1848                                                    |
| c_est_counts_inferior_colliculus_1848                                             | decimal | est_counts.inferior colliculus.1848                                             |
| c_tpm_inferior_colliculus_2849                                                    | decimal | TPM.inferior colliculus.2849                                                    |
| c_est_counts_inferior_colliculus_2849                                             | decimal | est_counts.inferior colliculus.2849                                             |
| c_tpm_inferior_colliculus_1890                                                    | decimal | TPM.inferior colliculus.1890                                                    |
| c_est_counts_inferior_colliculus_1890                                             | decimal | est_counts.inferior colliculus.1890                                             |
| c_tpm_inferior_colliculus_2097                                                    | decimal | TPM.inferior colliculus.2097                                                    |
| c_est_counts_inferior_colliculus_2097                                             | decimal | est_counts.inferior colliculus.2097                                             |
| c_tpm_inferior_frontal_gyrus__opercular_2865                                      | decimal | TPM.inferior frontal gyrus, opercular.2865                                      |
| c_est_counts_inferior_frontal_gyrus__opercular_2865                               | decimal | est_counts.inferior frontal gyrus, opercular.2865                               |
| c_tpm_inferior_frontal_gyrus__opercular_2866                                      | decimal | TPM.inferior frontal gyrus, opercular.2866                                      |
| c_est_counts_inferior_frontal_gyrus__opercular_2866                               | decimal | est_counts.inferior frontal gyrus, opercular.2866                               |
| c_tpm_inferior_frontal_gyrus__opercular_2867                                      | decimal | TPM.inferior frontal gyrus, opercular.2867                                      |
| c_est_counts_inferior_frontal_gyrus__opercular_2867                               | decimal | est_counts.inferior frontal gyrus, opercular.2867                               |
| c_tpm_inferior_frontal_gyrus__opercular_2868                                      | decimal | TPM.inferior frontal gyrus, opercular.2868                                      |
| c_est_counts_inferior_frontal_gyrus__opercular_2868                               | decimal | est_counts.inferior frontal gyrus, opercular.2868                               |
| c_tpm_inferior_frontal_gyrus__opercular_2869                                      | decimal | TPM.inferior frontal gyrus, opercular.2869                                      |
| c_est_counts_inferior_frontal_gyrus__opercular_2869                               | decimal | est_counts.inferior frontal gyrus, opercular.2869                               |
| c_tpm_inferior_frontal_gyrus__opercular_2871                                      | decimal | TPM.inferior frontal gyrus, opercular.2871                                      |
| c_est_counts_inferior_frontal_gyrus__opercular_2871                               | decimal | est_counts.inferior frontal gyrus, opercular.2871                               |
| c_tpm_inferior_frontal_gyrus__opercular_2872                                      | decimal | TPM.inferior frontal gyrus, opercular.2872                                      |
| c_est_counts_inferior_frontal_gyrus__opercular_2872                               | decimal | est_counts.inferior frontal gyrus, opercular.2872                               |
| c_tpm_inferior_frontal_gyrus__opercular_2873                                      | decimal | TPM.inferior frontal gyrus, opercular.2873                                      |
| c_est_counts_inferior_frontal_gyrus__opercular_2873                               | decimal | est_counts.inferior frontal gyrus, opercular.2873                               |
| c_tpm_inferior_frontal_gyrus__opercular_2874                                      | decimal | TPM.inferior frontal gyrus, opercular.2874                                      |
| c_est_counts_inferior_frontal_gyrus__opercular_2874                               | decimal | est_counts.inferior frontal gyrus, opercular.2874                               |
| c_tpm_inferior_frontal_gyrus__opercular_2875                                      | decimal | TPM.inferior frontal gyrus, opercular.2875                                      |
| c_est_counts_inferior_frontal_gyrus__opercular_2875                               | decimal | est_counts.inferior frontal gyrus, opercular.2875                               |
| c_tpm_inferior_olive_2178                                                         | decimal | TPM.inferior olive.2178                                                         |
| c_est_counts_inferior_olive_2178                                                  | decimal | est_counts.inferior olive.2178                                                  |
| c_tpm_inferior_olive_2379                                                         | decimal | TPM.inferior olive.2379                                                         |
| c_est_counts_inferior_olive_2379                                                  | decimal | est_counts.inferior olive.2379                                                  |
| c_tpm_inferior_olive_2628                                                         | decimal | TPM.inferior olive.2628                                                         |
| c_est_counts_inferior_olive_2628                                                  | decimal | est_counts.inferior olive.2628                                                  |
| c_tpm_inferior_olive_2563                                                         | decimal | TPM.inferior olive.2563                                                         |
| c_est_counts_inferior_olive_2563                                                  | decimal | est_counts.inferior olive.2563                                                  |
| c_tpm_inferior_olive_2085                                                         | decimal | TPM.inferior olive.2085                                                         |
| c_est_counts_inferior_olive_2085                                                  | decimal | est_counts.inferior olive.2085                                                  |
| c_tpm_inferior_parietal_lobule_2418                                               | decimal | TPM.inferior parietal lobule.2418                                               |
| c_est_counts_inferior_parietal_lobule_2418                                        | decimal | est_counts.inferior parietal lobule.2418                                        |
| c_tpm_inferior_parietal_lobule_2599                                               | decimal | TPM.inferior parietal lobule.2599                                               |
| c_est_counts_inferior_parietal_lobule_2599                                        | decimal | est_counts.inferior parietal lobule.2599                                        |
| c_tpm_inferior_parietal_lobule_2606                                               | decimal | TPM.inferior parietal lobule.2606                                               |
| c_est_counts_inferior_parietal_lobule_2606                                        | decimal | est_counts.inferior parietal lobule.2606                                        |
| c_tpm_inferior_parietal_lobule_2876                                               | decimal | TPM.inferior parietal lobule.2876                                               |
| c_est_counts_inferior_parietal_lobule_2876                                        | decimal | est_counts.inferior parietal lobule.2876                                        |
| c_tpm_inferior_temporal_gyrus_1880                                                | decimal | TPM.inferior temporal gyrus.1880                                                |
| c_est_counts_inferior_temporal_gyrus_1880                                         | decimal | est_counts.inferior temporal gyrus.1880                                         |
| c_tpm_inferior_temporal_gyrus_2430                                                | decimal | TPM.inferior temporal gyrus.2430                                                |
| c_est_counts_inferior_temporal_gyrus_2430                                         | decimal | est_counts.inferior temporal gyrus.2430                                         |
| c_tpm_inferior_temporal_gyrus_1965                                                | decimal | TPM.inferior temporal gyrus.1965                                                |
| c_est_counts_inferior_temporal_gyrus_1965                                         | decimal | est_counts.inferior temporal gyrus.1965                                         |
| c_tpm_inferior_temporal_gyrus_2689                                                | decimal | TPM.inferior temporal gyrus.2689                                                |
| c_est_counts_inferior_temporal_gyrus_2689                                         | decimal | est_counts.inferior temporal gyrus.2689                                         |
| c_tpm_inferior_temporal_gyrus_1970                                                | decimal | TPM.inferior temporal gyrus.1970                                                |
| c_est_counts_inferior_temporal_gyrus_1970                                         | decimal | est_counts.inferior temporal gyrus.1970                                         |
| c_tpm_inferior_temporal_gyrus_1808                                                | decimal | TPM.inferior temporal gyrus.1808                                                |
| c_est_counts_inferior_temporal_gyrus_1808                                         | decimal | est_counts.inferior temporal gyrus.1808                                         |
| c_tpm_intraparietal_deep_sulcus_2230                                              | decimal | TPM.intraparietal deep sulcus.2230                                              |
| c_est_counts_intraparietal_deep_sulcus_2230                                       | decimal | est_counts.intraparietal deep sulcus.2230                                       |
| c_tpm_intraparietal_deep_sulcus_2669                                              | decimal | TPM.intraparietal deep sulcus.2669                                              |
| c_est_counts_intraparietal_deep_sulcus_2669                                       | decimal | est_counts.intraparietal deep sulcus.2669                                       |
| c_tpm_intraparietal_deep_sulcus_2102                                              | decimal | TPM.intraparietal deep sulcus.2102                                              |
| c_est_counts_intraparietal_deep_sulcus_2102                                       | decimal | est_counts.intraparietal deep sulcus.2102                                       |
| c_tpm_intraparietal_deep_sulcus_2600                                              | decimal | TPM.intraparietal deep sulcus.2600                                              |
| c_est_counts_intraparietal_deep_sulcus_2600                                       | decimal | est_counts.intraparietal deep sulcus.2600                                       |
| c_tpm_intraparietal_deep_sulcus_2607                                              | decimal | TPM.intraparietal deep sulcus.2607                                              |
| c_est_counts_intraparietal_deep_sulcus_2607                                       | decimal | est_counts.intraparietal deep sulcus.2607                                       |
| c_tpm_intraparietal_deep_sulcus_2798                                              | decimal | TPM.intraparietal deep sulcus.2798                                              |
| c_est_counts_intraparietal_deep_sulcus_2798                                       | decimal | est_counts.intraparietal deep sulcus.2798                                       |
| c_tpm_kolliker_fuse_nucleus_2163                                                  | decimal | TPM.Kolliker-Fuse nucleus.2163                                                  |
| c_est_counts_kolliker_fuse_nucleus_2163                                           | decimal | est_counts.Kolliker-Fuse nucleus.2163                                           |
| c_tpm_kolliker_fuse_nucleus_2793                                                  | decimal | TPM.Kolliker-Fuse nucleus.2793                                                  |
| c_est_counts_kolliker_fuse_nucleus_2793                                           | decimal | est_counts.Kolliker-Fuse nucleus.2793                                           |
| c_tpm_kolliker_fuse_nucleus_2315                                                  | decimal | TPM.Kolliker-Fuse nucleus.2315                                                  |
| c_est_counts_kolliker_fuse_nucleus_2315                                           | decimal | est_counts.Kolliker-Fuse nucleus.2315                                           |
| c_tpm_lateral_amygdala_2256                                                       | decimal | TPM.lateral amygdala.2256                                                       |
| c_est_counts_lateral_amygdala_2256                                                | decimal | est_counts.lateral amygdala.2256                                                |
| c_tpm_lateral_amygdala_2516                                                       | decimal | TPM.lateral amygdala.2516                                                       |
| c_est_counts_lateral_amygdala_2516                                                | decimal | est_counts.lateral amygdala.2516                                                |
| c_tpm_lateral_amygdala_2255                                                       | decimal | TPM.lateral amygdala.2255                                                       |
| c_est_counts_lateral_amygdala_2255                                                | decimal | est_counts.lateral amygdala.2255                                                |
| c_tpm_lateral_amygdala_2534                                                       | decimal | TPM.lateral amygdala.2534                                                       |
| c_est_counts_lateral_amygdala_2534                                                | decimal | est_counts.lateral amygdala.2534                                                |
| c_tpm_lateral_amygdala_2830                                                       | decimal | TPM.lateral amygdala.2830                                                       |
| c_est_counts_lateral_amygdala_2830                                                | decimal | est_counts.lateral amygdala.2830                                                |
| c_tpm_lateral_amygdala_1883                                                       | decimal | TPM.lateral amygdala.1883                                                       |
| c_est_counts_lateral_amygdala_1883                                                | decimal | est_counts.lateral amygdala.1883                                                |
| c_tpm_lateral_funiculus__white_matter__2094                                       | decimal | TPM.lateral funiculus (white matter).2094                                       |
| c_est_counts_lateral_funiculus__white_matter__2094                                | decimal | est_counts.lateral funiculus (white matter).2094                                |
| c_tpm_lateral_funiculus__white_matter__2099                                       | decimal | TPM.lateral funiculus (white matter).2099                                       |
| c_est_counts_lateral_funiculus__white_matter__2099                                | decimal | est_counts.lateral funiculus (white matter).2099                                |
| c_tpm_lateral_funiculus__white_matter__2192                                       | decimal | TPM.lateral funiculus (white matter).2192                                       |
| c_est_counts_lateral_funiculus__white_matter__2192                                | decimal | est_counts.lateral funiculus (white matter).2192                                |
| c_tpm_lateral_funiculus__white_matter__2294                                       | decimal | TPM.lateral funiculus (white matter).2294                                       |
| c_est_counts_lateral_funiculus__white_matter__2294                                | decimal | est_counts.lateral funiculus (white matter).2294                                |
| c_tpm_lateral_geniculate_body_2035                                                | decimal | TPM.lateral geniculate body.2035                                                |
| c_est_counts_lateral_geniculate_body_2035                                         | decimal | est_counts.lateral geniculate body.2035                                         |
| c_tpm_lateral_geniculate_body_1953                                                | decimal | TPM.lateral geniculate body.1953                                                |
| c_est_counts_lateral_geniculate_body_1953                                         | decimal | est_counts.lateral geniculate body.1953                                         |
| c_tpm_lateral_geniculate_body_2659                                                | decimal | TPM.lateral geniculate body.2659                                                |
| c_est_counts_lateral_geniculate_body_2659                                         | decimal | est_counts.lateral geniculate body.2659                                         |
| c_tpm_lateral_geniculate_body_2399                                                | decimal | TPM.lateral geniculate body.2399                                                |
| c_est_counts_lateral_geniculate_body_2399                                         | decimal | est_counts.lateral geniculate body.2399                                         |
| c_tpm_lateral_geniculate_body_2841                                                | decimal | TPM.lateral geniculate body.2841                                                |
| c_est_counts_lateral_geniculate_body_2841                                         | decimal | est_counts.lateral geniculate body.2841                                         |
| c_tpm_lateral_geniculate_body_2857                                                | decimal | TPM.lateral geniculate body.2857                                                |
| c_est_counts_lateral_geniculate_body_2857                                         | decimal | est_counts.lateral geniculate body.2857                                         |
| c_tpm_lateral_geniculate_body_2575                                                | decimal | TPM.lateral geniculate body.2575                                                |
| c_est_counts_lateral_geniculate_body_2575                                         | decimal | est_counts.lateral geniculate body.2575                                         |
| c_tpm_lateral_geniculate_body_2106                                                | decimal | TPM.lateral geniculate body.2106                                                |
| c_est_counts_lateral_geniculate_body_2106                                         | decimal | est_counts.lateral geniculate body.2106                                         |
| c_tpm_lateral_hypothalamic_area_2412                                              | decimal | TPM.lateral hypothalamic area.2412                                              |
| c_est_counts_lateral_hypothalamic_area_2412                                       | decimal | est_counts.lateral hypothalamic area.2412                                       |
| c_tpm_lateral_hypothalamic_area_2228                                              | decimal | TPM.lateral hypothalamic area.2228                                              |
| c_est_counts_lateral_hypothalamic_area_2228                                       | decimal | est_counts.lateral hypothalamic area.2228                                       |
| c_tpm_lateral_hypothalamic_area_1791                                              | decimal | TPM.lateral hypothalamic area.1791                                              |
| c_est_counts_lateral_hypothalamic_area_1791                                       | decimal | est_counts.lateral hypothalamic area.1791                                       |
| c_tpm_lateral_hypothalamic_area_2271                                              | decimal | TPM.lateral hypothalamic area.2271                                              |
| c_est_counts_lateral_hypothalamic_area_2271                                       | decimal | est_counts.lateral hypothalamic area.2271                                       |
| c_tpm_lateral_lemniscal_nuclei_2036                                               | decimal | TPM.lateral lemniscal nuclei.2036                                               |
| c_est_counts_lateral_lemniscal_nuclei_2036                                        | decimal | est_counts.lateral lemniscal nuclei.2036                                        |
| c_tpm_lateral_lemniscal_nuclei_2320                                               | decimal | TPM.lateral lemniscal nuclei.2320                                               |
| c_est_counts_lateral_lemniscal_nuclei_2320                                        | decimal | est_counts.lateral lemniscal nuclei.2320                                        |
| c_tpm_lateral_lemniscal_nuclei_2453                                               | decimal | TPM.lateral lemniscal nuclei.2453                                               |
| c_est_counts_lateral_lemniscal_nuclei_2453                                        | decimal | est_counts.lateral lemniscal nuclei.2453                                        |
| c_tpm_lateral_lemniscal_nuclei_2746                                               | decimal | TPM.lateral lemniscal nuclei.2746                                               |
| c_est_counts_lateral_lemniscal_nuclei_2746                                        | decimal | est_counts.lateral lemniscal nuclei.2746                                        |
| c_tpm_lateral_lemniscal_nuclei_2169                                               | decimal | TPM.lateral lemniscal nuclei.2169                                               |
| c_est_counts_lateral_lemniscal_nuclei_2169                                        | decimal | est_counts.lateral lemniscal nuclei.2169                                        |
| c_tpm_lateral_medullary_reticular_nucleus_2374                                    | decimal | TPM.lateral medullary reticular nucleus.2374                                    |
| c_est_counts_lateral_medullary_reticular_nucleus_2374                             | decimal | est_counts.lateral medullary reticular nucleus.2374                             |
| c_tpm_lateral_medullary_reticular_nucleus_2852                                    | decimal | TPM.lateral medullary reticular nucleus.2852                                    |
| c_est_counts_lateral_medullary_reticular_nucleus_2852                             | decimal | est_counts.lateral medullary reticular nucleus.2852                             |
| c_tpm_lateral_medullary_reticular_nucleus_2804                                    | decimal | TPM.lateral medullary reticular nucleus.2804                                    |
| c_est_counts_lateral_medullary_reticular_nucleus_2804                             | decimal | est_counts.lateral medullary reticular nucleus.2804                             |
| c_tpm_lateral_medullary_reticular_nucleus_2305                                    | decimal | TPM.lateral medullary reticular nucleus.2305                                    |
| c_est_counts_lateral_medullary_reticular_nucleus_2305                             | decimal | est_counts.lateral medullary reticular nucleus.2305                             |
| c_tpm_lateral_medullary_reticular_nucleus_2190                                    | decimal | TPM.lateral medullary reticular nucleus.2190                                    |
| c_est_counts_lateral_medullary_reticular_nucleus_2190                             | decimal | est_counts.lateral medullary reticular nucleus.2190                             |
| c_tpm_lateral_medullary_reticular_nucleus_2044                                    | decimal | TPM.lateral medullary reticular nucleus.2044                                    |
| c_est_counts_lateral_medullary_reticular_nucleus_2044                             | decimal | est_counts.lateral medullary reticular nucleus.2044                             |
| c_tpm_lateral_parabrachial_nucleus_2790                                           | decimal | TPM.lateral parabrachial nucleus.2790                                           |
| c_est_counts_lateral_parabrachial_nucleus_2790                                    | decimal | est_counts.lateral parabrachial nucleus.2790                                    |
| c_tpm_lateral_parabrachial_nucleus_2013                                           | decimal | TPM.lateral parabrachial nucleus.2013                                           |
| c_est_counts_lateral_parabrachial_nucleus_2013                                    | decimal | est_counts.lateral parabrachial nucleus.2013                                    |
| c_tpm_lateral_parabrachial_nucleus_2139                                           | decimal | TPM.lateral parabrachial nucleus.2139                                           |
| c_est_counts_lateral_parabrachial_nucleus_2139                                    | decimal | est_counts.lateral parabrachial nucleus.2139                                    |
| c_tpm_lateral_parabrachial_nucleus_2792                                           | decimal | TPM.lateral parabrachial nucleus.2792                                           |
| c_est_counts_lateral_parabrachial_nucleus_2792                                    | decimal | est_counts.lateral parabrachial nucleus.2792                                    |
| c_tpm_lateral_thalamic_nuclei_2661                                                | decimal | TPM.lateral thalamic nuclei.2661                                                |
| c_est_counts_lateral_thalamic_nuclei_2661                                         | decimal | est_counts.lateral thalamic nuclei.2661                                         |
| c_tpm_lateral_thalamic_nuclei_2577                                                | decimal | TPM.lateral thalamic nuclei.2577                                                |
| c_est_counts_lateral_thalamic_nuclei_2577                                         | decimal | est_counts.lateral thalamic nuclei.2577                                         |
| c_tpm_lateral_thalamic_nuclei_2573                                                | decimal | TPM.lateral thalamic nuclei.2573                                                |
| c_est_counts_lateral_thalamic_nuclei_2573                                         | decimal | est_counts.lateral thalamic nuclei.2573                                         |
| c_tpm_lateral_thalamic_nuclei_2765                                                | decimal | TPM.lateral thalamic nuclei.2765                                                |
| c_est_counts_lateral_thalamic_nuclei_2765                                         | decimal | est_counts.lateral thalamic nuclei.2765                                         |
| c_tpm_lateral_thalamic_nuclei_1903                                                | decimal | TPM.lateral thalamic nuclei.1903                                                |
| c_est_counts_lateral_thalamic_nuclei_1903                                         | decimal | est_counts.lateral thalamic nuclei.1903                                         |
| c_tpm_lateral_vestibular_nucleus_2311                                             | decimal | TPM.lateral vestibular nucleus.2311                                             |
| c_est_counts_lateral_vestibular_nucleus_2311                                      | decimal | est_counts.lateral vestibular nucleus.2311                                      |
| c_tpm_lateral_vestibular_nucleus_2184                                             | decimal | TPM.lateral vestibular nucleus.2184                                             |
| c_est_counts_lateral_vestibular_nucleus_2184                                      | decimal | est_counts.lateral vestibular nucleus.2184                                      |
| c_tpm_lingual_gyrus_2838                                                          | decimal | TPM.lingual gyrus.2838                                                          |
| c_est_counts_lingual_gyrus_2838                                                   | decimal | est_counts.lingual gyrus.2838                                                   |
| c_tpm_lingual_gyrus_2688                                                          | decimal | TPM.lingual gyrus.2688                                                          |
| c_est_counts_lingual_gyrus_2688                                                   | decimal | est_counts.lingual gyrus.2688                                                   |
| c_tpm_lingual_gyrus_2618                                                          | decimal | TPM.lingual gyrus.2618                                                          |
| c_est_counts_lingual_gyrus_2618                                                   | decimal | est_counts.lingual gyrus.2618                                                   |
| c_tpm_lingual_gyrus_2073                                                          | decimal | TPM.lingual gyrus.2073                                                          |
| c_est_counts_lingual_gyrus_2073                                                   | decimal | est_counts.lingual gyrus.2073                                                   |
| c_tpm_lingual_gyrus_1893                                                          | decimal | TPM.lingual gyrus.1893                                                          |
| c_est_counts_lingual_gyrus_1893                                                   | decimal | est_counts.lingual gyrus.1893                                                   |
| c_tpm_locus_coeruleus_2317                                                        | decimal | TPM.locus coeruleus.2317                                                        |
| c_est_counts_locus_coeruleus_2317                                                 | decimal | est_counts.locus coeruleus.2317                                                 |
| c_tpm_locus_coeruleus_2162                                                        | decimal | TPM.locus coeruleus.2162                                                        |
| c_est_counts_locus_coeruleus_2162                                                 | decimal | est_counts.locus coeruleus.2162                                                 |
| c_tpm_locus_coeruleus_2123                                                        | decimal | TPM.locus coeruleus.2123                                                        |
| c_est_counts_locus_coeruleus_2123                                                 | decimal | est_counts.locus coeruleus.2123                                                 |
| c_tpm_locus_coeruleus_2720                                                        | decimal | TPM.locus coeruleus.2720                                                        |
| c_est_counts_locus_coeruleus_2720                                                 | decimal | est_counts.locus coeruleus.2720                                                 |
| c_tpm_locus_coeruleus_1980                                                        | decimal | TPM.locus coeruleus.1980                                                        |
| c_est_counts_locus_coeruleus_1980                                                 | decimal | est_counts.locus coeruleus.1980                                                 |
| c_tpm_locus_coeruleus_2014                                                        | decimal | TPM.locus coeruleus.2014                                                        |
| c_est_counts_locus_coeruleus_2014                                                 | decimal | est_counts.locus coeruleus.2014                                                 |
| c_tpm_locus_coeruleus_2788                                                        | decimal | TPM.locus coeruleus.2788                                                        |
| c_est_counts_locus_coeruleus_2788                                                 | decimal | est_counts.locus coeruleus.2788                                                 |
| c_tpm_mammillary_body_1834                                                        | decimal | TPM.mammillary body.1834                                                        |
| c_est_counts_mammillary_body_1834                                                 | decimal | est_counts.mammillary body.1834                                                 |
| c_tpm_mammillary_body_1948                                                        | decimal | TPM.mammillary body.1948                                                        |
| c_est_counts_mammillary_body_1948                                                 | decimal | est_counts.mammillary body.1948                                                 |
| c_tpm_mammillary_body_2413                                                        | decimal | TPM.mammillary body.2413                                                        |
| c_est_counts_mammillary_body_2413                                                 | decimal | est_counts.mammillary body.2413                                                 |
| c_tpm_mammillary_body_1923                                                        | decimal | TPM.mammillary body.1923                                                        |
| c_est_counts_mammillary_body_1923                                                 | decimal | est_counts.mammillary body.1923                                                 |
| c_tpm_mammillary_body_1945                                                        | decimal | TPM.mammillary body.1945                                                        |
| c_est_counts_mammillary_body_1945                                                 | decimal | est_counts.mammillary body.1945                                                 |
| c_tpm_medial_dorsal_thalamic_nucleus_1930                                         | decimal | TPM.medial dorsal thalamic nucleus.1930                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_1930                                  | decimal | est_counts.medial dorsal thalamic nucleus.1930                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_2039                                         | decimal | TPM.medial dorsal thalamic nucleus.2039                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_2039                                  | decimal | est_counts.medial dorsal thalamic nucleus.2039                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_2026                                         | decimal | TPM.medial dorsal thalamic nucleus.2026                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_2026                                  | decimal | est_counts.medial dorsal thalamic nucleus.2026                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_2498                                         | decimal | TPM.medial dorsal thalamic nucleus.2498                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_2498                                  | decimal | est_counts.medial dorsal thalamic nucleus.2498                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_1810                                         | decimal | TPM.medial dorsal thalamic nucleus.1810                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_1810                                  | decimal | est_counts.medial dorsal thalamic nucleus.1810                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_2660                                         | decimal | TPM.medial dorsal thalamic nucleus.2660                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_2660                                  | decimal | est_counts.medial dorsal thalamic nucleus.2660                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_1971                                         | decimal | TPM.medial dorsal thalamic nucleus.1971                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_1971                                  | decimal | est_counts.medial dorsal thalamic nucleus.1971                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_2283                                         | decimal | TPM.medial dorsal thalamic nucleus.2283                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_2283                                  | decimal | est_counts.medial dorsal thalamic nucleus.2283                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_2492                                         | decimal | TPM.medial dorsal thalamic nucleus.2492                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_2492                                  | decimal | est_counts.medial dorsal thalamic nucleus.2492                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_2576                                         | decimal | TPM.medial dorsal thalamic nucleus.2576                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_2576                                  | decimal | est_counts.medial dorsal thalamic nucleus.2576                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_2572                                         | decimal | TPM.medial dorsal thalamic nucleus.2572                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_2572                                  | decimal | est_counts.medial dorsal thalamic nucleus.2572                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_2402                                         | decimal | TPM.medial dorsal thalamic nucleus.2402                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_2402                                  | decimal | est_counts.medial dorsal thalamic nucleus.2402                                  |
| c_tpm_medial_dorsal_thalamic_nucleus_1859                                         | decimal | TPM.medial dorsal thalamic nucleus.1859                                         |
| c_est_counts_medial_dorsal_thalamic_nucleus_1859                                  | decimal | est_counts.medial dorsal thalamic nucleus.1859                                  |
| c_tpm_medial_geniculate_body_1811                                                 | decimal | TPM.medial geniculate body.1811                                                 |
| c_est_counts_medial_geniculate_body_1811                                          | decimal | est_counts.medial geniculate body.1811                                          |
| c_tpm_medial_geniculate_body_2217                                                 | decimal | TPM.medial geniculate body.2217                                                 |
| c_est_counts_medial_geniculate_body_2217                                          | decimal | est_counts.medial geniculate body.2217                                          |
| c_tpm_medial_geniculate_body_2207                                                 | decimal | TPM.medial geniculate body.2207                                                 |
| c_est_counts_medial_geniculate_body_2207                                          | decimal | est_counts.medial geniculate body.2207                                          |
| c_tpm_medial_geniculate_body_2571                                                 | decimal | TPM.medial geniculate body.2571                                                 |
| c_est_counts_medial_geniculate_body_2571                                          | decimal | est_counts.medial geniculate body.2571                                          |
| c_tpm_medial_geniculate_body_2657                                                 | decimal | TPM.medial geniculate body.2657                                                 |
| c_est_counts_medial_geniculate_body_2657                                          | decimal | est_counts.medial geniculate body.2657                                          |
| c_tpm_medial_geniculate_body_2650                                                 | decimal | TPM.medial geniculate body.2650                                                 |
| c_est_counts_medial_geniculate_body_2650                                          | decimal | est_counts.medial geniculate body.2650                                          |
| c_tpm_medial_geniculate_body_2049                                                 | decimal | TPM.medial geniculate body.2049                                                 |
| c_est_counts_medial_geniculate_body_2049                                          | decimal | est_counts.medial geniculate body.2049                                          |
| c_tpm_medial_olivary_nucleus_1943                                                 | decimal | TPM.medial olivary nucleus.1943                                                 |
| c_est_counts_medial_olivary_nucleus_1943                                          | decimal | est_counts.medial olivary nucleus.1943                                          |
| c_tpm_medial_olivary_nucleus_2851                                                 | decimal | TPM.medial olivary nucleus.2851                                                 |
| c_est_counts_medial_olivary_nucleus_2851                                          | decimal | est_counts.medial olivary nucleus.2851                                          |
| c_tpm_medial_olivary_nucleus_2138                                                 | decimal | TPM.medial olivary nucleus.2138                                                 |
| c_est_counts_medial_olivary_nucleus_2138                                          | decimal | est_counts.medial olivary nucleus.2138                                          |
| c_tpm_medial_olivary_nucleus_1962                                                 | decimal | TPM.medial olivary nucleus.1962                                                 |
| c_est_counts_medial_olivary_nucleus_1962                                          | decimal | est_counts.medial olivary nucleus.1962                                          |
| c_tpm_medial_parabrachial_nucleus_2156                                            | decimal | TPM.medial parabrachial nucleus.2156                                            |
| c_est_counts_medial_parabrachial_nucleus_2156                                     | decimal | est_counts.medial parabrachial nucleus.2156                                     |
| c_tpm_medial_parabrachial_nucleus_2854                                            | decimal | TPM.medial parabrachial nucleus.2854                                            |
| c_est_counts_medial_parabrachial_nucleus_2854                                     | decimal | est_counts.medial parabrachial nucleus.2854                                     |
| c_tpm_medial_parabrachial_nucleus_2170                                            | decimal | TPM.medial parabrachial nucleus.2170                                            |
| c_est_counts_medial_parabrachial_nucleus_2170                                     | decimal | est_counts.medial parabrachial nucleus.2170                                     |
| c_tpm_medial_parabrachial_nucleus_2463                                            | decimal | TPM.medial parabrachial nucleus.2463                                            |
| c_est_counts_medial_parabrachial_nucleus_2463                                     | decimal | est_counts.medial parabrachial nucleus.2463                                     |
| c_tpm_medial_parabrachial_nucleus_2786                                            | decimal | TPM.medial parabrachial nucleus.2786                                            |
| c_est_counts_medial_parabrachial_nucleus_2786                                     | decimal | est_counts.medial parabrachial nucleus.2786                                     |
| c_tpm_medial_periolivary_nuclei_2081                                              | decimal | TPM.medial periolivary nuclei.2081                                              |
| c_est_counts_medial_periolivary_nuclei_2081                                       | decimal | est_counts.medial periolivary nuclei.2081                                       |
| c_tpm_medial_periolivary_nuclei_2458                                              | decimal | TPM.medial periolivary nuclei.2458                                              |
| c_est_counts_medial_periolivary_nuclei_2458                                       | decimal | est_counts.medial periolivary nuclei.2458                                       |
| c_tpm_medial_periolivary_nuclei_2791                                              | decimal | TPM.medial periolivary nuclei.2791                                              |
| c_est_counts_medial_periolivary_nuclei_2791                                       | decimal | est_counts.medial periolivary nuclei.2791                                       |
| c_tpm_medial_periolivary_nuclei_2171                                              | decimal | TPM.medial periolivary nuclei.2171                                              |
| c_est_counts_medial_periolivary_nuclei_2171                                       | decimal | est_counts.medial periolivary nuclei.2171                                       |
| c_tpm_medial_periolivary_nuclei_2063                                              | decimal | TPM.medial periolivary nuclei.2063                                              |
| c_est_counts_medial_periolivary_nuclei_2063                                       | decimal | est_counts.medial periolivary nuclei.2063                                       |
| c_tpm_medial_vestibular_nucleus_2624                                              | decimal | TPM.medial vestibular nucleus.2624                                              |
| c_est_counts_medial_vestibular_nucleus_2624                                       | decimal | est_counts.medial vestibular nucleus.2624                                       |
| c_tpm_medial_vestibular_nucleus_2093                                              | decimal | TPM.medial vestibular nucleus.2093                                              |
| c_est_counts_medial_vestibular_nucleus_2093                                       | decimal | est_counts.medial vestibular nucleus.2093                                       |
| c_tpm_medial_vestibular_nucleus_2803                                              | decimal | TPM.medial vestibular nucleus.2803                                              |
| c_est_counts_medial_vestibular_nucleus_2803                                       | decimal | est_counts.medial vestibular nucleus.2803                                       |
| c_tpm_medial_vestibular_nucleus_2801                                              | decimal | TPM.medial vestibular nucleus.2801                                              |
| c_est_counts_medial_vestibular_nucleus_2801                                       | decimal | est_counts.medial vestibular nucleus.2801                                       |
| c_tpm_medial_vestibular_nucleus_2743                                              | decimal | TPM.medial vestibular nucleus.2743                                              |
| c_est_counts_medial_vestibular_nucleus_2743                                       | decimal | est_counts.medial vestibular nucleus.2743                                       |
| c_tpm_medial_vestibular_nucleus_2134                                              | decimal | TPM.medial vestibular nucleus.2134                                              |
| c_est_counts_medial_vestibular_nucleus_2134                                       | decimal | est_counts.medial vestibular nucleus.2134                                       |
| c_tpm_median_raphe_nucleus_2220                                                   | decimal | TPM.median raphe nucleus.2220                                                   |
| c_est_counts_median_raphe_nucleus_2220                                            | decimal | est_counts.median raphe nucleus.2220                                            |
| c_tpm_middle_cingulate_cortex_2539                                                | decimal | TPM.middle cingulate cortex.2539                                                |
| c_est_counts_middle_cingulate_cortex_2539                                         | decimal | est_counts.middle cingulate cortex.2539                                         |
| c_tpm_middle_cingulate_cortex_2633                                                | decimal | TPM.middle cingulate cortex.2633                                                |
| c_est_counts_middle_cingulate_cortex_2633                                         | decimal | est_counts.middle cingulate cortex.2633                                         |
| c_tpm_middle_cingulate_cortex_2640                                                | decimal | TPM.middle cingulate cortex.2640                                                |
| c_est_counts_middle_cingulate_cortex_2640                                         | decimal | est_counts.middle cingulate cortex.2640                                         |
| c_tpm_middle_cingulate_cortex_2028                                                | decimal | TPM.middle cingulate cortex.2028                                                |
| c_est_counts_middle_cingulate_cortex_2028                                         | decimal | est_counts.middle cingulate cortex.2028                                         |
| c_tpm_middle_cingulate_cortex_2357                                                | decimal | TPM.middle cingulate cortex.2357                                                |
| c_est_counts_middle_cingulate_cortex_2357                                         | decimal | est_counts.middle cingulate cortex.2357                                         |
| c_tpm_middle_temporal_gyrus_1819                                                  | decimal | TPM.middle temporal gyrus.1819                                                  |
| c_est_counts_middle_temporal_gyrus_1819                                           | decimal | est_counts.middle temporal gyrus.1819                                           |
| c_tpm_middle_temporal_gyrus_2611                                                  | decimal | TPM.middle temporal gyrus.2611                                                  |
| c_est_counts_middle_temporal_gyrus_2611                                           | decimal | est_counts.middle temporal gyrus.2611                                           |
| c_tpm_middle_temporal_gyrus_2034                                                  | decimal | TPM.middle temporal gyrus.2034                                                  |
| c_est_counts_middle_temporal_gyrus_2034                                           | decimal | est_counts.middle temporal gyrus.2034                                           |
| c_tpm_middle_temporal_gyrus_2616                                                  | decimal | TPM.middle temporal gyrus.2616                                                  |
| c_est_counts_middle_temporal_gyrus_2616                                           | decimal | est_counts.middle temporal gyrus.2616                                           |
| c_tpm_middle_temporal_gyrus_1799                                                  | decimal | TPM.middle temporal gyrus.1799                                                  |
| c_est_counts_middle_temporal_gyrus_1799                                           | decimal | est_counts.middle temporal gyrus.1799                                           |
| c_tpm_motor_facial_nucleus_2126                                                   | decimal | TPM.motor facial nucleus.2126                                                   |
| c_est_counts_motor_facial_nucleus_2126                                            | decimal | est_counts.motor facial nucleus.2126                                            |
| c_tpm_motor_facial_nucleus_2327                                                   | decimal | TPM.motor facial nucleus.2327                                                   |
| c_est_counts_motor_facial_nucleus_2327                                            | decimal | est_counts.motor facial nucleus.2327                                            |
| c_tpm_motor_facial_nucleus_2795                                                   | decimal | TPM.motor facial nucleus.2795                                                   |
| c_est_counts_motor_facial_nucleus_2795                                            | decimal | est_counts.motor facial nucleus.2795                                            |
| c_tpm_motor_facial_nucleus_2365                                                   | decimal | TPM.motor facial nucleus.2365                                                   |
| c_est_counts_motor_facial_nucleus_2365                                            | decimal | est_counts.motor facial nucleus.2365                                            |
| c_tpm_motor_facial_nucleus_2697                                                   | decimal | TPM.motor facial nucleus.2697                                                   |
| c_est_counts_motor_facial_nucleus_2697                                            | decimal | est_counts.motor facial nucleus.2697                                            |
| c_tpm_motor_facial_nucleus_2062                                                   | decimal | TPM.motor facial nucleus.2062                                                   |
| c_est_counts_motor_facial_nucleus_2062                                            | decimal | est_counts.motor facial nucleus.2062                                            |
| c_tpm_motor_hypoglossal_nucleus_2461                                              | decimal | TPM.motor hypoglossal nucleus.2461                                              |
| c_est_counts_motor_hypoglossal_nucleus_2461                                       | decimal | est_counts.motor hypoglossal nucleus.2461                                       |
| c_tpm_motor_hypoglossal_nucleus_2182                                              | decimal | TPM.motor hypoglossal nucleus.2182                                              |
| c_est_counts_motor_hypoglossal_nucleus_2182                                       | decimal | est_counts.motor hypoglossal nucleus.2182                                       |
| c_tpm_motor_hypoglossal_nucleus_2125                                              | decimal | TPM.motor hypoglossal nucleus.2125                                              |
| c_est_counts_motor_hypoglossal_nucleus_2125                                       | decimal | est_counts.motor hypoglossal nucleus.2125                                       |
| c_tpm_motor_hypoglossal_nucleus_2132                                              | decimal | TPM.motor hypoglossal nucleus.2132                                              |
| c_est_counts_motor_hypoglossal_nucleus_2132                                       | decimal | est_counts.motor hypoglossal nucleus.2132                                       |
| c_tpm_motor_hypoglossal_nucleus_2277                                              | decimal | TPM.motor hypoglossal nucleus.2277                                              |
| c_est_counts_motor_hypoglossal_nucleus_2277                                       | decimal | est_counts.motor hypoglossal nucleus.2277                                       |
| c_tpm_motor_trigeminal_nucleus_2335                                               | decimal | TPM.motor trigeminal nucleus.2335                                               |
| c_est_counts_motor_trigeminal_nucleus_2335                                        | decimal | est_counts.motor trigeminal nucleus.2335                                        |
| c_tpm_motor_trigeminal_nucleus_2079                                               | decimal | TPM.motor trigeminal nucleus.2079                                               |
| c_est_counts_motor_trigeminal_nucleus_2079                                        | decimal | est_counts.motor trigeminal nucleus.2079                                        |
| c_tpm_motor_trigeminal_nucleus_2321                                               | decimal | TPM.motor trigeminal nucleus.2321                                               |
| c_est_counts_motor_trigeminal_nucleus_2321                                        | decimal | est_counts.motor trigeminal nucleus.2321                                        |
| c_tpm_motor_trigeminal_nucleus_2560                                               | decimal | TPM.motor trigeminal nucleus.2560                                               |
| c_est_counts_motor_trigeminal_nucleus_2560                                        | decimal | est_counts.motor trigeminal nucleus.2560                                        |
| c_tpm_motor_trigeminal_nucleus_2309                                               | decimal | TPM.motor trigeminal nucleus.2309                                               |
| c_est_counts_motor_trigeminal_nucleus_2309                                        | decimal | est_counts.motor trigeminal nucleus.2309                                        |
| c_tpm_nuclei_of_the_trapezoid_body_2159                                           | decimal | TPM.nuclei of the trapezoid body.2159                                           |
| c_est_counts_nuclei_of_the_trapezoid_body_2159                                    | decimal | est_counts.nuclei of the trapezoid body.2159                                    |
| c_tpm_nuclei_of_the_trapezoid_body_2166                                           | decimal | TPM.nuclei of the trapezoid body.2166                                           |
| c_est_counts_nuclei_of_the_trapezoid_body_2166                                    | decimal | est_counts.nuclei of the trapezoid body.2166                                    |
| c_tpm_nuclei_of_the_trapezoid_body_2368                                           | decimal | TPM.nuclei of the trapezoid body.2368                                           |
| c_est_counts_nuclei_of_the_trapezoid_body_2368                                    | decimal | est_counts.nuclei of the trapezoid body.2368                                    |
| c_tpm_nuclei_of_the_trapezoid_body_2735                                           | decimal | TPM.nuclei of the trapezoid body.2735                                           |
| c_est_counts_nuclei_of_the_trapezoid_body_2735                                    | decimal | est_counts.nuclei of the trapezoid body.2735                                    |
| c_tpm_nuclei_of_the_trapezoid_body_1983                                           | decimal | TPM.nuclei of the trapezoid body.1983                                           |
| c_est_counts_nuclei_of_the_trapezoid_body_1983                                    | decimal | est_counts.nuclei of the trapezoid body.1983                                    |
| c_tpm_nucleus_accumbens_2698                                                      | decimal | TPM.nucleus accumbens.2698                                                      |
| c_est_counts_nucleus_accumbens_2698                                               | decimal | est_counts.nucleus accumbens.2698                                               |
| c_tpm_nucleus_accumbens_2824                                                      | decimal | TPM.nucleus accumbens.2824                                                      |
| c_est_counts_nucleus_accumbens_2824                                               | decimal | est_counts.nucleus accumbens.2824                                               |
| c_tpm_nucleus_accumbens_2732                                                      | decimal | TPM.nucleus accumbens.2732                                                      |
| c_est_counts_nucleus_accumbens_2732                                               | decimal | est_counts.nucleus accumbens.2732                                               |
| c_tpm_nucleus_accumbens_2286                                                      | decimal | TPM.nucleus accumbens.2286                                                      |
| c_est_counts_nucleus_accumbens_2286                                               | decimal | est_counts.nucleus accumbens.2286                                               |
| c_tpm_nucleus_accumbens_1856                                                      | decimal | TPM.nucleus accumbens.1856                                                      |
| c_est_counts_nucleus_accumbens_1856                                               | decimal | est_counts.nucleus accumbens.1856                                               |
| c_tpm_nucleus_accumbens_2391                                                      | decimal | TPM.nucleus accumbens.2391                                                      |
| c_est_counts_nucleus_accumbens_2391                                               | decimal | est_counts.nucleus accumbens.2391                                               |
| c_tpm_nucleus_accumbens_1806                                                      | decimal | TPM.nucleus accumbens.1806                                                      |
| c_est_counts_nucleus_accumbens_1806                                               | decimal | est_counts.nucleus accumbens.1806                                               |
| c_tpm_nucleus_accumbens_1783                                                      | decimal | TPM.nucleus accumbens.1783                                                      |
| c_est_counts_nucleus_accumbens_1783                                               | decimal | est_counts.nucleus accumbens.1783                                               |
| c_tpm_nucleus_ambiguus_2096                                                       | decimal | TPM.nucleus ambiguus.2096                                                       |
| c_est_counts_nucleus_ambiguus_2096                                                | decimal | est_counts.nucleus ambiguus.2096                                                |
| c_tpm_nucleus_ambiguus_2071                                                       | decimal | TPM.nucleus ambiguus.2071                                                       |
| c_est_counts_nucleus_ambiguus_2071                                                | decimal | est_counts.nucleus ambiguus.2071                                                |
| c_tpm_nucleus_basalis_of_meynert_2569                                             | decimal | TPM.nucleus basalis of Meynert.2569                                             |
| c_est_counts_nucleus_basalis_of_meynert_2569                                      | decimal | est_counts.nucleus basalis of Meynert.2569                                      |
| c_tpm_nucleus_basalis_of_meynert_2393                                             | decimal | TPM.nucleus basalis of Meynert.2393                                             |
| c_est_counts_nucleus_basalis_of_meynert_2393                                      | decimal | est_counts.nucleus basalis of Meynert.2393                                      |
| c_tpm_nucleus_basalis_of_meynert_2821                                             | decimal | TPM.nucleus basalis of Meynert.2821                                             |
| c_est_counts_nucleus_basalis_of_meynert_2821                                      | decimal | est_counts.nucleus basalis of Meynert.2821                                      |
| c_tpm_nucleus_basalis_of_meynert_2484                                             | decimal | TPM.nucleus basalis of Meynert.2484                                             |
| c_est_counts_nucleus_basalis_of_meynert_2484                                      | decimal | est_counts.nucleus basalis of Meynert.2484                                      |
| c_tpm_nucleus_cuneatus_2376                                                       | decimal | TPM.nucleus cuneatus.2376                                                       |
| c_est_counts_nucleus_cuneatus_2376                                                | decimal | est_counts.nucleus cuneatus.2376                                                |
| c_tpm_nucleus_cuneatus_2562                                                       | decimal | TPM.nucleus cuneatus.2562                                                       |
| c_est_counts_nucleus_cuneatus_2562                                                | decimal | est_counts.nucleus cuneatus.2562                                                |
| c_tpm_nucleus_cuneatus_2380                                                       | decimal | TPM.nucleus cuneatus.2380                                                       |
| c_est_counts_nucleus_cuneatus_2380                                                | decimal | est_counts.nucleus cuneatus.2380                                                |
| c_tpm_nucleus_cuneatus_2381                                                       | decimal | TPM.nucleus cuneatus.2381                                                       |
| c_est_counts_nucleus_cuneatus_2381                                                | decimal | est_counts.nucleus cuneatus.2381                                                |
| c_tpm_nucleus_cuneatus_2805                                                       | decimal | TPM.nucleus cuneatus.2805                                                       |
| c_est_counts_nucleus_cuneatus_2805                                                | decimal | est_counts.nucleus cuneatus.2805                                                |
| c_tpm_nucleus_cuneatus_2564                                                       | decimal | TPM.nucleus cuneatus.2564                                                       |
| c_est_counts_nucleus_cuneatus_2564                                                | decimal | est_counts.nucleus cuneatus.2564                                                |
| c_tpm_nucleus_cuneatus_2808                                                       | decimal | TPM.nucleus cuneatus.2808                                                       |
| c_est_counts_nucleus_cuneatus_2808                                                | decimal | est_counts.nucleus cuneatus.2808                                                |
| c_tpm_nucleus_cuneatus_2100                                                       | decimal | TPM.nucleus cuneatus.2100                                                       |
| c_est_counts_nucleus_cuneatus_2100                                                | decimal | est_counts.nucleus cuneatus.2100                                                |
| c_tpm_nucleus_cuneatus_2131                                                       | decimal | TPM.nucleus cuneatus.2131                                                       |
| c_est_counts_nucleus_cuneatus_2131                                                | decimal | est_counts.nucleus cuneatus.2131                                                |
| c_tpm_nucleus_gracilis_2382                                                       | decimal | TPM.nucleus gracilis.2382                                                       |
| c_est_counts_nucleus_gracilis_2382                                                | decimal | est_counts.nucleus gracilis.2382                                                |
| c_tpm_nucleus_gracilis_2627                                                       | decimal | TPM.nucleus gracilis.2627                                                       |
| c_est_counts_nucleus_gracilis_2627                                                | decimal | est_counts.nucleus gracilis.2627                                                |
| c_tpm_nucleus_gracilis_2299                                                       | decimal | TPM.nucleus gracilis.2299                                                       |
| c_est_counts_nucleus_gracilis_2299                                                | decimal | est_counts.nucleus gracilis.2299                                                |
| c_tpm_nucleus_of_the_diagonal_band_2029                                           | decimal | TPM.nucleus of the diagonal band.2029                                           |
| c_est_counts_nucleus_of_the_diagonal_band_2029                                    | decimal | est_counts.nucleus of the diagonal band.2029                                    |
| c_tpm_nucleus_of_the_diagonal_band_2775                                           | decimal | TPM.nucleus of the diagonal band.2775                                           |
| c_est_counts_nucleus_of_the_diagonal_band_2775                                    | decimal | est_counts.nucleus of the diagonal band.2775                                    |
| c_tpm_nucleus_of_the_diagonal_band_1812                                           | decimal | TPM.nucleus of the diagonal band.1812                                           |
| c_est_counts_nucleus_of_the_diagonal_band_1812                                    | decimal | est_counts.nucleus of the diagonal band.1812                                    |
| c_tpm_nucleus_of_the_diagonal_band_2195                                           | decimal | TPM.nucleus of the diagonal band.2195                                           |
| c_est_counts_nucleus_of_the_diagonal_band_2195                                    | decimal | est_counts.nucleus of the diagonal band.2195                                    |
| c_tpm_nucleus_of_the_diagonal_band_1979                                           | decimal | TPM.nucleus of the diagonal band.1979                                           |
| c_est_counts_nucleus_of_the_diagonal_band_1979                                    | decimal | est_counts.nucleus of the diagonal band.1979                                    |
| c_tpm_nucleus_raphe_magnus_2160                                                   | decimal | TPM.nucleus raphe magnus.2160                                                   |
| c_est_counts_nucleus_raphe_magnus_2160                                            | decimal | est_counts.nucleus raphe magnus.2160                                            |
| c_tpm_nucleus_raphe_magnus_2328                                                   | decimal | TPM.nucleus raphe magnus.2328                                                   |
| c_est_counts_nucleus_raphe_magnus_2328                                            | decimal | est_counts.nucleus raphe magnus.2328                                            |
| c_tpm_nucleus_raphe_magnus_2459                                                   | decimal | TPM.nucleus raphe magnus.2459                                                   |
| c_est_counts_nucleus_raphe_magnus_2459                                            | decimal | est_counts.nucleus raphe magnus.2459                                            |
| c_tpm_nucleus_raphe_magnus_2455                                                   | decimal | TPM.nucleus raphe magnus.2455                                                   |
| c_est_counts_nucleus_raphe_magnus_2455                                            | decimal | est_counts.nucleus raphe magnus.2455                                            |
| c_tpm_nucleus_raphe_magnus_2172                                                   | decimal | TPM.nucleus raphe magnus.2172                                                   |
| c_est_counts_nucleus_raphe_magnus_2172                                            | decimal | est_counts.nucleus raphe magnus.2172                                            |
| c_tpm_nucleus_raphe_magnus_2051                                                   | decimal | TPM.nucleus raphe magnus.2051                                                   |
| c_est_counts_nucleus_raphe_magnus_2051                                            | decimal | est_counts.nucleus raphe magnus.2051                                            |
| c_tpm_nucleus_raphe_obscurus_2800                                                 | decimal | TPM.nucleus raphe obscurus.2800                                                 |
| c_est_counts_nucleus_raphe_obscurus_2800                                          | decimal | est_counts.nucleus raphe obscurus.2800                                          |
| c_tpm_nucleus_raphe_obscurus_2845                                                 | decimal | TPM.nucleus raphe obscurus.2845                                                 |
| c_est_counts_nucleus_raphe_obscurus_2845                                          | decimal | est_counts.nucleus raphe obscurus.2845                                          |
| c_tpm_nucleus_raphe_obscurus_2142                                                 | decimal | TPM.nucleus raphe obscurus.2142                                                 |
| c_est_counts_nucleus_raphe_obscurus_2142                                          | decimal | est_counts.nucleus raphe obscurus.2142                                          |
| c_tpm_nucleus_raphe_pallidus_1924                                                 | decimal | TPM.nucleus raphe pallidus.1924                                                 |
| c_est_counts_nucleus_raphe_pallidus_1924                                          | decimal | est_counts.nucleus raphe pallidus.1924                                          |
| c_tpm_nucleus_raphe_pallidus_2183                                                 | decimal | TPM.nucleus raphe pallidus.2183                                                 |
| c_est_counts_nucleus_raphe_pallidus_2183                                          | decimal | est_counts.nucleus raphe pallidus.2183                                          |
| c_tpm_nucleus_raphe_pallidus_2145                                                 | decimal | TPM.nucleus raphe pallidus.2145                                                 |
| c_est_counts_nucleus_raphe_pallidus_2145                                          | decimal | est_counts.nucleus raphe pallidus.2145                                          |
| c_tpm_nucleus_reuniens_2205                                                       | decimal | TPM.nucleus reuniens.2205                                                       |
| c_est_counts_nucleus_reuniens_2205                                                | decimal | est_counts.nucleus reuniens.2205                                                |
| c_tpm_nucleus_reuniens_2210                                                       | decimal | TPM.nucleus reuniens.2210                                                       |
| c_est_counts_nucleus_reuniens_2210                                                | decimal | est_counts.nucleus reuniens.2210                                                |
| c_tpm_nucleus_reuniens_2212                                                       | decimal | TPM.nucleus reuniens.2212                                                       |
| c_est_counts_nucleus_reuniens_2212                                                | decimal | est_counts.nucleus reuniens.2212                                                |
| c_tpm_nucleus_rhomboideus_2206                                                    | decimal | TPM.nucleus rhomboideus.2206                                                    |
| c_est_counts_nucleus_rhomboideus_2206                                             | decimal | est_counts.nucleus rhomboideus.2206                                             |
| c_tpm_nucleus_rhomboideus_2280                                                    | decimal | TPM.nucleus rhomboideus.2280                                                    |
| c_est_counts_nucleus_rhomboideus_2280                                             | decimal | est_counts.nucleus rhomboideus.2280                                             |
| c_tpm_nucleus_rhomboideus_2213                                                    | decimal | TPM.nucleus rhomboideus.2213                                                    |
| c_est_counts_nucleus_rhomboideus_2213                                             | decimal | est_counts.nucleus rhomboideus.2213                                             |
| c_tpm_nucleus_tractus_solitarii_2307                                              | decimal | TPM.nucleus tractus solitarii.2307                                              |
| c_est_counts_nucleus_tractus_solitarii_2307                                       | decimal | est_counts.nucleus tractus solitarii.2307                                       |
| c_tpm_nucleus_tractus_solitarii_2144                                              | decimal | TPM.nucleus tractus solitarii.2144                                              |
| c_est_counts_nucleus_tractus_solitarii_2144                                       | decimal | est_counts.nucleus tractus solitarii.2144                                       |
| c_tpm_nucleus_tractus_solitarii_2191                                              | decimal | TPM.nucleus tractus solitarii.2191                                              |
| c_est_counts_nucleus_tractus_solitarii_2191                                       | decimal | est_counts.nucleus tractus solitarii.2191                                       |
| c_tpm_nucleus_tractus_solitarii_2656                                              | decimal | TPM.nucleus tractus solitarii.2656                                              |
| c_est_counts_nucleus_tractus_solitarii_2656                                       | decimal | est_counts.nucleus tractus solitarii.2656                                       |
| c_tpm_occipital_cortex_2426                                                       | decimal | TPM.occipital cortex.2426                                                       |
| c_est_counts_occipital_cortex_2426                                                | decimal | est_counts.occipital cortex.2426                                                |
| c_tpm_occipital_cortex_2470                                                       | decimal | TPM.occipital cortex.2470                                                       |
| c_est_counts_occipital_cortex_2470                                                | decimal | est_counts.occipital cortex.2470                                                |
| c_tpm_occipital_cortex_2608                                                       | decimal | TPM.occipital cortex.2608                                                       |
| c_est_counts_occipital_cortex_2608                                                | decimal | est_counts.occipital cortex.2608                                                |
| c_tpm_occipital_cortex_2677                                                       | decimal | TPM.occipital cortex.2677                                                       |
| c_est_counts_occipital_cortex_2677                                                | decimal | est_counts.occipital cortex.2677                                                |
| c_tpm_occipital_cortex_1842                                                       | decimal | TPM.occipital cortex.1842                                                       |
| c_est_counts_occipital_cortex_1842                                                | decimal | est_counts.occipital cortex.1842                                                |
| c_tpm_occipital_cortex__white_matter__2259                                        | decimal | TPM.occipital cortex (white matter).2259                                        |
| c_est_counts_occipital_cortex__white_matter__2259                                 | decimal | est_counts.occipital cortex (white matter).2259                                 |
| c_tpm_occipital_cortex__white_matter__2257                                        | decimal | TPM.occipital cortex (white matter).2257                                        |
| c_est_counts_occipital_cortex__white_matter__2257                                 | decimal | est_counts.occipital cortex (white matter).2257                                 |
| c_tpm_olfactory_area_2440                                                         | decimal | TPM.olfactory area.2440                                                         |
| c_est_counts_olfactory_area_2440                                                  | decimal | est_counts.olfactory area.2440                                                  |
| c_tpm_olfactory_area_2542                                                         | decimal | TPM.olfactory area.2542                                                         |
| c_est_counts_olfactory_area_2542                                                  | decimal | est_counts.olfactory area.2542                                                  |
| c_tpm_olfactory_area_2352                                                         | decimal | TPM.olfactory area.2352                                                         |
| c_est_counts_olfactory_area_2352                                                  | decimal | est_counts.olfactory area.2352                                                  |
| c_tpm_olfactory_area_1805                                                         | decimal | TPM.olfactory area.1805                                                         |
| c_est_counts_olfactory_area_1805                                                  | decimal | est_counts.olfactory area.1805                                                  |
| c_tpm_olfactory_area_2222                                                         | decimal | TPM.olfactory area.2222                                                         |
| c_est_counts_olfactory_area_2222                                                  | decimal | est_counts.olfactory area.2222                                                  |
| c_tpm_olfactory_area_2756                                                         | decimal | TPM.olfactory area.2756                                                         |
| c_est_counts_olfactory_area_2756                                                  | decimal | est_counts.olfactory area.2756                                                  |
| c_tpm_olfactory_tubercle_1846                                                     | decimal | TPM.olfactory tubercle.1846                                                     |
| c_est_counts_olfactory_tubercle_1846                                              | decimal | est_counts.olfactory tubercle.1846                                              |
| c_tpm_olfactory_tubercle_2856                                                     | decimal | TPM.olfactory tubercle.2856                                                     |
| c_est_counts_olfactory_tubercle_2856                                              | decimal | est_counts.olfactory tubercle.2856                                              |
| c_tpm_olfactory_tubercle_1998                                                     | decimal | TPM.olfactory tubercle.1998                                                     |
| c_est_counts_olfactory_tubercle_1998                                              | decimal | est_counts.olfactory tubercle.1998                                              |
| c_tpm_olfactory_tubercle_2487                                                     | decimal | TPM.olfactory tubercle.2487                                                     |
| c_est_counts_olfactory_tubercle_2487                                              | decimal | est_counts.olfactory tubercle.2487                                              |
| c_tpm_orbitofrontal_gyrus__anterior_2862                                          | decimal | TPM.orbitofrontal gyrus, anterior.2862                                          |
| c_est_counts_orbitofrontal_gyrus__anterior_2862                                   | decimal | est_counts.orbitofrontal gyrus, anterior.2862                                   |
| c_tpm_orbitofrontal_gyrus__anterior_2863                                          | decimal | TPM.orbitofrontal gyrus, anterior.2863                                          |
| c_est_counts_orbitofrontal_gyrus__anterior_2863                                   | decimal | est_counts.orbitofrontal gyrus, anterior.2863                                   |
| c_tpm_orbitofrontal_gyrus__anterior_2864                                          | decimal | TPM.orbitofrontal gyrus, anterior.2864                                          |
| c_est_counts_orbitofrontal_gyrus__anterior_2864                                   | decimal | est_counts.orbitofrontal gyrus, anterior.2864                                   |
| c_tpm_paracentral_lobule__anterior_1926                                           | decimal | TPM.paracentral lobule, anterior.1926                                           |
| c_est_counts_paracentral_lobule__anterior_1926                                    | decimal | est_counts.paracentral lobule, anterior.1926                                    |
| c_tpm_paracentral_lobule__anterior_1754                                           | decimal | TPM.paracentral lobule, anterior.1754                                           |
| c_est_counts_paracentral_lobule__anterior_1754                                    | decimal | est_counts.paracentral lobule, anterior.1754                                    |
| c_tpm_paracentral_lobule__anterior_2474                                           | decimal | TPM.paracentral lobule, anterior.2474                                           |
| c_est_counts_paracentral_lobule__anterior_2474                                    | decimal | est_counts.paracentral lobule, anterior.2474                                    |
| c_tpm_paracentral_lobule__anterior_2638                                           | decimal | TPM.paracentral lobule, anterior.2638                                           |
| c_est_counts_paracentral_lobule__anterior_2638                                    | decimal | est_counts.paracentral lobule, anterior.2638                                    |
| c_tpm_paracentral_lobule__anterior_1776                                           | decimal | TPM.paracentral lobule, anterior.1776                                           |
| c_est_counts_paracentral_lobule__anterior_1776                                    | decimal | est_counts.paracentral lobule, anterior.1776                                    |
| c_tpm_paracentral_lobule__anterior_2340                                           | decimal | TPM.paracentral lobule, anterior.2340                                           |
| c_est_counts_paracentral_lobule__anterior_2340                                    | decimal | est_counts.paracentral lobule, anterior.2340                                    |
| c_tpm_paracentral_lobule__posterior_2345                                          | decimal | TPM.paracentral lobule, posterior.2345                                          |
| c_est_counts_paracentral_lobule__posterior_2345                                   | decimal | est_counts.paracentral lobule, posterior.2345                                   |
| c_tpm_paracentral_lobule__posterior_2446                                          | decimal | TPM.paracentral lobule, posterior.2446                                          |
| c_est_counts_paracentral_lobule__posterior_2446                                   | decimal | est_counts.paracentral lobule, posterior.2446                                   |
| c_tpm_paracentral_lobule__posterior_1764                                          | decimal | TPM.paracentral lobule, posterior.1764                                          |
| c_est_counts_paracentral_lobule__posterior_1764                                   | decimal | est_counts.paracentral lobule, posterior.1764                                   |
| c_tpm_paracentral_lobule__posterior_2551                                          | decimal | TPM.paracentral lobule, posterior.2551                                          |
| c_est_counts_paracentral_lobule__posterior_2551                                   | decimal | est_counts.paracentral lobule, posterior.2551                                   |
| c_tpm_paracentral_lobule__posterior_1775                                          | decimal | TPM.paracentral lobule, posterior.1775                                          |
| c_est_counts_paracentral_lobule__posterior_1775                                   | decimal | est_counts.paracentral lobule, posterior.1775                                   |
| c_tpm_parahippocampal_cortex_2532                                                 | decimal | TPM.parahippocampal cortex.2532                                                 |
| c_est_counts_parahippocampal_cortex_2532                                          | decimal | est_counts.parahippocampal cortex.2532                                          |
| c_tpm_parahippocampal_cortex_1850                                                 | decimal | TPM.parahippocampal cortex.1850                                                 |
| c_est_counts_parahippocampal_cortex_1850                                          | decimal | est_counts.parahippocampal cortex.1850                                          |
| c_tpm_parahippocampal_cortex_1990                                                 | decimal | TPM.parahippocampal cortex.1990                                                 |
| c_est_counts_parahippocampal_cortex_1990                                          | decimal | est_counts.parahippocampal cortex.1990                                          |
| c_tpm_parahippocampal_cortex_2245                                                 | decimal | TPM.parahippocampal cortex.2245                                                 |
| c_est_counts_parahippocampal_cortex_2245                                          | decimal | est_counts.parahippocampal cortex.2245                                          |
| c_tpm_parahippocampal_cortex_2692                                                 | decimal | TPM.parahippocampal cortex.2692                                                 |
| c_est_counts_parahippocampal_cortex_2692                                          | decimal | est_counts.parahippocampal cortex.2692                                          |
| c_tpm_parahippocampal_cortex_2693                                                 | decimal | TPM.parahippocampal cortex.2693                                                 |
| c_est_counts_parahippocampal_cortex_2693                                          | decimal | est_counts.parahippocampal cortex.2693                                          |
| c_tpm_parahippocampal_cortex_1933                                                 | decimal | TPM.parahippocampal cortex.1933                                                 |
| c_est_counts_parahippocampal_cortex_1933                                          | decimal | est_counts.parahippocampal cortex.1933                                          |
| c_tpm_parahippocampal_cortex_2250                                                 | decimal | TPM.parahippocampal cortex.2250                                                 |
| c_est_counts_parahippocampal_cortex_2250                                          | decimal | est_counts.parahippocampal cortex.2250                                          |
| c_tpm_parahippocampal_cortex_2622                                                 | decimal | TPM.parahippocampal cortex.2622                                                 |
| c_est_counts_parahippocampal_cortex_2622                                          | decimal | est_counts.parahippocampal cortex.2622                                          |
| c_tpm_parahippocampal_cortex_2018                                                 | decimal | TPM.parahippocampal cortex.2018                                                 |
| c_est_counts_parahippocampal_cortex_2018                                          | decimal | est_counts.parahippocampal cortex.2018                                          |
| c_tpm_parahippocampal_cortex__white_matter__2157                                  | decimal | TPM.parahippocampal cortex (white matter).2157                                  |
| c_est_counts_parahippocampal_cortex__white_matter__2157                           | decimal | est_counts.parahippocampal cortex (white matter).2157                           |
| c_tpm_paramedian_reticular_nucleus_2313                                           | decimal | TPM.paramedian reticular nucleus.2313                                           |
| c_est_counts_paramedian_reticular_nucleus_2313                                    | decimal | est_counts.paramedian reticular nucleus.2313                                    |
| c_tpm_paramedian_reticular_nucleus_2057                                           | decimal | TPM.paramedian reticular nucleus.2057                                           |
| c_est_counts_paramedian_reticular_nucleus_2057                                    | decimal | est_counts.paramedian reticular nucleus.2057                                    |
| c_tpm_paramedian_reticular_nucleus_2050                                           | decimal | TPM.paramedian reticular nucleus.2050                                           |
| c_est_counts_paramedian_reticular_nucleus_2050                                    | decimal | est_counts.paramedian reticular nucleus.2050                                    |
| c_tpm_paramedian_reticular_nucleus_2052                                           | decimal | TPM.paramedian reticular nucleus.2052                                           |
| c_est_counts_paramedian_reticular_nucleus_2052                                    | decimal | est_counts.paramedian reticular nucleus.2052                                    |
| c_tpm_paraventricular_nucleus_2700                                                | decimal | TPM.paraventricular nucleus.2700                                                |
| c_est_counts_paraventricular_nucleus_2700                                         | decimal | est_counts.paraventricular nucleus.2700                                         |
| c_tpm_parietal_operculum_2719                                                     | decimal | TPM.parietal operculum.2719                                                     |
| c_est_counts_parietal_operculum_2719                                              | decimal | est_counts.parietal operculum.2719                                              |
| c_tpm_parietal_operculum_1763                                                     | decimal | TPM.parietal operculum.1763                                                     |
| c_est_counts_parietal_operculum_1763                                              | decimal | est_counts.parietal operculum.1763                                              |
| c_tpm_parietal_operculum_2552                                                     | decimal | TPM.parietal operculum.2552                                                     |
| c_est_counts_parietal_operculum_2552                                              | decimal | est_counts.parietal operculum.2552                                              |
| c_tpm_parietal_operculum_2356                                                     | decimal | TPM.parietal operculum.2356                                                     |
| c_est_counts_parietal_operculum_2356                                              | decimal | est_counts.parietal operculum.2356                                              |
| c_tpm_parieto_insular_cortex_2232                                                 | decimal | TPM.parieto-insular cortex.2232                                                 |
| c_est_counts_parieto_insular_cortex_2232                                          | decimal | est_counts.parieto-insular cortex.2232                                          |
| c_tpm_parieto_insular_cortex_2671                                                 | decimal | TPM.parieto-insular cortex.2671                                                 |
| c_est_counts_parieto_insular_cortex_2671                                          | decimal | est_counts.parieto-insular cortex.2671                                          |
| c_tpm_parieto_insular_cortex_1976                                                 | decimal | TPM.parieto-insular cortex.1976                                                 |
| c_est_counts_parieto_insular_cortex_1976                                          | decimal | est_counts.parieto-insular cortex.1976                                          |
| c_tpm_parieto_insular_cortex_2508                                                 | decimal | TPM.parieto-insular cortex.2508                                                 |
| c_est_counts_parieto_insular_cortex_2508                                          | decimal | est_counts.parieto-insular cortex.2508                                          |
| c_tpm_parieto_insular_cortex_2831                                                 | decimal | TPM.parieto-insular cortex.2831                                                 |
| c_est_counts_parieto_insular_cortex_2831                                          | decimal | est_counts.parieto-insular cortex.2831                                          |
| c_tpm_parieto_occipital_transitional_area_2270                                    | decimal | TPM.parieto-occipital transitional area.2270                                    |
| c_est_counts_parieto_occipital_transitional_area_2270                             | decimal | est_counts.parieto-occipital transitional area.2270                             |
| c_tpm_parieto_occipital_transitional_area_2468                                    | decimal | TPM.parieto-occipital transitional area.2468                                    |
| c_est_counts_parieto_occipital_transitional_area_2468                             | decimal | est_counts.parieto-occipital transitional area.2468                             |
| c_tpm_parieto_occipital_transitional_area_2674                                    | decimal | TPM.parieto-occipital transitional area.2674                                    |
| c_est_counts_parieto_occipital_transitional_area_2674                             | decimal | est_counts.parieto-occipital transitional area.2674                             |
| c_tpm_parieto_occipital_transitional_area_2683                                    | decimal | TPM.parieto-occipital transitional area.2683                                    |
| c_est_counts_parieto_occipital_transitional_area_2683                             | decimal | est_counts.parieto-occipital transitional area.2683                             |
| c_tpm_parieto_occipital_transitional_area_1784                                    | decimal | TPM.parieto-occipital transitional area.1784                                    |
| c_est_counts_parieto_occipital_transitional_area_1784                             | decimal | est_counts.parieto-occipital transitional area.1784                             |
| c_tpm_parieto_temporal_junction__white_matter__2774                               | decimal | TPM.parieto-temporal junction (white matter).2774                               |
| c_est_counts_parieto_temporal_junction__white_matter__2774                        | decimal | est_counts.parieto-temporal junction (white matter).2774                        |
| c_tpm_parieto_temporal_junction__white_matter__2469                               | decimal | TPM.parieto-temporal junction (white matter).2469                               |
| c_est_counts_parieto_temporal_junction__white_matter__2469                        | decimal | est_counts.parieto-temporal junction (white matter).2469                        |
| c_tpm_parieto_temporal_junction__white_matter__2770                               | decimal | TPM.parieto-temporal junction (white matter).2770                               |
| c_est_counts_parieto_temporal_junction__white_matter__2770                        | decimal | est_counts.parieto-temporal junction (white matter).2770                        |
| c_tpm_parieto_temporal_junction__white_matter__1935                               | decimal | TPM.parieto-temporal junction (white matter).1935                               |
| c_est_counts_parieto_temporal_junction__white_matter__1935                        | decimal | est_counts.parieto-temporal junction (white matter).1935                        |
| c_tpm_parieto_temporal_junction__white_matter__1999                               | decimal | TPM.parieto-temporal junction (white matter).1999                               |
| c_est_counts_parieto_temporal_junction__white_matter__1999                        | decimal | est_counts.parieto-temporal junction (white matter).1999                        |
| c_tpm_parieto_temporal_junction__white_matter__2121                               | decimal | TPM.parieto-temporal junction (white matter).2121                               |
| c_est_counts_parieto_temporal_junction__white_matter__2121                        | decimal | est_counts.parieto-temporal junction (white matter).2121                        |
| c_tpm_parvicellular_reticular_nuclei_2119                                         | decimal | TPM.parvicellular reticular nuclei.2119                                         |
| c_est_counts_parvicellular_reticular_nuclei_2119                                  | decimal | est_counts.parvicellular reticular nuclei.2119                                  |
| c_tpm_parvicellular_reticular_nuclei_2558                                         | decimal | TPM.parvicellular reticular nuclei.2558                                         |
| c_est_counts_parvicellular_reticular_nuclei_2558                                  | decimal | est_counts.parvicellular reticular nuclei.2558                                  |
| c_tpm_parvicellular_reticular_nuclei_2095                                         | decimal | TPM.parvicellular reticular nuclei.2095                                         |
| c_est_counts_parvicellular_reticular_nuclei_2095                                  | decimal | est_counts.parvicellular reticular nuclei.2095                                  |
| c_tpm_parvicellular_reticular_nuclei__medullary_2181                              | decimal | TPM.parvicellular reticular nuclei, medullary.2181                              |
| c_est_counts_parvicellular_reticular_nuclei__medullary_2181                       | decimal | est_counts.parvicellular reticular nuclei, medullary.2181                       |
| c_tpm_parvicellular_reticular_nuclei__medullary_2189                              | decimal | TPM.parvicellular reticular nuclei, medullary.2189                              |
| c_est_counts_parvicellular_reticular_nuclei__medullary_2189                       | decimal | est_counts.parvicellular reticular nuclei, medullary.2189                       |
| c_tpm_parvicellular_reticular_nuclei__medullary_2091                              | decimal | TPM.parvicellular reticular nuclei, medullary.2091                              |
| c_est_counts_parvicellular_reticular_nuclei__medullary_2091                       | decimal | est_counts.parvicellular reticular nuclei, medullary.2091                       |
| c_tpm_pedunculopontine_tegmental_nucleus_2338                                     | decimal | TPM.pedunculopontine tegmental nucleus.2338                                     |
| c_est_counts_pedunculopontine_tegmental_nucleus_2338                              | decimal | est_counts.pedunculopontine tegmental nucleus.2338                              |
| c_tpm_pedunculopontine_tegmental_nucleus_2334                                     | decimal | TPM.pedunculopontine tegmental nucleus.2334                                     |
| c_est_counts_pedunculopontine_tegmental_nucleus_2334                              | decimal | est_counts.pedunculopontine tegmental nucleus.2334                              |
| c_tpm_pedunculopontine_tegmental_nucleus_1921                                     | decimal | TPM.pedunculopontine tegmental nucleus.1921                                     |
| c_est_counts_pedunculopontine_tegmental_nucleus_1921                              | decimal | est_counts.pedunculopontine tegmental nucleus.1921                              |
| c_tpm_periaquaductal_grey__anterior_1947                                          | decimal | TPM.periaquaductal grey, anterior.1947                                          |
| c_est_counts_periaquaductal_grey__anterior_1947                                   | decimal | est_counts.periaquaductal grey, anterior.1947                                   |
| c_tpm_periaquaductal_grey__anterior_2502                                          | decimal | TPM.periaquaductal grey, anterior.2502                                          |
| c_est_counts_periaquaductal_grey__anterior_2502                                   | decimal | est_counts.periaquaductal grey, anterior.2502                                   |
| c_tpm_periaquaductal_grey__anterior_1795                                          | decimal | TPM.periaquaductal grey, anterior.1795                                          |
| c_est_counts_periaquaductal_grey__anterior_1795                                   | decimal | est_counts.periaquaductal grey, anterior.1795                                   |
| c_tpm_periaquaductal_grey__dorsal_1831                                            | decimal | TPM.periaquaductal grey, dorsal.1831                                            |
| c_est_counts_periaquaductal_grey__dorsal_1831                                     | decimal | est_counts.periaquaductal grey, dorsal.1831                                     |
| c_tpm_periaquaductal_grey__dorsal_1840                                            | decimal | TPM.periaquaductal grey, dorsal.1840                                            |
| c_est_counts_periaquaductal_grey__dorsal_1840                                     | decimal | est_counts.periaquaductal grey, dorsal.1840                                     |
| c_tpm_periaquaductal_grey__dorsal_2464                                            | decimal | TPM.periaquaductal grey, dorsal.2464                                            |
| c_est_counts_periaquaductal_grey__dorsal_2464                                     | decimal | est_counts.periaquaductal grey, dorsal.2464                                     |
| c_tpm_periaquaductal_grey__dorsal_2850                                            | decimal | TPM.periaquaductal grey, dorsal.2850                                            |
| c_est_counts_periaquaductal_grey__dorsal_2850                                     | decimal | est_counts.periaquaductal grey, dorsal.2850                                     |
| c_tpm_periaquaductal_grey__lateral_2053                                           | decimal | TPM.periaquaductal grey, lateral.2053                                           |
| c_est_counts_periaquaductal_grey__lateral_2053                                    | decimal | est_counts.periaquaductal grey, lateral.2053                                    |
| c_tpm_periaquaductal_grey__lateral_2272                                           | decimal | TPM.periaquaductal grey, lateral.2272                                           |
| c_est_counts_periaquaductal_grey__lateral_2272                                    | decimal | est_counts.periaquaductal grey, lateral.2272                                    |
| c_tpm_periaquaductal_grey__lateral_2140                                           | decimal | TPM.periaquaductal grey, lateral.2140                                           |
| c_est_counts_periaquaductal_grey__lateral_2140                                    | decimal | est_counts.periaquaductal grey, lateral.2140                                    |
| c_tpm_perirhinal_gyrus_1794                                                       | decimal | TPM.perirhinal gyrus.1794                                                       |
| c_est_counts_perirhinal_gyrus_1794                                                | decimal | est_counts.perirhinal gyrus.1794                                                |
| c_tpm_perirhinal_gyrus_1847                                                       | decimal | TPM.perirhinal gyrus.1847                                                       |
| c_est_counts_perirhinal_gyrus_1847                                                | decimal | est_counts.perirhinal gyrus.1847                                                |
| c_tpm_perirhinal_gyrus_2521                                                       | decimal | TPM.perirhinal gyrus.2521                                                       |
| c_est_counts_perirhinal_gyrus_2521                                                | decimal | est_counts.perirhinal gyrus.2521                                                |
| c_tpm_perirhinal_gyrus_1841                                                       | decimal | TPM.perirhinal gyrus.1841                                                       |
| c_est_counts_perirhinal_gyrus_1841                                                | decimal | est_counts.perirhinal gyrus.1841                                                |
| c_tpm_perirhinal_gyrus_2848                                                       | decimal | TPM.perirhinal gyrus.2848                                                       |
| c_est_counts_perirhinal_gyrus_2848                                                | decimal | est_counts.perirhinal gyrus.2848                                                |
| c_tpm_peritrigeminal_nucleus_2179                                                 | decimal | TPM.peritrigeminal nucleus.2179                                                 |
| c_est_counts_peritrigeminal_nucleus_2179                                          | decimal | est_counts.peritrigeminal nucleus.2179                                          |
| c_tpm_peritrigeminal_nucleus_2067                                                 | decimal | TPM.peritrigeminal nucleus.2067                                                 |
| c_est_counts_peritrigeminal_nucleus_2067                                          | decimal | est_counts.peritrigeminal nucleus.2067                                          |
| c_tpm_peritrigeminal_nucleus_2136                                                 | decimal | TPM.peritrigeminal nucleus.2136                                                 |
| c_est_counts_peritrigeminal_nucleus_2136                                          | decimal | est_counts.peritrigeminal nucleus.2136                                          |
| c_tpm_piriform_cortex_2347                                                        | decimal | TPM.piriform cortex.2347                                                        |
| c_est_counts_piriform_cortex_2347                                                 | decimal | est_counts.piriform cortex.2347                                                 |
| c_tpm_piriform_cortex_2153                                                        | decimal | TPM.piriform cortex.2153                                                        |
| c_est_counts_piriform_cortex_2153                                                 | decimal | est_counts.piriform cortex.2153                                                 |
| c_tpm_pontine_nuclei_2109                                                         | decimal | TPM.pontine nuclei.2109                                                         |
| c_est_counts_pontine_nuclei_2109                                                  | decimal | est_counts.pontine nuclei.2109                                                  |
| c_tpm_pontine_nuclei_2727                                                         | decimal | TPM.pontine nuclei.2727                                                         |
| c_est_counts_pontine_nuclei_2727                                                  | decimal | est_counts.pontine nuclei.2727                                                  |
| c_tpm_pontine_nuclei_2115                                                         | decimal | TPM.pontine nuclei.2115                                                         |
| c_est_counts_pontine_nuclei_2115                                                  | decimal | est_counts.pontine nuclei.2115                                                  |
| c_tpm_pontine_nuclei_2319                                                         | decimal | TPM.pontine nuclei.2319                                                         |
| c_est_counts_pontine_nuclei_2319                                                  | decimal | est_counts.pontine nuclei.2319                                                  |
| c_tpm_pontine_nuclei_2454                                                         | decimal | TPM.pontine nuclei.2454                                                         |
| c_est_counts_pontine_nuclei_2454                                                  | decimal | est_counts.pontine nuclei.2454                                                  |
| c_tpm_pontine_nuclei_2787                                                         | decimal | TPM.pontine nuclei.2787                                                         |
| c_est_counts_pontine_nuclei_2787                                                  | decimal | est_counts.pontine nuclei.2787                                                  |
| c_tpm_pontine_nuclei_1968                                                         | decimal | TPM.pontine nuclei.1968                                                         |
| c_est_counts_pontine_nuclei_1968                                                  | decimal | est_counts.pontine nuclei.1968                                                  |
| c_tpm_pontine_nuclei_1863                                                         | decimal | TPM.pontine nuclei.1863                                                         |
| c_est_counts_pontine_nuclei_1863                                                  | decimal | est_counts.pontine nuclei.1863                                                  |
| c_tpm_pontine_raphe_nucleus_2122                                                  | decimal | TPM.pontine raphe nucleus.2122                                                  |
| c_est_counts_pontine_raphe_nucleus_2122                                           | decimal | est_counts.pontine raphe nucleus.2122                                           |
| c_tpm_pontine_raphe_nucleus_2853                                                  | decimal | TPM.pontine raphe nucleus.2853                                                  |
| c_est_counts_pontine_raphe_nucleus_2853                                           | decimal | est_counts.pontine raphe nucleus.2853                                           |
| c_tpm_postcentral_gyrus_2533                                                      | decimal | TPM.postcentral gyrus.2533                                                      |
| c_est_counts_postcentral_gyrus_2533                                               | decimal | est_counts.postcentral gyrus.2533                                               |
| c_tpm_postcentral_gyrus__dorsal_2151                                              | decimal | TPM.postcentral gyrus, dorsal.2151                                              |
| c_est_counts_postcentral_gyrus__dorsal_2151                                       | decimal | est_counts.postcentral gyrus, dorsal.2151                                       |
| c_tpm_postcentral_gyrus__dorsal_2350                                              | decimal | TPM.postcentral gyrus, dorsal.2350                                              |
| c_est_counts_postcentral_gyrus__dorsal_2350                                       | decimal | est_counts.postcentral gyrus, dorsal.2350                                       |
| c_tpm_postcentral_gyrus__dorsal_2544                                              | decimal | TPM.postcentral gyrus, dorsal.2544                                              |
| c_est_counts_postcentral_gyrus__dorsal_2544                                       | decimal | est_counts.postcentral gyrus, dorsal.2544                                       |
| c_tpm_postcentral_gyrus__dorsal_2477                                              | decimal | TPM.postcentral gyrus, dorsal.2477                                              |
| c_est_counts_postcentral_gyrus__dorsal_2477                                       | decimal | est_counts.postcentral gyrus, dorsal.2477                                       |
| c_tpm_postcentral_gyrus__dorsal_1836                                              | decimal | TPM.postcentral gyrus, dorsal.1836                                              |
| c_est_counts_postcentral_gyrus__dorsal_1836                                       | decimal | est_counts.postcentral gyrus, dorsal.1836                                       |
| c_tpm_postcentral_gyrus__dorsal_2339                                              | decimal | TPM.postcentral gyrus, dorsal.2339                                              |
| c_est_counts_postcentral_gyrus__dorsal_2339                                       | decimal | est_counts.postcentral gyrus, dorsal.2339                                       |
| c_tpm_postcentral_gyrus__middle_2248                                              | decimal | TPM.postcentral gyrus, middle.2248                                              |
| c_est_counts_postcentral_gyrus__middle_2248                                       | decimal | est_counts.postcentral gyrus, middle.2248                                       |
| c_tpm_postcentral_gyrus__middle_2444                                              | decimal | TPM.postcentral gyrus, middle.2444                                              |
| c_est_counts_postcentral_gyrus__middle_2444                                       | decimal | est_counts.postcentral gyrus, middle.2444                                       |
| c_tpm_postcentral_gyrus__middle_2545                                              | decimal | TPM.postcentral gyrus, middle.2545                                              |
| c_est_counts_postcentral_gyrus__middle_2545                                       | decimal | est_counts.postcentral gyrus, middle.2545                                       |
| c_tpm_postcentral_gyrus__middle_1897                                              | decimal | TPM.postcentral gyrus, middle.1897                                              |
| c_est_counts_postcentral_gyrus__middle_1897                                       | decimal | est_counts.postcentral gyrus, middle.1897                                       |
| c_tpm_postcentral_gyrus__middle_2146                                              | decimal | TPM.postcentral gyrus, middle.2146                                              |
| c_est_counts_postcentral_gyrus__middle_2146                                       | decimal | est_counts.postcentral gyrus, middle.2146                                       |
| c_tpm_postcentral_gyrus__ventral_2445                                             | decimal | TPM.postcentral gyrus, ventral.2445                                             |
| c_est_counts_postcentral_gyrus__ventral_2445                                      | decimal | est_counts.postcentral gyrus, ventral.2445                                      |
| c_tpm_postcentral_gyrus__ventral_2836                                             | decimal | TPM.postcentral gyrus, ventral.2836                                             |
| c_est_counts_postcentral_gyrus__ventral_2836                                      | decimal | est_counts.postcentral gyrus, ventral.2836                                      |
| c_tpm_postcentral_gyrus__ventral_2024                                             | decimal | TPM.postcentral gyrus, ventral.2024                                             |
| c_est_counts_postcentral_gyrus__ventral_2024                                      | decimal | est_counts.postcentral gyrus, ventral.2024                                      |
| c_tpm_posterior_cingulate_cortex_2473                                             | decimal | TPM.posterior cingulate cortex.2473                                             |
| c_est_counts_posterior_cingulate_cortex_2473                                      | decimal | est_counts.posterior cingulate cortex.2473                                      |
| c_tpm_posterior_cingulate_cortex_1759                                             | decimal | TPM.posterior cingulate cortex.1759                                             |
| c_est_counts_posterior_cingulate_cortex_1759                                      | decimal | est_counts.posterior cingulate cortex.1759                                      |
| c_tpm_posterior_cingulate_cortex_2553                                             | decimal | TPM.posterior cingulate cortex.2553                                             |
| c_est_counts_posterior_cingulate_cortex_2553                                      | decimal | est_counts.posterior cingulate cortex.2553                                      |
| c_tpm_posterior_cingulate_cortex__dorsal_2343                                     | decimal | TPM.posterior cingulate cortex, dorsal.2343                                     |
| c_est_counts_posterior_cingulate_cortex__dorsal_2343                              | decimal | est_counts.posterior cingulate cortex, dorsal.2343                              |
| c_tpm_posterior_cingulate_cortex__dorsal_2540                                     | decimal | TPM.posterior cingulate cortex, dorsal.2540                                     |
| c_est_counts_posterior_cingulate_cortex__dorsal_2540                              | decimal | est_counts.posterior cingulate cortex, dorsal.2540                              |
| c_tpm_posterior_cingulate_cortex__dorsal_2634                                     | decimal | TPM.posterior cingulate cortex, dorsal.2634                                     |
| c_est_counts_posterior_cingulate_cortex__dorsal_2634                              | decimal | est_counts.posterior cingulate cortex, dorsal.2634                              |
| c_tpm_posterior_cingulate_cortex__dorsal_2641                                     | decimal | TPM.posterior cingulate cortex, dorsal.2641                                     |
| c_est_counts_posterior_cingulate_cortex__dorsal_2641                              | decimal | est_counts.posterior cingulate cortex, dorsal.2641                              |
| c_tpm_posterior_cingulate_cortex__dorsal_2076                                     | decimal | TPM.posterior cingulate cortex, dorsal.2076                                     |
| c_est_counts_posterior_cingulate_cortex__dorsal_2076                              | decimal | est_counts.posterior cingulate cortex, dorsal.2076                              |
| c_tpm_posterior_cingulate_cortex__dorsal_2556                                     | decimal | TPM.posterior cingulate cortex, dorsal.2556                                     |
| c_est_counts_posterior_cingulate_cortex__dorsal_2556                              | decimal | est_counts.posterior cingulate cortex, dorsal.2556                              |
| c_tpm_posterior_cingulate_cortex__ventral_2346                                    | decimal | TPM.posterior cingulate cortex, ventral.2346                                    |
| c_est_counts_posterior_cingulate_cortex__ventral_2346                             | decimal | est_counts.posterior cingulate cortex, ventral.2346                             |
| c_tpm_posterior_cingulate_cortex__ventral_2541                                    | decimal | TPM.posterior cingulate cortex, ventral.2541                                    |
| c_est_counts_posterior_cingulate_cortex__ventral_2541                             | decimal | est_counts.posterior cingulate cortex, ventral.2541                             |
| c_tpm_posterior_cingulate_cortex__ventral_2635                                    | decimal | TPM.posterior cingulate cortex, ventral.2635                                    |
| c_est_counts_posterior_cingulate_cortex__ventral_2635                             | decimal | est_counts.posterior cingulate cortex, ventral.2635                             |
| c_tpm_posterior_cingulate_cortex__ventral_1762                                    | decimal | TPM.posterior cingulate cortex, ventral.1762                                    |
| c_est_counts_posterior_cingulate_cortex__ventral_1762                             | decimal | est_counts.posterior cingulate cortex, ventral.1762                             |
| c_tpm_posterior_cingulate_cortex__ventral_1994                                    | decimal | TPM.posterior cingulate cortex, ventral.1994                                    |
| c_est_counts_posterior_cingulate_cortex__ventral_1994                             | decimal | est_counts.posterior cingulate cortex, ventral.1994                             |
| c_tpm_posterior_cingulate_cortex__ventral_2448                                    | decimal | TPM.posterior cingulate cortex, ventral.2448                                    |
| c_est_counts_posterior_cingulate_cortex__ventral_2448                             | decimal | est_counts.posterior cingulate cortex, ventral.2448                             |
| c_tpm_posterior_insular_cortex_2231                                               | decimal | TPM.posterior insular cortex.2231                                               |
| c_est_counts_posterior_insular_cortex_2231                                        | decimal | est_counts.posterior insular cortex.2231                                        |
| c_tpm_posterior_insular_cortex_2597                                               | decimal | TPM.posterior insular cortex.2597                                               |
| c_est_counts_posterior_insular_cortex_2597                                        | decimal | est_counts.posterior insular cortex.2597                                        |
| c_tpm_posterior_insular_cortex_2832                                               | decimal | TPM.posterior insular cortex.2832                                               |
| c_est_counts_posterior_insular_cortex_2832                                        | decimal | est_counts.posterior insular cortex.2832                                        |
| c_tpm_posterior_insular_cortex_2603                                               | decimal | TPM.posterior insular cortex.2603                                               |
| c_est_counts_posterior_insular_cortex_2603                                        | decimal | est_counts.posterior insular cortex.2603                                        |
| c_tpm_posterior_insular_cortex_2511                                               | decimal | TPM.posterior insular cortex.2511                                               |
| c_est_counts_posterior_insular_cortex_2511                                        | decimal | est_counts.posterior insular cortex.2511                                        |
| c_tpm_posterior_insular_cortex_1823                                               | decimal | TPM.posterior insular cortex.1823                                               |
| c_est_counts_posterior_insular_cortex_1823                                        | decimal | est_counts.posterior insular cortex.1823                                        |
| c_tpm_posterior_thalamic_nucleus_2655                                             | decimal | TPM.posterior thalamic nucleus.2655                                             |
| c_est_counts_posterior_thalamic_nucleus_2655                                      | decimal | est_counts.posterior thalamic nucleus.2655                                      |
| c_tpm_posterior_thalamic_nucleus_2649                                             | decimal | TPM.posterior thalamic nucleus.2649                                             |
| c_est_counts_posterior_thalamic_nucleus_2649                                      | decimal | est_counts.posterior thalamic nucleus.2649                                      |
| c_tpm_posterior_thalamic_nucleus_2495                                             | decimal | TPM.posterior thalamic nucleus.2495                                             |
| c_est_counts_posterior_thalamic_nucleus_2495                                      | decimal | est_counts.posterior thalamic nucleus.2495                                      |
| c_tpm_posterior_thalamic_nucleus_2266                                             | decimal | TPM.posterior thalamic nucleus.2266                                             |
| c_est_counts_posterior_thalamic_nucleus_2266                                      | decimal | est_counts.posterior thalamic nucleus.2266                                      |
| c_tpm_posteroventral_cochlear_nucleus_2371                                        | decimal | TPM.posteroventral cochlear nucleus.2371                                        |
| c_est_counts_posteroventral_cochlear_nucleus_2371                                 | decimal | est_counts.posteroventral cochlear nucleus.2371                                 |
| c_tpm_posteroventral_cochlear_nucleus_2341                                        | decimal | TPM.posteroventral cochlear nucleus.2341                                        |
| c_est_counts_posteroventral_cochlear_nucleus_2341                                 | decimal | est_counts.posteroventral cochlear nucleus.2341                                 |
| c_tpm_posteroventral_cochlear_nucleus_2135                                        | decimal | TPM.posteroventral cochlear nucleus.2135                                        |
| c_est_counts_posteroventral_cochlear_nucleus_2135                                 | decimal | est_counts.posteroventral cochlear nucleus.2135                                 |
| c_tpm_posteroventral_cochlear_nucleus_2752                                        | decimal | TPM.posteroventral cochlear nucleus.2752                                        |
| c_est_counts_posteroventral_cochlear_nucleus_2752                                 | decimal | est_counts.posteroventral cochlear nucleus.2752                                 |
| c_tpm_posteroventral_cochlear_nucleus_2070                                        | decimal | TPM.posteroventral cochlear nucleus.2070                                        |
| c_est_counts_posteroventral_cochlear_nucleus_2070                                 | decimal | est_counts.posteroventral cochlear nucleus.2070                                 |
| c_tpm_precentral_gyrus_2557                                                       | decimal | TPM.precentral gyrus.2557                                                       |
| c_est_counts_precentral_gyrus_2557                                                | decimal | est_counts.precentral gyrus.2557                                                |
| c_tpm_precentral_gyrus__dorsal_2442                                               | decimal | TPM.precentral gyrus, dorsal.2442                                               |
| c_est_counts_precentral_gyrus__dorsal_2442                                        | decimal | est_counts.precentral gyrus, dorsal.2442                                        |
| c_tpm_precentral_gyrus__dorsal_1756                                               | decimal | TPM.precentral gyrus, dorsal.1756                                               |
| c_est_counts_precentral_gyrus__dorsal_1756                                        | decimal | est_counts.precentral gyrus, dorsal.1756                                        |
| c_tpm_precentral_gyrus__dorsal_2476                                               | decimal | TPM.precentral gyrus, dorsal.2476                                               |
| c_est_counts_precentral_gyrus__dorsal_2476                                        | decimal | est_counts.precentral gyrus, dorsal.2476                                        |
| c_tpm_precentral_gyrus__dorsal_2354                                               | decimal | TPM.precentral gyrus, dorsal.2354                                               |
| c_est_counts_precentral_gyrus__dorsal_2354                                        | decimal | est_counts.precentral gyrus, dorsal.2354                                        |
| c_tpm_precentral_gyrus__middle_1909                                               | decimal | TPM.precentral gyrus, middle.1909                                               |
| c_est_counts_precentral_gyrus__middle_1909                                        | decimal | est_counts.precentral gyrus, middle.1909                                        |
| c_tpm_precentral_gyrus__middle_2443                                               | decimal | TPM.precentral gyrus, middle.2443                                               |
| c_est_counts_precentral_gyrus__middle_2443                                        | decimal | est_counts.precentral gyrus, middle.2443                                        |
| c_tpm_precentral_gyrus__middle_2475                                               | decimal | TPM.precentral gyrus, middle.2475                                               |
| c_est_counts_precentral_gyrus__middle_2475                                        | decimal | est_counts.precentral gyrus, middle.2475                                        |
| c_tpm_precentral_gyrus__middle_2549                                               | decimal | TPM.precentral gyrus, middle.2549                                               |
| c_est_counts_precentral_gyrus__middle_2549                                        | decimal | est_counts.precentral gyrus, middle.2549                                        |
| c_tpm_precentral_gyrus__middle_1969                                               | decimal | TPM.precentral gyrus, middle.1969                                               |
| c_est_counts_precentral_gyrus__middle_1969                                        | decimal | est_counts.precentral gyrus, middle.1969                                        |
| c_tpm_precentral_gyrus__ventral_2630                                              | decimal | TPM.precentral gyrus, ventral.2630                                              |
| c_est_counts_precentral_gyrus__ventral_2630                                       | decimal | est_counts.precentral gyrus, ventral.2630                                       |
| c_tpm_precentral_gyrus__ventral_2678                                              | decimal | TPM.precentral gyrus, ventral.2678                                              |
| c_est_counts_precentral_gyrus__ventral_2678                                       | decimal | est_counts.precentral gyrus, ventral.2678                                       |
| c_tpm_precentral_gyrus__ventral_2550                                              | decimal | TPM.precentral gyrus, ventral.2550                                              |
| c_est_counts_precentral_gyrus__ventral_2550                                       | decimal | est_counts.precentral gyrus, ventral.2550                                       |
| c_tpm_precentral_gyrus__ventral_2662                                              | decimal | TPM.precentral gyrus, ventral.2662                                              |
| c_est_counts_precentral_gyrus__ventral_2662                                       | decimal | est_counts.precentral gyrus, ventral.2662                                       |
| c_tpm_precuneus_2594                                                              | decimal | TPM.precuneus.2594                                                              |
| c_est_counts_precuneus_2594                                                       | decimal | est_counts.precuneus.2594                                                       |
| c_tpm_precuneus_2467                                                              | decimal | TPM.precuneus.2467                                                              |
| c_est_counts_precuneus_2467                                                       | decimal | est_counts.precuneus.2467                                                       |
| c_tpm_precuneus_1780                                                              | decimal | TPM.precuneus.1780                                                              |
| c_est_counts_precuneus_1780                                                       | decimal | est_counts.precuneus.1780                                                       |
| c_tpm_precuneus_2673                                                              | decimal | TPM.precuneus.2673                                                              |
| c_est_counts_precuneus_2673                                                       | decimal | est_counts.precuneus.2673                                                       |
| c_tpm_precuneus_2510                                                              | decimal | TPM.precuneus.2510                                                              |
| c_est_counts_precuneus_2510                                                       | decimal | est_counts.precuneus.2510                                                       |
| c_tpm_precuneus_1782                                                              | decimal | TPM.precuneus.1782                                                              |
| c_est_counts_precuneus_1782                                                       | decimal | est_counts.precuneus.1782                                                       |
| c_tpm_premotor_cortex__dorsal_2027                                                | decimal | TPM.premotor cortex, dorsal.2027                                                |
| c_est_counts_premotor_cortex__dorsal_2027                                         | decimal | est_counts.premotor cortex, dorsal.2027                                         |
| c_tpm_premotor_cortex__dorsal_2536                                                | decimal | TPM.premotor cortex, dorsal.2536                                                |
| c_est_counts_premotor_cortex__dorsal_2536                                         | decimal | est_counts.premotor cortex, dorsal.2536                                         |
| c_tpm_premotor_cortex__dorsal_2631                                                | decimal | TPM.premotor cortex, dorsal.2631                                                |
| c_est_counts_premotor_cortex__dorsal_2631                                         | decimal | est_counts.premotor cortex, dorsal.2631                                         |
| c_tpm_premotor_cortex__dorsal_1878                                                | decimal | TPM.premotor cortex, dorsal.1878                                                |
| c_est_counts_premotor_cortex__dorsal_1878                                         | decimal | est_counts.premotor cortex, dorsal.1878                                         |
| c_tpm_premotor_cortex__dorsal_2554                                                | decimal | TPM.premotor cortex, dorsal.2554                                                |
| c_est_counts_premotor_cortex__dorsal_2554                                         | decimal | est_counts.premotor cortex, dorsal.2554                                         |
| c_tpm_premotor_cortex__ventral_1779                                               | decimal | TPM.premotor cortex, ventral.1779                                               |
| c_est_counts_premotor_cortex__ventral_1779                                        | decimal | est_counts.premotor cortex, ventral.1779                                        |
| c_tpm_premotor_cortex__ventral_2349                                               | decimal | TPM.premotor cortex, ventral.2349                                               |
| c_est_counts_premotor_cortex__ventral_2349                                        | decimal | est_counts.premotor cortex, ventral.2349                                        |
| c_tpm_premotor_cortex__ventral_1757                                               | decimal | TPM.premotor cortex, ventral.1757                                               |
| c_est_counts_premotor_cortex__ventral_1757                                        | decimal | est_counts.premotor cortex, ventral.1757                                        |
| c_tpm_premotor_cortex__ventral_2637                                               | decimal | TPM.premotor cortex, ventral.2637                                               |
| c_est_counts_premotor_cortex__ventral_2637                                        | decimal | est_counts.premotor cortex, ventral.2637                                        |
| c_tpm_premotor_cortex__ventral_1881                                               | decimal | TPM.premotor cortex, ventral.1881                                               |
| c_est_counts_premotor_cortex__ventral_1881                                        | decimal | est_counts.premotor cortex, ventral.1881                                        |
| c_tpm_premotor_cortex__ventral_1777                                               | decimal | TPM.premotor cortex, ventral.1777                                               |
| c_est_counts_premotor_cortex__ventral_1777                                        | decimal | est_counts.premotor cortex, ventral.1777                                        |
| c_tpm_preoptic_area_1861                                                          | decimal | TPM.preoptic area.1861                                                          |
| c_est_counts_preoptic_area_1861                                                   | decimal | est_counts.preoptic area.1861                                                   |
| c_tpm_preoptic_area_2414                                                          | decimal | TPM.preoptic area.2414                                                          |
| c_est_counts_preoptic_area_2414                                                   | decimal | est_counts.preoptic area.2414                                                   |
| c_tpm_preoptic_area_1907                                                          | decimal | TPM.preoptic area.1907                                                          |
| c_est_counts_preoptic_area_1907                                                   | decimal | est_counts.preoptic area.1907                                                   |
| c_tpm_prepositus_hypoglossal_nucleus_2086                                         | decimal | TPM.prepositus hypoglossal nucleus.2086                                         |
| c_est_counts_prepositus_hypoglossal_nucleus_2086                                  | decimal | est_counts.prepositus hypoglossal nucleus.2086                                  |
| c_tpm_prepositus_hypoglossal_nucleus_2855                                         | decimal | TPM.prepositus hypoglossal nucleus.2855                                         |
| c_est_counts_prepositus_hypoglossal_nucleus_2855                                  | decimal | est_counts.prepositus hypoglossal nucleus.2855                                  |
| c_tpm_pretectal_area_1817                                                         | decimal | TPM.pretectal area.1817                                                         |
| c_est_counts_pretectal_area_1817                                                  | decimal | est_counts.pretectal area.1817                                                  |
| c_tpm_pretectal_area_1944                                                         | decimal | TPM.pretectal area.1944                                                         |
| c_est_counts_pretectal_area_1944                                                  | decimal | est_counts.pretectal area.1944                                                  |
| c_tpm_pretectal_area_2007                                                         | decimal | TPM.pretectal area.2007                                                         |
| c_est_counts_pretectal_area_2007                                                  | decimal | est_counts.pretectal area.2007                                                  |
| c_tpm_pretectal_area_1815                                                         | decimal | TPM.pretectal area.1815                                                         |
| c_est_counts_pretectal_area_1815                                                  | decimal | est_counts.pretectal area.1815                                                  |
| c_tpm_pretectal_area_2825                                                         | decimal | TPM.pretectal area.2825                                                         |
| c_est_counts_pretectal_area_2825                                                  | decimal | est_counts.pretectal area.2825                                                  |
| c_tpm_pretectal_area_2224                                                         | decimal | TPM.pretectal area.2224                                                         |
| c_est_counts_pretectal_area_2224                                                  | decimal | est_counts.pretectal area.2224                                                  |
| c_tpm_pretectal_area_2667                                                         | decimal | TPM.pretectal area.2667                                                         |
| c_est_counts_pretectal_area_2667                                                  | decimal | est_counts.pretectal area.2667                                                  |
| c_tpm_pretectal_area_2407                                                         | decimal | TPM.pretectal area.2407                                                         |
| c_est_counts_pretectal_area_2407                                                  | decimal | est_counts.pretectal area.2407                                                  |
| c_tpm_pretectal_area_2273                                                         | decimal | TPM.pretectal area.2273                                                         |
| c_est_counts_pretectal_area_2273                                                  | decimal | est_counts.pretectal area.2273                                                  |
| c_tpm_pretectal_area_2316                                                         | decimal | TPM.pretectal area.2316                                                         |
| c_est_counts_pretectal_area_2316                                                  | decimal | est_counts.pretectal area.2316                                                  |
| c_tpm_pretectal_area_1816                                                         | decimal | TPM.pretectal area.1816                                                         |
| c_est_counts_pretectal_area_1816                                                  | decimal | est_counts.pretectal area.1816                                                  |
| c_tpm_principal_sensory_trigeminal_nucleus_2158                                   | decimal | TPM.principal sensory trigeminal nucleus.2158                                   |
| c_est_counts_principal_sensory_trigeminal_nucleus_2158                            | decimal | est_counts.principal sensory trigeminal nucleus.2158                            |
| c_tpm_principal_sensory_trigeminal_nucleus_2008                                   | decimal | TPM.principal sensory trigeminal nucleus.2008                                   |
| c_est_counts_principal_sensory_trigeminal_nucleus_2008                            | decimal | est_counts.principal sensory trigeminal nucleus.2008                            |
| c_tpm_principal_sensory_trigeminal_nucleus_2367                                   | decimal | TPM.principal sensory trigeminal nucleus.2367                                   |
| c_est_counts_principal_sensory_trigeminal_nucleus_2367                            | decimal | est_counts.principal sensory trigeminal nucleus.2367                            |
| c_tpm_principal_sensory_trigeminal_nucleus_2324                                   | decimal | TPM.principal sensory trigeminal nucleus.2324                                   |
| c_est_counts_principal_sensory_trigeminal_nucleus_2324                            | decimal | est_counts.principal sensory trigeminal nucleus.2324                            |
| c_tpm_pulvinar_1899                                                               | decimal | TPM.pulvinar.1899                                                               |
| c_est_counts_pulvinar_1899                                                        | decimal | est_counts.pulvinar.1899                                                        |
| c_tpm_pulvinar_1972                                                               | decimal | TPM.pulvinar.1972                                                               |
| c_est_counts_pulvinar_1972                                                        | decimal | est_counts.pulvinar.1972                                                        |
| c_tpm_pulvinar_2499                                                               | decimal | TPM.pulvinar.2499                                                               |
| c_est_counts_pulvinar_2499                                                        | decimal | est_counts.pulvinar.2499                                                        |
| c_tpm_pulvinar_1929                                                               | decimal | TPM.pulvinar.1929                                                               |
| c_est_counts_pulvinar_1929                                                        | decimal | est_counts.pulvinar.1929                                                        |
| c_tpm_pulvinar_2582                                                               | decimal | TPM.pulvinar.2582                                                               |
| c_est_counts_pulvinar_2582                                                        | decimal | est_counts.pulvinar.2582                                                        |
| c_tpm_pulvinar_2398                                                               | decimal | TPM.pulvinar.2398                                                               |
| c_est_counts_pulvinar_2398                                                        | decimal | est_counts.pulvinar.2398                                                        |
| c_tpm_pulvinar_1932                                                               | decimal | TPM.pulvinar.1932                                                               |
| c_est_counts_pulvinar_1932                                                        | decimal | est_counts.pulvinar.1932                                                        |
| c_tpm_pulvinar_2724                                                               | decimal | TPM.pulvinar.2724                                                               |
| c_est_counts_pulvinar_2724                                                        | decimal | est_counts.pulvinar.2724                                                        |
| c_tpm_pulvinar_2496                                                               | decimal | TPM.pulvinar.2496                                                               |
| c_est_counts_pulvinar_2496                                                        | decimal | est_counts.pulvinar.2496                                                        |
| c_tpm_pulvinar_2214                                                               | decimal | TPM.pulvinar.2214                                                               |
| c_est_counts_pulvinar_2214                                                        | decimal | est_counts.pulvinar.2214                                                        |
| c_tpm_putamen_2466                                                                | decimal | TPM.putamen.2466                                                                |
| c_est_counts_putamen_2466                                                         | decimal | est_counts.putamen.2466                                                         |
| c_tpm_putamen_2489                                                                | decimal | TPM.putamen.2489                                                                |
| c_est_counts_putamen_2489                                                         | decimal | est_counts.putamen.2489                                                         |
| c_tpm_putamen_1838                                                                | decimal | TPM.putamen.1838                                                                |
| c_est_counts_putamen_1838                                                         | decimal | est_counts.putamen.1838                                                         |
| c_tpm_putamen_2647                                                                | decimal | TPM.putamen.2647                                                                |
| c_est_counts_putamen_2647                                                         | decimal | est_counts.putamen.2647                                                         |
| c_tpm_putamen_1937                                                                | decimal | TPM.putamen.1937                                                                |
| c_est_counts_putamen_1937                                                         | decimal | est_counts.putamen.1937                                                         |
| c_tpm_putamen_2482                                                                | decimal | TPM.putamen.2482                                                                |
| c_est_counts_putamen_2482                                                         | decimal | est_counts.putamen.2482                                                         |
| c_tpm_putamen_1829                                                                | decimal | TPM.putamen.1829                                                                |
| c_est_counts_putamen_1829                                                         | decimal | est_counts.putamen.1829                                                         |
| c_tpm_red_nucleus_1954                                                            | decimal | TPM.red nucleus.1954                                                            |
| c_est_counts_red_nucleus_1954                                                     | decimal | est_counts.red nucleus.1954                                                     |
| c_tpm_red_nucleus_1821                                                            | decimal | TPM.red nucleus.1821                                                            |
| c_est_counts_red_nucleus_1821                                                     | decimal | est_counts.red nucleus.1821                                                     |
| c_tpm_red_nucleus_2227                                                            | decimal | TPM.red nucleus.2227                                                            |
| c_est_counts_red_nucleus_2227                                                     | decimal | est_counts.red nucleus.2227                                                     |
| c_tpm_red_nucleus_2769                                                            | decimal | TPM.red nucleus.2769                                                            |
| c_est_counts_red_nucleus_2769                                                     | decimal | est_counts.red nucleus.2769                                                     |
| c_tpm_red_nucleus_1904                                                            | decimal | TPM.red nucleus.1904                                                            |
| c_est_counts_red_nucleus_1904                                                     | decimal | est_counts.red nucleus.1904                                                     |
| c_tpm_red_nucleus_2785                                                            | decimal | TPM.red nucleus.2785                                                            |
| c_est_counts_red_nucleus_2785                                                     | decimal | est_counts.red nucleus.2785                                                     |
| c_tpm_red_nucleus_2503                                                            | decimal | TPM.red nucleus.2503                                                            |
| c_est_counts_red_nucleus_2503                                                     | decimal | est_counts.red nucleus.2503                                                     |
| c_tpm_red_nucleus_2725                                                            | decimal | TPM.red nucleus.2725                                                            |
| c_est_counts_red_nucleus_2725                                                     | decimal | est_counts.red nucleus.2725                                                     |
| c_tpm_red_nucleus_2584                                                            | decimal | TPM.red nucleus.2584                                                            |
| c_est_counts_red_nucleus_2584                                                     | decimal | est_counts.red nucleus.2584                                                     |
| c_tpm_red_nucleus_2588                                                            | decimal | TPM.red nucleus.2588                                                            |
| c_est_counts_red_nucleus_2588                                                     | decimal | est_counts.red nucleus.2588                                                     |
| c_tpm_red_nucleus_2823                                                            | decimal | TPM.red nucleus.2823                                                            |
| c_est_counts_red_nucleus_2823                                                     | decimal | est_counts.red nucleus.2823                                                     |
| c_tpm_red_nucleus_1865                                                            | decimal | TPM.red nucleus.1865                                                            |
| c_est_counts_red_nucleus_1865                                                     | decimal | est_counts.red nucleus.1865                                                     |
| c_tpm_reticular_pontine_nucleus__caudal_2332                                      | decimal | TPM.reticular pontine nucleus, caudal.2332                                      |
| c_est_counts_reticular_pontine_nucleus__caudal_2332                               | decimal | est_counts.reticular pontine nucleus, caudal.2332                               |
| c_tpm_reticular_pontine_nucleus__caudal_2457                                      | decimal | TPM.reticular pontine nucleus, caudal.2457                                      |
| c_est_counts_reticular_pontine_nucleus__caudal_2457                               | decimal | est_counts.reticular pontine nucleus, caudal.2457                               |
| c_tpm_reticular_pontine_nucleus__caudal_2559                                      | decimal | TPM.reticular pontine nucleus, caudal.2559                                      |
| c_est_counts_reticular_pontine_nucleus__caudal_2559                               | decimal | est_counts.reticular pontine nucleus, caudal.2559                               |
| c_tpm_reticular_pontine_nucleus__caudal_2092                                      | decimal | TPM.reticular pontine nucleus, caudal.2092                                      |
| c_est_counts_reticular_pontine_nucleus__caudal_2092                               | decimal | est_counts.reticular pontine nucleus, caudal.2092                               |
| c_tpm_reticular_pontine_nucleus__oral_1939                                        | decimal | TPM.reticular pontine nucleus, oral.1939                                        |
| c_est_counts_reticular_pontine_nucleus__oral_1939                                 | decimal | est_counts.reticular pontine nucleus, oral.1939                                 |
| c_tpm_reticular_pontine_nucleus__oral_2366                                        | decimal | TPM.reticular pontine nucleus, oral.2366                                        |
| c_est_counts_reticular_pontine_nucleus__oral_2366                                 | decimal | est_counts.reticular pontine nucleus, oral.2366                                 |
| c_tpm_reticular_pontine_nucleus__oral_2361                                        | decimal | TPM.reticular pontine nucleus, oral.2361                                        |
| c_est_counts_reticular_pontine_nucleus__oral_2361                                 | decimal | est_counts.reticular pontine nucleus, oral.2361                                 |
| c_tpm_reticular_pontine_nucleus__oral_2012                                        | decimal | TPM.reticular pontine nucleus, oral.2012                                        |
| c_est_counts_reticular_pontine_nucleus__oral_2012                                 | decimal | est_counts.reticular pontine nucleus, oral.2012                                 |
| c_tpm_reticular_pontine_nucleus__oral_2167                                        | decimal | TPM.reticular pontine nucleus, oral.2167                                        |
| c_est_counts_reticular_pontine_nucleus__oral_2167                                 | decimal | est_counts.reticular pontine nucleus, oral.2167                                 |
| c_tpm_reticulotegmental_nucleus_2333                                              | decimal | TPM.reticulotegmental nucleus.2333                                              |
| c_est_counts_reticulotegmental_nucleus_2333                                       | decimal | est_counts.reticulotegmental nucleus.2333                                       |
| c_tpm_reticulotegmental_nucleus_2322                                              | decimal | TPM.reticulotegmental nucleus.2322                                              |
| c_est_counts_reticulotegmental_nucleus_2322                                       | decimal | est_counts.reticulotegmental nucleus.2322                                       |
| c_tpm_reticulotegmental_nucleus_2452                                              | decimal | TPM.reticulotegmental nucleus.2452                                              |
| c_est_counts_reticulotegmental_nucleus_2452                                       | decimal | est_counts.reticulotegmental nucleus.2452                                       |
| c_tpm_reticulotegmental_nucleus_2325                                              | decimal | TPM.reticulotegmental nucleus.2325                                              |
| c_est_counts_reticulotegmental_nucleus_2325                                       | decimal | est_counts.reticulotegmental nucleus.2325                                       |
| c_tpm_retrosplenial_cortex_1951                                                   | decimal | TPM.retrosplenial cortex.1951                                                   |
| c_est_counts_retrosplenial_cortex_1951                                            | decimal | est_counts.retrosplenial cortex.1951                                            |
| c_tpm_retrosplenial_cortex_2675                                                   | decimal | TPM.retrosplenial cortex.2675                                                   |
| c_est_counts_retrosplenial_cortex_2675                                            | decimal | est_counts.retrosplenial cortex.2675                                            |
| c_tpm_retrosplenial_cortex_1914                                                   | decimal | TPM.retrosplenial cortex.1914                                                   |
| c_est_counts_retrosplenial_cortex_1914                                            | decimal | est_counts.retrosplenial cortex.1914                                            |
| c_tpm_septal_nuclei_2031                                                          | decimal | TPM.septal nuclei.2031                                                          |
| c_est_counts_septal_nuclei_2031                                                   | decimal | est_counts.septal nuclei.2031                                                   |
| c_tpm_septal_nuclei_2394                                                          | decimal | TPM.septal nuclei.2394                                                          |
| c_est_counts_septal_nuclei_2394                                                   | decimal | est_counts.septal nuclei.2394                                                   |
| c_tpm_septal_nuclei_2199                                                          | decimal | TPM.septal nuclei.2199                                                          |
| c_est_counts_septal_nuclei_2199                                                   | decimal | est_counts.septal nuclei.2199                                                   |
| c_tpm_septal_nuclei_2009                                                          | decimal | TPM.septal nuclei.2009                                                          |
| c_est_counts_septal_nuclei_2009                                                   | decimal | est_counts.septal nuclei.2009                                                   |
| c_tpm_septal_nuclei_2629                                                          | decimal | TPM.septal nuclei.2629                                                          |
| c_est_counts_septal_nuclei_2629                                                   | decimal | est_counts.septal nuclei.2629                                                   |
| c_tpm_septal_nuclei_2059                                                          | decimal | TPM.septal nuclei.2059                                                          |
| c_est_counts_septal_nuclei_2059                                                   | decimal | est_counts.septal nuclei.2059                                                   |
| c_tpm_septal_nuclei_1960                                                          | decimal | TPM.septal nuclei.1960                                                          |
| c_est_counts_septal_nuclei_1960                                                   | decimal | est_counts.septal nuclei.1960                                                   |
| c_tpm_somatomor_cortex__precentral_gyrus__white_matter__2439                      | decimal | TPM.somatomor cortex, precentral gyrus (white matter).2439                      |
| c_est_counts_somatomor_cortex__precentral_gyrus__white_matter__2439               | decimal | est_counts.somatomor cortex, precentral gyrus (white matter).2439               |
| c_tpm_somatosensory_cortex__postcentral_gyrus__ventral__white_matter__2623        | decimal | TPM.somatosensory cortex, postcentral gyrus, ventral (white matter).2623        |
| c_est_counts_somatosensory_cortex__postcentral_gyrus__ventral__white_matter__2623 | decimal | est_counts.somatosensory cortex, postcentral gyrus, ventral (white matter).2623 |
| c_tpm_spinal_trigeminal_nucleus__caudal_2312                                      | decimal | TPM.spinal trigeminal nucleus, caudal.2312                                      |
| c_est_counts_spinal_trigeminal_nucleus__caudal_2312                               | decimal | est_counts.spinal trigeminal nucleus, caudal.2312                               |
| c_tpm_spinal_trigeminal_nucleus__caudal_2308                                      | decimal | TPM.spinal trigeminal nucleus, caudal.2308                                      |
| c_est_counts_spinal_trigeminal_nucleus__caudal_2308                               | decimal | est_counts.spinal trigeminal nucleus, caudal.2308                               |
| c_tpm_spinal_trigeminal_nucleus__caudal_2390                                      | decimal | TPM.spinal trigeminal nucleus, caudal.2390                                      |
| c_est_counts_spinal_trigeminal_nucleus__caudal_2390                               | decimal | est_counts.spinal trigeminal nucleus, caudal.2390                               |
| c_tpm_spinal_trigeminal_nucleus__caudal_2642                                      | decimal | TPM.spinal trigeminal nucleus, caudal.2642                                      |
| c_est_counts_spinal_trigeminal_nucleus__caudal_2642                               | decimal | est_counts.spinal trigeminal nucleus, caudal.2642                               |
| c_tpm_spinal_trigeminal_nucleus__caudal_2447                                      | decimal | TPM.spinal trigeminal nucleus, caudal.2447                                      |
| c_est_counts_spinal_trigeminal_nucleus__caudal_2447                               | decimal | est_counts.spinal trigeminal nucleus, caudal.2447                               |
| c_tpm_spinal_trigeminal_nucleus__interpolar_2625                                  | decimal | TPM.spinal trigeminal nucleus, interpolar.2625                                  |
| c_est_counts_spinal_trigeminal_nucleus__interpolar_2625                           | decimal | est_counts.spinal trigeminal nucleus, interpolar.2625                           |
| c_tpm_spinal_trigeminal_nucleus__interpolar_2033                                  | decimal | TPM.spinal trigeminal nucleus, interpolar.2033                                  |
| c_est_counts_spinal_trigeminal_nucleus__interpolar_2033                           | decimal | est_counts.spinal trigeminal nucleus, interpolar.2033                           |
| c_tpm_spinal_trigeminal_nucleus__interpolar_2389                                  | decimal | TPM.spinal trigeminal nucleus, interpolar.2389                                  |
| c_est_counts_spinal_trigeminal_nucleus__interpolar_2389                           | decimal | est_counts.spinal trigeminal nucleus, interpolar.2389                           |
| c_tpm_spinal_trigeminal_nucleus__interpolar_2386                                  | decimal | TPM.spinal trigeminal nucleus, interpolar.2386                                  |
| c_est_counts_spinal_trigeminal_nucleus__interpolar_2386                           | decimal | est_counts.spinal trigeminal nucleus, interpolar.2386                           |
| c_tpm_spinal_trigeminal_nucleus__interpolar_2066                                  | decimal | TPM.spinal trigeminal nucleus, interpolar.2066                                  |
| c_est_counts_spinal_trigeminal_nucleus__interpolar_2066                           | decimal | est_counts.spinal trigeminal nucleus, interpolar.2066                           |
| c_tpm_spinal_trigeminal_nucleus__oral_2164                                        | decimal | TPM.spinal trigeminal nucleus, oral.2164                                        |
| c_est_counts_spinal_trigeminal_nucleus__oral_2164                                 | decimal | est_counts.spinal trigeminal nucleus, oral.2164                                 |
| c_tpm_spinal_trigeminal_nucleus__oral_2737                                        | decimal | TPM.spinal trigeminal nucleus, oral.2737                                        |
| c_est_counts_spinal_trigeminal_nucleus__oral_2737                                 | decimal | est_counts.spinal trigeminal nucleus, oral.2737                                 |
| c_tpm_spinal_trigeminal_nucleus__oral_1978                                        | decimal | TPM.spinal trigeminal nucleus, oral.1978                                        |
| c_est_counts_spinal_trigeminal_nucleus__oral_1978                                 | decimal | est_counts.spinal trigeminal nucleus, oral.1978                                 |
| c_tpm_spinal_vestibular_nucleus_2796                                              | decimal | TPM.spinal vestibular nucleus.2796                                              |
| c_est_counts_spinal_vestibular_nucleus_2796                                       | decimal | est_counts.spinal vestibular nucleus.2796                                       |
| c_tpm_spinal_vestibular_nucleus_2780                                              | decimal | TPM.spinal vestibular nucleus.2780                                              |
| c_est_counts_spinal_vestibular_nucleus_2780                                       | decimal | est_counts.spinal vestibular nucleus.2780                                       |
| c_tpm_spinal_vestibular_nucleus_2186                                              | decimal | TPM.spinal vestibular nucleus.2186                                              |
| c_est_counts_spinal_vestibular_nucleus_2186                                       | decimal | est_counts.spinal vestibular nucleus.2186                                       |
| c_tpm_spinal_vestibular_nucleus_2384                                              | decimal | TPM.spinal vestibular nucleus.2384                                              |
| c_est_counts_spinal_vestibular_nucleus_2384                                       | decimal | est_counts.spinal vestibular nucleus.2384                                       |
| c_tpm_spinal_vestibular_nucleus_2806                                              | decimal | TPM.spinal vestibular nucleus.2806                                              |
| c_est_counts_spinal_vestibular_nucleus_2806                                       | decimal | est_counts.spinal vestibular nucleus.2806                                       |
| c_tpm_spinal_vestibular_nucleus_2748                                              | decimal | TPM.spinal vestibular nucleus.2748                                              |
| c_est_counts_spinal_vestibular_nucleus_2748                                       | decimal | est_counts.spinal vestibular nucleus.2748                                       |
| c_tpm_stria_terminalis__bed_nucleus_1974                                          | decimal | TPM.stria terminalis, bed nucleus.1974                                          |
| c_est_counts_stria_terminalis__bed_nucleus_1974                                   | decimal | est_counts.stria terminalis, bed nucleus.1974                                   |
| c_tpm_stria_terminalis__bed_nucleus_2486                                          | decimal | TPM.stria terminalis, bed nucleus.2486                                          |
| c_est_counts_stria_terminalis__bed_nucleus_2486                                   | decimal | est_counts.stria terminalis, bed nucleus.2486                                   |
| c_tpm_stria_terminalis__bed_nucleus_2201                                          | decimal | TPM.stria terminalis, bed nucleus.2201                                          |
| c_est_counts_stria_terminalis__bed_nucleus_2201                                   | decimal | est_counts.stria terminalis, bed nucleus.2201                                   |
| c_tpm_subcentral_gyrus__s2_2072                                                   | decimal | TPM.subcentral gyrus, S2.2072                                                   |
| c_est_counts_subcentral_gyrus__s2_2072                                            | decimal | est_counts.subcentral gyrus, S2.2072                                            |
| c_tpm_subcentral_gyrus__s2_2351                                                   | decimal | TPM.subcentral gyrus, S2.2351                                                   |
| c_est_counts_subcentral_gyrus__s2_2351                                            | decimal | est_counts.subcentral gyrus, S2.2351                                            |
| c_tpm_subcentral_gyrus__s2_2762                                                   | decimal | TPM.subcentral gyrus, S2.2762                                                   |
| c_est_counts_subcentral_gyrus__s2_2762                                            | decimal | est_counts.subcentral gyrus, S2.2762                                            |
| c_tpm_subcentral_gyrus__s2_2839                                                   | decimal | TPM.subcentral gyrus, S2.2839                                                   |
| c_est_counts_subcentral_gyrus__s2_2839                                            | decimal | est_counts.subcentral gyrus, S2.2839                                            |
| c_tpm_subcentral_gyrus__s2_1964                                                   | decimal | TPM.subcentral gyrus, S2.1964                                                   |
| c_est_counts_subcentral_gyrus__s2_1964                                            | decimal | est_counts.subcentral gyrus, S2.1964                                            |
| c_tpm_subcentral_gyrus__s2_2555                                                   | decimal | TPM.subcentral gyrus, S2.2555                                                   |
| c_est_counts_subcentral_gyrus__s2_2555                                            | decimal | est_counts.subcentral gyrus, S2.2555                                            |
| c_tpm_subcoeruleus_area_1958                                                      | decimal | TPM.subcoeruleus area.1958                                                      |
| c_est_counts_subcoeruleus_area_1958                                               | decimal | est_counts.subcoeruleus area.1958                                               |
| c_tpm_subcoeruleus_area_2323                                                      | decimal | TPM.subcoeruleus area.2323                                                      |
| c_est_counts_subcoeruleus_area_2323                                               | decimal | est_counts.subcoeruleus area.2323                                               |
| c_tpm_subcoeruleus_area_2451                                                      | decimal | TPM.subcoeruleus area.2451                                                      |
| c_est_counts_subcoeruleus_area_2451                                               | decimal | est_counts.subcoeruleus area.2451                                               |
| c_tpm_subcoeruleus_area_2369                                                      | decimal | TPM.subcoeruleus area.2369                                                      |
| c_est_counts_subcoeruleus_area_2369                                               | decimal | est_counts.subcoeruleus area.2369                                               |
| c_tpm_subcoeruleus_area_2089                                                      | decimal | TPM.subcoeruleus area.2089                                                      |
| c_est_counts_subcoeruleus_area_2089                                               | decimal | est_counts.subcoeruleus area.2089                                               |
| c_tpm_subiculum_1901                                                              | decimal | TPM.subiculum.1901                                                              |
| c_est_counts_subiculum_1901                                                       | decimal | est_counts.subiculum.1901                                                       |
| c_tpm_subiculum_2729                                                              | decimal | TPM.subiculum.2729                                                              |
| c_est_counts_subiculum_2729                                                       | decimal | est_counts.subiculum.2729                                                       |
| c_tpm_subiculum_2619                                                              | decimal | TPM.subiculum.2619                                                              |
| c_est_counts_subiculum_2619                                                       | decimal | est_counts.subiculum.2619                                                       |
| c_tpm_subiculum_2438                                                              | decimal | TPM.subiculum.2438                                                              |
| c_est_counts_subiculum_2438                                                       | decimal | est_counts.subiculum.2438                                                       |
| c_tpm_subiculum_1977                                                              | decimal | TPM.subiculum.1977                                                              |
| c_est_counts_subiculum_1977                                                       | decimal | est_counts.subiculum.1977                                                       |
| c_tpm_subiculum_2042                                                              | decimal | TPM.subiculum.2042                                                              |
| c_est_counts_subiculum_2042                                                       | decimal | est_counts.subiculum.2042                                                       |
| c_tpm_substantia_nigra_1916                                                       | decimal | TPM.substantia nigra.1916                                                       |
| c_est_counts_substantia_nigra_1916                                                | decimal | est_counts.substantia nigra.1916                                                |
| c_tpm_substantia_nigra_1889                                                       | decimal | TPM.substantia nigra.1889                                                       |
| c_est_counts_substantia_nigra_1889                                                | decimal | est_counts.substantia nigra.1889                                                |
| c_tpm_substantia_nigra_2241                                                       | decimal | TPM.substantia nigra.2241                                                       |
| c_est_counts_substantia_nigra_2241                                                | decimal | est_counts.substantia nigra.2241                                                |
| c_tpm_substantia_nigra_1941                                                       | decimal | TPM.substantia nigra.1941                                                       |
| c_est_counts_substantia_nigra_1941                                                | decimal | est_counts.substantia nigra.1941                                                |
| c_tpm_substantia_nigra_2699                                                       | decimal | TPM.substantia nigra.2699                                                       |
| c_est_counts_substantia_nigra_2699                                                | decimal | est_counts.substantia nigra.2699                                                |
| c_tpm_substantia_nigra_2409                                                       | decimal | TPM.substantia nigra.2409                                                       |
| c_est_counts_substantia_nigra_2409                                                | decimal | est_counts.substantia nigra.2409                                                |
| c_tpm_substantia_nigra_2590                                                       | decimal | TPM.substantia nigra.2590                                                       |
| c_est_counts_substantia_nigra_2590                                                | decimal | est_counts.substantia nigra.2590                                                |
| c_tpm_substantia_nigra_2583                                                       | decimal | TPM.substantia nigra.2583                                                       |
| c_est_counts_substantia_nigra_2583                                                | decimal | est_counts.substantia nigra.2583                                                |
| c_tpm_substantia_nigra_2665                                                       | decimal | TPM.substantia nigra.2665                                                       |
| c_est_counts_substantia_nigra_2665                                                | decimal | est_counts.substantia nigra.2665                                                |
| c_tpm_substantia_nigra_1851                                                       | decimal | TPM.substantia nigra.1851                                                       |
| c_est_counts_substantia_nigra_1851                                                | decimal | est_counts.substantia nigra.1851                                                |
| c_tpm_subthalamic_nucleus_2779                                                    | decimal | TPM.subthalamic nucleus.2779                                                    |
| c_est_counts_subthalamic_nucleus_2779                                             | decimal | est_counts.subthalamic nucleus.2779                                             |
| c_tpm_subthalamic_nucleus_2056                                                    | decimal | TPM.subthalamic nucleus.2056                                                    |
| c_est_counts_subthalamic_nucleus_2056                                             | decimal | est_counts.subthalamic nucleus.2056                                             |
| c_tpm_subthalamic_nucleus_2124                                                    | decimal | TPM.subthalamic nucleus.2124                                                    |
| c_est_counts_subthalamic_nucleus_2124                                             | decimal | est_counts.subthalamic nucleus.2124                                             |
| c_tpm_subthalamic_nucleus_2275                                                    | decimal | TPM.subthalamic nucleus.2275                                                    |
| c_est_counts_subthalamic_nucleus_2275                                             | decimal | est_counts.subthalamic nucleus.2275                                             |
| c_tpm_subthalamic_nucleus_2216                                                    | decimal | TPM.subthalamic nucleus.2216                                                    |
| c_est_counts_subthalamic_nucleus_2216                                             | decimal | est_counts.subthalamic nucleus.2216                                             |
| c_tpm_subthalamic_nucleus_2406                                                    | decimal | TPM.subthalamic nucleus.2406                                                    |
| c_est_counts_subthalamic_nucleus_2406                                             | decimal | est_counts.subthalamic nucleus.2406                                             |
| c_tpm_subthalamic_nucleus_2282                                                    | decimal | TPM.subthalamic nucleus.2282                                                    |
| c_est_counts_subthalamic_nucleus_2282                                             | decimal | est_counts.subthalamic nucleus.2282                                             |
| c_tpm_subthalamic_nucleus_2658                                                    | decimal | TPM.subthalamic nucleus.2658                                                    |
| c_est_counts_subthalamic_nucleus_2658                                             | decimal | est_counts.subthalamic nucleus.2658                                             |
| c_tpm_superior_colliculus_1913                                                    | decimal | TPM.superior colliculus.1913                                                    |
| c_est_counts_superior_colliculus_1913                                             | decimal | est_counts.superior colliculus.1913                                             |
| c_tpm_superior_colliculus_2087                                                    | decimal | TPM.superior colliculus.2087                                                    |
| c_est_counts_superior_colliculus_2087                                             | decimal | est_counts.superior colliculus.2087                                             |
| c_tpm_superior_colliculus_1995                                                    | decimal | TPM.superior colliculus.1995                                                    |
| c_est_counts_superior_colliculus_1995                                             | decimal | est_counts.superior colliculus.1995                                             |
| c_tpm_superior_colliculus_1796                                                    | decimal | TPM.superior colliculus.1796                                                    |
| c_est_counts_superior_colliculus_1796                                             | decimal | est_counts.superior colliculus.1796                                             |
| c_tpm_superior_colliculus_2261                                                    | decimal | TPM.superior colliculus.2261                                                    |
| c_est_counts_superior_colliculus_2261                                             | decimal | est_counts.superior colliculus.2261                                             |
| c_tpm_superior_colliculus_2668                                                    | decimal | TPM.superior colliculus.2668                                                    |
| c_est_counts_superior_colliculus_2668                                             | decimal | est_counts.superior colliculus.2668                                             |
| c_tpm_superior_colliculus_2664                                                    | decimal | TPM.superior colliculus.2664                                                    |
| c_est_counts_superior_colliculus_2664                                             | decimal | est_counts.superior colliculus.2664                                             |
| c_tpm_superior_colliculus_2587                                                    | decimal | TPM.superior colliculus.2587                                                    |
| c_est_counts_superior_colliculus_2587                                             | decimal | est_counts.superior colliculus.2587                                             |
| c_tpm_superior_colliculus_1895                                                    | decimal | TPM.superior colliculus.1895                                                    |
| c_est_counts_superior_colliculus_1895                                             | decimal | est_counts.superior colliculus.1895                                             |
| c_tpm_superior_colliculus_1839                                                    | decimal | TPM.superior colliculus.1839                                                    |
| c_est_counts_superior_colliculus_1839                                             | decimal | est_counts.superior colliculus.1839                                             |
| c_tpm_superior_olive_2329                                                         | decimal | TPM.superior olive.2329                                                         |
| c_est_counts_superior_olive_2329                                                  | decimal | est_counts.superior olive.2329                                                  |
| c_tpm_superior_olive_2561                                                         | decimal | TPM.superior olive.2561                                                         |
| c_est_counts_superior_olive_2561                                                  | decimal | est_counts.superior olive.2561                                                  |
| c_tpm_superior_olive_2364                                                         | decimal | TPM.superior olive.2364                                                         |
| c_est_counts_superior_olive_2364                                                  | decimal | est_counts.superior olive.2364                                                  |
| c_tpm_superior_olive_1875                                                         | decimal | TPM.superior olive.1875                                                         |
| c_est_counts_superior_olive_1875                                                  | decimal | est_counts.superior olive.1875                                                  |
| c_tpm_superior_olive_2020                                                         | decimal | TPM.superior olive.2020                                                         |
| c_est_counts_superior_olive_2020                                                  | decimal | est_counts.superior olive.2020                                                  |
| c_tpm_superior_parietal_lobule_2229                                               | decimal | TPM.superior parietal lobule.2229                                               |
| c_est_counts_superior_parietal_lobule_2229                                        | decimal | est_counts.superior parietal lobule.2229                                        |
| c_tpm_superior_parietal_lobule_1992                                               | decimal | TPM.superior parietal lobule.1992                                               |
| c_est_counts_superior_parietal_lobule_1992                                        | decimal | est_counts.superior parietal lobule.1992                                        |
| c_tpm_superior_parietal_lobule_2672                                               | decimal | TPM.superior parietal lobule.2672                                               |
| c_est_counts_superior_parietal_lobule_2672                                        | decimal | est_counts.superior parietal lobule.2672                                        |
| c_tpm_superior_parietal_lobule_2605                                               | decimal | TPM.superior parietal lobule.2605                                               |
| c_est_counts_superior_parietal_lobule_2605                                        | decimal | est_counts.superior parietal lobule.2605                                        |
| c_tpm_superior_parietal_lobule_1800                                               | decimal | TPM.superior parietal lobule.1800                                               |
| c_est_counts_superior_parietal_lobule_1800                                        | decimal | est_counts.superior parietal lobule.1800                                        |
| c_tpm_superior_temporal_gyrus_2025                                                | decimal | TPM.superior temporal gyrus.2025                                                |
| c_est_counts_superior_temporal_gyrus_2025                                         | decimal | est_counts.superior temporal gyrus.2025                                         |
| c_tpm_superior_temporal_gyrus_2687                                                | decimal | TPM.superior temporal gyrus.2687                                                |
| c_est_counts_superior_temporal_gyrus_2687                                         | decimal | est_counts.superior temporal gyrus.2687                                         |
| c_tpm_superior_temporal_gyrus_1844                                                | decimal | TPM.superior temporal gyrus.1844                                                |
| c_est_counts_superior_temporal_gyrus_1844                                         | decimal | est_counts.superior temporal gyrus.1844                                         |
| c_tpm_superior_temporal_gyrus_2615                                                | decimal | TPM.superior temporal gyrus.2615                                                |
| c_est_counts_superior_temporal_gyrus_2615                                         | decimal | est_counts.superior temporal gyrus.2615                                         |
| c_tpm_superior_temporal_gyrus_1843                                                | decimal | TPM.superior temporal gyrus.1843                                                |
| c_est_counts_superior_temporal_gyrus_1843                                         | decimal | est_counts.superior temporal gyrus.1843                                         |
| c_tpm_superior_vestibular_nucleus_2015                                            | decimal | TPM.superior vestibular nucleus.2015                                            |
| c_est_counts_superior_vestibular_nucleus_2015                                     | decimal | est_counts.superior vestibular nucleus.2015                                     |
| c_tpm_superior_vestibular_nucleus_2383                                            | decimal | TPM.superior vestibular nucleus.2383                                            |
| c_est_counts_superior_vestibular_nucleus_2383                                     | decimal | est_counts.superior vestibular nucleus.2383                                     |
| c_tpm_superior_vestibular_nucleus_2061                                            | decimal | TPM.superior vestibular nucleus.2061                                            |
| c_est_counts_superior_vestibular_nucleus_2061                                     | decimal | est_counts.superior vestibular nucleus.2061                                     |
| c_tpm_supplementary_motor_cortex_1993                                             | decimal | TPM.supplementary motor cortex.1993                                             |
| c_est_counts_supplementary_motor_cortex_1993                                      | decimal | est_counts.supplementary motor cortex.1993                                      |
| c_tpm_supplementary_motor_cortex_2537                                             | decimal | TPM.supplementary motor cortex.2537                                             |
| c_est_counts_supplementary_motor_cortex_2537                                      | decimal | est_counts.supplementary motor cortex.2537                                      |
| c_tpm_supplementary_motor_cortex_2632                                             | decimal | TPM.supplementary motor cortex.2632                                             |
| c_est_counts_supplementary_motor_cortex_2632                                      | decimal | est_counts.supplementary motor cortex.2632                                      |
| c_tpm_supplementary_motor_cortex_2548                                             | decimal | TPM.supplementary motor cortex.2548                                             |
| c_est_counts_supplementary_motor_cortex_2548                                      | decimal | est_counts.supplementary motor cortex.2548                                      |
| c_tpm_supramarginal_gyrus_2513                                                    | decimal | TPM.supramarginal gyrus.2513                                                    |
| c_est_counts_supramarginal_gyrus_2513                                             | decimal | est_counts.supramarginal gyrus.2513                                             |
| c_tpm_supramarginal_gyrus_2415                                                    | decimal | TPM.supramarginal gyrus.2415                                                    |
| c_est_counts_supramarginal_gyrus_2415                                             | decimal | est_counts.supramarginal gyrus.2415                                             |
| c_tpm_supramarginal_gyrus_1991                                                    | decimal | TPM.supramarginal gyrus.1991                                                    |
| c_est_counts_supramarginal_gyrus_1991                                             | decimal | est_counts.supramarginal gyrus.1991                                             |
| c_tpm_supramarginal_gyrus_2601                                                    | decimal | TPM.supramarginal gyrus.2601                                                    |
| c_est_counts_supramarginal_gyrus_2601                                             | decimal | est_counts.supramarginal gyrus.2601                                             |
| c_tpm_supramarginal_gyrus_1798                                                    | decimal | TPM.supramarginal gyrus.1798                                                    |
| c_est_counts_supramarginal_gyrus_1798                                             | decimal | est_counts.supramarginal gyrus.1798                                             |
| c_tpm_supraoptic_nucleus_2835                                                     | decimal | TPM.supraoptic nucleus.2835                                                     |
| c_est_counts_supraoptic_nucleus_2835                                              | decimal | est_counts.supraoptic nucleus.2835                                              |
| c_tpm_supraoptic_nucleus_2043                                                     | decimal | TPM.supraoptic nucleus.2043                                                     |
| c_est_counts_supraoptic_nucleus_2043                                              | decimal | est_counts.supraoptic nucleus.2043                                              |
| c_tpm_supraoptic_nucleus_1894                                                     | decimal | TPM.supraoptic nucleus.1894                                                     |
| c_est_counts_supraoptic_nucleus_1894                                              | decimal | est_counts.supraoptic nucleus.1894                                              |
| c_tpm_temporal_pole_2518                                                          | decimal | TPM.temporal pole.2518                                                          |
| c_est_counts_temporal_pole_2518                                                   | decimal | est_counts.temporal pole.2518                                                   |
| c_tpm_temporal_pole_1832                                                          | decimal | TPM.temporal pole.1832                                                          |
| c_est_counts_temporal_pole_1832                                                   | decimal | est_counts.temporal pole.1832                                                   |
| c_tpm_temporal_pole_2612                                                          | decimal | TPM.temporal pole.2612                                                          |
| c_est_counts_temporal_pole_2612                                                   | decimal | est_counts.temporal pole.2612                                                   |
| c_tpm_temporal_pole_1853                                                          | decimal | TPM.temporal pole.1853                                                          |
| c_est_counts_temporal_pole_1853                                                   | decimal | est_counts.temporal pole.1853                                                   |
| c_tpm_temporal_pole_1826                                                          | decimal | TPM.temporal pole.1826                                                          |
| c_est_counts_temporal_pole_1826                                                   | decimal | est_counts.temporal pole.1826                                                   |
| c_tpm_temporal_white_matter_2254                                                  | decimal | TPM.temporal white matter.2254                                                  |
| c_est_counts_temporal_white_matter_2254                                           | decimal | est_counts.temporal white matter.2254                                           |
| c_tpm_temporal_white_matter_2736                                                  | decimal | TPM.temporal white matter.2736                                                  |
| c_est_counts_temporal_white_matter_2736                                           | decimal | est_counts.temporal white matter.2736                                           |
| c_tpm_temporal_white_matter_2523                                                  | decimal | TPM.temporal white matter.2523                                                  |
| c_est_counts_temporal_white_matter_2523                                           | decimal | est_counts.temporal white matter.2523                                           |
| c_tpm_temporal_white_matter_2524                                                  | decimal | TPM.temporal white matter.2524                                                  |
| c_est_counts_temporal_white_matter_2524                                           | decimal | est_counts.temporal white matter.2524                                           |
| c_tpm_temporal_white_matter_1801                                                  | decimal | TPM.temporal white matter.1801                                                  |
| c_est_counts_temporal_white_matter_1801                                           | decimal | est_counts.temporal white matter.1801                                           |
| c_tpm_temporo_insular_cortex__parainsular_gyrus_2416                              | decimal | TPM.temporo-insular cortex, parainsular gyrus.2416                              |
| c_est_counts_temporo_insular_cortex__parainsular_gyrus_2416                       | decimal | est_counts.temporo-insular cortex, parainsular gyrus.2416                       |
| c_tpm_temporo_insular_cortex__parainsular_gyrus_2598                              | decimal | TPM.temporo-insular cortex, parainsular gyrus.2598                              |
| c_est_counts_temporo_insular_cortex__parainsular_gyrus_2598                       | decimal | est_counts.temporo-insular cortex, parainsular gyrus.2598                       |
| c_tpm_temporo_insular_cortex__parainsular_gyrus_2264                              | decimal | TPM.temporo-insular cortex, parainsular gyrus.2264                              |
| c_est_counts_temporo_insular_cortex__parainsular_gyrus_2264                       | decimal | est_counts.temporo-insular cortex, parainsular gyrus.2264                       |
| c_tpm_temporo_insular_cortex__parainsular_gyrus_2676                              | decimal | TPM.temporo-insular cortex, parainsular gyrus.2676                              |
| c_est_counts_temporo_insular_cortex__parainsular_gyrus_2676                       | decimal | est_counts.temporo-insular cortex, parainsular gyrus.2676                       |
| c_tpm_temporo_insular_cortex__parainsular_gyrus_2512                              | decimal | TPM.temporo-insular cortex, parainsular gyrus.2512                              |
| c_est_counts_temporo_insular_cortex__parainsular_gyrus_2512                       | decimal | est_counts.temporo-insular cortex, parainsular gyrus.2512                       |
| c_tpm_temporo_insular_cortex__parainsular_gyrus_1802                              | decimal | TPM.temporo-insular cortex, parainsular gyrus.1802                              |
| c_est_counts_temporo_insular_cortex__parainsular_gyrus_1802                       | decimal | est_counts.temporo-insular cortex, parainsular gyrus.1802                       |
| c_tpm_temporo_occipital_transitional_zone_1793                                    | decimal | TPM.temporo-occipital transitional zone.1793                                    |
| c_est_counts_temporo_occipital_transitional_zone_1793                             | decimal | est_counts.temporo-occipital transitional zone.1793                             |
| c_tpm_temporo_occipital_transitional_zone_2251                                    | decimal | TPM.temporo-occipital transitional zone.2251                                    |
| c_est_counts_temporo_occipital_transitional_zone_2251                             | decimal | est_counts.temporo-occipital transitional zone.2251                             |
| c_tpm_temporo_occipital_transitional_zone_1900                                    | decimal | TPM.temporo-occipital transitional zone.1900                                    |
| c_est_counts_temporo_occipital_transitional_zone_1900                             | decimal | est_counts.temporo-occipital transitional zone.1900                             |
| c_tpm_transversal_temporal_gyrus__anterior_1910                                   | decimal | TPM.transversal temporal gyrus, anterior.1910                                   |
| c_est_counts_transversal_temporal_gyrus__anterior_1910                            | decimal | est_counts.transversal temporal gyrus, anterior.1910                            |
| c_tpm_transversal_temporal_gyrus__anterior_2610                                   | decimal | TPM.transversal temporal gyrus, anterior.2610                                   |
| c_est_counts_transversal_temporal_gyrus__anterior_2610                            | decimal | est_counts.transversal temporal gyrus, anterior.2610                            |
| c_tpm_transversal_temporal_gyrus__anterior_1888                                   | decimal | TPM.transversal temporal gyrus, anterior.1888                                   |
| c_est_counts_transversal_temporal_gyrus__anterior_1888                            | decimal | est_counts.transversal temporal gyrus, anterior.1888                            |
| c_tpm_transversal_temporal_gyrus__anterior_2522                                   | decimal | TPM.transversal temporal gyrus, anterior.2522                                   |
| c_est_counts_transversal_temporal_gyrus__anterior_2522                            | decimal | est_counts.transversal temporal gyrus, anterior.2522                            |
| c_tpm_transversal_temporal_gyrus__anterior_1809                                   | decimal | TPM.transversal temporal gyrus, anterior.1809                                   |
| c_est_counts_transversal_temporal_gyrus__anterior_1809                            | decimal | est_counts.transversal temporal gyrus, anterior.1809                            |
| c_tpm_transversal_temporal_gyrus__posterior_2833                                  | decimal | TPM.transversal temporal gyrus, posterior.2833                                  |
| c_est_counts_transversal_temporal_gyrus__posterior_2833                           | decimal | est_counts.transversal temporal gyrus, posterior.2833                           |
| c_tpm_transversal_temporal_gyrus__posterior_2520                                  | decimal | TPM.transversal temporal gyrus, posterior.2520                                  |
| c_est_counts_transversal_temporal_gyrus__posterior_2520                           | decimal | est_counts.transversal temporal gyrus, posterior.2520                           |
| c_tpm_transversal_temporal_gyrus__posterior_1967                                  | decimal | TPM.transversal temporal gyrus, posterior.1967                                  |
| c_est_counts_transversal_temporal_gyrus__posterior_1967                           | decimal | est_counts.transversal temporal gyrus, posterior.1967                           |
| c_tpm_transversal_temporal_gyrus__posterior_2614                                  | decimal | TPM.transversal temporal gyrus, posterior.2614                                  |
| c_est_counts_transversal_temporal_gyrus__posterior_2614                           | decimal | est_counts.transversal temporal gyrus, posterior.2614                           |
| c_tpm_transversal_temporal_gyrus__posterior_1922                                  | decimal | TPM.transversal temporal gyrus, posterior.1922                                  |
| c_est_counts_transversal_temporal_gyrus__posterior_1922                           | decimal | est_counts.transversal temporal gyrus, posterior.1922                           |
| c_tpm_ventral_medullary_reticular_nucleus_2372                                    | decimal | TPM.ventral medullary reticular nucleus.2372                                    |
| c_est_counts_ventral_medullary_reticular_nucleus_2372                             | decimal | est_counts.ventral medullary reticular nucleus.2372                             |
| c_tpm_ventral_medullary_reticular_nucleus_2060                                    | decimal | TPM.ventral medullary reticular nucleus.2060                                    |
| c_est_counts_ventral_medullary_reticular_nucleus_2060                             | decimal | est_counts.ventral medullary reticular nucleus.2060                             |
| c_tpm_ventral_periolivary_nuclei_2165                                             | decimal | TPM.ventral periolivary nuclei.2165                                             |
| c_est_counts_ventral_periolivary_nuclei_2165                                      | decimal | est_counts.ventral periolivary nuclei.2165                                      |
| c_tpm_ventral_periolivary_nuclei_2794                                             | decimal | TPM.ventral periolivary nuclei.2794                                             |
| c_est_counts_ventral_periolivary_nuclei_2794                                      | decimal | est_counts.ventral periolivary nuclei.2794                                      |
| c_tpm_ventral_periolivary_nuclei_2130                                             | decimal | TPM.ventral periolivary nuclei.2130                                             |
| c_est_counts_ventral_periolivary_nuclei_2130                                      | decimal | est_counts.ventral periolivary nuclei.2130                                      |
| c_tpm_ventral_periolivary_nuclei_2023                                             | decimal | TPM.ventral periolivary nuclei.2023                                             |
| c_est_counts_ventral_periolivary_nuclei_2023                                      | decimal | est_counts.ventral periolivary nuclei.2023                                      |
| c_tpm_ventral_posterolateral_thalamic_nucleus_2581                                | decimal | TPM.ventral posterolateral thalamic nucleus.2581                                |
| c_est_counts_ventral_posterolateral_thalamic_nucleus_2581                         | decimal | est_counts.ventral posterolateral thalamic nucleus.2581                         |
| c_tpm_ventral_posterolateral_thalamic_nucleus_2397                                | decimal | TPM.ventral posterolateral thalamic nucleus.2397                                |
| c_est_counts_ventral_posterolateral_thalamic_nucleus_2397                         | decimal | est_counts.ventral posterolateral thalamic nucleus.2397                         |
| c_tpm_ventral_posterolateral_thalamic_nucleus_2197                                | decimal | TPM.ventral posterolateral thalamic nucleus.2197                                |
| c_est_counts_ventral_posterolateral_thalamic_nucleus_2197                         | decimal | est_counts.ventral posterolateral thalamic nucleus.2197                         |
| c_tpm_ventral_posterolateral_thalamic_nucleus_2570                                | decimal | TPM.ventral posterolateral thalamic nucleus.2570                                |
| c_est_counts_ventral_posterolateral_thalamic_nucleus_2570                         | decimal | est_counts.ventral posterolateral thalamic nucleus.2570                         |
| c_tpm_ventral_posterolateral_thalamic_nucleus_2578                                | decimal | TPM.ventral posterolateral thalamic nucleus.2578                                |
| c_est_counts_ventral_posterolateral_thalamic_nucleus_2578                         | decimal | est_counts.ventral posterolateral thalamic nucleus.2578                         |
| c_tpm_ventral_posterolateral_thalamic_nucleus_2740                                | decimal | TPM.ventral posterolateral thalamic nucleus.2740                                |
| c_est_counts_ventral_posterolateral_thalamic_nucleus_2740                         | decimal | est_counts.ventral posterolateral thalamic nucleus.2740                         |
| c_tpm_ventral_posteromedial_thalamic_nucleus_2202                                 | decimal | TPM.ventral posteromedial thalamic nucleus.2202                                 |
| c_est_counts_ventral_posteromedial_thalamic_nucleus_2202                          | decimal | est_counts.ventral posteromedial thalamic nucleus.2202                          |
| c_tpm_ventral_posteromedial_thalamic_nucleus_2758                                 | decimal | TPM.ventral posteromedial thalamic nucleus.2758                                 |
| c_est_counts_ventral_posteromedial_thalamic_nucleus_2758                          | decimal | est_counts.ventral posteromedial thalamic nucleus.2758                          |
| c_tpm_ventral_posteromedial_thalamic_nucleus_2281                                 | decimal | TPM.ventral posteromedial thalamic nucleus.2281                                 |
| c_est_counts_ventral_posteromedial_thalamic_nucleus_2281                          | decimal | est_counts.ventral posteromedial thalamic nucleus.2281                          |
| c_tpm_ventral_posteromedial_thalamic_nucleus_2653                                 | decimal | TPM.ventral posteromedial thalamic nucleus.2653                                 |
| c_est_counts_ventral_posteromedial_thalamic_nucleus_2653                          | decimal | est_counts.ventral posteromedial thalamic nucleus.2653                          |
| c_tpm_ventral_posteromedial_thalamic_nucleus_2127                                 | decimal | TPM.ventral posteromedial thalamic nucleus.2127                                 |
| c_est_counts_ventral_posteromedial_thalamic_nucleus_2127                          | decimal | est_counts.ventral posteromedial thalamic nucleus.2127                          |
| c_tpm_ventral_tegmental_area_1915                                                 | decimal | TPM.ventral tegmental area.1915                                                 |
| c_est_counts_ventral_tegmental_area_1915                                          | decimal | est_counts.ventral tegmental area.1915                                          |
| c_tpm_ventral_tegmental_area_2223                                                 | decimal | TPM.ventral tegmental area.2223                                                 |
| c_est_counts_ventral_tegmental_area_2223                                          | decimal | est_counts.ventral tegmental area.2223                                          |
| c_tpm_ventral_tegmental_area_2021                                                 | decimal | TPM.ventral tegmental area.2021                                                 |
| c_est_counts_ventral_tegmental_area_2021                                          | decimal | est_counts.ventral tegmental area.2021                                          |
| c_tpm_ventral_tegmental_area_2410                                                 | decimal | TPM.ventral tegmental area.2410                                                 |
| c_est_counts_ventral_tegmental_area_2410                                          | decimal | est_counts.ventral tegmental area.2410                                          |
| c_tpm_ventral_tegmental_area_2218                                                 | decimal | TPM.ventral tegmental area.2218                                                 |
| c_est_counts_ventral_tegmental_area_2218                                          | decimal | est_counts.ventral tegmental area.2218                                          |
| c_tpm_ventral_tegmental_area_1942                                                 | decimal | TPM.ventral tegmental area.1942                                                 |
| c_est_counts_ventral_tegmental_area_1942                                          | decimal | est_counts.ventral tegmental area.1942                                          |
| c_tpm_ventral_thalamic_nuclei_1912                                                | decimal | TPM.ventral thalamic nuclei.1912                                                |
| c_est_counts_ventral_thalamic_nuclei_1912                                         | decimal | est_counts.ventral thalamic nuclei.1912                                         |
| c_tpm_ventral_thalamic_nuclei_2291                                                | decimal | TPM.ventral thalamic nuclei.2291                                                |
| c_est_counts_ventral_thalamic_nuclei_2291                                         | decimal | est_counts.ventral thalamic nuclei.2291                                         |
| c_tpm_ventral_thalamic_nuclei_2285                                                | decimal | TPM.ventral thalamic nuclei.2285                                                |
| c_est_counts_ventral_thalamic_nuclei_2285                                         | decimal | est_counts.ventral thalamic nuclei.2285                                         |
| c_tpm_ventral_thalamic_nuclei_2580                                                | decimal | TPM.ventral thalamic nuclei.2580                                                |
| c_est_counts_ventral_thalamic_nuclei_2580                                         | decimal | est_counts.ventral thalamic nuclei.2580                                         |
| c_tpm_ventral_thalamic_nuclei_1845                                                | decimal | TPM.ventral thalamic nuclei.1845                                                |
| c_est_counts_ventral_thalamic_nuclei_1845                                         | decimal | est_counts.ventral thalamic nuclei.1845                                         |
| c_tpm_ventral_thalamic_nuclei_2858                                                | decimal | TPM.ventral thalamic nuclei.2858                                                |
| c_est_counts_ventral_thalamic_nuclei_2858                                         | decimal | est_counts.ventral thalamic nuclei.2858                                         |
| c_tpm_ventral_thalamic_nuclei_2204                                                | decimal | TPM.ventral thalamic nuclei.2204                                                |
| c_est_counts_ventral_thalamic_nuclei_2204                                         | decimal | est_counts.ventral thalamic nuclei.2204                                         |
| c_tpm_ventral_thalamic_nuclei_2652                                                | decimal | TPM.ventral thalamic nuclei.2652                                                |
| c_est_counts_ventral_thalamic_nuclei_2652                                         | decimal | est_counts.ventral thalamic nuclei.2652                                         |
| c_tpm_ventral_thalamic_nuclei_1860                                                | decimal | TPM.ventral thalamic nuclei.1860                                                |
| c_est_counts_ventral_thalamic_nuclei_1860                                         | decimal | est_counts.ventral thalamic nuclei.1860                                         |
| c_tpm_ventrolateral_medulla__a1_c1_cell_groups_2180                               | decimal | TPM.ventrolateral medulla, A1-C1 cell groups.2180                               |
| c_est_counts_ventrolateral_medulla__a1_c1_cell_groups_2180                        | decimal | est_counts.ventrolateral medulla, A1-C1 cell groups.2180                        |
| c_tpm_ventrolateral_medulla__a1_c1_cell_groups_2118                               | decimal | TPM.ventrolateral medulla, A1-C1 cell groups.2118                               |
| c_est_counts_ventrolateral_medulla__a1_c1_cell_groups_2118                        | decimal | est_counts.ventrolateral medulla, A1-C1 cell groups.2118                        |
| c_tpm_ventrolateral_medulla__a1_c1_cell_groups_2302                               | decimal | TPM.ventrolateral medulla, A1-C1 cell groups.2302                               |
| c_est_counts_ventrolateral_medulla__a1_c1_cell_groups_2302                        | decimal | est_counts.ventrolateral medulla, A1-C1 cell groups.2302                        |
| c_tpm_ventrolateral_medulla__a1_c1_cell_groups_2741                               | decimal | TPM.ventrolateral medulla, A1-C1 cell groups.2741                               |
| c_est_counts_ventrolateral_medulla__a1_c1_cell_groups_2741                        | decimal | est_counts.ventrolateral medulla, A1-C1 cell groups.2741                        |
| c_tpm_ventrolateral_medulla__a1_c1_cell_groups_1986                               | decimal | TPM.ventrolateral medulla, A1-C1 cell groups.1986                               |
| c_est_counts_ventrolateral_medulla__a1_c1_cell_groups_1986                        | decimal | est_counts.ventrolateral medulla, A1-C1 cell groups.1986                        |
| c_tpm_ventrolateral_tegmental_area__a5_ne_cell_group_2359                         | decimal | TPM.ventrolateral tegmental area, A5 NE cell group.2359                         |
| c_est_counts_ventrolateral_tegmental_area__a5_ne_cell_group_2359                  | decimal | est_counts.ventrolateral tegmental area, A5 NE cell group.2359                  |
| c_tpm_ventrolateral_tegmental_area__a5_ne_cell_group_2161                         | decimal | TPM.ventrolateral tegmental area, A5 NE cell group.2161                         |
| c_est_counts_ventrolateral_tegmental_area__a5_ne_cell_group_2161                  | decimal | est_counts.ventrolateral tegmental area, A5 NE cell group.2161                  |
| c_tpm_ventrolateral_tegmental_area__a5_ne_cell_group_2456                         | decimal | TPM.ventrolateral tegmental area, A5 NE cell group.2456                         |
| c_est_counts_ventrolateral_tegmental_area__a5_ne_cell_group_2456                  | decimal | est_counts.ventrolateral tegmental area, A5 NE cell group.2456                  |
| c_tpm_ventrolateral_tegmental_area__a5_ne_cell_group_2449                         | decimal | TPM.ventrolateral tegmental area, A5 NE cell group.2449                         |
| c_est_counts_ventrolateral_tegmental_area__a5_ne_cell_group_2449                  | decimal | est_counts.ventrolateral tegmental area, A5 NE cell group.2449                  |
| c_tpm_ventrolateral_tegmental_area__a5_ne_cell_group_2840                         | decimal | TPM.ventrolateral tegmental area, A5 NE cell group.2840                         |
| c_est_counts_ventrolateral_tegmental_area__a5_ne_cell_group_2840                  | decimal | est_counts.ventrolateral tegmental area, A5 NE cell group.2840                  |
| c_tpm_ventrolateral_tegmental_area__a5_ne_cell_group_1959                         | decimal | TPM.ventrolateral tegmental area, A5 NE cell group.1959                         |
| c_est_counts_ventrolateral_tegmental_area__a5_ne_cell_group_1959                  | decimal | est_counts.ventrolateral tegmental area, A5 NE cell group.1959                  |
| c_tpm_ventromedial_nucleus_1822                                                   | decimal | TPM.ventromedial nucleus.1822                                                   |
| c_est_counts_ventromedial_nucleus_1822                                            | decimal | est_counts.ventromedial nucleus.1822                                            |
| c_tpm_ventromedial_nucleus_1982                                                   | decimal | TPM.ventromedial nucleus.1982                                                   |
| c_est_counts_ventromedial_nucleus_1982                                            | decimal | est_counts.ventromedial nucleus.1982                                            |
| c_tpm_vermis_1928                                                                 | decimal | TPM.vermis.1928                                                                 |
| c_est_counts_vermis_1928                                                          | decimal | est_counts.vermis.1928                                                          |
| c_tpm_vermis_2460                                                                 | decimal | TPM.vermis.2460                                                                 |
| c_est_counts_vermis_2460                                                          | decimal | est_counts.vermis.2460                                                          |
| c_tpm_vermis_2834                                                                 | decimal | TPM.vermis.2834                                                                 |
| c_est_counts_vermis_2834                                                          | decimal | est_counts.vermis.2834                                                          |
| c_tpm_vermis_1778                                                                 | decimal | TPM.vermis.1778                                                                 |
| c_est_counts_vermis_1778                                                          | decimal | est_counts.vermis.1778                                                          |
| c_tpm_vermis_1751                                                                 | decimal | TPM.vermis.1751                                                                 |
| c_est_counts_vermis_1751                                                          | decimal | est_counts.vermis.1751                                                          |
| c_tpm_vermis_1988                                                                 | decimal | TPM.vermis.1988                                                                 |
| c_est_counts_vermis_1988                                                          | decimal | est_counts.vermis.1988                                                          |
| c_tpm_vermis_1770                                                                 | decimal | TPM.vermis.1770                                                                 |
| c_est_counts_vermis_1770                                                          | decimal | est_counts.vermis.1770                                                          |
| c_tpm_vermis_1766                                                                 | decimal | TPM.vermis.1766                                                                 |
| c_est_counts_vermis_1766                                                          | decimal | est_counts.vermis.1766                                                          |
| c_tpm_vermis_1825                                                                 | decimal | TPM.vermis.1825                                                                 |
| c_est_counts_vermis_1825                                                          | decimal | est_counts.vermis.1825                                                          |
| c_tpm_zona_incerta_2403                                                           | decimal | TPM.zona incerta.2403                                                           |
| c_est_counts_zona_incerta_2403                                                    | decimal | est_counts.zona incerta.2403                                                    |
| c_tpm_zona_incerta_2215                                                           | decimal | TPM.zona incerta.2215                                                           |
| c_est_counts_zona_incerta_2215                                                    | decimal | est_counts.zona incerta.2215                                                    |
| c_tpm_zona_incerta_2663                                                           | decimal | TPM.zona incerta.2663                                                           |
| c_est_counts_zona_incerta_2663                                                    | decimal | est_counts.zona incerta.2663                                                    |
| c_tpm_zona_incerta_2208                                                           | decimal | TPM.zona incerta.2208                                                           |
| c_est_counts_zona_incerta_2208                                                    | decimal | est_counts.zona incerta.2208                                                    |
| c_tpm_zona_incerta_2822                                                           | decimal | TPM.zona incerta.2822                                                           |
| c_est_counts_zona_incerta_2822                                                    | decimal | est_counts.zona incerta.2822                                                    |

## 28 proteinatlas

| Unnamed: 0   | dtype   | description |
|:----------------|:--------|:----------------|
| c_gene                                         | text    | 基因的标准名称。                    |
| c_gene_synonym                                 | text    | 基因的别名或同义词。                  |
| c_ensembl                                      | text    | Ensembl数据库中的基因标识符。          |
| c_gene_description                             | text    | 基因的简要描述。                    |
| c_uniprot                                      | text    | Uniprot数据库中的蛋白标识符。          |
| c_chromosome                                   | text    | 基因所在的染色体。                   |
| c_position                                     | text    | 基因在染色体上的位置。                 |
| c_protein_class                                | text    | 蛋白质类别，如转录因子、酶等。             |
| c_biological_process                           | text    | 基因参与的生物学过程。                 |
| c_molecular_function                           | text    | 基因编码的蛋白质的分子功能。              |
| c_disease_involvement                          | text    | 基因与哪些疾病相关。                  |
| c_evidence                                     | text    | 支持基因功能或特性的证据级别。             |
| c_hpa_evidence                                 | text    | 来自HPA数据库的证据。                |
| c_uniprot_evidence                             | text    | 来自UniProt数据库的证据。            |
| c_nextprot_evidence                            | text    | 来自NeXtProt数据库的证据。           |
| c_rna_tissue_specificity                       | text    | RNA在不同组织中的特异性表达。            |
| c_rna_tissue_distribution                      | text    | RNA在不同组织中的分布情况。             |
| c_rna_tissue_specificity_score                 | decimal | RNA组织特异性评分。                 |
| c_rna_tissue_specific_ntpm                     | text    | RNA在特定组织中的标准化转录本数（nTPM）。    |
| c_rna_single_cell_type_specificity             | text    | RNA在单细胞类型中的特异性表达。           |
| c_rna_single_cell_type_distribution            | text    | RNA在不同单细胞类型中的分布。            |
| c_rna_single_cell_type_specificity_score       | decimal | RNA单细胞类型特异性评分。              |
| c_rna_single_cell_type_specific_ntpm           | text    | RNA在特定单细胞类型中的标准化转录本数（nTPM）。 |
| c_rna_cancer_specificity                       | text    | RNA在癌症中的特异性表达。              |
| c_rna_cancer_distribution                      | text    | RNA在不同癌症类型中的分布。             |
| c_rna_cancer_specificity_score                 | decimal | RNA癌症特异性评分。                 |
| c_rna_cancer_specific_fpkm                     | text    | RNA在特定癌症中的标准化转录本数（FPKM）。    |
| c_rna_brain_regional_specificity               | text    | RNA在脑区域中的特异性表达。             |
| c_rna_brain_regional_distribution              | text    | RNA在不同脑区域中的分布。              |
| c_rna_brain_regional_specificity_score         | decimal | RNA脑区域特异性评分。                |
| c_rna_brain_regional_specific_ntpm             | text    | RNA在特定脑区域中的标准化转录本数（nTPM）。   |
| c_rna_blood_cell_specificity                   | text    | RNA在血细胞中的特异性表达。             |
| c_rna_blood_cell_distribution                  | text    | RNA在不同血细胞类型中的分布。            |
| c_rna_blood_cell_specificity_score             | decimal | RNA血细胞特异性评分。                |
| c_rna_blood_cell_specific_ntpm                 | text    | RNA在特定血细胞类型中的标准化转录本数（nTPM）。 |
| c_rna_blood_lineage_specificity                | text    | RNA在血液谱系中的特异性表达。            |
| c_rna_blood_lineage_distribution               | text    | RNA在不同血液谱系中的分布。             |
| c_rna_blood_lineage_specificity_score          | decimal | RNA血液谱系特异性评分。               |
| c_rna_blood_lineage_specific_ntpm              | text    | RNA在特定血液谱系中的标准化转录本数（nTPM）。  |
| c_rna_cell_line_specificity                    | text    | RNA在细胞系中的特异性表达。             |
| c_rna_cell_line_distribution                   | text    | RNA在不同细胞系中的分布。              |
| c_rna_cell_line_specificity_score              | decimal | RNA细胞系特异性评分。                |
| c_rna_cell_line_specific_ntpm                  | text    | RNA在特定细胞系中的标准化转录本数（nTPM）。   |
| c_rna_tissue_cell_type_enrichment              | text    | RNA在组织细胞类型中的富集情况。           |
| c_rna_mouse_brain_regional_specificity         | text    | RNA在小鼠脑区域中的特异性表达。           |
| c_rna_mouse_brain_regional_distribution        | text    | RNA在不同小鼠脑区域中的分布。            |
| c_rna_mouse_brain_regional_specificity_score   | decimal | RNA小鼠脑区域特异性评分。              |
| c_rna_mouse_brain_regional_specific_ntpm       | text    | RNA在特定小鼠脑区域中的标准化转录本数（nTPM）。 |
| c_rna_pig_brain_regional_specificity           | text    | RNA在猪脑区域中的特异性表达。            |
| c_rna_pig_brain_regional_distribution          | text    | RNA在不同猪脑区域中的分布。             |
| c_rna_pig_brain_regional_specificity_score     | decimal | RNA猪脑区域特异性评分。               |
| c_rna_pig_brain_regional_specific_ntpm         | text    | RNA在特定猪脑区域中的标准化转录本数（nTPM）。  |
| c_antibody                                     | text    | 针对该基因编码的蛋白质的抗体信息。           |
| c_reliability__ih_                             | text    | 免疫组织化学（IH）的可靠性评分。           |
| c_reliability__mouse_brain_                    | text    | 小鼠脑中数据的可靠性评分。               |
| c_reliability__if_                             | text    | 免疫荧光（IF）的可靠性评分。             |
| c_subcellular_location                         | text    | 蛋白质的亚细胞定位。                  |
| c_secretome_location                           | text    | 蛋白质在分泌系统中的定位。               |
| c_secretome_function                           | text    | 蛋白质在分泌系统中的功能。               |
| c_ccd_protein                                  | text    | CCD数据库中的蛋白质信息。              |
| c_ccd_transcript                               | text    | CCD数据库中的转录本信息。              |
| c_blood_concentration___conc__blood_im__pg_l_  | decimal | 血液中蛋白质的免疫测定浓度（pg/L）。        |
| c_blood_concentration___conc__blood_ms__pg_l_  | decimal | 血液中蛋白质的质谱测定浓度（pg/L）。        |
| c_blood_expression_cluster                     | text    | 血液中基因表达簇信息。                 |
| c_tissue_expression_cluster                    | text    | 组织中基因表达簇信息。                 |
| c_brain_expression_cluster                     | text    | 大脑中基因表达簇信息。                 |
| c_cell_line_expression_cluster                 | text    | 细胞系中基因表达簇信息。                |
| c_single_cell_expression_cluster               | text    | 单细胞中基因表达簇信息。                |
| c_interactions                                 | decimal | 基因或蛋白质的相互作用信息。              |
| c_subcellular_main_location                    | text    | 蛋白质的主要亚细胞定位。                |
| c_subcellular_additional_location              | text    | 蛋白质的附加亚细胞定位。                |
| c_antibody_rrid                                | text    | 抗体的RRID（资源标识符）。             |
| c_pathology_prognostics___breast_cancer        | text    | 乳腺癌中的病理预后信息。                |
| c_pathology_prognostics___cervical_cancer      | text    | 宫颈癌中的病理预后信息。                |
| c_pathology_prognostics___colorectal_cancer    | text    | 结直肠癌中的病理预后信息。               |
| c_pathology_prognostics___endometrial_cancer   | text    | 子宫内膜癌中的病理预后信息。              |
| c_pathology_prognostics___glioma               | text    | 胶质瘤中的病理预后信息。                |
| c_pathology_prognostics___head_and_neck_cancer | text    | 头颈癌中的病理预后信息。                |
| c_pathology_prognostics___liver_cancer         | text    | 肝癌中的病理预后信息。                 |
| c_pathology_prognostics___lung_cancer          | text    | 肺癌中的病理预后信息。                 |
| c_pathology_prognostics___melanoma             | text    | 黑色素瘤中的病理预后信息。               |
| c_pathology_prognostics___ovarian_cancer       | text    | 卵巢癌中的病理预后信息。                |
| c_pathology_prognostics___pancreatic_cancer    | text    | 胰腺癌中的病理预后信息。                |
| c_pathology_prognostics___prostate_cancer      | text    | 前列腺癌中的病理预后信息。               |
| c_pathology_prognostics___renal_cancer         | text    | 肾癌中的病理预后信息。                 |
| c_pathology_prognostics___stomach_cancer       | text    | 胃癌中的病理预后信息。                 |
| c_pathology_prognostics___testis_cancer        | text    | 睾丸癌中的病理预后信息。                |
| c_pathology_prognostics___thyroid_cancer       | text    | 甲状腺癌中的病理预后信息。               |
| c_pathology_prognostics___urothelial_cancer    | text    | 尿路上皮癌中的病理预后信息。              |



