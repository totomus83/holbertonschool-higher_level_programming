#!/usr/bin/python3
'''
this file sort a list
'''


class MyList(list):
    """sort a ist onf integer"""
    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
