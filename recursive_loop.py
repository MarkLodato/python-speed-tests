#!/usr/bin/python
from cmath import exp, pi
from common import main

def _fft(N, x, xo, s, y, yo):
    if N <= 1:
        y[yo] = x[xo]
        return
    M = N / 2
    _fft(M, x, xo, 2*s, y, yo)
    _fft(M, x, xo+s, 2*s, y, yo+M)
    base = -2j*pi / N
    for k in xrange(M):
        a = y[yo+k]
        b = y[yo+k+M] * exp(base*k)
        y[yo+k] = a + b
        y[yo+k+M] = a - b


def fft(x, y):
    _fft(len(x), x, 0, 1, y, 0)
    return y


def setup(N):
    return range(N), [None]*N


if __name__ == "__main__":
    main(fft, setup)
