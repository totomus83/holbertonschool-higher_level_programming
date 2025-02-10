#!/usr/bin/python3
'''
append a python list to a json file
'''


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except Exception:
    my_list = []
arguments = sys.argv[1:]
my_list.extend(arguments)
save_to_json_file(my_list, "add_item.json")
