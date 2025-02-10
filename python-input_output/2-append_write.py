#!/usr/bin/python3
'''
this function print the content
'''


def append_write(filename="", text=""):
    '''
    print the text file
    '''
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
    return num
