#!/usr/bin/python3
"""This module defines the class Square"""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2
