#!/usr/bin/env python3
def print_last_digit(number):
    if number >= 0:
        last_int = number % 10
    else:
        last_int = (10 - number % 10)
    print(last_int, end='')
    return (last_int)
