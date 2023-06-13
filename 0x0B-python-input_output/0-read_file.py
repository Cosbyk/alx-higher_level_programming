#!/usr/bin/python3
'''
This function reads a text file.
'''


def read_file(filename=""):
    '''
    Prints out the contents of (UTF8) file.
    '''
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            print(line, end="")
