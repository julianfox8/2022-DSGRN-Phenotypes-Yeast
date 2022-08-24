import DSGRN,ast


def hex_order_grabber(net,plist):
    '''
    Given a DSGRN network and a parameter list, this function creates a list of hex orders of the mini-pulse generator nodes for every parameter index in the list, excluding the hex order for Clb2. 
    '''
    net = DSGRN.Network(net)
    pg = DSGRN.ParameterGraph(net)
    hex_orders = set()
    for i in plist:
        param = pg.parameter(i)
        hex_order = tuple()
        for j in range(net.size()):
            if j == 3:
                pass
            else:
                hex_order = hex_order + ((param.logic()[j].hex(),str(ast.literal_eval(str(param.order()[j])))))
        hex_orders.add(hex_order)
    return(hex_orders)