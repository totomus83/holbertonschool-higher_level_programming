#!/usr/bin/python3
'''
this file contain a class BaseGeometry and a class rectangle
inheriting from BaseGeometry
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define subclass Rectangle who inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
