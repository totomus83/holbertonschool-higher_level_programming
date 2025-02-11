#!/usr/bin/python3
'''
This module retrieve a dictionary representation of a Student instance
'''


class Student:
    """a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        filter = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                filter[key] = value
        return filter
