#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]  # Deletes the key-value pair if the key exists
    return a_dictionary
