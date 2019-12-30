#!/usr/bin/python3
def uppercase(str):
    converison = ''
    for i in (str):
        uppercase = ord(i)
        if uppercase >= ord('a') and uppercase <= ord('z'):
            uppercase = uppercase - 32
        converison += chr(uppercase)
    print("{:s}".format(converison))
