#!/usr/bin/python3

from sys import argv

if __name__ =="__main__":

    addition = 0

    for i in range(len(argv[1:])):
        addition += int(argv[i])
    print("{:d}".format(addition))
