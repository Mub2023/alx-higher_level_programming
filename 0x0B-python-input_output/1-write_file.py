#!/usr/bin/python3
"""a medul that writes
a string to a text file (UTF8)
and returns the number of characters
written"""


def write_file(filename="", text=""):
    """a function that writes"""
    with open(filename, "w", encoding="utf8") as w:
        return w.write(text)
