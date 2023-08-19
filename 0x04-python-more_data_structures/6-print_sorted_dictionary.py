#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    srt = sorted(a_dictionary)
    for i in srt:
        print("{}: {}".format(i, a_dictionary.get(i)))
