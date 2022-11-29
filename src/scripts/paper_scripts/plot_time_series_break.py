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

    for i in rows:
        ordered_vals[i] = vals[i]
    f,(ax,ax2) =plt.subplots(2,1,sharex=True,gridspec_kw={'height_ratios': [1,3]})
    ax.set_prop_cycle(color=colors)
    ax2.set_prop_cycle(color=colors)
    for l,s in ordered_vals.items():
        ax.plot(times,s,label=l)
        ax2.plot(times,s,label=l)

    ax.set_ylim(4000, 4500)  # outliers only
    ax2.set_ylim(0, 2000)  # most of the data
    ax.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax.tick_params(axis='x',bottom =False,top=False)
    #ax.tick_params(labeltop='off')
    ax2.xaxis.tick_bottom()
    d = .015  # how big to make the diagonal lines in axes coordinates
    # arguments to pass to plot, just so we don't keep repeating them
    kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
    ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
    ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
    ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
    ax.legend(fontsize=11)
    #plt.title('cse4 mutant time series data')
    plt.xlabel('time (min)',fontsize=15)
    plt.ylabel('transcript levels (a.u.)',fontsize=15)
    plt.ylim([0,2000])
    plt.xlim([50,300])
    plt.show()


if __name__ == "__main__":
    plot_genes(sys.argv[1],ast.literal_eval(sys.argv[2]))

