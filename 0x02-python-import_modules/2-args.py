#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    i = 0

    if n == 2:
        print("{}argument:".format(n - 1))
    elif n == 1:
        print("{}argument:".format(n - 1))
    else:
        print{"{}argument:".format(n - 1))
    for arg in argv:
        if i == 0:
            i += 1
            continue
        print("{}: {}".format(i, arg))
        i += 1
