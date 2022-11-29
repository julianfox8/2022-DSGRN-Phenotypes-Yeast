import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys,ast


def plot_genes(fname,rows):
    if fname.endswith('.csv'):
        df1 = pd.read_csv(fname,sep="\\t",delimiter=',')
        df = df1.loc[df1["gene_ID"].isin(rows)]
    if fname.endswith('.txt'):
        df1 = pd.read_csv(fname, sep="\t", error_bad_lines=False, skiprows=28)
        #df1 = pd.read_csv(fname, sep="\t", error_bad_lines=False)
        df1 = df1.iloc[:, 3:]
        df = df1.loc[df1["symbol"].isin(rows)]
    if fname.endswith('.tsv'):
        df1 = pd.read_csv(fname, sep="\t")
        df = df1.loc[df1["gene_ID"].isin(rows)]
    times = np.asarray([float(t) for t in df.columns[1:]])
    vals = {v[0] : [float(t) for t in v[1:]] for v in df.values}
    ordered_vals = {}
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    colors = colors[:3] + colors[4:]  # skip red for red/green colorblindness
    plt.gca().set_prop_cycle(color=colors)
    for i in rows:
        ordered_vals[i] = vals[i]
    for l,s in ordered_vals.items():
        plt.plot(times,s,label=l)
    plt.legend(fontsize=11)
    plt.xlabel('time (min)',fontsize=15)
    plt.ylabel('transcript levels (a.u.)',fontsize=15)
    plt.ylim([0,3000])
    plt.xlim([50,300])
    plt.show()


if __name__ == "__main__":
    plot_genes(sys.argv[1],ast.literal_eval(sys.argv[2]))

