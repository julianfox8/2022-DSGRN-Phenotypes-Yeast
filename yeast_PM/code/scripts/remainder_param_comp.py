import json
import DSGRN
import sys, os, ast
from dsgrn_net_query.utilities.file_utilities import read_networks

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


def hex_order_comp(net,wt_pm,fp_list):
    wt_dict = json.load(open(wt_pm))
    net_spec = read_networks(net)
    wt_plist = wt_dict[net_spec[0]]
    fp_dict = json.load(open(fp_list))
    fp_list = sum(fp_dict.values(),[])
    #fp_list = json.load(open(fp_list))
    fp_hex_order = hex_order_grabber(net,fp_list)
    shared_hex_order = {}
    for n,pl in wt_plist:
        noise_hex_order = hex_order_grabber(net,pl)
        shared_hex_order[n] = len(fp_hex_order.intersection(noise_hex_order))
    f = os.path.basename(fp_list).split('_')[0]
    filename = "{}_remainder.json".format(f)
    with open(filename, "w") as f:
        json.dump(shared_hex_order,f)


if __name__ == '__main__':
    net =sys.argv[1]
    wt_pm = sys.argv[2]
    fp_list = sys.argv[3]
    hex_order_comp(net, wt_pm, fp_list)
