import pathlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from cycler import cycler
from functools import reduce

plt.style.use(pathlib.Path(__file__).parent.resolve() / "project.mplstyle")

def main():

    data = np.load("plt117501-hdf5-zfp-0.0000001.npy")

    comp = 10
    xidx = 0
    yidx = 0
    zidx = 48
    plt.figure("velocityx-0")
    plt.imshow(np.flip(data[comp, xidx, :, :].T, axis=1), origin="lower")

    plt.figure("velocityx-1")
    plt.imshow(data[comp, :, yidx, :].T, origin='lower')
    
    plt.figure("velocityx-2")
    plt.imshow(data[comp, :, :, zidx].T, origin='lower')

    # Save the plots
    pname = "plots_npy.pdf"
    with PdfPages(pname) as pdf:
        plt.figure("velocityx-0")
        plt.colorbar()
        plt.xlabel(r"$y$", fontsize=22, fontweight="bold")
        plt.ylabel(r"$z$", fontsize=22, fontweight="bold")
        pdf.savefig(dpi=300)

        plt.figure("velocityx-1")
        plt.colorbar()
        plt.xlabel(r"$x$", fontsize=22, fontweight="bold")
        plt.ylabel(r"$z$", fontsize=22, fontweight="bold")
        pdf.savefig(dpi=300)

        plt.figure("velocityx-2")
        plt.colorbar()
        plt.xlabel(r"$x$", fontsize=22, fontweight="bold")
        plt.ylabel(r"$y$", fontsize=22, fontweight="bold")
        pdf.savefig(dpi=300)


if __name__ == "__main__":
    main()
