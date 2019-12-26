#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    if len(argv[1:]) == 0:
        print("0 arguments.".format(len(argv)))

    elif len(argv[2:]) == 1:
        print("1 argument:")
        print("1: {}".format(argv))

    else:
        print("{:d} arguments:".format(len(argv[1:])))

    for x in (argv[1:]):
        print("{:d}: {}".format(argv.index(x), x))
