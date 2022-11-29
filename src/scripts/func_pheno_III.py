import json
import sys, os
from dsgrn_pheno_tools.hex_order_grabber import hex_order_grabber
from dsgrn_net_query.utilities.file_utilities import read_networks

def hex_order_comp(net,wt_pm,fp_file, noise, resultdir=''):
    """
    

    :net= the network .txt file corresponding to the network used to find the pattern matches
    :wt_pm_dict= the dictionary containing the results from matching the network to the wild-type dataset
    :fp_file= the clb2 factor graph hex code label for the cellular phenotype of interest
    :noise= 
    :resultdir= path to results directory

    :output: dictionary .json file containing the number of matches at each noise level for that specific phenotype and proxy
    """
    wt_dict = json.load(open(wt_pm))
    net_spec = read_networks(net)
    wt_plist = wt_dict[net_spec[0]][-1][1]
    fp_dict = json.load(open(fp_file))
    fp_list = sum(fp_dict.values(),[])
    fp_hex_order = hex_order_grabber(net,fp_list)
    shared_hex_order = {}
    noise_hex_order = hex_order_grabber(net,wt_plist)
    shared_hex_order[noise] = list(fp_hex_order.intersection(noise_hex_order))
    net_name = os.path.splitext(os.path.basename(net))[0]
    f = os.path.basename(fp_file).split('_')[0]
    filename = "{}_{}_overall_remainder_test_params.json".format(net_name,f)
    dir = os.path.join(resultdir, filename)
    with open(dir, "w") as f:
        json.dump(shared_hex_order,f)


if __name__ == '__main__':
    net =sys.argv[1]
    wt_pm = sys.argv[2]
    fp_file = sys.argv[3]
    noise = sys.argv[4]
    resultdir = sys.argv[5]
    hex_order_comp(net, wt_pm, fp_file, noise, resultdir)
