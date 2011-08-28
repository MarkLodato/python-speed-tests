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
    idx = np.arange(N)
    idx.shape = (N, 1)
    trans_size = 2
    while trans_size <= N:
        t = np.arange(trans_size >> 1)
        wb = np.exp(-2j * np.pi / trans_size * t)
        i = idx[0::2]
        j = idx[1::2]
        a = x[i]
        b = x[j] * wb
        x[i] = a + b
        x[j] = a - b
        trans_size <<= 1
        idx.shape = (idx.shape[0] / 2, idx.shape[1] * 2)


def fft(x):
    x = x.copy()
    fft_in_place(x)
    return x


def setup(N):
    return np.arange(N, dtype='complex'),


if __name__ == "__main__":
    main(fft, setup)
