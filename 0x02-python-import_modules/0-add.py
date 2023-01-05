#!/usr/bin/python3
import sys
print("add_0", sys.argv[0])
n = len(sys.argv)


def add(a, b):
    a = 1
    b = 2


for i in range(1, n):
    print("{} + {} = {}".format(a, b, sum), end='')
