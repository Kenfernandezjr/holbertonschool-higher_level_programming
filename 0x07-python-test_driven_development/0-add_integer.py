#!/usr/bin/python3
def add_integer(a, b=98):

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    if type(a) is not int and float:
        raise TypeError("a must be an integer")
    if type(b) is not int and float:
        raise TypeError("b must be an integer")
    return a + b
