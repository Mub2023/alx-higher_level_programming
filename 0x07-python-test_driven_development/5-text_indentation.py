#!/usr/bin/python3
"""
prints a text with 2 new lines after
each of these characters: . ? and :
text must be a string.
There should be no space at the beginning or at the end.
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after , ? :
    TEXT MUST BE STRING!!!!!.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    f = False
    for line in text:
        if f:
            f = False
            continue
        print(line, end="")
        if line == '.' or line == '?' or line == ':':
            print("\n")
            f = True
