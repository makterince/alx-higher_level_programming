#!/usr/bin/python3
""" module returns json string representation of a python obj """

import json


def to_json_string(my_obj):
    """ parse python obj into json string"""

    return json.dumps(my_obj)
