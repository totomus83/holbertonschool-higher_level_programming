#!/usr/bin/python3
'''
say_my_name takes 2 string (or 1 if first name at least is a string)
and print them
'''
def say_my_name(first_name=None, last_name=""):
    '''
    Prints the first name and last name
    '''
    if first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name == "":
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
