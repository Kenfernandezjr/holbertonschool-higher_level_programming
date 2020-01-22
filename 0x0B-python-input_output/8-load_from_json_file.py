#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, 'r') as load_file:
        return json.loads(load_file.read())
