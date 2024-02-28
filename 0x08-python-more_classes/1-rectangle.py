#!/usr/bin/python3
"""This method defines the rectangle class"""


class Rectangle:
    """This class represents a rectangle."""

    def __init__(self, width = 0, height = 0):
        """Initializes the Rectangle instance.

        Args:
            width(int): The width of the rectangle.
            height(int): The height of the rectangle.

        Raises:
            TypeError: if width or height is not an integer.
            ValuError: if width or height is less than 0.
        """
        self.__width = width
        self.__height = height

    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            Value (int): The width of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValuError: if value or is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """Retrieve the height of the rectanlge."""
        return self.__height

    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            Value (int): The height of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValuError: if value or is less than 0.

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("heigh must be >= 0")
        self.__height = value
