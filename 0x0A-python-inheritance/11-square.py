#!/usr/bin/python3
""" creating a class that inherits from basegeometry """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ inherits from the class of rectangle """

    def __init__(self, size):
        """ initialize the size """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns area of square """

        return (self.__size * self.__size)

    def __str__(self):
        """ printing format """

        return ("[Square] {}/{}".format(self.__size, self.__size))
