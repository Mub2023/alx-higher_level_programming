#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value or not a_dictionary:
        return (a_dictionary)
    new = a_dictionary.copy()
    for x in list(new.keys()):
        if a_dictionary[x] == value:
            del a_dictionary[x]
    return (new)
