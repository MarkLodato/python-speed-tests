CC = gcc
CFLAGS = -O2 -Wall -Wextra -g

all : c

c : LDFLAGS = -lm

clean :
	$(RM) c
