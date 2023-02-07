#!/usr/bin/python3
""" first creating a class list """


class MyList(list):
    """ inherited stuffs from list"""

    def print_sorted(self):
        """ print sorted list """

        print(sorted(self))
