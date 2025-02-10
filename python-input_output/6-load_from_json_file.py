#!/usr/bin/python3
'''
this module read a json str from a file and convert it to a python obj
'''


import json


def load_from_json_file(filename):
    '''
    read and convert json file
    '''
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
