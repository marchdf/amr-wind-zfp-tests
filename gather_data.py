#!/usr/bin/env python

import glob
import pathlib
import csv


def main():

    fnames = glob.glob("*.log")
    plt_pfx = "plt117501"
    lst = []
    for fname in fnames:
        name = fname.replace(".log", "")
        with open(fname, "r") as f:
            for line in f:
                if "amr-wind::IOManager::write_plot_file" in line:
                    time = float(line.split()[3])

        plt_path = pathlib.Path(f"{plt_pfx}-{name}")
        if plt_path.is_dir():
            sze = sum(f.stat().st_size for f in plt_path.glob("**/*") if f.is_file())
        elif plt_path.is_file():
            sze = plt_path.stat().st_size
        lst.append({"name": name, "time": time, "size": sze})
    keys = lst[0].keys()
    fname = "data.csv"
    with open(fname, "w", newline="") as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(lst)


if __name__ == "__main__":
    main()
