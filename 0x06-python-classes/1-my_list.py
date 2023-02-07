#!/usr/bin/python3
""" first creating a class list """


class MyList(list):
    """ print sorted list"""
    def print_sorted(self):
        print(sorted(self))
