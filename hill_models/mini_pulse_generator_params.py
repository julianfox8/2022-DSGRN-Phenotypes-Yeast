import json, random, itertools, ast
from dsgrn_utilities import parameter_building as pb
from dsgrn_utilities import network2logicfile as nl


def get_parameters(network,CLB2_index,fname,num_samples):
    # Get mini pulse generator params from Julian's results and choose a subsample to test
    # Example fname: "parameter_lists/WT_clb2_nonE_swi5_nrm1_overall_remainder.json" 
    all_params = json.load(open(fname))
    if num_samples < len(all_params):
        sample_params = random.sample(all_params,num_samples)
    else:
        sample_params = all_params
    # Get CLB2 logic parameters
    num_inedges, num_outedges, groups, essential = nl.get_info_from_network(network)
    CLB2_logics = nl.get_hexstrings(num_inedges[CLB2_index],num_outedges[CLB2_index],groups[CLB2_index],essential[CLB2_index])

    # Get CLB2 order parameters
    first_order = list(range(num_outedges[CLB2_index]))
    CLB2_orders = list(itertools.permutations(first_order))

    # Get CLB2 factor parameters
    CLB2_factors = list(itertools.product(CLB2_logics,CLB2_orders))

    # Construct full parameters
    params = []
    for p in sample_params:
        for f in CLB2_factors:
            hexcodes = p[0:6:2] + [f[0], p[6]]
            orders = [ast.literal_eval(x) for x in p[1:6:2]] + [f[1], ast.literal_eval(p[7])]
            params.append(pb.construct_parameter(network,hexcodes,orders))
    return params


def get_mutant_parameters(network,CLB2_index,fname,num_samples):
    # Get mini pulse generator params from Julian's results and choose a subsample to test
    # Example fname: "parameter_lists/WT_clb2_nonE_swi5_nrm1_overall_remainder.json" 
    all_params = json.load(open(fname))
    if num_samples < len(all_params):
        sample_params = random.sample(all_params,num_samples)
    else:
        sample_params = all_params
    # Get CLB2 logic parameters
    num_inedges, num_outedges, groups, essential = nl.get_info_from_network(network)
    # These were curated manually to be all the logic parameters where Clb2 (1 in, 3 out) is constant 
    CLB2_logics = ["00", "09", "1B", "3F"]

    # Get CLB2 order parameters
    first_order = list(range(num_outedges[CLB2_index]))

    # Get CLB2 factor parameters
    CLB2_factors = list(itertools.product(CLB2_logics,[first_order]))

    # Construct full parameters
    params = []
    for p in sample_params:
        for f in CLB2_factors:
            hexcodes = p[0:6:2] + [f[0], p[6]]
            orders = [ast.literal_eval(x) for x in p[1:6:2]] + [f[1], ast.literal_eval(p[7])]
            params.append(pb.construct_parameter(network,hexcodes,orders))
    return params


def extract_mini_param_from_full(fname, savename, clb2index=3):
    # example: fname = "parameter_lists/WT_clb2_nonE_swi5_nrm1_overall_remainder_nonzero_foldchange.json"
    # savename = "parameter_lists/WT_clb2_nonE_swi5_nrm1_overall_remainder_nonzero_foldchange_mini.json"
    l = json.load(open(fname))
    hexes = l[::2]
    orders=l[1::2]
    mini_hexes = [h[:clb2index]+[h[clb2index+1]] for h in hexes]
    mini_orders = [o[:clb2index]+[o[clb2index+1]] for o in orders]
    interleave = []
    for P in zip(mini_hexes,mini_orders):
        il = []
        for h,o in zip(*P):
            il.append(h)
            il.append(str(o))
        interleave.append(il)
    json.dump(interleave,open(savename,"w"))


if __name__ == "__main__":
    import sys
    # first arg is fname of json with the form [[hexes],[orders],[hexes],[orders],...]
    # second arg is fname of json in which to save the mini pulse generator parameters in Julian's format
    extract_mini_param_from_full(sys.argv[1], sys.argv[2])




