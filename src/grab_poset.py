from dsgrn_net_query.utilities.file_utilities import read_networks
from dsgrn_net_query.utilities.poset_utilities import calculate_poset
from dsgrn_net_query.queries.CountPatternMatch_large_networks import get_posets
import sys
import json
import DSGRN

def poset_grabber(param, network):
    param_dict = json.load(open(param))
    network_spec = read_networks(network)
    net = DSGRN.Network(network)
    poe = calculate_poset(param_dict,network_spec)
    events = poe[0][('CLB2', 'NDD1', 'SWI4', 'SWI5', 'YHP1')][0][1][0]
    event_ordering = poe[0][('CLB2', 'NDD1', 'SWI4', 'SWI5', 'YHP1')][0][1][1]
    p = DSGRN.PosetOfExtrema(net, events, event_ordering)
    pg = DSGRN.PatternGraph(p)
    DSGRN.DrawGraph(pg).render()


if __name__ == "__main__":
    param = sys.argv[1]
    network = sys.argv[2]
    poset_grabber(param, network)