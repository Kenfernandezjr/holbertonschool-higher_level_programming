#!/usr/bin/python3
"""Repo name and owner name, lists the last 10 commits by owner"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2],
                                                              argv[1])
    req = requests.get(url)
    com_list = req.json()
    com_dict = {}
    for coms in com_list:
        date = coms.get('commit').get('author').get('date')
        sha = coms.get('sha')
        name = coms.get('commit').get('author').get('name')
        com_dict.update({date: {'sha': sha, 'name': name}})
    i = 0
    for k in sorted(com_dict.keys(), reverse=True):
        if i < 10:
            print("{}: {}".format(com_dict.get(k).get('sha'),
                                  com_dict.get(k).get('name')))
        i += 1
