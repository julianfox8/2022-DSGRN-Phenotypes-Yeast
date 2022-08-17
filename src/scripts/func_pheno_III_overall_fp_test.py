import DSGRN
import sqlite3
import json, sys, os, tqdm
from dsgrn_net_query.utilities.file_utilities import read_networks
from modules.fp_filter import fp_filter

def fp_queries(db):
        c = sqlite3.connect(db)
        cursor = c.cursor()
        FP_query = dict(set([ row for row in cursor.execute('select ParameterIndex,label from Signatures natural join ( select MorseGraphIndex,label from MorseGraphAnnotations where label like "FP { _, 0, 2, _, 1 }" except select MorseGraphIndex,Source from MorseGraphEdges);')]))
        fp_filtered = fp_filter(FP_query)
        with open("fp_query_test.json", "w") as f:
            json.dump(fp_filtered, f)


if __name__ == '__main__':
    db =sys.argv[1]
    fp_queries(db)