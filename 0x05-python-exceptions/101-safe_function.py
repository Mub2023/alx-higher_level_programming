#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
            result = fct(*args)
            return result
    except Exception as d:
            print("Exception: {}".format(d), file=sys.stderr)
            return None
