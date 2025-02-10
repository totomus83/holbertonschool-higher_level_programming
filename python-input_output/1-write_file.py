#!/usr/bin/python3
'''
this function print the content
'''


def write_file(filename="", text=""):
    '''
    print the text file
    '''
    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
    return num
