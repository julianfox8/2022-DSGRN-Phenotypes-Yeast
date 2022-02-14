import DSGRN
import sqlite3
import json, sys
from collections import defaultdict


def XC_grabber(db,net):
    c = sqlite3.connect(db)
    cursor = c.cursor()
    query = list(set([ row[0] for row in cursor.execute('select ParameterIndex from Signatures natural join ( select MorseGraphIndex,Vertex from MorseGraphAnnotations where label like "FP%" except select MorseGraphIndex,Source from MorseGraphEdges)')]))
    with open("fp_list_expanded.json", "w") as f:
        json.dump(query,f)
    network = DSGRN.Network(net)
    pg = DSGRN.ParameterGraph(network)
    fp_matches = defaultdict(int)
    for j in query:
        p = pg.parameter(j)
        dg = DSGRN.DomainGraph(p)
        mg = DSGRN.MorseGraph(dg)
        for i in range(0, mg.poset().size()):
            if mg.annotation(i)[0].startswith("FP") and len(mg.poset().children(i)) == 0:
                fp_matches[mg.annotation(i)[0]] += 1
    with open("fp_list_expanded_count.json", 'w') as f:
        json.dump(fp_matches,f)

if __name__ == '__main__':
    db =sys.argv[1]
    net = sys.argv[2]
    XC_grabber(db, net)
