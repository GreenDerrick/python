#!/usr/bin/python3
def element_at(my_list, idx):
    count = len(my_list)
    if idx < 0 or idx > count:
        print("None")
    else:
        print("{}".format(my_list[idx]))
