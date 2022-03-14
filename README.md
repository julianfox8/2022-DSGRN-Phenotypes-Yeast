# Overview

This module is used to investigate a hypothetical Yeast cell cycle model using experimental time series data sets. It is capable of performing DSGRN partial pattern matching which is a newly implemented tool of DSGRN. 

## Dependencies
Python 3.6/3.7, mpi4py 3.0.3, pandas, progressbar2, DSGRN (https://github.com/shaunharker/DSGRN or https://github.com/marciogameiro/DSGRN), dsgrn_net_query (https://github.com/breecummins/dsgrn_net_query), min_interval_posets (https://github.com/breecummins/min_interval_posets), and dsgrn_utilities (https://github.com/breecummins/dsgrn_utilities).

## Algorithm 
### Step 1
The first step in using this module is to run a pattern match query which requires a DSGRN network and a experimental time series dataset corresponding to the nodes within the network. A more in depth explanation of how to use the pattern matching query can be found within the dsgrn_net_query github repo (https://github.com/breecummins/dsgrn_net_query). Once the dynamic of interest, in this case a partial cycle, is identified a pattern matching query corresponding to the dynamic is run with the network and time series. The output of this query is a dictionary containing a list of DSGRN parameters for each of the specified noise levels. This process is applied to a wild-type and mutant time series using the same network, giving us two lists of parameters which will be compared in the next step.

### Step 2
The second step will use the two output dictionaries, from the first step to determine which parameters share dynamics given a single change in the logic of a node in the network. 
