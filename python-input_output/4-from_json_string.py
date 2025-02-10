#!/usr/bin/python3
'''
this file contain a function that convert json str to python obj
'''


import json


def from_json_string(my_str):
    '''
    convert json str to python obj
    '''
    python = json.loads(my_str)
    return python
