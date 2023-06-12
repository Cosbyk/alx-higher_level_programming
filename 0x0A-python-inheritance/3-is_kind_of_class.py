#!/usr/bin/python3
'''
A function that checks if object is an instance of or if
an object is an instance of a class that inherited from
specified class.
'''


def is_kind_of_class(obj, a_class):
    '''
    returns true if object is an instance of a specified
    class or of class of inherited from the same
    '''
    return (isinstance(obj, a_class))
