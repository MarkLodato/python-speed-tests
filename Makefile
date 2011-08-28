CC = gcc
CFLAGS = -O2 -Wall -Wextra -Werror -g
PYTHON = python

C_TARGS = recursive_c inplace_c
PYX_TARGS = inplace_cython
PY_TARGS = inplace_loop recursive_loop recursive_comprehension
TARGETS = $(C_TARGS) $(PYX_TARGS) $(PY_TARGS)

CYTHON_C = $(foreach x,$(PYX_TARGS) $(PY_TARGS),$x.c)

all : $(TARGETS)

$(TARGETS) : LDFLAGS = -lm

% : %.pyx
	$(PYTHON) cython_build $^

% : %.py
	$(PYTHON) cython_build $^

clean :
	$(RM) $(TARGETS) *.pyc *.o $(CYTHON_C)
