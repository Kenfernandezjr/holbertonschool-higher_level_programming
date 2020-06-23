#!/usr/bin/python3
"""take an url and email"""

from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(argv[1], data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
