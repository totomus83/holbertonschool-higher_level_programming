#!/usr/bin/python3
number = 0
for number in range(100):
    if number == 99:
        print("{:02}".format(number))
    else:
        print("{:02}".format(number), end=", ")
