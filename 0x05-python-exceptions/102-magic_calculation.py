#!/usr/bin/python3
def magic_calculation(a, b):
    import sys
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
                result += a ** b / i
        except Exception as w:
            print("Exception: {}".format(w), file=sys.stderr)
            b += a
            break
    return result

