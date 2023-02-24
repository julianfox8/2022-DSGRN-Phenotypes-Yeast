# Overview

This module is used to investigate a hypothetical Yeast cell cycle model using experimental time series data sets. It is capable of performing DSGRN partial pattern matching which is a newly implemented tool of DSGRN. It is assumed that the user of this repo has read 

## Dependencies
Python 3.6/3.7, mpi4py 3.0.3, pandas, progressbar2, DSGRN (https://github.com/shaunharker/DSGRN or https://github.com/marciogameiro/DSGRN), dsgrn_net_query (https://github.com/breecummins/dsgrn_net_query), min_interval_posets (https://github.com/breecummins/min_interval_posets), and dsgrn_utilities (https://github.com/breecummins/dsgrn_utilities).




## dsgrn_pheno_tools

fp_filter.py

hex_order_grabber.py

param_list_reconstruct.py


## Create DSGRN Database

Once all the dependencies have been installed you will need to create a database (.db) file for the wavepool model network using the 'WT_clb2_nonE.txt' file in the networks subdirectory.
Thae command to do this is:

```
mpiexec -n <num_of_processors> WT_clb2_nonE.txt WT_clb2_nonE.db
```

## Dynamical Phenotype I
### Algorithm 

The goal of this query is to identify DSGRN parameters which have been pattern matched to a wild-type time series dataset.
The first step in using this module is to run a pattern match query which requires a DSGRN network and a experimental time series dataset corresponding to the nodes within the network. A more in depth explanation of how to use the pattern matching query can be found within the dsgrn_net_query github repo (https://github.com/breecummins/dsgrn_net_query). Once the dynamic of interest, in the wild-type case a full cycle, is identified a pattern matching query is run to match parameters of the network of interest and a time series dataset. It should be noted that the dynamic of interest for the mutant query is a partial cycle where Clb2 is not oscillating.The output of this query is a dictionary containing a list of DSGRN parameters for each of the specified noise levels. This process is applied to a wild-type and mutant time series using the same network, giving us two lists of parameters which will be compared in the next step. The same function is used to examine all wild-type datasets for each proxy, while a proxy specific function is used to examine the mutant datasets.

Here is a commmand for a wild-type query:
```
mpiexec -n <num_of_processors> python ~/dsgrn_net_query/src/dsgrn_net_query/queries/CountPatternMatch_large_networks_parameter_indices.py <path_to_dsgrn_network_file> <path_to_list_of_dsgrn_parameters> <path_to_result_directory>
```

Alternatively, here is the command for a mutant query:

```
mpiexec -n <num_of_processors> python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/func_pheno_II_mutant_check/CountPatternMatch_<mutant_name>.py <path_to_dsgrn_network_file> <path_to_list_of_dsgrn_parameters> <path_to_result_directory>
```





## Dynamical Phenotype II
### Algorithm 

The goal of this query is to identify DSGRN parameters which have been pattern matched to one of the four cycling mutants, additionally this query finds the mini-pulse generator (MPG) parameters which are shared between the pattern mathes identified in DSGRN phenotype I (wild-type) and the mutant attern matches found in the first step of this query.
The first step in this to run a pattern matching query for the mutant datasets of interest. Similar to the pattern matching done in DSGRN Phenotype I, the output of this query is a dictionary of lists of parameter indices with keys for each list representing the noise level used applied to the time sereis dataset. The next step in the algorithm for phenotype II will use the output dictionaries from the first step to determine which parameters from the wild-type pattern matches share the same mini-pulse generator remainder parameter as parameters from a mutant dataset. This query was done with each proxy for each mutant dataset, totaling in 16 queries. 

Here is the command to run dynamical phenotype II:
```
python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/func_pheno_II_test.py <path_to_wild_type_pattern_matched_dict> <path_to_mutant_pattern_matched_dict>  <path_to_dsgrn_network_file_corresponding_proxy_set_of_interest> <string_of_clb2_logic_label_corresponding_to_mutant_of_interest> <path_to_result_directory>
```

## Dynamical Phenotype II relaxed
### Algorithm

The goal of the relaxed phenotype is to identify phenotype-permissible DSGRN parameter which, similarly to phenotype II, have been patterned matched to one of the four cycling mutants. This query takes the same arguments as functional phenotype II except for the logic label which is not needed since this is a phenotype-permissible query. 

Here is the command to run dynamical phenotype II:
```
python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/func_pheno_II_test.py <path_to_wild_type_pattern_matched_dict> <path_to_mutant_pattern_matched_dict>  <path_to_dsgrn_network_file_corresponding_proxy_set_of_interest> <path_to_result_directory>
```



## Dynamical Phenotype III
### Algorithm 

The first step in this query is to identify the fixed point (FP) associated with the checkpoint mutant of interest. The next step in this query is to find the MPG parameters that are shared between the the DSGRN parameters identified in DSGRN Phenotype I and the DSGRN parameters which exhibit the FP of interest. Similarly to dynamical phenotype II, we are gathering two lists of DSGRN parameters and finding the intersection between these two lists. 

The command to compile the FPs of interest is:

```
python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/dynamical_pheno_III_test_list.py <path_to_mini_wavepool_database_file>
```

The command to run dynamical phenotype II is:

```
python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/dynamical_pheno_III.py <path_to_dsgrn_network_file_corresponding_proxy_set_of_interest> <path_to_wild_type_pattern_matched_dict> <path_to_fp_dictionary> <string_of_noise_level> <path_to_result_directory> 
```


## Co-existing Phenotypes

The goal of this query is to identify all the MPG parameters that exhibit all the transcriptional phenotypes of interest (wild-type cycling, and the six mutant phenotypes: the four cycling and 2 chekpoint mutants). This query requires that Dynamical phenotypes I, relaxed II, and III must have been completed.

The command for this query is:
```
python ~/2022-DSGRN-Phenotypes-Yeast/src/scripts/co_existing_pheno.py <path_to_dsgrn_network_file_corresponding_proxy_set_of_interest> <path_to_fp_dictionary> <path_to_wild_type_pattern_matched_dict> <path_to_clb2_on_mutant_pattern_matched_dict> <path_to_clb2_off_mutant_pattern_matched_dict> <path_to_clb2_int_high_mutant_pattern_matched_dict> <path_to_clb2_int_lo_mutant_pattern_matched_dict>  <path_to_dsgrn_network_file_corresponding_proxy_set_of_interest> <path_to_result_directory>
```
