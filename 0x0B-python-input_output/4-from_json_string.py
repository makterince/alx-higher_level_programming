#!/usr/bin/python
""" module takes a string input and returns a python object """

import json


def from_json_string(my_str):
    """ parse json string into a python object """

    return json.loads(my_str)
