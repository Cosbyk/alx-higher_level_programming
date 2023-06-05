#!/usr/bin/python3
'''Define rectangle class.'''


class Rectangle:
    '''Represent rectangle'''

    def __init__(self, width=0, height=0):
        ''''Initializes new rectangle.

        Args:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
        '''
        self._Rectangle_width = width
        self._Rectangle_height = height

    @property
    def width(self):
        '''Get width of rectangle'''
        return self._Rectangle_width

    @width.setter
    def width(self, value):
        '''Set width of rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle_width = value

    @property
    def height(self):
        '''Get height of rectangle'''
        return self._Rectangle_height

    @height.setter
    def height(self, value):
        '''Set height of rectangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle_height = value
