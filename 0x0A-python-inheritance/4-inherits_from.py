#!/usr/bin/python3
""" direct or indirect inheritance check """


def inherits_from(obj, a_class):
    """ check if obj is a direct inheritance """

    obj_type = type(obj)
    is_subclass = issubclass(obj_type, a_class)
    is_not_class = obj_type is not a_class
    if is_subclass and is_not_class:
        return True
    else:
        return False
