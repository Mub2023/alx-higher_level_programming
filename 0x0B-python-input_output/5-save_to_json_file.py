#!/usr/bin/python3
"""a function that writes an
Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to text file using json
    Args:
    my_obj: is the python object
    filename: is the txt file will be written in
    """
    load = json.dumps(my_obj)
    with open(filename, "w") as x:
        return x.write(load)
