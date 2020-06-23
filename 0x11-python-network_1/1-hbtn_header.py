#!/usr/bin/python3
""" script to get X-request-id """

from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        r = response.info()
        print(r.get('X-Request-Id'))
