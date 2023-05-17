#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_number = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D': 500, 'M' : 1000}
    res = 0
    for x in range(len(roman_string)):
        if x > 0 and roman_number[roman_string[x]] > roman_number[roman_string[x - 1]]:
            res += roman_number[roman_string[x]] - 2 * roman_number[roman_string[x - 1]]
        else:
            res += roman_number[roman_string[x]]
    return res
