#!/usr/bin/python3
'''
the function defines a class Student
'''


class Student:
    '''
    Represent Student
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Creates new student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        representation of student
        '''
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict
