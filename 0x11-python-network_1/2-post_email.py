#!/usr/bin/python3
"""take an url and email"""

from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    values = {
        'email': argv[2]
    }
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)

    with urllib.request.urlopen(req) as response:
        r = response.read()
        print(r.decode('utf-8'))
