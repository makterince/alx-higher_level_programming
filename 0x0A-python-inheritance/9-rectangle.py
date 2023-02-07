#!/usr/bin/python3
""" creating a class that inherits from basegeometry """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ initialize the parameters """

    def __init__(self, width, height):
        """ initializing private and public """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area of a rectangle """

        return self.__width * self.__height

    def __str__(self):
        """ str printing format """

        print("[Rectangle] {}/{}".format(self.__width, self.__height))
