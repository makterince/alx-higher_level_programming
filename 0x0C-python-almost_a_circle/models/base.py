#!/usr/bin/python3
""" creating a base class """


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize this method """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
