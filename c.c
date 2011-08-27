#include <complex.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#define TIMEDIF(x, y) (y.tv_sec - x.tv_sec + 1e-6 * (y.tv_usec - x.tv_usec))

static void
fft(size_t N, complex double *x, size_t s, complex double *y)
{
    size_t M, k;
    complex double base, a, b;
    if (N <= 1) {
        x[0] = y[0];
        return;
    }
    M = N / 2;
    fft(M, x, 2*s, y);
    fft(M, x+s, 2*s, y+M);
    base = -2j * M_PI / N;
    for (k = 0; k < M; k++) {
        a = y[k];
        b = y[k+M] * cexp(base*k);
        y[k] = a + b;
        y[k+M] = a - b;
    }
}

int
main(int argc, char **argv)
{
    long logN, count;
    size_t i, N;
    struct timeval tv0, tv1;
    complex double *x, *y;

    if (argc < 2 || argc > 3) {
        fprintf(stderr, "USAGE: %s log-size [iterations]\n", argv[0]);
        exit(1);
    }
    logN = strtol(argv[1], NULL, 0);
    count = argc > 2 ? strtol(argv[2], NULL, 0) : 1;

    if (logN <= 0 || count <= 0) {
        fprintf(stderr, "both arguments must be positive integers\n");
        exit(1);
    }
    if (logN > 31) {
        fprintf(stderr, "logN must be less than 32\n");
        exit(1);
    }
    N = 1UL << logN;

    x = malloc(N * sizeof *x);
    y = malloc(N * sizeof *y);
    if (!x || !y) {
        perror("malloc");
        exit(1);
    }
    for (i = 0; i < N; i++)
        x[i] = i;

    gettimeofday(&tv0, NULL);
    for (i = 0; i < (size_t)count; i++)
        fft(N, x, 1, y);
    gettimeofday(&tv1, NULL);

    printf("%f seconds per loop\n", TIMEDIF(tv0, tv1) / count);

    return 0;
}
