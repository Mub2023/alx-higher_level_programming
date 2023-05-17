#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value or not a_dictionary:
        return (a_dictionary)
    for x in list(a_dictionary.keys()):
        if a_dictionary[x] == value:
            del a_dictionary[x]
    return (a_dictionary)
