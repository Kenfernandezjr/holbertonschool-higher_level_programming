#!/usr/bin/python3
"""script for URL and email"""


import requests
from sys import argv

if __name__ == "__main__":
    values = {
        'email': argv[2]
    }
    temp = requests.post(argv[1], data=values)
    print(temp.text)
