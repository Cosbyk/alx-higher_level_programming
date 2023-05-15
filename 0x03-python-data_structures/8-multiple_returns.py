#!/usr/bin/python3

def multiple_returns(sentence):
    '''returns a tuple with the length of a string and its first character'''
    tuple_x = ()
    if len(sentence) == 0:
        tuple_x = 0
    else:
        tuple_x = len(sentence), sentence[0]
    return tuple_x
