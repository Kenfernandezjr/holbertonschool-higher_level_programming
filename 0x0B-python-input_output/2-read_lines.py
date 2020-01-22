#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding = "utf-8") as myFile:
        counter = 0

        for line in myFile:
            if nb_lines <= 0 or nb_lines >= counter:
                print(line, end="")
            counter += 1
