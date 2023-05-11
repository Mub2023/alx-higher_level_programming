#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    mysum = 0
    for x in range(len(sys.argv) - 1):
        mysum += int(sys.argv[x + 1])

    print("{}".format(mysum))
