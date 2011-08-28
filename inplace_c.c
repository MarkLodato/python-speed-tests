#include "common.h"

static void
bitrev_shuffle(size_t N, complex double *x)
{
    complex double temp1;
    size_t i, j, b;
    for (i = 1, j = 0; i < N; i++) {
        for (b = N / 2; j >= b; b /= 2)
            j -= b;
        j += b;
        if (j > i) {
            temp1 = x[j];
            x[j] = x[i];
            x[i] = temp1;
        }
    }
}


static void
fft_in_place(size_t N, complex double *x)
{
    size_t t, i, j, trans_size, trans;
    complex double wb, wb_step, a, b;

    bitrev_shuffle(N, x);

    for (trans_size = 2; trans_size <= N; trans_size *= 2) {
        wb = 1;
        wb_step = cexp(-2j * M_PI / trans_size);
        for (t = 0; t < trans_size / 2; t++)  {
            for (trans = 0; trans < N / trans_size; trans++)  {
                i = trans * trans_size + t;
                j = i + trans_size / 2;
                a = x[i];
                b = x[j] * wb;
                x[i] = a + b;
                x[j] = a - b;
            }
            wb *= wb_step;
        }
    }
}

static void
fft(size_t N, const complex double *x, complex double *y)
{
    memcpy(y, x, N * sizeof *x);
    fft_in_place(N, y);
}
