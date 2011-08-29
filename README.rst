This repository contains a few tests for comparing the speed between CPython_
("Pure Python"), PyPy_, and Cython_, plus various combinations of NumPy_.
There are two main programs, both `radix-2 FFTs`_: an in-place, non-recursive
version and an out-of-place, recursive version.  Furthermore, the recursive
FFT has Python version with and without list comprehensions.

Results
=======

Here are the results for a 2^20 FFT on my machine:

.. table:: Iterative FFT

    ==========  ========  =======================  ============
    Time (sec)  Relative  Program                  Effort Spent
    ==========  ========  =======================  ============
    0.4313      1.00x     c                        mild
    0.7068      1.64x     python / numpy           significant
    1.4551      3.37x     cython / numpy           mild*
    2.8243      6.55x     pypy                     none*
    6.1235      14.2x     cythonrun                none*
    8.6668      20.0x     python                   mild
    ==========  ========  =======================  ============

.. table:: Recursive FFT

    ==========  ========  =======================  ============
    Time (sec)  Relative  Program                  Effort Spent
    ==========  ========  =======================  ============
    0.7254      1.00x     c                        mild
    3.4818      4.80x     pypy loop                none*
    5.9375      8.19x     pypy comprehension       none*
    7.6153      10.5x     cythonrun loop           none*
    10.4645     14.4x     python loop              moderate
    12.5445     17.3x     cythonrun comprehension  none*
    13.7589     19.0x     python comprehension     mild
    16.6426     22.9x     python numpy             mild
    ==========  ========  =======================  ============

\* given the Python version

The results should be interpreted with a large grain of salt.  Besides the
python/numpy version of the in-place FFT, no particular attempt was made to
optimize any of the programs.  The above "effort spent" estimations are given
that I already had prior knowledge of C, Python, Cython, and NumPy.

For reference, ``numpy.fft.fft()`` takes 0.1648 seconds, 0.37x the time of my
C version.


Analysis
========

I am a firm believer in Python for numerical work, especially for people who
are not hardcore programmers.  Sure, the program might be 10–100x slower than
it could be, but the savings in programmer time is often well worth it.  Plus,
the Python interactive shell is wonderful for analyzing data.

If you have already written a program in Python and it doesn't use NumPy,
there is no reason not to try PyPy.  It takes absolutely no additional effort
and it could speed up your program significantly.

NumPy is fantastic and often gives speeds that are very close to C, but it has
a substantial learning curve and sometimes requires significant effort to
achieve such speeds.  For example, the NumPy iterative version took me three
times longer than the C version and still ran 60% slower.  I also don't
understand why the recursive Numpy program was so slow.  However, NumPy code
is usually easy to write and fast to execute, and more importantly, NumPy can
be used interactively from the Python shell.

Cython is interesting.  There are two ways to use it: cythonrun and normal
Cython.  Cythonrun is an automated process that takes a pure Python program,
compiles it into C, compiles the C into an executable that includes an
embedded interpreter, and executes it.  This is as simple as PyPy (though
there may be some configuration issues, and there are cruft files left lying
around) but the compilation time is significant and the speed gain is only
marginal.

The normal Cython process is to augment your Python program with C type
information (turning your Python code into Cython code).  This is where
you really get the big gains.  With some careful code, it is possible to
effectively write C in a Python-like language.  There are major drawbacks:
Cython has a high learning curve, requires knowledge of both C and Python,
requires a whole build process, and is generally not as easy to use as the
other solutions.  I think it certainly has its place, but probably only for
strong programmers.

All this said, I still like C and often find it to be just as easy as—and
sometimes easier than—Python.  If you want to write your number crunching
functions in C but have your high-level code in Python, I think Cython is a
great bridge between the two.


.. _CPython: http://python.org
.. _PyPy: http://pypy.org
.. _NumPy: http://numpy.scipy.org/
.. _Cython: http://cython.org
.. _radix-2 FFTs: http://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm
