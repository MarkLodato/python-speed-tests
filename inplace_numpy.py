#!/usr/bin/python
from common import main
import numpy as np


def bitrev_shuffle(x):
    N = len(x)
    j = 0
    for i in xrange(1, N):
        b = N >> 1
        while j >= b:
            j -= b
            b >>= 1
        j += b
        if j > i:
            x[i], x[j] = x[j], x[i]


def fft_in_place(x):
    N = len(x)
    bitrev_shuffle(x)
    x.shape = (N, 1)
    while x.shape[1] < N:
        t = np.arange(x.shape[1], dtype='complex')
        wb = np.exp(-1j * np.pi / x.shape[1] * t)
        a = x[0::2].copy()
        b = x[1::2] * wb
        x[0::2] = a + b
        x[1::2] = a - b
        x.shape = (x.shape[0] / 2, x.shape[1] * 2)
    x.shape = (N,)


def fft(x):
    x = x.copy()
    fft_in_place(x)
    return x


def setup(N):
    return np.arange(N, dtype='complex'),


if __name__ == "__main__":
    main(fft, setup)
