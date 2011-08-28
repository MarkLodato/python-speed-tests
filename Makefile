CC = gcc
CFLAGS = -O2 -Wall -Wextra -Werror -g
PYTHON = python

TARGETS = recursive_c inplace_c inplace_cython inplace_loop
CYTHON_C = inplace_cython.c inplace_loop.c

all : $(TARGETS)

$(TARGETS) : LDFLAGS = -lm

% : %.pyx
	$(PYTHON) cython_build $^

% : %.py
	$(PYTHON) cython_build $^

clean :
	$(RM) $(TARGETS) *.pyc *.o $(CYTHON_C)
