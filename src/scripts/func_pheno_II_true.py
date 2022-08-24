import json
import sys, os
from dsgrn_pheno_tools.param_list_reconstruct import param_list_reconstruct



def param_transition(wt_pm_dict, xc_pm_dict, network,logic_label, resultdir=''):
    '''
    The wt parameter dictionary for a specific proxy gets passed into this function to create a list of constructed clb2 perturbed parameters corresponding to a cellular phenotype of interest (clb2 ON, OFF, INT-HI, INT-LO) at each noise level where parameters were found. Each list of constructed parameters is intersected with the corresponding pattern matched list for partial cycling to determine the constructed parameters that are pattern matched to the mutant data set of interest.
    :wt_pm_dict= the dictionary containing the results from matching the network to the wild-type dataset
    :xc_pm_dict= the dictionary containing the results from mathcing the network to a mutant dataset
    :network= the network .txt file corresponding to the network used to find the pattern matches
    :fg_label= the clb2 factor graph hex code label for the cellular phenotype of interest
        example hex code: '3F' (hex cod eargument must be passed with quotations as in the example)
    :pheno= proxy label for the phenotype of interest used to label the output dictionary
    :resultdir= path to results directory

    :output: dictionary .json file containing the number of matches at each noise level for that specific phenotype and proxy
    '''
    param_reconstruct_dict = param_list_reconstruct( wt_pm_dict, xc_pm_dict, network, logic_label)
    net_name = os.path.splitext(os.path.basename(network))[0]
    fname = "{}_param_list_WT_XC_transition_test.json".format(net_name)
    dir = os.path.join(resultdir, fname)
    with open(dir, 'w') as f:
        json.dump(param_reconstruct_dict, f)

if __name__ == '__main__':
    wt_pm_dict = sys.argv[1]
    xc_pm_dict = sys.argv[2]
    network = sys.argv[3]
    logic_label = sys.argv[4]
    resultdir = sys.argv[5]
    param_transition(wt_pm_dict, xc_pm_dict, network, logic_label,  resultdir)
