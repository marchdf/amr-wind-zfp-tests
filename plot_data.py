"""Plot simulation data output."""

import pathlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import numpy as np
from cycler import cycler
from functools import reduce

plt.style.use(pathlib.Path(__file__).parent.resolve() / "project.mplstyle")


def bytes_to_mb(bytes):
    return bytes / (1024 * 1024)


def main():
    fname = "data.csv"
    df = pd.read_csv(fname)
    df["size"] = df["size"].apply(bytes_to_mb)
    df.sort_values(by=["name"], inplace=True)
    print(df)

    pname = "plots.pdf"
    cols = ["time", "size"]
    for col in cols:
        plt.figure(f"{col}", figsize=(14, 6))
        ax = plt.gca()
        ind = np.arange(len(df))
        width = 0.5
        ax.barh(
            ind,
            df[f"{col}"],
            width,
            align="center",
        )
        ax.set(yticks=ind, yticklabels=df.name)
        ax.invert_yaxis()

    # Save the plots
    with PdfPages(pname) as pdf:
        plt.figure("time")
        plt.xlabel(r"Time $[s]$", fontsize=22, fontweight="bold")
        pdf.savefig(dpi=300)

        plt.figure("size")
        plt.xlabel(r"Size $[MB]$", fontsize=22, fontweight="bold")
        pdf.savefig(dpi=300)


if __name__ == "__main__":
    main()
