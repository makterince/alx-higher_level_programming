#!/usr/bin/python3
""" appending a text at the end of a file """


def append_write(filename="", text=""):
    """ open the file with mode appendd """

    with open(filename, 'a', encoding="utf-8") as my_file:
        """ append text """

        my_file.write(text)
    return len(text)
