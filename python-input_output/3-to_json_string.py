#!/usr/bin/python3
'''
this file contain a function that convert a python object into a json string
'''


import json


def to_json_string(my_obj):
    '''
    convert pyhton object to json string
    '''
    json_string = json.dumps(my_obj)
    return json_string
