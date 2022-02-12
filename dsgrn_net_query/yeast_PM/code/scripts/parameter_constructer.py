import DSGRN, ast, json, os, sys
from dsgrn_utilities.parameter_building import construct_parameter
from dsgrn_net_query.utilities.file_utilities import read_networks



# def param_constructer(p, network,label, pg, clb2_con):
#         orders = []
#         hex_code = []
#         param = pg.parameter(p)
#         for j in range(network.size()):
#             hex_code.append(param.logic()[j].hex())
#             orders.append(ast.literal_eval(str(param.order()[j])))
#         hex_code[3] = label
#         new_param_OFF = construct_parameter(network, hex_code, orders)
#         clb2_con.append(pg.index(new_param_OFF))

def param_transition(wt_params, network, plist, noise, label , pheno, index, resultdir = ''):
        wt_dict = json.load(open(wt_params))
        net_spec = read_networks(network)
        net = DSGRN.Network(network)
        pg = DSGRN.ParameterGraph(net)
        wt_plist = wt_dict[net_spec[0]][int(index)][1]
        clb2_con = []
        for i in wt_plist:
            orders = []
            hex_code = []
            param = pg.parameter(i)
            for j in range(net.size()):
                hex_code.append(param.logic()[j].hex())
                orders.append(ast.literal_eval(str(param.order()[j])))
            hex_code[3] = label
            new_param_OFF = construct_parameter(net, hex_code, orders)
            clb2_con.append(pg.index(new_param_OFF))
        plist = json.load(open(plist))
        clb2_plist = plist[noise]
        clb2_trans = list(set(clb2_con).intersection(clb2_plist))
        net_name = os.path.splitext(os.path.basename(network))[0]
        fname = "{}_{}_{}.json".format(net_name, noise, pheno)
        dir = os.path.join(resultdir, fname)
        with open(dir, 'w') as f:
                json.dump(clb2_trans,f)


if __name__ == '__main__':
    wt_params = sys.argv[1]
    network = sys.argv[2]
    plist = sys.argv[3]
    noise = sys.argv[4]
    label = sys.argv[5]
    pheno = sys.argv[6]
    index = sys.argv[7]
    resultdir = sys.argv[8]
    param_transition(wt_params, network, plist, noise, label, pheno, index, resultdir)
