#include <complex.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/time.h>

#define TIMEDIF(x, y) (y.tv_sec - x.tv_sec + 1e-6 * (y.tv_usec - x.tv_usec))

static void fft(size_t N, const complex double *x, complex double *y);

static void
usage(const char *progname)
{
    fprintf(stderr, "USAGE: %s [-v] log-size [iterations]\n", progname);
    exit(1);
}


int
main(int argc, char **argv)
{
    long logN, count;
    size_t i, N;
    struct timeval tv0, tv1;
    complex double *x, *y;
    int c;
    int verbose = 0, quiet = 0;
    double t;

    while ((c = getopt(argc, argv, "vqh")) != -1) {
        switch (c) {
            case 'v':
                verbose++;
                break;
            case 'q':
                quiet++;
                break;
            case 'h':
            default:
                usage(argv[0]);
        }
    }

    if (optind == argc)
        usage(argv[0]);
    logN = strtol(argv[optind++], NULL, 0);
    count = 1;
    if (optind > argc)
        count = strtol(argv[optind++], NULL, 0);
    if (optind > argc)
        usage(argv[0]);

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
        fft(N, x, y);
    gettimeofday(&tv1, NULL);

    if (verbose >= 1) {
        for (i = 0; i < N; i++)
            printf("%3.4f + %3.4fj\n", creal(y[i]), cimag(y[i]));
        printf("\n");
    }

    t = TIMEDIF(tv0, tv1) / count;
    if (quiet == 0)
        printf("%f seconds per loop\n", t);
    else
        printf("%f\n", t);

    return 0;
}
