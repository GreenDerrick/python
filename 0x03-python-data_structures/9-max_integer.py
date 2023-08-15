#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = None
    count = len(my_list)
    if my_list == []:
        return biggest
    elif count < 2:
        biggest = my_list[-1]
        return biggest
    else:
        biggest = my_list[0]
        idx = 0
        while idx <= count - 1:
            if my_list[idx] > biggest:
                biggest = my_list[idx]
                idx += 1
            else:
                idx += 1
                continue
        return biggest
