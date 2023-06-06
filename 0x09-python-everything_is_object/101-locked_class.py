#!/usr/bin/python3
'''Defines  locked class'''


class LockedClass:
    '''Allows only an attribute known as first_name
    '''

    __slots__ = ["first_name"]
