#!/usr/bin/env python
import sys
import numpy

# read parameters from distributed cache
f = open('params','r')
paramline = f.readline()
params = paramline.strip().split()
a = float(params[0])
b = float(params[1])
f.close()

# process input data
for line in sys.stdin:
    line = line.strip()

    words = line.split()
    ti = float(words[0])
    yi = float(words[1])

    expbt  = numpy.exp(b*ti)

    f    = (yi-a*expbt)
    dfda = -2*expbt*(yi-a*expbt)
    dfdb = -2*a*ti*expbt*(yi-a*expbt)

    key = "1"
    count = 1
    print '%s\t%d\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f' % (key, count, f, dfda, dfdb, f*dfda, f*dfdb, dfda*dfda, dfda*dfdb, dfdb*dfdb)
