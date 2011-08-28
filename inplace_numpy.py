#!/usr/bin/python
from common import main
import numpy as np


def bitrev_shuffle(x):
    N = len(x)
    logN = int(np.log2(N))
    assert logN <= 32
    i = np.arange(N, dtype=np.uint32)
    i = ((i >> 1) & 0x55555555) | ((i & 0x55555555) << 1)
    i = ((i >> 2) & 0x33333333) | ((i & 0x33333333) << 2)
    i = ((i >> 4) & 0x0F0F0F0F) | ((i & 0x0F0F0F0F) << 4)
    i = ((i >> 8) & 0x00FF00FF) | ((i & 0x00FF00FF) << 8)
    i = ( i >> 16             ) | ( i               << 16)
    i >>= (32 - logN)
    x[:] = x[i]


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
