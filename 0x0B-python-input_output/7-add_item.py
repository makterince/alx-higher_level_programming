#!/usr/bin/python3
"""script adds all arguments to a python list """

import sys

import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    c_json = load_from_json_file(filename)
except FileNotFoundError:
    c_json = []
except json.decoder.JSONDecodeError:
    c_json = []

for item in sys.argv[1:]:
    c_json += [item]
    save_to_json_file(c_json, filename)
