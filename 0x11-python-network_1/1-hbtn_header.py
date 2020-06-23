#!/usr/bin/python3
""" script to get X-request-id  """

import urllib.request
from sys import argv


with urllib.request.urlopen(argv[1]) as response:
    r = response.info()
    print(r.get('X-Request-Id'))
