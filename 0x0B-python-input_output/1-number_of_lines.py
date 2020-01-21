#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding="utf-8") as myFile:

        lineNumber = 1

        while True:

            line = myFile.readlines()

            if not line:
                break

            for x in line:
                lineNumber += 1
            return lineNumber
