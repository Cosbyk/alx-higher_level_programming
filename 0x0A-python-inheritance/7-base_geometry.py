#!/usr/bin/python3
'''
A function that defines a base geometry class
'''


class BaseGeometry:
    '''
    the class that represents a base geometry
    '''

    def area(self):
        '''
        method not yet implemented yet
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        verifies the value as an integer
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
