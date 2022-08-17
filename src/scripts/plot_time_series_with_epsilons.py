import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys,ast
import matplotlib
#matplotlib.rcParams['text.usetex'] = True

def plot_genes(fname,rows,e):
    #df1 = pd.read_csv(fname,sep="\t", delimiter=',')
    df1 = pd.read_csv(fname, sep="\t")
    df = df1.loc[df1["gene_ID"].isin(rows)]
    times = np.asarray([float(t) for t in df.columns[1:]])
    vals = {v[0] : [float(t) for t in v[1:]] for v in df.values}
    vals[r'Ndd1'] = vals['NDD1']
    del vals['NDD1']
    e1 =1+float(e)
    e2 =1- float(e)
    vals_plus_e = np.array(list(vals.values())) * e1
    vals_minus_e = np.array(list(vals.values())) *e2
    vals[r'$Ndd1 \/\/ plus \/\/ 10\%$'] = vals_plus_e[0].tolist()
    vals[r'$Ndd1 \/\/ minus \/\/ 10\%$'] = vals_minus_e[0].tolist()

    for l,s in vals.items():
        plt.plot(times,s,label=l)
    plt.hlines(440.2, 0, 250, linestyles='dotted')
    plt.hlines(150,148.8,177,color = 'r')
    plt.vlines(148.8, 0, 440.2, linestyles='dotted')
    plt.vlines(177, 0, 440.2, linestyles='dotted')
    plt.ylim(100,None)
    plt.xlim(50,None)
    plt.legend()
    #plt.title('{}'.format(fname.split('.')[0]))
    plt.xlabel('time (min)')
    plt.ylabel('transcript levels (a.u.)')
    plt.show()


if __name__ == "__main__":
    plot_genes(sys.argv[1],ast.literal_eval(sys.argv[2]),sys.argv[3])