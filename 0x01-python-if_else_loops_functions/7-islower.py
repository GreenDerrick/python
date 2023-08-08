#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if chr(i) == c:
            print("{} is lower".format(c))
