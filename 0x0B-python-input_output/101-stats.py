#!/usr/bin/python3
"""Reads from standard input and computes metrics.
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, Scode):
    """Print accumulated metrics."""
    print("File size: {}".format(size))
    for k in sorted(Scode):
        print("{}: {}".format(k, Scode[k]))


if __name__ == "__main__":
    import sys

    size = 0
    Scode = {}
    known_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    ct = 0

    try:
        for line in sys.stdin:
            if ct == 10:
                print_stats(size, Scode)
                ct = 1
            else:
                ct += 1

            line = line.split()

            try:
                size += int(line[-1])
            except(IndexError, ValueError):
                pass
            try:
                if line[-2] in known_codes:
                    if Scode.get(line[-2], -1) == -1:
                        Scode[line[-2]] = 1
                    else:
                        Scode[line[-2]] += 1
            except IndexError:
                pass
        print_stats(size, Scode)

    except KeyboardInterrupt:
        print_stats(size, Scode)
        raise
