#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''a function that finds all multiples of 2 in a list'''
    list_2 = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            list_2.append(True)
        else:
            list_2.append(False)
    return list_2
