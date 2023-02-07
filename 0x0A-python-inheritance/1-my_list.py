#!/usr/bin/python3
""" create a class thats is a subclass of list """


class MyList(list):
    """ inherits from class List """

    def print_sorted(self):
        """ sort list out """

        print(sorted(self))
