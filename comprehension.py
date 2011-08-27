#!/usr/bin/python
from cmath import exp, pi
import sys
import time

def fft(x):
    N = len(x)
    if N <= 1:
        return x

    even = fft(x[0::2])
    odd =  fft(x[1::2])

    M = N / 2
    expBase = -2j*pi/N
    l = [even[k] + exp(expBase*k) * odd[k] for k in xrange(M)]
    r = [even[k] - exp(expBase*k) * odd[k] for k in xrange(M)]

    return l + r


def setup(N, count):
    return range(N),


def main(func=fft, setup=setup):
    if not 2 <= len(sys.argv) <= 3:
        print >>sys.stderr, "USAGE: %s log-size [iterations]" % sys.argv[0]
        sys.exit(1)
    N = 1 << int(sys.argv[1])
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    x = setup(N, count)
    t0 = time.time()
    for i in xrange(count):
        y = func(*x)
    t1 = time.time()

    print "%s seconds per loop" % ((t1-t0)/count)


if __name__ == "__main__":
    main()
