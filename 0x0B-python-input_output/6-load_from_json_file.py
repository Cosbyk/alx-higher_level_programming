#!/usr/bin/python3
'''
a function that creates an Object from a JSON file
'''
import json


def load_from_json_file(filename):
    '''
    converts JSON file to a Python object
    '''
    with open(filename, "r") as file:
        my_obj = json.load(file)
    return my_obj
