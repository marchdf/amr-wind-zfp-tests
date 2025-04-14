# coding: utf-8
import h5py
import hdf5plugin
import yt
import argparse
import glob


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
    args = parser.parse_args()
    fname = args.fname
    outfile = args.outfile

    ds = yt.load(
        fname, units_override={"length_unit": (1.0, "m"), "time_unit": (1.0, "s")}
    )

    Lx, Ly, Lz = ds.domain_right_edge
    Lx = float(Lx)
    Ly = float(Ly)
    slc = yt.SlicePlot(ds, normal=2, fields="velocityx", center=[Lx // 2, Ly // 2, 90])
    slc.save(outfile)

    # Nx, Ny, Nz = ds.domain_dimensions
    # all_data = ds.covering_grid(level=0, left_edge=[0, 0.0, 0.0], dims=[Nx, Ny, Nz])
    # print(f"Covering grid size: {all_data.shape}")


if __name__ == "__main__":
    main()
