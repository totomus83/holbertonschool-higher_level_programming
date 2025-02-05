#!/usr/bin/python3
'''
this function checks if obj is of an allowed type
'''


def is_kind_of_class(obj, a_class):
    '''
   check if type matches or an obj of inherited class
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
