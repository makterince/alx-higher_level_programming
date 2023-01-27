#!/usr/bin/python3
""" creating a square class """


class Square:
    """ creating an instance of it with size """
    def __init__(self, size=None):
        self.__size = size
        """ raising an exception """
        if size != int():
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
