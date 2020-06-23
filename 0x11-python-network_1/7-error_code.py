#!/usr/bin/python3
"""Displays body or error code"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    red = requests.get(url)
    if red.status_code == 200:
        print(red.text)
    else:
        print('Error code: {}'.format(red.status_code))
