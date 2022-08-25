import DSGRN, json, ast
from dsgrn_utilities.parameter_building import construct_parameter
from dsgrn_net_query.utilities.file_utilities import read_networks



def param_list_reconstruct(wt_pm_dict,xc_pm_dict,network,logic_label):
    """
    Given two json dictionaries, a wild-type patttern matched dictionary and a mutant pattern matched dictionary, this function reconstructs the wild-type parameter list for a given noise using the same mini-pulse generator and a given hex code to determine the logic on the Clb2 node. This reconstructed parameter list is intersected with the list of mutant pattern matches for the same noise level to determine the number of wild-type pattern matches that shares the same mini-pulse generator remainder parameter as a mutant pattern matched parameter.
    """      
    net_spec = read_networks(network)
    net = DSGRN.Network(network)
    pg = DSGRN.ParameterGraph(net)
    wt_dict = json.load(open(wt_pm_dict))
    wt_plist = wt_dict[net_spec[0]]
    xc_pm_dict = json.load(open(xc_pm_dict))
    xc_pm_plist = xc_pm_dict[net_spec[0]][-1][1]
    clb2_con = [] 
    for i in wt_plist[-1][1]:
        orders = []
        hex_code = []
        param = pg.parameter(i)
        for j in range(net.size()):
            hex_code.append(param.logic()[j].hex())
            orders.append(ast.literal_eval(str(param.order()[j])))
        hex_code[3] = logic_label
        new_param = construct_parameter(net, hex_code, orders)
        clb2_con.append(pg.index(new_param))
    xc_pm = list(set(xc_pm_plist).intersection(clb2_con))
    return(xc_pm)