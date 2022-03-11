#!/usr/bin/bash

#WT queries
time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices.py ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_nrm1.txt ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/p_file_wt.json ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/swi5_nrm1/  #phenotype I, WT, proxies swi5/nrm1

time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices.py ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_yox1.txt ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/p_file_wt.json ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/swi5_yox1/  #phenotype I, WT, proxies swi5/yox1

time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices.py ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_nrm1.txt ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/p_file_wt.json ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/ace2_nrm1/  #phenotype I, WT, proxies ace2/nrm1

time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices.py ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_yox1.txt ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/p_file_wt.json ~/2022-DSGRN-Phenotypes-Yeast/yeast_PM/functional_phenotype_I/wild_type/ace2_yox1/  #phenotype I, WT, proxies ace2/yox1

#clb2_ON queries
#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_SWI5_NRM1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_swi5_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/p_file_clb2_ON.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/swi5_nrm1/  #phenotype II, clb2_ON, proxies swi5/nrm1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_SWI5_YOX1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_swi5_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/p_file_clb2_ON.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/swi5_yox1/  #phenotype II, clb2_ON, proxies swi5/yox1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_ACE2_NRM1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/p_file_clb2_ON.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/ace2_nrm1/  ~/dsgrn_net_query/yeast_PM/networks/WT_nonE_ace2_nrm1.txt #phenotype II, clb2_ON, proxies ace2/nrm1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_ACE2_YOX1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_ace2_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/p_file_clb2_ON.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/ace2_yox1/  #phenotype II, clb2_ON, proxies ace2/yox1

#clb2_OFF queries
#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_SWI5_NRM1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_swi5_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/p_file_clb2_OFF.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/swi5_nrm1/  #phenotype II, clb2_OFF, proxies swi5/nrm1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_SWI5_YOX1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_swi5_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/p_file_clb2_OFF.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/swi5_yox1/  #phenotype II, clb2_OFF, proxies swi5/yox1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_ACE2_NRM1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/p_file_clb2_OFF.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_nrm1/ ~/dsgrn_net_query/yeast_PM/networks/WT_nonE_ace2_nrm1.txt #phenotype II, clb2_OFF, proxies ace2/nrm1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_ACE2_YOX1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_ace2_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/p_file_clb2_OFF.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_OFF/ace2_yox1/  #phenotype II, clb2_OFF, proxies ace2/yox1

##clb2_high_mod queries
#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_SWI5_NRM1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_swi5_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_high_mod/param_file_high_mod.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_high_mod/swi5_nrm1/  #phenotype II, clb2_high_mod, proxies swi5/nrm1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_SWI5_YOX1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_swi5_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_high_mod/param_file_high_mod.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_high_mod/swi5_yox1/  #phenotype II, clb2_high_mod, proxies swi5/yox1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_ACE2_NRM1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_high_mod/param_file_high_mod.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_high_mod/ace2_nrm1/  #phenotype II, clb2_high_mod, proxies ace2/nrm1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_ACE2_YOX1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_ace2_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_high_mod/param_file_high_mod.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_high_mod/ace2_yox1/  #phenotype II, clb2_high_mod, proxies ace2/yox1

##clb2_low_mod queries
#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_SWI5_NRM1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_swi5_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/param_file_low_mod.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/swi5_nrm1/  #phenotype II, clb2_low_mod, proxies swi5/nrm1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_SWI5_YOX1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_swi5_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/param_file_low_mod.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/swi5_yox1/  #phenotype II, clb2_low_mod, proxies swi5/yox1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_ACE2_NRM1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/param_file_low_mod.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/ace2_nrm1/  #phenotype II, clb2_low_mod, proxies ace2/nrm1

#time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_ACE2_YOX1.py ~/dsgrn_net_query/yeast_PM/networks/WT_clb2_nonE_ace2_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/param_file_low_mod.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_low_mod/ace2_yox1/  #phenotype II, clb2_low_mod, proxies ace2/yox1
