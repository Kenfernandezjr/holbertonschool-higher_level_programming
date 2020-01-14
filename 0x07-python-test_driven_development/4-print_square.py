#!/usr/bin/python3
def print_square(size):

    if size is None:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if int(size) is float and size < O:
        raise TypeError("size must be an integer")

    for col in range(size):
        for row in range(size):
            print("#", end="")
        print("")
