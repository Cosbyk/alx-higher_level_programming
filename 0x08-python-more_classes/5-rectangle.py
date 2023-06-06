#!/usr/bin/python3
'''Defines rectangle class'''


class Rectangle:
    '''Represent rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializes a rectangle
        Args:
            width (int): Width of rectangle
            height (int): Height of rectangle
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

    def area(self):
        '''Returns area of rectangle'''
        return self._Rectangle_width * self._Rectangle_height

    def perimeter(self):
        '''Returns perimeter of rectangle'''
        if self._Rectangle_width == 0 or self._Rectangle_height == 0:
            return 0
        return 2 * (self._Rectangle_width + self._Rectangle_height)

    def __str__(self):
        '''Returns reprresentation of rectangle

        # character to represent rectangle
        '''
        if self._Rectangle_width == 0 or self._Rectangle_height == 0:
            return ""

        rect = []
        for x in range(self._Rectangle_height):
            [rect.append("#") for y in range(self._Rectangle_width)]
            if x != self._Rectangle_height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        '''Return string representation rectangle'''
        rect = "Rectangle(" + str(self._Rectangle_width)
        rect += ", " + str(self._Rectangle_height) + ")"
        return rect

    def __del__(self):
        '''Print a message on deletion of rectangle.'''
        print("Bye rectangle...")
