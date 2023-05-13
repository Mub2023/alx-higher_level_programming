#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for w in matrix:
            for c in w:
                print("{:d}".format(c), end=" " if c != w[-1] else "")
            print()
