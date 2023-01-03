#!/usr/bin/python3
for small_alpha in range(ord('a'), ord('z')+1):
    small_alphabet = chr(small_alpha)
    if small_alphabet not in "qe":
        print(small_alphabet, end="")
