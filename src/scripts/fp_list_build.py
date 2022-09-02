import DSGRN
import json,ast,sys
from dsgrn_net_query.utilities.file_utilities import read_networks


def fp_compiler(network,wt_pm,fp_list):
    net = DSGRN.Network(network)
    net_spec = read_networks(network)
    wt_plist = json.load(open(wt_pm))
    wt_plist = wt_plist[net_spec[0]][-1]
    print(len(wt_plist))
    print(wt_plist[1])
    print(wt_plist[0])
    pg = DSGRN.ParameterGraph(net)
    fp_plist = json.load(open(fp_list))
    full_param_ho = {}
    for i in fp_plist:
        param = pg.parameter(i)
        hex_order = tuple()
        for j in range(net.size()):
            if j == 3:
                pass
            else:
                hex_order = hex_order + ((param.logic()[j].hex(),str(ast.literal_eval(str(param.order()[j])))))
        full_param_ho[i] = hex_order
    print(len(full_param_ho))
    wt_set = set()
    for j in wt_plist:
        param = pg.parameter(i)
        hex_order = tuple()
        for j in range(net.size()):
            if j == 3:
                pass
            else:
                hex_order = hex_order + ((param.logic()[j].hex(),str(ast.literal_eval(str(param.order()[j])))))
        wt_set.add(hex_order)
    print(len(wt_set))
    remainder_overlap = wt_set.intersection(set(full_param_ho.values()))
    fp_pi_list = [k for k in full_param_ho.keys() if full_param_ho[k] in remainder_overlap ]
    with open("fp_overlap_swi5_nrm1_plist.json", 'w') as f:
        json.dump(fp_pi_list,f)
    
if __name__ == '__main__':
    net =sys.argv[1]
    wt_pm = sys.argv[2]
    fp_file = sys.argv[3]
    fp_compiler(net, wt_pm, fp_file)