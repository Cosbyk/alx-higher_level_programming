#!/usr/bin/python3
'''
A class that defines a class Student
'''


class Student:
    '''
    Represents the student.'''

    def __init__(self, first_name, last_name, age):
        '''Initializes the Student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        json_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return json_dict
