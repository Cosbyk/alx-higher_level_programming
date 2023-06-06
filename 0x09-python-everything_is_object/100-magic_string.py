#!/usr/bin/python3
def magic_string():
    magic_string.number = getattr(magic_string, 'number', 0) + 1
    return ', '.join(['BestSchool' for i in range(magic_string.number)])
