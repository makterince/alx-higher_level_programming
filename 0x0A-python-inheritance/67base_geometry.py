#!/usr/bin/python3
""" creating an empty class """


class BaseGeometry:
    """ not empty anymore """
    
    def area(self):
        """ raise an exception """

        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ checking if it is an instance"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
