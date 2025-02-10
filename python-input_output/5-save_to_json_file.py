#!/usr/bin/python3
'''
this module convert python obj into json str and write it in a file txt
'''


import json


def save_to_json_file(my_obj, filename):
    '''
    this convert python obj into json str and write it in a file txt
    '''
    json_string = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json_string)
