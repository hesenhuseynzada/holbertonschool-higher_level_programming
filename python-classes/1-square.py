#!/usr/bin/python3
"""A module that defines a square."""
class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the new square (no type/value verification).
        """
        self.__size = size
