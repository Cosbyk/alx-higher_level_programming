#!/usr/bin/python3
'''
 A class "Rectangle" that inherits from "BaseGeometry".
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    The class represents  rectangle with BaseGeometry
    '''

    def __init__(self, width, height):
        '''
        Construct new rectangle
        '''

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        '''
        Returns area of rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Prints the print() and returns str() representation 
        of a Rectangle.
        '''
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
