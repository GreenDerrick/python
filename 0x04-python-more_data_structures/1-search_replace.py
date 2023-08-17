#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_last = my_list.copy()
    for idx, item in enumerate(list_last):
        if item == search:
            list_last[idx] = replace
    return list_last
