#!/usr/bin/python3
number1 = 0
number2 = 1
for number1 in range(10):
    for number2 in range(number1 + 1, 10):
        if number1 == 8 and number2 == 9:
            print("{:01}{:01}".format(number1, number2), end="")
        else:
            print("{:01}{:01}".format(number1, number2), end=", ")
