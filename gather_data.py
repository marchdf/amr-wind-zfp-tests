#!/usr/bin/env python

import glob
import pathlib
import csv
import modify_hdf5_attributes as mha
import yt
import numpy as np


def main():

    fnames = glob.glob("*.log")
    plt_pfx = "plt117501"
    pnames = glob.glob(f"{plt_pfx}*")
    lst = []

    # Get the number of fields from the native plt file
    fname = f"{plt_pfx}-native"
    with open(f"{fname}/Header", "r") as f:
        f.readline()
        nfields = int(f.readline())
    pname = fname.replace(".log", "")
    nds = yt.load(
        pname, units_override={"length_unit": (1.0, "m"), "time_unit": (1.0, "s")}
    )
    native_data = nds.covering_grid(
        level=0, left_edge=[0, 0.0, 0.0], dims=nds.domain_dimensions
    )

    for fname in fnames:
        name = fname.replace(".log", "")
        pname = f"{plt_pfx}-{name}"

        if "hdf5" in pname:
            mha.modify_attributes(pname)

        ds = yt.load(
            pname, units_override={"length_unit": (1.0, "m"), "time_unit": (1.0, "s")}
        )
        all_data = ds.covering_grid(
            level=0, left_edge=[0, 0.0, 0.0], dims=ds.domain_dimensions
        )
        error = np.linalg.norm(all_data["velocityx"] - native_data["velocityx"])

        with open(fname, "r") as f:
            ncells = 0
            for line in f:
                if "grids" in line and "cells" in line:
                    ncells += int(line.split("cells")[0].split()[-1])
                if "amr-wind::IOManager::write_plot_file" in line:
                    time = float(line.split()[3])

        plt_path = pathlib.Path(f"{plt_pfx}-{name}")
        if plt_path.is_dir():
            sze = sum(f.stat().st_size for f in plt_path.glob("**/*") if f.is_file())
        elif plt_path.is_file():
            sze = plt_path.stat().st_size
        lst.append(
            {
                "name": name,
                "time": time,
                "size": sze,
                "ncells": ncells,
                "nfields": nfields,
                "error": error.value,
            }
        )
    keys = lst[0].keys()
    fname = "data.csv"
    with open(fname, "w", newline="") as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(lst)


if __name__ == "__main__":
    main()
