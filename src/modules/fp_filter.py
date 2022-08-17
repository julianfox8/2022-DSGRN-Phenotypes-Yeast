

def query_filter(unfiltered_l):
    '''
    Given a list of tuples containing a fixed point (FP) label and a DSGRN parameter index, this function filters the FP labels, grabs the parameter indices corrseponding to the FP of interest and stores this data in a dictionary. The FP label of interest is 'FP { 0-1, 0, 2, 0-2, 1 }', SAC FP. The dictionary that is compiled has keys containing FP labels and values containing DSGRN parameters corresponding to each FP label, respectively. 
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