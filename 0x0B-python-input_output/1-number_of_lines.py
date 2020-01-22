#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding="utf-8") as myFile:

        lineNumber = 0
        line = myFile.readlines()
        for x in line:
            lineNumber += 1
        return lineNumber
