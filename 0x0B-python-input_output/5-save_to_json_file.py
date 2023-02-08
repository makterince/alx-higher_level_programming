#!/usr/bin/python3
""" module writes an object to a text file using json """

import json


def save_to_json_file(my_obj, filename):
    """ open file with write mode """

    with open(filename, 'w') as my_file:
        """ parse through json representation"""

        json.dump(my_obj, my_file)
