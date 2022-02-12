import DSGRN
import sqlite3
import sys
import json
import ast
from dsgrn_utilities.parameter_building import construct_parameter

#XC_grabber creates a list of all parameters exhibiting a stable XC
#param_compare creates two lists containing the parameters with clb2 OFF and clb2 ON that exhibit a stable XC



def XC_grabber(db):
    c = sqlite3.connect(db)
    cursor = c.cursor()
    query = [ row[0] for row in cursor.execute('select ParameterIndex,Vertex from Signatures natural join ( select MorseGraphIndex,Vertex from MorseGraphAnnotations where label="XC {sbf, yhp1, sff, swi5/ace2}" except select MorseGraphIndex,Source from MorseGraphEdges);')]
    return query

def param_compare(net, query):
    query = json.load(open(query))
    network = DSGRN.Network(net)
    pg = DSGRN.ParameterGraph(network)
    clb2_OFF = []
    clb2_ON = []
    for i in query:
        param = pg.parameter(i)
        param_logic = param.logic()[3].hex()
        if param_logic == '09':
            clb2_OFF.append(i)
        elif param_logic == '1B':
            clb2_ON.append(i)
    with open("clb2_low_mod_XC.json", 'w') as f:
        json.dump(clb2_OFF,f)
    with open("clb2_high_mod_XC.json", 'w') as f:
        json.dump(clb2_ON,f)
    # return clb2_OFF
    # return clb2_ON



def parameter_checker(net, clb2_ON , clb2_OFF):
    network = DSGRN.Network(net)
    pg = DSGRN.ParameterGraph(network)
    low_parameters = []
    for i in clb2_ON:
        orders = []
        hex_code = []
        param = pg.parameter(i)
        for j in range(network.size()):
            hex_code.append(param.logic()[j].hex())
            orders.append(ast.literal_eval(str(param.order()[j])))
        hex_code[3] = '00'
        new_param = construct_parameter(network, hex_code, orders)
        low_parameters.append(pg.index(new_param))
    similar_param = set(low_parameters).intersection(clb2_OFF)
    with open('similar_param_data.txt', 'wb') as fp:
        pickle.dump(similar_param, fp)
    return(similar_param)
if __name__ == '__main__':
    #db = sys.argv[1]
    #query = XC_grabber(db)
    query = sys.argv[2]
    net = sys.argv[1]
    param_compare(net, query)
