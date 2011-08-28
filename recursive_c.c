#include "common.h"

static void
fft_s(size_t N, const complex double *x, size_t s, complex double *y)
{
    size_t M, k;
    complex double base, a, b;
    if (N <= 1) {
        y[0] = x[0];
        return;
    }
    M = N / 2;
    fft_s(M, x, 2*s, y);
    fft_s(M, x+s, 2*s, y+M);
    base = -2j * M_PI / N;
    for (k = 0; k < M; k++) {
        a = y[k];
        b = y[k+M] * cexp(base*k);
        y[k] = a + b;
        y[k+M] = a - b;
    }
}

static void
fft(size_t N, const complex double *x, complex double *y)
{
    fft_s(N, x, 1, y);
}
