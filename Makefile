CC = gcc
CFLAGS = -O2 -Wall -Wextra -Werror -g

TARGETS = recursive_c inplace_c

all : $(TARGETS)

$(TARGETS) : LDFLAGS = -lm

clean :
	$(RM) $(TARGETS) *.pyc
