#!/usr/bin/python3
import hidden_4 as hidden
if __name__ == "__main__":
    for Name in dir(hidden):
        if Name[:2] != '__':
            print('{}'.format(Name))
