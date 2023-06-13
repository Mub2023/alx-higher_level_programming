#!/usr/bin/python3
"""appends a string at the end of
a text file (UTF8)and returns
the number of characters added:"""


def append_write(filename="", text=""):
    """a function that appends a string
    to the end of file """
    with open(filename, mode="a", encoding="utf8") as wi:
        return wi.write(text)
