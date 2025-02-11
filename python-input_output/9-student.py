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

    def to_json(self):
        return self.__dict__
