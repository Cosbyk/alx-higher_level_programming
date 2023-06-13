#!/usr/bin/python3
'''
A Function that writes an Object to text file using JSON file-writing function
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    writes an Object to a text file, using a JSON representation
    '''
    with open(filename, "w") as file:
        json.dump(my_obj, file)
