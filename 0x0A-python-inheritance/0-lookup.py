#!/usr/bin/python3
'''
   The function returns the list of available attributes and methods
   of an object.
'''


def lookup(obj):
    ''' Retrieves the list of attributes and methods available for 
    the specified object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names available for the object.
     '''
    return dir(obj)
