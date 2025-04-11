"""Plot simulation data output."""

import pathlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import numpy as np
from cycler import cycler
from functools import reduce

plt.style.use(pathlib.Path(__file__).parent.resolve() / "project.mplstyle")

def main():
    fname = "data.csv"
    df = pd.read_csv(fname)
    print(df)

    pname = "plots.pdf"
    plt.figure("timing", figsize=(14, 6))
    ax = plt.gca()
    ind = np.arange(len(df))
    width = 1
    ax.barh(
        ind,
        df.time,
        width,
        align="center",
    )
    ax.set(yticks=ind, yticklabels=df.name, ylim=[2 * width - 1, len(df)])
    ax.invert_yaxis()

    # Save the plots
    with PdfPages(pname) as pdf:
        plt.figure("timing")
        plt.xlabel(r"Time $[s]$", fontsize=22, fontweight="bold")
        plt.setp(ax.get_xmajorticklabels(), fontsize=22, fontweight="bold")
        plt.setp(ax.get_ymajorticklabels(), fontsize=22, fontweight="bold")
        plt.tight_layout()
        pdf.savefig(dpi=300)
    
if __name__ == "__main__":
    main()
