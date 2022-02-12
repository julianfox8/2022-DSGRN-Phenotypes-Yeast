#!/usr/bin/bash

#clb2_ON queries cho (mod high data)

time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_SWI5_NRM1.py ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/p_file_clb2_ON_cho.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/swi5_nrm1/cho_data/ ~/dsgrn_net_query/yeast_PM/networks/WT_without_clb2/WT_nonE_swi5_nrm1.txt #phenotype II, clb2_ON, proxies swi5/nrm1

time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_SWI5_YOX1.py ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_swi5_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/p_file_clb2_ON_cho.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/swi5_yox1/cho_data/ ~/dsgrn_net_query/yeast_PM/networks/WT_without_clb2/WT_nonE_swi5_yox1.txt #phenotype II, clb2_ON, proxies swi5/yox1

time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_ACE2_NRM1.py ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_nrm1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/p_file_clb2_ON_cho.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/ace2_nrm1/cho_data/ ~/dsgrn_net_query/yeast_PM/networks/WT_without_clb2/WT_nonE_ace2_nrm1.txt #phenotype II, clb2_ON, proxies ace2/nrm1

time mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices_ACE2_YOX1.py ~/dsgrn_net_query/yeast_PM/networks/WT_with_clb2/WT_clb2_nonE_ace2_yox1.txt ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/p_file_clb2_ON_cho.json ~/dsgrn_net_query/yeast_PM/functional_phenotype_II/clb2_ON/ace2_yox1/cho_data/ ~/dsgrn_net_query/yeast_PM/networks/WT_without_clb2/WT_nonE_ace2_yox1.txt #phenotype II, clb2_ON, proxies ace2/yox1
