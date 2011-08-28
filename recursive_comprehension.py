#!/usr/bin/python
from cmath import exp, pi
from common import main

def fft(x):
    N = len(x)
    if N <= 1:
        return x

    even = fft(x[0::2])
    odd =  fft(x[1::2])

    M = N / 2
    expBase = -2j*pi/N
    l = [even[k] + exp(expBase*k) * odd[k] for k in xrange(M)]
    r = [even[k] - exp(expBase*k) * odd[k] for k in xrange(M)]

    return l + r


if __name__ == "__main__":
    main(fft)
