#!/usr/bin/python3
'''
this function print the content
'''


def read_file(filename=""):
    '''
    print the text file
    '''
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print(content, end="")  
