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
    size_t b, i, j, trans_size, trans;
    complex double wb, wb_step, temp1, temp2;

    bitrev_shuffle(N, x);

    for (trans_size = 2; trans_size <= N; trans_size *= 2) {
        wb = 1;
        wb_step = cexp(-2j * M_PI / trans_size);
        for (b = 0; b < trans_size / 2; b++)  {
            for (trans = 0; trans < N / trans_size; trans++)  {
                i = trans * trans_size + b;
                j = i + trans_size / 2;
                temp1 = x[i];
                temp2 = x[j] * wb;
                x[i] = temp1 + temp2;
                x[j] = temp1 - temp2;
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
