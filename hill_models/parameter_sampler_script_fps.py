import json,ast,os
import DSGRN
import numpy as np
import pandas as pd
from math import ceil
from dsgrn_utilities import pattern_match_single_param as pmsp
from dsgrn_utilities import hillmodel
import datetime, time, sys,random
import mini_pulse_generator_params as mini
from dsgrn_utilities import parameter_building as pb


# Julian's network
network_spec = """
SWI4 : (~NRM1)(~CLB2)(SWI4)(SWI5) : E
NRM1 : (SWI4) : E
NDD1 : (SWI4)(CLB2) : E
CLB2 : (NDD1)
SWI5 : (~CLB2)(NDD1) : E
"""

# This is sloppy, I should compute it
size_of_CLB2_factor_graph = 60

# Create the DSGRN network and parameter graph objects
network = DSGRN.Network(network_spec)
param_graph = DSGRN.ParameterGraph(network)

####### Choices of parameters ######
# Specify the number of parameters to sample. (see below for note)
num_param_samples = 1200
# (For mini pulse generator parameters, the number above is size_of_CLB2_factor_graph multiplied by the number of mini pulse generator parameters to sample. E.g., when size_of_CLB2_factor_graph = 60 then num_param_samples = 60000 means sample 1000 mini pulse generator parameters.)

# Specify the maximum number of successful ODE parameter samples to save 
num_samples_to_save_per_param = 5

# Specify maximum number of parameter sets to try per parameter
max_count = 1000

# Specify the Hill exponent
hill_exp = 10

# Specify the fold change below which a time trace is considered constant
# This fold change will be checked during the last third of the time series in order to allow for transients
fold_thresh = 2
#####################################

# When calling this script, three arguments must be passed
# 1. the name of a folder in which to store the results
# 2. True or False, sample from saved list of parameter indices instead of constructing parameters from mini pulse generator hexcodes and orders
# 3. If True, the name of a json file containing a list of parameter nodes or if False, the name of a json file containing a list of mini pulse generator parameters from which to construct full parameter nodes and sample
#
# For example, the script call
#
# python parameter_sampler_script_fps.py results_folder True paramlist.json
#
# will sampling DSGRN parameters from paramlist.json and check for a fixed point after a transient


# Specify folder in which to save output
results_dir = sys.argv[1]

# Get the DSGRN parameter objects
if ast.literal_eval(sys.argv[2]):
    # Get params from Julian's results and choose a subsample to test
    all_params = json.load(open(sys.argv[3]))
    if num_param_samples <= len(all_params):
        sample_params = random.sample(all_params,num_param_samples)
    else:
        raise ValueError("Sample size must be less than total number of parameters.")
    sample_params = [param_graph.parameter(p) for p in sample_params]
else:
    CLB2_index = pb.name2index(network,"CLB2")
    num_mini_params_to_sample = int(ceil(num_param_samples/size_of_CLB2_factor_graph))
    sample_params = mini.get_parameters(network,CLB2_index,sys.argv[3],num_mini_params_to_sample)

# Specify initial conditions and time series sampling range and rate 
init_cond = np.random.rand(network.size())
trace_begin = 0
trace_end = 20
trace_num_samp = 200
# ---------------------------------------------

# Create a DSGRN parameter node sampler object
sampler = DSGRN.ParameterSampler(network)

# Specify a parameter node in the parameter graph
for pk,param_node in enumerate(sample_params):

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    start_time = time.time()
    count = 0
    saved_samples = 0
    fold_change_count = 0

    while count < max_count and saved_samples < num_samples_to_save_per_param:

        count = count + 1

        # Sample from the specified parameter node
        param_samp_dict = json.loads(sampler.sample(param_node))['Parameter']  # dictionary of parameter choices

        # Create Hill function ODE models
        hill_model = hillmodel.hillmodel(network_spec, param_samp_dict, hill_exp,old_format=False)

        # Integrate parameterized ODEs for shorter time with coarser sampling
        samp_time, samp_traces, nodes = hill_model.simulateHillModel(init_cond,
                                                                     trace_begin,
                                                                     trace_end,
                                                                     (trace_end - trace_begin) / trace_num_samp)

        # Check that the fold change of all traces is below the threshold during the last third of the time series
        fold_change = all(
                np.array(samp_traces[round(len(samp_time)/3):]).max(axis=0) / np.array(samp_traces[round(len(samp_time)/3):]).min(
                axis=0) < fold_thresh)
        # hill_model.plotResults(samp_time, truncated_samp_traces,
        #     savename=os.path.join(results_dir,"data_plot_p{}_{}.pdf".format(param_ind,saved_samples)),
        #     show=True,
        #     plotoptions={'linewidth':2},
        #     legendoptions={'fontsize':24,'loc':'upper left', 'bbox_to_anchor':(1, 1)},
        #     figuresize = (20,10),
        #     labeloptions={'xlabel' : 'Time', 'ylabel' : 'Expression','fontsize' : 14}
        #     )

        if fold_change:
            saved_samples += 1
            # plot the traces for visual inspection and sanity check
            hill_model.plotResults(samp_time, samp_traces,
                           savename=os.path.join(results_dir,"data_plot_p{}_{}_{}.pdf".format(pk+1,saved_samples,timestamp)),
                           show=False,
                           plotoptions={'linewidth':2},
                           legendoptions={'fontsize':24,'loc':'upper left', 'bbox_to_anchor':(1, 1)},
                           figuresize = (20,10),
                           labeloptions={'xlabel' : 'Time', 'ylabel' : 'Expression','fontsize' : 14}
                           )
            # Save the parameter values and coarsely-sampled time series traces of the ODE simulation to disk
            yeast_dict = {'Network': network.specification(),
                            'DSGRN Parameter' : [[x.hex() for x in param_node.logic()],[x.permutation() for x in param_node.order()]],
                            'Parameter': param_samp_dict,
                            'Hill Exponent': hill_exp,
                            'Time': samp_time,
                            'Traces': [list(trace) for trace in samp_traces],
                            'Nodes': nodes
                            }

            with open(os.path.join(results_dir,'hillmodel_p{}_{}_{}.json'.format(pk+1,saved_samples,timestamp)), 'w') as f:
                json.dump(yeast_dict, f)

            trace_df = pd.DataFrame()
            trace_df['time'] = samp_time
            for i in range(len(nodes)):
                trace_df[nodes[i]] = np.array(samp_traces)[:, i]
            trace_df = trace_df.set_index("time").transpose().rename_axis("gene_ID")       

            # Save the time series traces to a pipeline readable .tsv file
            with open(os.path.join(results_dir,'data_p{}_{}_{}.tsv'.format(pk+1,saved_samples,timestamp)), 'w') as f:
                f.write("# Time series output to pipeline readable format\n")
                f.write("# Generated on %s\n" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                trace_df.to_csv(f, sep='\t')
        
    print("For sample parameter #{}, there were {} samples tested, matches found = {}.".format(pk+1,count,saved_samples))
    print("The number of samples with an acceptable fold change was {}.".format(fold_change_count))
    print("Time elapsed is {:02f} minutes.".format((time.time() - start_time)/60))

    if fold_change_count:
        print("DSGRN parameter: {}, {}".format([x.hex() for x in param_node.logic()],[x.permutation() for x in param_node.order()]))






