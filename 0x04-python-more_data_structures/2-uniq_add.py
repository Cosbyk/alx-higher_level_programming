#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_ints = set(my_list)
    for x in my_list:
        if isinstance(x, int):
            unique_ints.add(x)
    result = sum(unique_ints)
    return result
