import DSGRN
import sqlite3
import json, sys, os, tqdm
from dsgrn_net_query.utilities.file_utilities import read_networks

def query_filter(unfiltered_l):
    '''
    Given a list of tuples containing a fixed point (FP) label and a DSGRN parameter index, this function filters the FP labels, grabs the parameter indices corrseponding to the FP of interest and stores this data in a dictionary. The FP label of interest is 'FP { 0-1, 0, 2, 0-2, 1 }'. The dictionary that is compiled has keys containing FP labels and values containing DSGRN parameters corresponding to each FP label, respectively. 
    '''
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
        c = sqlite3.connect(db)
        cursor = c.cursor()
        monostable_query = list(set([row[0] for row in cursor.execute("select ParameterIndex from Signatures natural join (select MorseGraphIndex, count(*) as StableCount from (select MorseGraphIndex,Vertex from MorseGraphVertices except select MorseGraphIndex,Source from MorseGraphEdges) group by MorseGraphIndex) where StableCount=1;")]))
        FP_query = dict(set([ row for row in cursor.execute('select ParameterIndex,label from Signatures natural join ( select MorseGraphIndex,label from MorseGraphAnnotations where label like "FP { _, 0, 2, _, 1 }" except select MorseGraphIndex,Source from MorseGraphEdges);')]))
        monostable_fp_keys = set(monostable_query).intersection(FP_query.keys())
        monostable_fp = {k:FP_query[k] for k in monostable_fp_keys}
        monostable_fp_filtered = query_filter(monostable_fp)
        with open("monostable_fp_query.json", "w") as f:
            json.dump(monostable_fp_filtered, f)


if __name__ == '__main__':
    db =sys.argv[1]
    fp_queries(db)