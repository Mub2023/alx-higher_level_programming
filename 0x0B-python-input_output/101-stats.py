#!/usr/bin/python3
"""Reads from standard input and computes metrics.
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
from collections import Counter


def print_stats(size, Scode):
    """Print accumulated metrics."""
    print("File size: {}".format(size))
    for k in sorted(Scode):
        print("{}: {}".format(k, Scode[k]))


if __name__ == "__main__":
    import sys

    size = 0
    Scode = Counter()
    ct = 0

    with sys.stdin as f:
        try:
            for line in f:
                if ct == 10:
                    print_stats(size, Scode)
                    ct = 0
                ct += 1

                line = line.split()

                try:
                    size += int(line[-1])
                    Scode[line[-2]] += 1
                except (IndexError, ValueError):
                    pass
            print_stats(size, Scode)

        except KeyboardInterrupt:
            print_stats(size, Scode)
            raise
