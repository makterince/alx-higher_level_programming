#!/usr/bin/python3
"""script adds all arguments to a python list """

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"


def add_item(*args):
    """ lists all arguments """

    items = load_from_json_file(filename)
    items += list(args)
    save_to_json_file(items, filename)


if __name__ == '__main__':
    add_item(*sys.argv[1:])
