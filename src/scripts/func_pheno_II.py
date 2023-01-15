import json
import sys, os
from dsgrn_pheno_tools.param_list_reconstruct import param_list_reconstruct



def param_transition(wt_pm_dict, xc_pm_dict, net,logic_label, resultdir=''):
    '''

    Finds the list of intersecting mini-pulse generator parameters between wild-type pattern matched parameters and partial cycle pattern matched parameters corresponding to one of the cycling mutants
    :wt_pm_list = the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to the wild-type dataset
    :xc_pm_list = the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to one of the four oscillating mutant datasets
    :net= the network .txt file corresponding to the network used to find the pattern matches
    :logic_label= the clb2 factor graph hex code label for the cellular phenotype of interest
        example hex code: '3F' (hex code argument must be passed with quotations as in the example)
    :resultdir= path to results directory

    :output: dictionary .json file containing the matches at each noise level for that specific phenotype and proxy stored as a list of hex codes for the mini-pulse generator
    
    '''

    param_reconstruct_list = param_list_reconstruct( wt_pm_dict, xc_pm_dict, network, logic_label)
    net_name = os.path.splitext(os.path.basename(net))[0]
    fname = "{}_param_list_WT_XC_transition_test.json".format(net_name)
    dir = os.path.join(resultdir, fname)
    with open(dir, 'w') as f:
        json.dump(param_reconstruct_list, f)

if __name__ == '__main__':
    wt_pm_dict = sys.argv[1]
    xc_pm_dict = sys.argv[2]
    network = sys.argv[3]
    logic_label = sys.argv[4]
    resultdir = sys.argv[5]
    param_transition(wt_pm_dict, xc_pm_dict, network, logic_label,  resultdir)
