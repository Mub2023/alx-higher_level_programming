#!/usr/bin/python3
def magic_string(static={"c": 0}):
    static["c"] += 1
    return str("BestSchool, " * static["c"])[:-2]
