#!/usr/bin/python3
""" reading text file utf8 """


def read_file(filename=""):
    """ opening the file """

    with open("UTF8", encoding="utf-8") as my_file:
        read_file = my_file.read()
