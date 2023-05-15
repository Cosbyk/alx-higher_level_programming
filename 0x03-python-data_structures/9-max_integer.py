#!/usr/bin/python3

def max_integer(my_list=[]):
    '''finds the biggest integer of a list'''
    if not my_list:
        return None

    bigst_int = my_list[0]

    for x in my_list[1:]:
        if x > bigst_int:
            bigst_int = x

    return bigst_int
