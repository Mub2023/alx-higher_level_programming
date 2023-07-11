#!/usr/bin/python3
"""inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file,"""
    new = ""
    with open(filename) as x:
        for i in x:
            new += i
            if search_string in i:
                new += new_string
    with open(filename, "w") as wi:
        wi.write(new)
