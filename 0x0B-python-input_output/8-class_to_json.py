#!/usr/bin/python3
""" this module takes in an ibject and creates an empty directory """


def class_to_json(obj):
    """ class takes in an oobject """

    obj_dict = {}
    for attr, value in obj.__dict__.items():
        """ iterate over the attributes """

        if isinstance(value, (list, dict, str, int, bool)):
            """ check if the statement is of data type"""

            obj_dict[attr] = value
    return obj_dict
