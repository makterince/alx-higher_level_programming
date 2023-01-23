#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
try:
    for i in my_list:
        x = my_list[i]
    print(x)
except ValueError:
    print("an error occured")
except:
    print("x is too big")
