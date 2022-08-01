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

def fp_hex_order_grabber(net,plist):
    net = DSGRN.Network(net)
    pg = DSGRN.ParameterGraph(net)
    fp_hex_orders = set()
    for i in plist:
        param = pg.parameter(i[0])
        hex_order = tuple()
        for j in range(net.size()):
            if j == 3:
                pass
            else:
                hex_order = hex_order + ((param.logic()[j].hex(),str(ast.literal_eval(str(param.order()[j])))))
        fp_hex_orders.add(hex_order)
    return(fp_hex_orders)


def mutant_hex_order(net,hi_pm,lo_pm,int_hi_pm,int_lo_pm):
    net_spec = read_networks(net)
    hi_plist = json.load(open(hi_pm))
    hi_plist = hi_plist[net_spec[0]]
    hi_hex_order = hex_order_grabber(net,hi_plist[-1][1])
    print(len(hi_hex_order))
    del hi_plist
    lo_plist = json.load(open(lo_pm))
    lo_plist = lo_plist[net_spec[0]]
    lo_hex_order = hex_order_grabber(net,lo_plist[-1][1])
    hi_lo_hex_order = hi_hex_order.intersection(lo_hex_order)
    print(len(lo_hex_order))
    del lo_plist,lo_hex_order, hi_hex_order
    int_hi_plist = json.load(open(int_hi_pm))
    int_hi_plist = int_hi_plist[net_spec[0]]
    int_hi_hex_order = hex_order_grabber(net,int_hi_plist[-1][1])
    print(len(int_hi_plist))
    hi_lo_int_hi_hex_order = hi_lo_hex_order.intersection(int_hi_hex_order)
    del int_hi_plist, int_hi_hex_order
    int_lo_plist = json.load(open(int_lo_pm))
    int_lo_plist = int_lo_plist[net_spec[0]]
    int_lo_hex_order = hex_order_grabber(net,int_lo_plist[-1][1])
    print(len(int_lo_hex_order))
    overall_mutant_hex_order = hi_lo_int_hi_hex_order.intersection(int_lo_hex_order)
    return overall_mutant_hex_order

def overall_remainder_comp(checkpoint_fps,net,wt_pm,hi_pm,lo_pm,int_hi_pm,int_lo_pm):
    net_spec = read_networks(net)
    mutant_hex_order_list = mutant_hex_order(net, hi_pm,lo_pm,int_hi_pm,int_lo_pm)
    print("mutant remainder parameters = {}".format(len(mutant_hex_order_list)))
    wt_dict = json.load(open(wt_pm))
    wt_plist = wt_dict[net_spec[0]]
    wt_hex_order = hex_order_grabber(net,wt_plist[-1][1])
    cycling_hex_order = wt_hex_order.intersection(mutant_hex_order_list)
    print("cycling remainder parameters = {}".format(len(cycling_hex_order)))
    fp_plist = json.load(open(checkpoint_fps))
    fp_hex_order = fp_hex_order_grabber(net,fp_plist)
    overall_hex_order_set = fp_hex_order.intersection(cycling_hex_order)
    print("overall remainder parameters = {}".format(len(overall_hex_order_set)))
    overall_hex_order = list(overall_hex_order_set)
    net_name = os.path.splitext(os.path.basename(net))[0]
    overall_fname = "{}_overall_remainder.json".format(net_name)
    with open(overall_fname,'w') as f:
        json.dump(list(overall_hex_order),f)
    cycling_fname = "{}_cycling_remainder.json".format(net_name)
    with open(cycling_fname,'w') as f:
        json.dump(list(cycling_hex_order),f)

if __name__ == '__main__':
    checkpoint_fps = sys.argv[1]
    net =sys.argv[2]
    wt_pm = sys.argv[3]
    hi_pm = sys.argv[4]
    lo_pm = sys.argv[5]
    int_hi_pm = sys.argv[6]
    int_lo_pm = sys.argv[7]
    overall_remainder_comp(checkpoint_fps,net,wt_pm,hi_pm,lo_pm,int_hi_pm,int_lo_pm)





