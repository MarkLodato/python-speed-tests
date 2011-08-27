#!/usr/bin/python
import numpy as np
from comprehension import main

def fft(x, y):
    N = len(x)
    if N <= 1:
        y[:] = x[:]
        return

    even = y[0::2]
    odd  = y[1::2]
    fft(x[0::2], even)
    fft(x[1::2], odd)

    M = len(odd)
    expBase = -2j * np.pi / N
    k = np.arange(M, dtype='complex')
    rhs = np.exp(expBase*k) * odd
    l = even + rhs
    r = even - rhs
    y[:M] = l
    y[M:] = r


def setup(N, count):
    x = np.arange(N, dtype='complex')
    y = np.empty_like(x)
    return x, y


if __name__ == "__main__":
    main(fft, setup)
