#!/usr/bin/python3
"""Script to get error code"""

import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            r = response.read()
            print(r.decode('utf-8'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
