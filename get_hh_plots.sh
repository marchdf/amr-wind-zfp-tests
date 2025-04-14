#!/usr/bin/env bash

# DATADIR="/projects/extremedata/mhenryde/amr-wind-zfp-tests/"
DATADIR="."
for i in `ls plt*hdf5*`
do
    python hh_plot.py -f $i -o plots/`basename $i`
done
