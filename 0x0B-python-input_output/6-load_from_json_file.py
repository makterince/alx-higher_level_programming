#!/usr/bin/python3
""" this module creates a file from a json rep"""

import json


def load_from_json_file(filename):
    """ open the  file in read mode"""

    with open(filename) as my_file:
        """ load the file with json rep """

        return json.load(my_file)
