import json
import DSGRN
import sys, os

def param_intersect(pm_params, xc_params, network, replicate, resultsdir=""):
    pm = json.load(open(pm_params))
    xc = json.load(open(xc_params))
    pm_dict = {}
    for k,v in pm.items():
        for t,l in v:
            xc_pm = list(set(xc).intersection(l))
            if xc_pm:
                pm_dict[t] = len(xc_pm)
    net_name = os.path.splitext(os.path.basename(network))[0]
    fname = "{}_{}.json".format(net_name, replicate)
    directory_fname = os.path.join(resultsdir, fname)
    with open(directory_fname, 'w') as f:
        json.dump(pm_dict,f)

if __name__ == '__main__':
    pm_params = sys.argv[1]
    xc_params = sys.argv[2]
    network = sys.argv[3]
    replicate = sys.argv[4]
    resultdir = sys.argv[5]
    param_intersect(pm_params, xc_params, network, replicate, resultdir)
