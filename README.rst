This repository contains a few tests for comparing the speed between CPython_
("Pure Python"), PyPy_, and Cython_, plus various combinations of NumPy_.
There are two main program types: an in-place `radix-2 FFT`_ (implemented as a
loop) and an out-of-place radix-2 FFT (implemented with recursion).
Furthermore, the recursive FFT has Python version with a list comprehension
and with a normal for loop.

Here are the results for a 2^20 FFT on my machine:

.. table:: In-Place FFT

    ==========  ==========
    Time (sec)  Program
    ==========  ==========
    0.4313      c
    0.7068      numpy
    1.4551      cython+numpy
    2.8243      pypy
    6.1235      cythonrun
    8.6668      python
    ==========  ==========

.. table:: Recursive FFT

    ==========  ==========
    Time (sec)  Program
    ==========  ==========
    0.7254      c
    3.4818      pypy-loop
    5.9375      pypy-comprehension
    7.6153      cythonrun-loop
    10.4645     python-loop
    12.5445     cythonrun-comprehension
    13.7589     python-comprehension
    16.6426     numpy
    ==========  ==========


.. _CPython: http://python.org
.. _PyPy: http://pypy.org
.. _NumPy: http://numpy.scipy.org/
.. _Cython: http://cython.org
.. _radix-2 FFT: http://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm
