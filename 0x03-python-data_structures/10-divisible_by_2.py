#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list_copy = [i for i in my_list]
    list1 = []
    for i in my_list_copy:
        if i % 2 == 0:
            list1.append(True)
        else:
            list1.append(False)
    return list1
