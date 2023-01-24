#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in my_list:
        my_list[i] = x
        try:
            print("{:d}".format(x), end="")
            i += 1
        except (TypeError, ValueError):
            pass
