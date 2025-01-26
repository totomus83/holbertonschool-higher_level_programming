#!/usr/bin/python3
'''
the file 0-add_integer adds a and b if requirement are met
otherwise raise an error
'''


def add_integer(a, b=98):
    '''
    adds a and b they are int
    if they are a float that dont exceed valid range, convert float to int
    otherwise raise an error
    '''
    if isinstance(a, float):
        if a != a:
            raise ValueError("cannot convert float NaN to integer")
        if a < -1.7976931348623157e+308 or a > 1.7976931348623157e+308:
            raise OverflowError("cannot convert float infinity to integer")
        else:
            a = int(a)
    if isinstance(b, float):
        if b != b:
            raise ValueError("cannot convert float NaN to integer")
        if b < -1.7976931348623157e+308 or b > 1.7976931348623157e+308:
            raise OverflowError("cannot convert float infinity to integer")
        else:
            b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
