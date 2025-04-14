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
    df["time_dof"] = df["time"] / (df["ncells"] * df["nfields"])
    df["size_dof"] = df["size"] / (df["ncells"] * df["nfields"])
    df["size"] = df["size"].apply(bytes_to_mb)
    native_size = df.loc[df["name"] == "native", "size"].values[0]
    native_time = df.loc[df["name"] == "native", "time"].values[0]
    df["time_norm"] = df["time"] / native_time
    df["size_norm"] = df["size"] / native_size
    df.sort_values(by=["name"], inplace=True)
    print(df)

    pname = "plots.pdf"
    cols = ["time", "size", "time_dof", "size_dof", "time_norm", "size_norm", "error"]
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

        plt.figure("time_dof")
        plt.xlabel(r"Time $[s/DoF]$", fontsize=22, fontweight="bold")
        pdf.savefig(dpi=300)

        plt.figure("size_dof")
        plt.xlabel(r"Size $[B/DoF]$", fontsize=22, fontweight="bold")
        pdf.savefig(dpi=300)

        plt.figure("time_norm")
        plt.xlabel(r"Time $[-]$", fontsize=22, fontweight="bold")
        pdf.savefig(dpi=300)

        plt.figure("size_norm")
        plt.xlabel(r"Size $[-]$", fontsize=22, fontweight="bold")
        pdf.savefig(dpi=300)

        plt.figure("error")
        plt.xlabel(r"Error $[m/s]$", fontsize=22, fontweight="bold")
        ax.set_xscale("log")
        pdf.savefig(dpi=300)


if __name__ == "__main__":
    main()
