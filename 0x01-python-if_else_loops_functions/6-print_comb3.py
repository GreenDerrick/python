#!/usr/bin/python3
for i in range(00, 90):
    if i < 89:
        print("{:02d}".format(i), end=(', '))
    else:
        print("{}".format(i))
