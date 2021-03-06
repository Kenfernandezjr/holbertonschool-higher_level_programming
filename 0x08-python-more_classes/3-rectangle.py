#!/usr/bin/python3
class Rectangle:

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __str__(self):

        string1 = ""

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                string1 += "#"
            string1 += "\n"
        return string1[:-1]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self, value):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        ar = self.__width * self.__height
        return ar

    def perimeter(self):

        if self.__width or self.__height == 0:
            perimeter = 0

        pmtr = self.__width + self.__height + self.__width + self.__height

        return pmtr
