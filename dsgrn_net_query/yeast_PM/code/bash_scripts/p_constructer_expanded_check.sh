#!/usr/bin/bash

#clb2_ON
#0.05 noise ace2_nrm1

python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_nrm1/dsgrn_net_query_results20210913155434/queries20210913155434/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/ace2_nrm1/cho_data/WT_clb2_nonE_ace2_nrm1_r1_param_list.json '0.05' '3F' 'clb2_on' "2" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/ace2_nrm1/cho_data/

#0.1 noise swi5_nrm1

python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/swi5_nrm1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/swi5_nrm1/cho_data/WT_clb2_nonE_swi5_nrm1_r1_param_list.json '0.1' '3F' 'clb2_on' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/swi5_nrm1/cho_data/

#0.1 noise swi5_yox1

python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/swi5_yox1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/swi5_yox1/cho_data/WT_clb2_nonE_swi5_yox1_r1_param_list.json '0.1' '3F' 'clb2_on' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/swi5_yox1/cho_data/

#0.1 noise ace2_nrm1

python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_nrm1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/ace2_nrm1/cho_data/WT_clb2_nonE_ace2_nrm1_r1_param_list.json '0.1' '3F' 'clb2_on' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/ace2_nrm1/cho_data/

#0.1 noise ace2_yox1

python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_yox1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/ace2_yox1/cho_data/WT_clb2_nonE_ace2_yox1_r1_param_list.json '0.1' '3F' 'clb2_on' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/ace2_yox1/cho_data/

#clb2_OFF
#0.05 noise ace2_nrm1
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_nrm1/dsgrn_net_query_results20210913155434/queries20210913155434/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_nrm1/cho_data_hi/WT_clb2_nonE_ace2_nrm1_r1_param_list.json '0.05' '00' 'clb2_off' "2" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_nrm1/cho_data_hi/
#
##0.1 noise swi5_nrm1
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/swi5_nrm1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/swi5_nrm1/cho_data_hi/WT_clb2_nonE_swi5_nrm1_r1_param_list.json '0.1' '00' 'clb2_off' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/swi5_nrm1/cho_data_hi/
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/swi5_nrm1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/swi5_nrm1/cho_data_lo/WT_clb2_nonE_swi5_nrm1_r1_param_list.json '0.1' '00' 'clb2_off' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/swi5_nrm1/cho_data_lo/
#
##0.1 noise swi5_yox1
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/swi5_yox1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/swi5_yox1/cho_data_hi/WT_clb2_nonE_swi5_yox1_r1_param_list.json '0.1' '00' 'clb2_off' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/swi5_yox1/cho_data_hi/
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/swi5_yox1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/swi5_yox1/cho_data_lo/WT_clb2_nonE_swi5_yox1_r1_param_list.json '0.1' '00' 'clb2_off' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/swi5_yox1/cho_data_lo/
#
##0.1 noise ace2_nrm1
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_nrm1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_nrm1/cho_data_hi/WT_clb2_nonE_ace2_nrm1_r1_param_list.json '0.1' '00' 'clb2_off' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_nrm1/cho_data_hi/
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_nrm1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_nrm1/cho_data_lo/WT_clb2_nonE_ace2_nrm1_r1_param_list.json '0.1' '00' 'clb2_off' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_nrm1/cho_data_lo/
#
##0.1 noise ace2_yox1
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_yox1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_yox1/cho_data_hi/WT_clb2_nonE_ace2_yox1_r1_param_list.json '0.1' '00' 'clb2_off' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_yox1/cho_data_hi/
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_yox1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_yox1/cho_data_lo/WT_clb2_nonE_ace2_yox1_r1_param_list.json '0.1' '00' 'clb2_off' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_yox1/cho_data_lo/
#
##clb2_low_mod orlando mutant
##0.025 noise swi5_nrm1
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/swi5_nrm1/dsgrn_net_query_results20210913155434/queries20210913155434/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/swi5_nrm1/orlando_data/WT_clb2_nonE_swi5_nrm1_r1_param_list.json '0.025' '09' 'clb2_low_mod' "1" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/swi5_nrm1/orlando_data/
#
##0.025 noise swi5_yox1
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/swi5_yox1/dsgrn_net_query_results20210913155434/queries20210913155434/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/swi5_yox1/orlando_data/WT_clb2_nonE_swi5_yox1_r1_param_list.json '0.025' '09' 'clb2_low_mod' "1" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/swi5_yox1/orlando_data/
#
##0.025 noise ace2_nrm1
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_nrm1/dsgrn_net_query_results20210913155434/queries20210913155434/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/ace2_nrm1/orlando_data/WT_clb2_nonE_ace2_nrm1_r1_param_list.json '0.025' '09' 'clb2_low_mod' "1" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/ace2_nrm1/orlando_data/
#
##0.025 noise ace2_yox1
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_yox1/dsgrn_net_query_results20210913155434/queries20210913155434/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/ace2_yox1/orlando_data/WT_clb2_nonE_ace2_yox1_r1_param_list.json '0.025' '09' 'clb2_low_mod' "1" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/ace2_yox1/orlando_data/
#
#
##0.1 noise swi5_nrm1
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/swi5_nrm1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/swi5_nrm1/orlando_data/WT_clb2_nonE_swi5_nrm1_r1_param_list.json '0.1' '09' 'clb2_low_mod' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/swi5_nrm1/orlando_data/
#
##0.1 noise swi5_yox1
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/swi5_yox1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/swi5_yox1/orlando_data/WT_clb2_nonE_swi5_yox1_r1_param_list.json '0.1' '09' 'clb2_low_mod' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/swi5_yox1/orlando_data/
#
##0.1 noise ace2_nrm1
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_nrm1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/ace2_nrm1/orlando_data/WT_clb2_nonE_ace2_nrm1_r1_param_list.json '0.1' '09' 'clb2_low_mod' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/ace2_nrm1/orlando_data/
#
##0.1 noise ace2_yox1
#
#python parameter_constructer.py ~/dsgrn_net_query/yeast_PM/functional_phenotype_I/wild_type/ace2_yox1/dsgrn_net_query_results20210913155435/queries20210913155435/query_results_stablefc_orlando2008_WildType_r1_trunc_param_list.json  ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/ace2_yox1/orlando_data/WT_clb2_nonE_ace2_yox1_r1_param_list.json '0.1' '09' 'clb2_low_mod' "0" ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/ace2_yox1/orlando_data/
