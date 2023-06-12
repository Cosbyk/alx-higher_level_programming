#!/usr/bin/python3
''' 
This class "MyList" inherits from "list".
'''


class MyList(list):
    '''
    A class that inherits from the built-in list.

    Methods:
        print_sorted(): Prints the elements of the list in sorted order.
    '''
    def print_sorted(self):
        '''
        Prints the elements of the list in sorted order.

        The list is sorted in ascending order then the sorted result 
        is printed to the console.
        '''
        print(sorted(self))
