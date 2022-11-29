# Overview

This module is used to investigate a hypothetical Yeast cell cycle model using experimental time series data sets. It is capable of performing DSGRN partial pattern matching which is a newly implemented tool of DSGRN. It is assumed that the user of this repo has read 

## Dependencies
Python 3.6/3.7, mpi4py 3.0.3, pandas, progressbar2, DSGRN (https://github.com/shaunharker/DSGRN or https://github.com/marciogameiro/DSGRN), dsgrn_net_query (https://github.com/breecummins/dsgrn_net_query), min_interval_posets (https://github.com/breecummins/min_interval_posets), and dsgrn_utilities (https://github.com/breecummins/dsgrn_utilities).




## dsgrn_pheno_tools

fp_filter.py

hex_order_grabber.py

param_list_reconstruct.py

## DSGRN Phenotype I
### Algorithm 

The first step in using this module is to run a pattern match query which requires a DSGRN network and a experimental time series dataset corresponding to the nodes within the network. A more in depth explanation of how to use the pattern matching query can be found within the dsgrn_net_query github repo (https://github.com/breecummins/dsgrn_net_query). Once the dynamic of interest, in this case a full cycle, is identified a pattern matching query corresponding to the dynamic is run with the network and time series. The output of this query is a dictionary containing a list of DSGRN parameters for each of the specified noise levels. This process is applied to a wild-type and mutant time series using the same network, giving us two lists of parameters which will be compared in the next step. The same function is used to examine all wild-type datasets for each proxy, while a proxy specific function is used to examine the mutant datasets.
'''
mpiexec -n 12 python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices.py /path/to/dsgrn_network_file /path/to/list_of_dsgrn_parameters /path/to/result_directory

/2022-DSGRN-Phenotypes-Yeast/src/scripts/func_pheno_II_mutant_check/CountPatternMatch_large_networks_parameter_indices.py
'''



## DSGRN Phenotype II
### Algorithm 

The algorithm for phenotype II will use the output dictionaries from the first step to determine which parameters from the wild-type pattern matches share the same mini-pulse generator remainder parameter as parameters from a mutant dataset. This query was done with each proxy for each mutant dataset, totaling in 16 queries. 

The function used for this algorithm is called pheno_II_script.py



## DSGRN Phenotype III
### Algorithm 


The function used for this algorithm is called pheno_III_script.py