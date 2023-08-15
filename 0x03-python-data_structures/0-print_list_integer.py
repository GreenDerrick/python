#!/usr/bin/python3
def print_list_integer(my_list=[]):
    count = 0
    i = len(my_list)
    while count < i:
        print(f"{}".format(my_list[count]))
        count += 1
