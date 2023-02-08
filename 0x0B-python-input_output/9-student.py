#!/usr/bin/python3
""" this module writes a class defines student by names and age"""


class Student:
    """ initialize name last name and age """

    def __init__(self, first_name, last_name, age):
        """privatize the parameter """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve the dictionary representation of a student"""

        obj_dict = {}
        for attr, value in self.__dict__.items():
            """iterate  over the attributes and values of the object"""

            if isinstance(value, (list, dict, str, int, bool)):
                """check if the value is of a serializable data type"""

                obj_dict[attr] = value
        return obj_dict
