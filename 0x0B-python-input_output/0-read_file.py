#!/usr/bin/python3
"""a medul that reads a
text file (UTF8) and
prints it to stdout:"""


def read_file(filename=""):
    """open a file wth UTF8 and
    prints it to stdout"""
    with open(filename, encoding="utf8") as x:
        string = x.read()
        print(string, end="")
