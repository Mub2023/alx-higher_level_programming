#!/usr/bin/python3
"""a script that reads stdin
line by line and computes metrics"""
import sys


def print_stat(size, status_code):
    """print the stats of size and status"""
    print("File size: {}".format(size))
    for x in sorted(status_code):
        print("{}: {}".format(key, status_code[x]))
if __name__ == "__main__":

    size = 0
    status_code = {}
    known_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    cn = 0

    try:
        for wi in sys.stdin:
            if cn == 10:
                print_stat(size, status_code)
                cn = 1
            else:
                cn += 1
            wi = wi.split()
            try:
                size += int(wi[-1])
            except (IndexError, ValueError):
                pass
            try:
                if wi[-2] in known_codes:
                    if status_code.get(wi[-2], 0) == 0:
                        status_code[wi[-2]] = 1
                    else:
                        status_code[wi[-2]] += 1
            except IndexError:
                pass

        print_stat(size, status_code)
    except KeyboardInterrupt:
        print_stat(size, status_code)
        raise
