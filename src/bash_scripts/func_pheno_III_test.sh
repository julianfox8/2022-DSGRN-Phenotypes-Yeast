#!/usr/bin/bash

python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/func_pheno_III_overall_fp_test.py ~/yeast_databases/WT_clb2_nonE.db

#swi5_nrm1
python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/func_pheno_III_overall_test.py ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_nrm1.txt ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/swi5_nrm1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/fp_query_test.json '0.1' ~//2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/results/

#swi5_yox1
python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/func_pheno_III_overall_test.py ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_yox1.txt ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/swi5_yox1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/fp_query_test.json '0.1' ~//2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/results/

#ace2_nrm1
python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/func_pheno_III_overall_test.py ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_nrm1.txt ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/ace2_nrm1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/fp_query_test.json '0.1' ~//2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/results/

#ace2_yox1
python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/func_pheno_III_overall_test.py ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_yox1.txt ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/ace2_yox1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/fp_query_test.json '0.1' ~//2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/results/
