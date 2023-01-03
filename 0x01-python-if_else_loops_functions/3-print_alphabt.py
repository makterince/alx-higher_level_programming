#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z')+1):
    small_letter = chr(alphabet)
    if small_letter not in "qe":
        print(small_letter, end="")
