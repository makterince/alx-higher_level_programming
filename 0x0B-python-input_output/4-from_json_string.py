#!/usr/bin/python3
""" module takes a string input and returns a python object """

import json


def from_json_string(my_str):
    """ returns json string into a python object """

    return json.loads(my_str)
