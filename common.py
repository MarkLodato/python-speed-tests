from cmath import exp, pi
from optparse import OptionParser
import time


def setup(N):
    return range(N),


def printer(x, y):
    for value in y:
        print '%3.4f + %3.4fj' % (value.real, value.imag)


def main(func, setup=setup, printer=printer):
    p = OptionParser(usage="%prog [-v] log-size [iterations]")
    p.add_option('-q', '--quiet', action='count', default=0,
            help="print only value in floating point")
    p.add_option('-v', '--verbose', action='count', default=0,
            help="print the FFT result")
    
    opts, args = p.parse_args()

    if not 1 <= len(args) <= 2:
        p.error('expected 1-2 positional args, got %d' % len(args))

    N = 1 << int(args[0])
    count = int(args[1]) if len(args) > 1 else 1

    x = setup(N)
    t0 = time.time()
    for i in xrange(count):
        y = func(*x)
    t1 = time.time()

    if opts.verbose >= 1:
        printer(x, y)
        print

    t = (t1-t0)/count
    if opts.quiet == 0:
        print "%f seconds per loop" % t
    else:
        print "%f" % t
