#!/usr/bin/python3
'''
the text_indentation function prints a string
everytime it encounters ':', '?' or '.'
it prints 2 blank lines
'''


def text_indentation(text=None):
    '''
    prints a text with 2 blank lines after ., ? and :
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text is None:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ':.?':
            print("{}".format(text[i]), end='')
            print()
            print()
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        else:
            print("{}".format(text[i]), end='')
        i += 1
