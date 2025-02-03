#!/usr/bin/python3
'''
this function checks if obj is of an allowed type
'''


def is_same_class(obj, a_class):
    """
    check if type matches
    """
    if type(obj) is a_class:
        return True
    else:
        return False
