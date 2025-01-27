#!/usr/bin/python3
'''
the __init__ function checks the requirement and set the __size to size
the area function returns the square of the size of the square
__size * __size
'''


class Square:
    """checks if size is an int and if it is > 0
    then return the square of __size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
