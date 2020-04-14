#!/usr/bin/python3
""" script to get request """


import urllib.request
from sys import argv


with urllib.request.urlopen(argv[1]) as response:
    print(response.info().get('X-Request-Id'))
