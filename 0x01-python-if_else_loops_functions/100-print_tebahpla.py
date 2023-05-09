#!/usr/bin/python3
x = 0
for y in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(y - x)), end="")
    x = 32 if x == 0 else 0
