#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    count = len(tuple_a)
    count1 = len(tuple_b)
    if count < 2:
        if count == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if count1 < 2:
        if count1 == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    final_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (final_tuple)
