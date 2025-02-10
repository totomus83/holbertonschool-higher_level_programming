#!/usr/bin/python3
'''
this module convert python obj into json str and write it in a file txt
'''


import json


def save_to_json_file(my_obj, filename):
    '''
    this convert python obj into json str and write it in a file txt
    '''
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
