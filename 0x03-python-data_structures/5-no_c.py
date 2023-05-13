#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            string += x
    return (string)
