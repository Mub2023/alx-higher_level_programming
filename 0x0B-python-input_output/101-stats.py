#!/usr/bin/python3
"""a script that reads stdin
line by line and computes metrics"""
import sys


def print_stat(size, known_codes):
    """print the stats of size and status"""
    print("File size: {}".format(size))
    for x, v in sorted(known_codes.items()):
        if v != 0:
            print("{}: {}".format(x, v))


size = 0
known_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
it = 0

try:
    for wi in sys.stdin:
        it += 1
        wi = wi.split()
        if len(wi) >= 2:
            temp = it
            if wi[-2] in known_codes:
                known_codes[wi[-2]] += 1
                it += 1
            try:
                size += int(wi[-1])
                if temp == it:
                    it += 1
            except IndexError:
                pass
        if it % 10 == 0:
            print_stat(size, known_codes)

    print_stat(size, known_codes)
except KeyboardInterrupt:
    print_stat(size, known_codes)
