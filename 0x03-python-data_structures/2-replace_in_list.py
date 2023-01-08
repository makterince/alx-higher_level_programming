#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for idx in range(len(my_list)):
        if idx < 0 and idx >= len(my_list):
            return my_list
        my_list[idx] = element
        return my_list
