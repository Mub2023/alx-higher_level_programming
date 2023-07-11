#!/usr/bin/python3
"""Reads from standard input and computes metrics.
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
from collections import Counter


MAX_LINES = 10

def print_stats(size, status_codes):
    """Print accumulated metrics."""
    print(f"File size: {size}")
    for k in sorted(status_codes):
        print(f"{k}: {status_codes[k]}")


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = Counter()
    ct = 0

    with sys.stdin as f:
        try:
            for line in f:
                if ct == MAX_LINES:
                    print_stats(size, status_codes)
                    ct = 0
                ct += 1

                line = line.split()

                try:
                    size += int(line[-1])
                    status_codes[line[-2]] += 1
                except (IndexError, ValueError):
                    pass
            else:
                print_stats(size, status_codes)

        except KeyboardInterrupt:
            print_stats(size, status_codes)
            raise
