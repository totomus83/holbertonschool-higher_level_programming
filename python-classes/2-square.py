#!/usr/bin/python3
'''
define class Square, checks if the requirement are met
raise error value if no
set size to a private attribute
'''


class Square:
    """class square that accepts only integers and positive number
    to its size private attribute"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
