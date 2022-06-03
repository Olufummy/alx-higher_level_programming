#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    count = 0
    if length == 1:
        print("{}".format(count))
    else:
        for i in range(1, length):
            count = count + int(argv[i])
        print(count)
