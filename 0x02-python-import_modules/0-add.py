#!/usr/bin/python3
import sys
print("add_0", sys.argv[0])
n = len(sys.argv)


def add(a, b):
    a = 1
    b = 2


sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])
print("{} + {} = {}".format(a, b, sum), end='')
