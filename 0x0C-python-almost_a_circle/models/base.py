#!/usr/bin/python3
import json
""" Base Class Module """


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Json list_dictories """
        if list_dictionaries is None:
            return("[]".format())
        else:
            return json.dumps(list_dictionaries)
