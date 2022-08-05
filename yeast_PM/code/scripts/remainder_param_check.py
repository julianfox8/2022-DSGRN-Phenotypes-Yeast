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


def hex_order_comp(net,wt_pm,fp_file, resultdir=''):
    wt_dict = json.load(open(wt_pm))
    net_spec = read_networks(net)
    wt_plist = wt_dict[net_spec[0]]
    noise_hex_order = hex_order_grabber(net,wt_plist[-1][1])
    net_name = os.path.splitext(os.path.basename(net))[0]
    f = os.path.basename(fp_file).split('_')[0]
    filename = "{}_{}_wt_remainder.json".format(net_name,f)
    dir = os.path.join(resultdir, filename)
    with open(dir, "w") as f:
        json.dump(len(noise_hex_order),f)


if __name__ == '__main__':
    net =sys.argv[1]
    wt_pm = sys.argv[2]
    resultdir = sys.argv[3]
    hex_order_comp(net, wt_pm, resultdir)
