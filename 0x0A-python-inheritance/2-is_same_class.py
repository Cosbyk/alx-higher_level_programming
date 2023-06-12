#!/usr/bin/python3
'''
Checks if object is an instance of a class
'''


def is_same_class(obj, a_class):
    '''
    If object is exactly an instance of the specified class
    it returns True, otherwise it returns false
    '''
    return (type(obj) == a_class)
