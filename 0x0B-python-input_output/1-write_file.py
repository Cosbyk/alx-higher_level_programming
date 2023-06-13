#!/usr/bin/python3
'''
The function writes a string to a text file (UTF8)
'''


def write_file(filename="", text=""):
    '''
    Writes string to (UTF8) file
    '''
    with open(filename, "w", encoding="utf8") as file:
        num_chars = file.write(text)
    return num_chars
