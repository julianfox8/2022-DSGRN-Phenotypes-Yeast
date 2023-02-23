import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys,ast

fontsize=18
plt.rcParams['font.size'] =fontsize
plt.rcParams['xtick.labelsize']=fontsize
plt.rcParams['ytick.labelsize']=fontsize


def plot_genes(fname,rows,figname="temp.pdf"):
    if fname.endswith(".tsv"):
        df = pd.read_csv(fname,sep="\t",comment="#")
    elif fname.endswith(".csv"):
        df = pd.read_csv(fname,sep=",",comment="#")
    else:
        raise ValueError("File type not recognized. Must be .tsv or .csv with comments using the character '#'.")
    df = df.loc[df["gene_ID"].isin(rows)]
    times = np.asarray([float(t) for t in df.columns[1:]])
    vals = {v[0] : [float(t) for t in v[1:]] for v in df.values}
    # ensure variables are in the same order as requested
    vals = {x : vals[x] for x in rows}
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    colors = colors[:3]+colors[4:]  #skip red for red/green colorblindness
    plt.figure()
    plt.gca().set_prop_cycle(color = colors)
    # sort for consistent colors
    vals = [(k,vals[k]) for k in rows]
    for l,s in vals:
        plt.plot(times,s,label=l)
    plt.legend(loc="best",fontsize=14)
    plt.ylabel("Expression",fontsize=fontsize)
    plt.xlabel("Time",fontsize=fontsize)
    plt.savefig(figname,bbox_inches="tight")
    plt.show()


def plot_genes_normalize(fname,rows,truncate=None,figname="temp.pdf"):
    if fname.endswith(".tsv"):
        df = pd.read_csv(fname,sep="\t",comment="#")
    elif fname.endswith(".csv"):
        df = pd.read_csv(fname,sep=",",comment="#")
    else:
        raise ValueError("File type not recognized. Must be .tsv or .csv with comments using the character '#'.")
    df = df.loc[df["gene_ID"].isin(rows)]
    times = np.asarray([float(t) for t in df.columns[1:]])
    if truncate:
        inds = np.where(times>truncate)
        if inds:
            times = times[:inds[0][0]]
    vals = {v[0] : np.array([float(t) for t in v[1:len(times)+1]]) for v in df.values}
    vals = {key : (v - min(v))/(max(v)-min(v)) for key,v in vals.items()}
    # ensure variables are in the same order as requested
    vals = {x : vals[x] for x in rows}
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    colors = colors[:3]+colors[4:]  #skip red for red/green colorblindness
    plt.figure()
    plt.gca().set_prop_cycle(color = colors)
    # sort for consistent colors
    vals = [(k,vals[k]) for k in rows]
    for l,s in vals:
        plt.plot(times,s,label=l)
    plt.ylabel("Expression",fontsize=fontsize)
    plt.xlabel("Time",fontsize=fontsize)
    plt.legend(loc="upper right",fontsize=14)
    plt.savefig(figname,bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    # first arg is file name of .tsv
    # second arg is a stringified list of gene names to plot
    # third arg is figure save name 
    # fourth (optional) arg is truncation time (how much of the time series to cut)
    # e.g.
    # python plot_ts.py time_series/cho_cdc14-3_r1_metdata.csv "['SWI4','NRM1','NDD1','SWI5']" "savefig.pdf" 10

    # normalize for pattern matching
    if len(sys.argv) < 5:
        plot_genes_normalize(sys.argv[1],ast.literal_eval(sys.argv[2]),figname=sys.argv[3])
    else:
        plot_genes_normalize(sys.argv[1],ast.literal_eval(sys.argv[2]),truncate=ast.literal_eval(sys.argv[4]),figname=sys.argv[3])

    # # do not normalize for FPs
    # plot_genes(sys.argv[1],ast.literal_eval(sys.argv[2]),figname=sys.argv[3])
