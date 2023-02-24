import json
import sys, os
from dsgrn_pheno_tools.hex_order_grabber import hex_order_grabber
from dsgrn_net_query.utilities.file_utilities import read_networks

def relaxed_param_transition(wt_pm_list, xc_pm_list, net, resultdir):
    """

    Finds the list of intersecting mini-pulse generator parameters between wild-type pattern matched parameters and partial cycle pattern matched parameters corresponding to one of the oscillating mutants
    :wt_pm_list = the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to the wild-type dataset
    :xc_pm_list = the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to one of the four oscillating mutant datasets
    :net= the network .txt file corresponding to the network used to find the pattern matches
    :resultdir= path to results directory

    :output: dictionary .json file containing the number of matches at each noise level for that specific phenotype and proxy
    
    """
    wt_dict = json.load(open(wt_pm_list))
    net_spec = read_networks(net)
    wt_plist = wt_dict[net_spec[0]][-1][1]
    wt_hex_order = hex_order_grabber(net,wt_plist)
    xc_dict = json.load(open(xc_pm_list))
    xc_plist = xc_dict[net_spec[0]][-1][1]
    xc_hex_order = hex_order_grabber(net,xc_plist)
    hex_order_list = list(wt_hex_order.intersection(xc_hex_order))
    net_name = os.path.splitext(os.path.basename(net))[0]
    filename = "{}_relaxed_pheno_II_params.json".format(net_name)
    dir = os.path.join(resultdir, filename)
    with open(dir, "w") as f:
        json.dump(hex_order_list,f)


if __name__ == '__main__':
    wt_pm_dict = sys.argv[1]
    xc_pm_dict = sys.argv[2]
    network = sys.argv[3]
    resultdir = sys.argv[4]
    relaxed_param_transition(wt_pm_dict, xc_pm_dict, network, resultdir)