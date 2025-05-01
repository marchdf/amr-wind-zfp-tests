# coding: utf-8
import h5py
import hdf5plugin
import yt
import argparse
import glob
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as plt


def main():
    """Plot data."""
    parser = argparse.ArgumentParser(description="A simple plot tool")
    parser.add_argument(
        "-f",
        "--fname",
        help="plt file to extract a slice plot from",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-o", "--outfile", help="Filename for output plot", required=True, type=str
    )
    parser.add_argument(
        "-z",
        "--z_height",
        help="Filename for output plot",
        required=False,
        type=float,
        default=90.0,
    )
    parser.add_argument(
        "-g",
        "--show_grid",
        help="Overlay the computational grid atop the countours",
        action = "store_true",
    )
    parser.add_argument(
        "--fields",
        help="Field from the plt file to plot",
        required=False,
        type=str,
        default=['velocityx'],
        nargs='+',
    )
    args = parser.parse_args()
    fname = args.fname
    outfile = args.outfile
    z_height = args.z_height
    show_grid = args.show_grid
    fields = args.fields

    ds = yt.load(
        fname, units_override={"length_unit": (1.0, "m"), "time_unit": (1.0, "s")}
    )

    Lx, Ly, Lz = ds.domain_right_edge - ds.domain_left_edge
    Lx = float(Lx)
    Ly = float(Ly)
    with PdfPages(outfile) as pdf:
        slc = yt.SlicePlot(
            ds, normal=2, fields=fields, center=[Lx // 2, Ly // 2, args.z_height]
        )
        slc.set_log('all', False)
        if show_grid:
            slc.annotate_grids()
        for field in fields:
            pdf.savefig(slc.plots[field].figure)

    ##slc.set_log(field, False)
    ##slc.save(outfile)
        #pdf.savefig()

    # Nx, Ny, Nz = ds.domain_dimensions
    # all_data = ds.covering_grid(level=0, left_edge=[0, 0.0, 0.0], dims=[Nx, Ny, Nz])
    # print(f"Covering grid size: {all_data.shape}")


if __name__ == "__main__":
    main()
