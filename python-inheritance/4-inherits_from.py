#!/usr/bin/python3
'''
This function check if obj is an instance of a class that inherited from the specified class
'''


def inherits_from(obj, a_class):
    '''
    Checks if obj an inherited class
    '''
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
