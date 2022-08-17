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
        if v.startswith("FP { 2") or v.startswith("FP { 3")or v.startswith("FP { 1"): 
            pass 
        elif v.endswith(", 0 }"): 
            pass 
        elif v not in filtered_l: 
            filtered_l[v] = [k] 
        else: 
            filtered_l[v].append(k)
    return filtered_l

def fp_queries(db):
        c = sqlite3.connect(db)
        cursor = c.cursor()
        FP_query = dict(set([ row for row in cursor.execute('select ParameterIndex,label from Signatures natural join ( select MorseGraphIndex,label from MorseGraphAnnotations where label like "FP { _, 0, 2, _, 1 }" except select MorseGraphIndex,Source from MorseGraphEdges);')]))
        fp_filtered = query_filter(FP_query)
        with open("fp_query_SAC.json", "w") as f:
            json.dump(fp_filtered, f)


if __name__ == '__main__':
    db =sys.argv[1]
    fp_queries(db)