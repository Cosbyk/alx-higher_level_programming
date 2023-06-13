#!/usr/bin/python3
'''
The function that appends a string at the end of a text file (UTF8)
'''


def append_write(filename="", text=""):
    '''
    appends a string at the end of a text file (UTF8)
    '''
    with open(filename, "a", encoding="utf8") as file:
        file.seek(0, 2)
        num_chars = file.write(text)
    return num_chars
