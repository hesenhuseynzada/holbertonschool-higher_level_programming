#!/usr/bin/python3
"""Defines an empty Rectangle class."""

class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height


    def width(self):
        return self.__width


    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be a non-negative integer")
        self.__width = value


    def height(self):
        return self.__height


    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be a non-negative integer")
        self.__height = value
