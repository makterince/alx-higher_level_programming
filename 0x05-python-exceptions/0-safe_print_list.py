#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
try:
    print(x)
except ValueError:
    print("an error occured")
except:
    print("x is too big")
