#!/usr/bin/python3
"""This module defines the class Square"""

class Square:
    """This class represents a square."""

    def __init__(self, size):
        """Initialize the Square instance.

        Args:
            size (int): The size of the square.

        Note:
            No type or value verification is performed.
        """

        self.__size = size
