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
from mpi4py import MPI
from mpi4py.futures import MPICommExecutor
import functools as ft

def runme(sp,hyperparams=None):
    pk,param_node = sp
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    start_time = time.time()
    count = 0
    saved_samples = 0
    fold_change_count = 0

    # Create a DSGRN parameter node sampler object
    sampler = DSGRN.ParameterSampler(hyperparams["network"])

    # change initial seed (sampling is deterministic)
    N = round(random.random()*1000000)
    for _ in range(N):
        sampler.sample(param_node)

    while count < hyperparams["max_count"] and saved_samples < hyperparams["num_samples_to_save_per_param"]:

        count = count + 1

        # Sample from the specified parameter node
        param_samp_dict = json.loads(sampler.sample(param_node))['Parameter']  # dictionary of parameter choices

        # Create Hill function ODE models
        hill_model = hillmodel.hillmodel(hyperparams["network"].specification(), param_samp_dict, hyperparams["hill_exp"],old_format=False)

        # Integrate parameterized ODEs for long time to remove transients, using a fine time step
        # This helps identify fold changes within a stable full cycle, instead of within transients
        fine_time, fine_traces, nodes = hill_model.simulateHillModel(hyperparams["init_cond"], 0, 20, .01)

        # Integrate parameterized ODEs for shorter time with coarser sampling
        samp_time, samp_traces, nodes = hill_model.simulateHillModel(fine_traces[-1],
                                                                     hyperparams["trace_begin"],
                                                                     hyperparams["trace_end"],
                                                                     (hyperparams["trace_end"] - hyperparams["trace_begin"]) / hyperparams["trace_num_samp"])

        # Check that the fold change of all traces exceeds the threshold
        if len(hyperparams["included_indices"]) == hyperparams["network"].size():
            fold_change = all(
                np.array(samp_traces).max(axis=0) / np.array(samp_traces).min(
                axis=0) >= hyperparams["fold_thresh"])
        else:
            truncated_samp_traces = np.array(samp_traces)[:,hyperparams["included_indices"]]
            truncated_samp_traces = list(truncated_samp_traces)
            fold_change = all(
                np.array(truncated_samp_traces).max(axis=0) / np.array(truncated_samp_traces).min(
                axis=0) >= hyperparams["fold_thresh"])
            # hill_model.plotResults(samp_time, truncated_samp_traces,
            #     savename=os.path.join(results_dir,"data_plot_p{}_{}.pdf".format(param_ind,saved_samples)),
            #     show=True,
            #     plotoptions={'linewidth':2},
            #     legendoptions={'fontsize':24,'loc':'upper left', 'bbox_to_anchor':(1, 1)},
            #     figuresize = (20,10),
            #     labeloptions={'xlabel' : 'Time', 'ylabel' : 'Expression','fontsize' : 14}
            #     )


        # Check that the coarse time series at this Hill function parameter matches the dynamic predictions of DSGRN
        if fold_change:
            fold_change_count += 1
            if len(hyperparams["included_indices"]) == hyperparams["network"].size():   
                pattern_match, poset = pmsp.main_fc_only(param_node, hyperparams["param_graph"], hyperparams["network"], samp_time, samp_traces, epsilons=[hyperparams["epsilon"]])
            else:
                pattern_match, poset = pmsp.main_pc_only(param_node, hyperparams["param_graph"], hyperparams["network"], samp_time, truncated_samp_traces, epsilons=[hyperparams["epsilon"]])

        if fold_change and pattern_match:
            saved_samples += 1
            # plot the traces for visual inspection and sanity check
            hill_model.plotResults(samp_time, samp_traces,
                           savename=os.path.join(hyperparams["results_dir"],"data_plot_p{}_{}_{}.pdf".format(pk+1,saved_samples,timestamp)),
                           show=False,
                           plotoptions={'linewidth':2},
                           legendoptions={'fontsize':24,'loc':'upper left', 'bbox_to_anchor':(1, 1)},
                           figuresize = (20,10),
                           labeloptions={'xlabel' : 'Time', 'ylabel' : 'Expression','fontsize' : 14}
                           )
            # Save the parameter values and coarsely-sampled time series traces of the ODE simulation to disk
            yeast_dict = {'Network': hyperparams["network"].specification(),
                            'DSGRN Parameter' : [[x.hex() for x in param_node.logic()],[x.permutation() for x in param_node.order()]],
                            'Parameter': param_samp_dict,
                            'Hill Exponent': hyperparams["hill_exp"],
                            'Time': samp_time,
                            'Traces': [list(trace) for trace in samp_traces],
                            'Nodes': nodes,
                            'Poset at eps = {}'.format(hyperparams["epsilon"]) : [list(poset[0][1][0]),list(poset[0][1][1])]}

            with open(os.path.join(hyperparams["results_dir"],'hillmodel_p{}_{}_{}.json'.format(pk+1,saved_samples,timestamp)), 'w') as f:
                json.dump(yeast_dict, f)

            trace_df = pd.DataFrame()
            trace_df['time'] = samp_time
            for i in range(len(nodes)):
                trace_df[nodes[i]] = np.array(samp_traces)[:, i]
            trace_df = trace_df.set_index("time").transpose().rename_axis("gene_ID")       

            # Save the time series traces to a pipeline readable .tsv file
            with open(os.path.join(hyperparams["results_dir"],'data_p{}_{}_{}.tsv'.format(pk+1,saved_samples,timestamp)), 'w') as f:
                f.write("# Time series output to pipeline readable format\n")
                f.write("# Generated on %s\n" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                trace_df.to_csv(f, sep='\t')
        
    print("For sample parameter #{}, there were {} samples tested, matches found = {}.".format(pk+1,count,saved_samples))
    print("The number of samples with an acceptable fold change was {}.".format(fold_change_count))
    print("Time elapsed was {:02f} minutes.".format((time.time() - start_time)/60))
    sys.stdout.flush()

    if fold_change_count:
        # print the parameter with nonzero fold change (this can be very rare)
        A = list(zip([x.hex() for x in param_node.logic()],[x.permutation() for x in param_node.order()]))
        B = []
        for a in A:
            B.extend(list(a))
        B = json.dumps([str(x) for x in B])
        print("DSGRN parameter: {}".format(B))
        sys.stdout.flush()

if __name__ == "__main__":

    # When calling this script, three arguments must be passed
    # 1. the name of a folder in which to store the results
    # 2. True or False, sample from saved list of parameter indices instead of constructing parameters from mini pulse generator hexcodes and orders
    # 3. If True, the name of a json file containing a list of parameter nodes or if False, the name of a json file containing a list of mini pulse generator parameters from which to construct full parameter nodes and sample

    # The remaining optional arguments are used when partial pattern matching. This is 
    # a variable number of node indices to keep during partial pattern matching. 
    # For example, in the network above, the nodes are numbered top to bottom as 0=SWI4, 1=NRM1, 2=NDD1, 3=CLB2, 4=SWI5.
    # The script call
    #
    # mpiexec -n 6 python parameter_sampler_script.py results_folder False mini_pulse.json 0 1 2 4
    #
    # will partial pattern match within a stable partial cycle over all genes except CLB2 after sampling from mini pulse generator parameters in mini_pulse.json with 6 mpi processes.
    #
    # The script call
    #
    # mpiexec -n 6 python parameter_sampler_script.py results_folder True paramlist.json
    #
    # will fully pattern match over all genes after sampling DSGRN parameters from paramlist.json in parallel over 6 mpi processes.


    # Initialize parameter dictionary
    hyperparams = {}

    # Julian's network
    network_spec = """
    SWI4 : (~NRM1)(~CLB2)(SWI4)(SWI5) : E
    NRM1 : (SWI4) : E
    NDD1 : (SWI4)(CLB2) : E
    CLB2 : (NDD1)
    SWI5 : (~CLB2)(NDD1) : E
    """

    # This is sloppy, I should compute it
    # 10 logic parameters, 6 threshold orders
    size_of_CLB2_factor_graph = 60
    # 4 logic parameters where Clb2 is constant, 1 threshold order
    size_of_CLB2_mutant_factor_graph = 4

    # Create the DSGRN network and parameter graph objects
    hyperparams["network"] = DSGRN.Network(network_spec)
    hyperparams["param_graph"] = DSGRN.ParameterGraph(hyperparams["network"])

    ####### Choices of parameters ######
    # Noise level for pattern matching simulated data
    hyperparams["epsilon"]=0.05

    # Specify the number of parameters to sample. (see below for note)
    hyperparams["num_param_samples"] = 1000
    # (For mini pulse generator parameters, the number above is size_of_CLB2_factor_graph multiplied by the number of mini pulse generator parameters to sample. E.g., when size_of_CLB2_factor_graph = 60 then num_param_samples = 60000 means sample 1000 mini pulse generator parameters.) For partial cycling, size_of_CLB2_mutant_factor_graph is used instead

    # Specify the maximum number of successful ODE parameter samples to save 
    hyperparams["num_samples_to_save_per_param"] = 5

    # Specify maximum number of parameter sets to try per parameter
    hyperparams["max_count"] = 1000

    # Specify the Hill exponent
    hyperparams["hill_exp"] = 10

    # Specify the acceptable fold change between the peak and trough in the oscillation
    hyperparams["fold_thresh"] = 2
    #####################################

    # Specify folder in which to save output
    hyperparams["results_dir"] = sys.argv[1]

    # Get the DSGRN parameter objects
    if ast.literal_eval(sys.argv[2]):
        # Get params from Julian's results and choose a subsample to test
        all_params = json.load(open(sys.argv[3]))
        if hyperparams["num_param_samples"] <= len(all_params):
            sample_params = random.sample(all_params,hyperparams["num_param_samples"])
        else:
            raise ValueError("Sample size must be less than total number of parameters.")
        sample_params = [hyperparams["param_graph"].parameter(p) for p in sample_params]
    else:
        CLB2_index = pb.name2index(hyperparams["network"],"CLB2")
        num_mini_params_to_sample = int(ceil(hyperparams["num_param_samples"]/size_of_CLB2_mutant_factor_graph))
        sample_params = mini.get_mutant_parameters(hyperparams["network"],CLB2_index,sys.argv[3],num_mini_params_to_sample)

    # Specify whether there is partial or full pattern matching
    if len(sys.argv) > 4:
        hyperparams["included_indices"] = sorted([ast.literal_eval(x) for x in sys.argv[4:]])
    else:
        hyperparams["included_indices"] = list(range(hyperparams["network"].size()))

    # Specify initial conditions and time series sampling range and rate 
    hyperparams["init_cond"] = np.random.rand(hyperparams["network"].size())
    hyperparams["trace_begin"] = 0
    hyperparams["trace_end"] = 20
    hyperparams["trace_num_samp"] = 200
    # ---------------------------------------------


    # Parallel implementation
    work = ft.partial(runme,hyperparams=hyperparams)
    with MPICommExecutor(MPI.COMM_WORLD, root=0) as executor:
        if executor is not None:
            print("Sampling parameters.")
            # no output returned, files saved within work function
            executor.map(work, enumerate(sample_params))
            




