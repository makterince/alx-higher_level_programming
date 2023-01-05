#!/usr/bin/python3
from sys import argv
n = len(sys.argv)
for i in range(1, n):
    ("{}: ".format(sys.argv), sys.argv[i], end='\n')
