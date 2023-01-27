#!/usr/bin/python3
""" creating a square class """


class Square:
    """ creating an instance of it with size """

    def __init__(self, size=0):
        """ raising an exception """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
