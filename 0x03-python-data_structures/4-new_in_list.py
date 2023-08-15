#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = len(my_list)
    my_list_cpy = [i for i in my_list]

    if idx < 0 or idx > count-1:
        return my_list_cpy
    else:
        my_list_cpy[idx] = element
        return (my_list_cpy)
