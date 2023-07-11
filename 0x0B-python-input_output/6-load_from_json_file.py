#!/usr/bin/python3
"""creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """loads from json file and create an
    python object
    Args:
    filename: the file name will be opened
    """
    with open(filename, "r") as x:
        return json.load(x)
