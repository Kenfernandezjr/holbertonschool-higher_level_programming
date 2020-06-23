#!/usr/bin/python3
"""Script to get error code"""

import urllib.request
from sys import argv


if __name__ == "__main__":

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as bad:
        print("Error code: {}".format(bad.code))
