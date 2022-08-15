import json
import DSGRN
import sys, os, ast, sqlite3
from dsgrn_net_query.utilities.file_utilities import read_networks
from pyrsistent import mutant

def hex_order_grabber(net,plist):
    net = DSGRN.Network(net)
    pg = DSGRN.ParameterGraph(net)
    hex_orders = set()
    for i in plist:
        param = pg.parameter(i)
        hex_order = tuple()
        for j in range(net.size()):
            if j == 3:
                pass
            else:
                hex_order = hex_order + ((param.logic()[j].hex(),str(ast.literal_eval(str(param.order()[j])))))
        hex_orders.add(hex_order)
    return(hex_orders)

def overall_remainder_comp(net,wt_pm,mutant_pm, resultdir):
    net_spec = read_networks(net)
    mutant_plist = json.load(open(mutant_pm))
    mutant_plist = mutant_plist[net_spec[0]]
    mutant_hex_order = hex_order_grabber(net,mutant_plist[-1][1])
    wt_dict = json.load(open(wt_pm))
    wt_plist = wt_dict[net_spec[0]]
    wt_hex_order = hex_order_grabber(net,wt_plist[-1][1])
    overall_hex_order_set = mutant_hex_order.intersection(wt_hex_order)
    print("remainder parameters = {}".format(len(overall_hex_order_set)))
    overall_hex_order = list(overall_hex_order_set)
    net_name = os.path.splitext(os.path.basename(net))[0]
    f_name = "{}_remainder.json".format(net_name)
    dir = os.path.join(resultdir, f_name)
    with open(dir,'w') as f:
        json.dump(overall_hex_order,f)

if __name__ == '__main__':
    net = sys.argv[1]
    wt_pm_dict = sys.argv[2]
    mutant_pm_dict = sys.argv[3]
    resultdir = sys.argv[4]
    overall_remainder_comp(net, wt_pm_dict, mutant_pm_dict, resultdir)
