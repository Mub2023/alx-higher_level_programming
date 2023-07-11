#!/usr/bin/python3
"""Reads from standard input and computes metrics.
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
def print_stats(size, s_codes):
    """Print accumulated metrics."""
    print("File size: {}".format(size))
    for key in sorted(s_codes):
        print("{}: {}".format(key, s_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    s_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if s_codes.get(line[-2], -1) == -1:
                        s_codes[line[-2]] = 1
                    else:
                        s_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, s_codes)

    except KeyboardInterrupt:
        print_stats(size, s_codes)
        raise
