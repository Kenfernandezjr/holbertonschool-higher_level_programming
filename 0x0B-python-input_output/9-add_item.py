#!/usr/bin/python3

from sys import argv

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

save_json = "add_item.json"

save_to_json_file(argv[1:], save_json)
