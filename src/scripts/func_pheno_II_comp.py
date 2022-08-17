import json
import DSGRN
import sys, os, ast
from tqdm import tqdm
from dsgrn_utilities.parameter_building import construct_parameter
from dsgrn_net_query.utilities.file_utilities import read_networks



def param_transition(wt_pm_dict, xc_pm_dict, network, fg_label, pheno, resultdir=''):
    '''
    The wt parameter dictionary for a specific proxy gets passed into this function to create a list of constructed clb2 perturbed parameters corresponding to a cellular phenotype of interest (clb2 ON, OFF, med HI, med LO) at each noise level where parameters were found. Each list of constructed parameters is intersected with the corresponding pattern matched list for partial cycling to determine the constructed parameters that are pattern matched to the mutant data set of interest.
    :wt_pm_dict= the dictionary containing the results from matching the network to the wild-type dataset
    :xc_pm_dict= the dictionary containing the results from mathcing the network to a mutant dataset
    :network= the network .txt file corresponding to the network used to find the pattern matches
    :fg_label= the clb2 factor graph hex code label for the cellular phenotype of interest
        example hex code: '3F' (hex cod eargument must be passed with quotations as in the example)
    :pheno= proxy label for the phenotype of interest used to label the output dictionary
    :resultdir= path to results directory

    :output: dictionary .json file containing the number of matches at each noise level for that specific phenotype and proxy
    '''

    net_spec = read_networks(network)
    net = DSGRN.Network(network)
    pg = DSGRN.ParameterGraph(net)
    wt_dict = json.load(open(wt_pm_dict))
    wt_plist = wt_dict[net_spec[0]]
    xc_pm_dict = json.load(open(xc_pm_dict))
    xc_pm_plist = xc_pm_dict[net_spec[0]]
    pm_dict = {}
    for noise,l in wt_plist:
        print("Starting transitions for {} proxy with a {} noise level:\n".format(pheno,noise), flush=True)
        clb2_con = [] 
        clb2_xc = []
        for index,v in enumerate(xc_pm_plist):
            if noise == xc_pm_plist[index][0]:
                clb2_xc = xc_pm_plist[index][1]
        for i in tqdm(wt_plist[int(noise)][1]):
            orders = []
            hex_code = []
            param = pg.parameter(i)
            for j in range(net.size()):
                hex_code.append(param.logic()[j].hex())
                orders.append(ast.literal_eval(str(param.order()[j])))
            hex_code[3] = fg_label
            new_param = construct_parameter(net, hex_code, orders)
            clb2_con.append(pg.index(new_param))
        print("Number of XC parameters = {}\n".format(len(clb2_xc)), flush=True)
        print("Number of reconstructed WT parameters = {}\n".format(len(clb2_con)), flush=True)
        xc_pm = list(set(clb2_xc).intersection(clb2_con))
        pm_dict[noise] = xc_pm
        print("End of transitions for {} proxy with a {} noise level: \n where {} matches were found between reconstructed WT parameters and XC parameters\n\n".format(pheno,noise,len(xc_pm)))
    net_name = os.path.splitext(os.path.basename(network))[0]
    fname = "{}_param_list_WT_XC_transition.json".format(net_name)
    dir = os.path.join(resultdir, fname)
    with open(dir, 'w') as f:
        json.dump(pm_dict, f)

if __name__ == '__main__':
    wt_pm_dict = sys.argv[1]
    xc_pm_dict = sys.argv[2]
    network = sys.argv[3]
    fg_label = sys.argv[4]
    pheno = sys.argv[5]
    resultdir = sys.argv[6]
    param_transition(wt_pm_dict, xc_pm_dict, network, fg_label, pheno, resultdir)
