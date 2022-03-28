import DSGRN
import sqlite3
import json, sys, os, tqdm
from dsgrn_net_query.utilities.file_utilities import read_networks

def query_filter(unfiltered_l):
    filtered_l = {}
    for k,v in unfiltered_l.items(): 
        if v.startswith("FP { 2") or v.startswith("FP { 3"): 
            pass 
        elif v.endswith("3, 1 }"): 
            pass 
        elif v not in filtered_l: 
            filtered_l[v] = [k] 
        else: 
            filtered_l[v].append(k)
    return filtered_l

def fp_queries(db):
    if os.path.exists("bistable_fp_query.json") and os.path.exists("multistable_fp_query.json"):
        multistable_fp =  json.load(open("multistable_fp_query.json"))
        bistable_fp = json.load(open("bistable_fp_query.json"))
    else:
        c = sqlite3.connect(db)
        cursor = c.cursor()
        bistable_query = list(set([row[0] for row in cursor.execute("select ParameterIndex from Signatures natural join (select MorseGraphIndex, count(*) as StableCount from (select MorseGraphIndex,Vertex from MorseGraphVertices except select MorseGraphIndex,Source from MorseGraphEdges) group by MorseGraphIndex) where StableCount=2;")]))
        multistable_query = list(set([row[0] for row in cursor.execute("select ParameterIndex from Signatures natural join (select MorseGraphIndex, count(*) as StableCount from (select MorseGraphIndex,Vertex from MorseGraphVertices except select MorseGraphIndex,Source from MorseGraphEdges) group by MorseGraphIndex) where StableCount>2;")]))
        FP_query = dict(set([ row for row in cursor.execute('select ParameterIndex,label from Signatures natural join ( select MorseGraphIndex,label from MorseGraphAnnotations where label like "FP { _, 0, 2, _, 1 }" except select MorseGraphIndex,Source from MorseGraphEdges);')]))
        bistable_fp_keys = set(bistable_query).intersection(FP_query.keys())
        bistable_fp = {k:FP_query[k] for k in bistable_fp_keys}
        multistable_fp_keys = set(multistable_query).intersection(FP_query.keys())
        multistable_fp = {k:FP_query[k] for k in tqdm.tqdm(multistable_fp_keys)}
        bistable_fp_filtered = query_filter(bistable_fp)
        with open("bistable_fp_query.json", "w") as f:
            json.dump(bistable_fp_filtered, f)
        multistable_fp_filtered = query_filter(multistable_fp)
        with open("multistable_fp_query.json", "w") as f:
            json.dump(multistable_fp_filtered, f)
    return multistable_fp_filtered, bistable_fp_filtered

def FC_FP_grabber(db,wt_pm, network, resultdir):
    multistable_fp,bistable_fp = fp_queries(db)
    wt_dict = json.load(open(wt_pm))
    net_spec = read_networks(network)
    wt_plist = wt_dict[net_spec[0]]
    fc_fp_dict = {}
    for n,l in wt_plist:
        bistable_list = {'bistable': {}}
        multistable_list = {'multistable': {}}
        for fp, bl in tqdm.tqdm(bistable_fp.items()):
            bl_fp = list(set(l).intersection(bl))
            bistable_list['bistable'][fp] = len(bl_fp)
        for fp, ml in tqdm.tqdm(multistable_fp.items()):
            ml_fp = list(set(l).intersection(ml))
            multistable_list['multistable'][fp] = len(ml_fp)
        fc_fp_dict[n] = bistable_list
        fc_fp_dict[n].update(multistable_list)
        print(bistable_list, multistable_list)
    net_name = os.path.splitext(os.path.basename(network))[0]
    fname = "{}_pheno_III.json".format(net_name)
    dir = os.path.join(resultdir, fname)
    with open(dir, 'w') as f:
        json.dump(fc_fp_dict,f)

if __name__ == '__main__':
    db =sys.argv[1]
    wt_pm = sys.argv[2]
    network = sys.argv[3]
    resultdir = sys.argv[4]
    FC_FP_grabber(db, wt_pm, network, resultdir)
