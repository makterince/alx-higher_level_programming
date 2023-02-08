#!/usr/bin/python3
""" reading text file utf8 """


def read_file(filename=""):
    """ opening the file """

    with open(filename, encoding="utf-8") as my_file:
        """loop to read each line of the file """

        for line in my_file:
            """ print to standard output"""

            print(line, end="")
