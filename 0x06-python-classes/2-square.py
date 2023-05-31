#!/usr/bin/python3
"""Class implementation for squares."""


class Square:
    """Define a class of square."""

    def __init__(self, size=0):
        """Load a new Square instance.

        Args:
            size (int): Size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
