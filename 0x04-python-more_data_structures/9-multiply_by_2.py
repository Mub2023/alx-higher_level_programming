#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult2 = a_dictionary.copy()
    keys = list(mult2.keys())
    for x in keys:
        mult2[x] *= 2
    return mult2
