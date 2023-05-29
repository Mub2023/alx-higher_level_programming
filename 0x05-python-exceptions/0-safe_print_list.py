#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for a in range(x):
        try:
            print(my_list[a], end="")
            c += 1
        except (IndexError, TypeError):
            break
    print()
    return (c)
