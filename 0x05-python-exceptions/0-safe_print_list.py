#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    value = 0
    for i in range(x):
        try:
            x = my_list[i]
            print(x, end="")
            value += 1
        except ValueError:
            pass
    print()
    return(value)
