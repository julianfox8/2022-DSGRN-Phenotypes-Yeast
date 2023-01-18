import json
import sys, os
from dsgrn_net_query.utilities.file_utilities import read_networks
from dsgrn_pheno_tools.hex_order_grabber import hex_order_grabber


def mutant_hex_order(net,hi_pm,lo_pm,int_hi_pm,int_lo_pm):
    '''

    Compiles the intersection of the hex orders corresponding to the mini-pulse generator across all four cycling mutants for a given proxy 
    :net: the network .txt file corresponding to the network used to find the pattern matches
    :hi_pm_dict=: the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to the clb2 ON dataset
    :lo_pm_dict=: the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to the clb2 OFF dataset
    :int_hi_pm_dict=: the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to the clb2 INT-H dataset
    :int_lo_pm_dict=: the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to the clb2 INT-L dataset
    :result_dir=: path to the result directory

    :output: list object containing the intersection of hex codes for the mini-pulse generator across all four cycling mutants for a given proxy
    
    
    '''

    net_spec = read_networks(net)
    hi_plist = json.load(open(hi_pm))
    hi_plist = hi_plist[net_spec[0]]
    hi_hex_order = hex_order_grabber(net,hi_plist[-1][1])
    del hi_plist
    lo_plist = json.load(open(lo_pm))
    lo_plist = lo_plist[net_spec[0]]
    lo_hex_order = hex_order_grabber(net,lo_plist[-1][1])
    hi_lo_hex_order = hi_hex_order.intersection(lo_hex_order)
    del lo_plist,lo_hex_order, hi_hex_order
    int_hi_plist = json.load(open(int_hi_pm))
    int_hi_plist = int_hi_plist[net_spec[0]]
    int_hi_hex_order = hex_order_grabber(net,int_hi_plist[-1][1])
    hi_lo_int_hi_hex_order = hi_lo_hex_order.intersection(int_hi_hex_order)
    del int_hi_plist, int_hi_hex_order
    int_lo_plist = json.load(open(int_lo_pm))
    int_lo_plist = int_lo_plist[net_spec[0]]
    int_lo_hex_order = hex_order_grabber(net,int_lo_plist[-1][1])
    overall_mutant_hex_order = hi_lo_int_hi_hex_order.intersection(int_lo_hex_order)
    return overall_mutant_hex_order

def overall_remainder_comp(checkpoint_fps,net,wt_pm,hi_pm,lo_pm,int_hi_pm,int_lo_pm,resultdir):
    '''

    Compiles the intersection of the hex orders corresponding to the mini-pulse generator across all four cycling mutants for a given proxy 
    :net: the network .txt file corresponding to the network used to find the pattern matches
    :hi_pm_dict=: the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to the clb2 ON dataset
    :lo_pm_dict=: the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to the clb2 OFF dataset
    :int_hi_pm_dict=: the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to the clb2 INT-H dataset
    :int_lo_pm_dict=: the .json file for the dictionary containing the results from matching the mini-wavepool network parameters to the clb2 INT-L dataset
    :result_dir=: path to the result directory

    :output: list object containing the intersection of hex codes for the mini-pulse generator across all four cycling mutants for a given proxy
    
    
    '''

    net_spec = read_networks(net)
    mutant_hex_order_list = mutant_hex_order(net, hi_pm,lo_pm,int_hi_pm,int_lo_pm)
    print("mutant remainder parameters = {}".format(len(mutant_hex_order_list)))
    wt_dict = json.load(open(wt_pm))
    wt_plist = wt_dict[net_spec[0]]
    wt_hex_order = hex_order_grabber(net,wt_plist[-1][1])
    cycling_hex_order = mutant_hex_order_list.intersection(wt_hex_order)
    print("cycling remainder parameters = {}".format(len(overall_hex_order_set)))
    fp_plist = json.load(open(checkpoint_fps))
    fp_hex_order = hex_order_grabber(net,fp_plist)
    overall_hex_order_set = fp_hex_order.intersection(cycling_hex_order)
    print("overall remainder parameters = {}".format(len(overall_hex_order_set)))
    overall_hex_order = list(overall_hex_order_set)
    net_name = os.path.splitext(os.path.basename(net))[0]
    f_name = "{}_cycling_remainder.json".format(net_name)
    dir = os.path.join(resultdir, f_name)
    with open(dir,'w') as f:
        json.dump(overall_hex_order,f)


if __name__ == '__main__':
    checkpoint_fps = sys.argv[1]
    net =sys.argv[2]
    wt_pm = sys.argv[3]
    hi_pm = sys.argv[4]
    lo_pm = sys.argv[5]
    int_hi_pm = sys.argv[6]
    int_lo_pm = sys.argv[7]
    result_dir = sys.argv[8]
    overall_remainder_comp(checkpoint_fps,net,wt_pm,hi_pm,lo_pm,int_hi_pm,int_lo_pm,result_dir)






