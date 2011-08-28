#!/usr/bin/python
import numpy as np
from common import main

def fft(x):
    N = len(x)
    if N <= 1:
        return x

    even = fft(x[0::2])
    odd =  fft(x[1::2])

    M = N / 2
    rhs = np.exp(-2j*np.pi/N * np.arange(M)) * odd
    l = even + rhs
    r = even - rhs

    return np.concatenate([l, r])


def setup(N):
    return np.arange(N, dtype='complex'),


if __name__ == "__main__":
    main(fft, setup)
