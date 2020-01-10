#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        ar = self.__size * self.__size
        return ar

    def my_print(self):
        for s in range(self.size):
            for y in range(self.size):
                print('#', end='')
            print()

        if self.size == 0:
            print()
