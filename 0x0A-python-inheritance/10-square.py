#!/usr/bin/python3
'''
Defines subclass Square of class Rectangle.
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Represent a class square
    '''

    def __init__(self, size):
        '''
        Constructs a new square
        '''
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
