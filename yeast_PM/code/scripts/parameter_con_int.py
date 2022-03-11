import json
import DSGRN
import sys, os, ast
from dsgrn_utilities.parameter_building import construct_parameter
from dsgrn_net_query.utilities.file_utilities import read_networks

'''
The wt parameter dictionary for a specific proxy gets passed into this function to create a list of constructed clb2 perturbed parameters corresponding to a cellular phenotype of interest (clb2 ON, OFF, med HI, med LO) at each noise level where parameters were found. Each list of constructed parameters is intersected with the corresponding pattern matched list for partial cycling to determine the constructed parameters that are pattern matched to the mutant data set of interest.
:wt_pm_dict= the dictionary containing the results from matching the network to the wild-type dataset
:xc_pm_dict= the dictionary containing the results from mathcing the network to a mutant dataset
:network= the network used to find the pattern matches
:fg_label= the clb2 factor graph hex code label for the cellular phenotype of interest
:pheno= proxy label for the phenotype of interest
:resultdir= path to results directory

'''

def param_transition(wt_pm_dict, xc_pm_dict, network, fg_label, pheno, resultdir=''):
    net_spec = read_networks(network)
    net = DSGRN.Network(network)
    pg = DSGRN.ParameterGraph(net)
    wt_dict = json.load(open(wt_pm_dict))
    wt_plist = wt_dict[net_spec[0]]
    xc_pm_dict = json.load(open(xc_pm_dict))
    xc_pm_plist = xc_pm_dict[net_spec[0]]
    pm_dict = {}
    for noise,l in wt_plist:
        clb2_con = []
        clb2_xc = []
        for i in wt_plist[int(noise)][1]:
            orders = []
            hex_code = []
            param = pg.parameter(i)
            for j in range(net.size()):
                hex_code.append(param.logic()[j].hex())
                orders.append(ast.literal_eval(str(param.order()[j])))
            hex_code[3] = fg_label
            new_param_OFF = construct_parameter(net, hex_code, orders)
            clb2_con.append(pg.index(new_param_OFF))
        for index,v in enumerate(xc_pm_plist):
            clb2_xc = xc_pm_plist[index][1]
        print(len(clb2_con))
        print(len(clb2_xc))
        xc_pm = list(set(clb2_xc).intersection(clb2_con))
        pm_dict[noise] = len(xc_pm)
    net_name = os.path.splitext(os.path.basename(network))[0]
    fname = "{}_{}_WT_XC_transition.json".format(net_name, pheno)
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
