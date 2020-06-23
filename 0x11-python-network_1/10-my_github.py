#!/usr/bin/python3
"""github credentials and displays your ID"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(argv[1], argv[2]))
    print(req.json().get('id'))
