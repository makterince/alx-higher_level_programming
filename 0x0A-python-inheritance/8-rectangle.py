#!/usr/bin/python3
""" creating a class that inherits from basegeometry """


class Rectangle(BaseGeometry):
    """ initialize the parameters """

    def __init__(self, width, height):
        """ initializing private and public """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

