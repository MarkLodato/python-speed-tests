from numpy cimport complex128_t as complex_t, ndarray
from libc.math cimport M_PI
cimport cython

from common import main
from cmath import exp
import numpy as np

@cython.boundscheck(False)
cdef bitrev_shuffle(ndarray[complex_t, ndim=1] x):
    cdef int N = x.shape[0]
    cdef int j = 0
    cdef int i, b
    cdef complex_t tmp
    for i in range(1, N):
        b = N >> 1
        while j >= b:
            j -= b
            b >>= 1
        j += b
        if j > i:
            tmp = x[i]
            x[i] = x[j]
            x[j] = tmp


@cython.boundscheck(False)
cdef fft_in_place(ndarray[complex_t, ndim=1] x):
    cdef int N = x.shape[0]
    cdef int trans_size = 2
    cdef complex_t wb, wb_step, a, b
    cdef int i, j, t

    bitrev_shuffle(x)
    while trans_size <= N:
        wb = 1+0j
        wb_step = exp(-2j * M_PI / trans_size)
        for t in range(trans_size >> 1):
            for trans in range(N / trans_size):
                i = trans * trans_size + t
                j = i + (trans_size >> 1)
                a = x[i]
                b = x[j] * wb
                x[i] = a + b
                x[j] = a - b
            wb *= wb_step
        trans_size <<= 1


def fft(x):
    x = x.copy()
    fft_in_place(x)
    return x


def setup(N):
    return np.arange(N, dtype='complex'),


if __name__ == "__main__":
    main(fft, setup)
