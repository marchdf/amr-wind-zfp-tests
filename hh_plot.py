# coding: utf-8
import yt


def main():
    plt_pfx = "plt117501"

    ds = yt.load(f"./{plt_pfx}-native")
    Lx, Ly, Lz = ds.domain_right_edge
    slc = yt.SlicePlot(
        ds, normal=2, fields="velocityx", center=[Lx / 2, Ly / 2, Lz / 10]
    )
    slc.save()


if __name__ == "__main__":
    main()
