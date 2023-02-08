#!/usr/bin/python3
""" module writes a string text into a file """


def write_file(filename="", text=""):
    """ open file with write mode set """

    with open(filename, 'w',  encoding="utf-8") as my_file:
        """ overwrite text in file """

        my_file.write(text)
    return len(text)
