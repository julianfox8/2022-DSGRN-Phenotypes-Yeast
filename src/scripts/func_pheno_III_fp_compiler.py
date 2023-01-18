import sqlite3
import json, sys
from dsgrn_pheno_tools.fp_filter import fp_filter

def fp_queries(db):
    '''
    
    Compiles the list of fixed points corresponding to the either of the checkpoint fixed points
    :db: the .db database file corresponding to the network of interest (mini-wavepool network)

    :output: dictionary .json file containing the parameters indices that have the fixed points of interest

    '''
    c = sqlite3.connect(db)
    cursor = c.cursor()
    FP_query = dict(set([ row for row in cursor.execute('select ParameterIndex,label from Signatures natural join ( select MorseGraphIndex,label from MorseGraphAnnotations where label like "FP { _, 1, 2, _, 1 }" except select MorseGraphIndex,Source from MorseGraphEdges);')]))
    fp_filtered = fp_filter(FP_query)
    with open("fp_query_DRC.json", "w") as f:
        json.dump(fp_filtered, f)


if __name__ == '__main__':
    db =sys.argv[1]
    fp_queries(db)