#!/usr/bin/python3
"""
7-base_geometry.py Module
"""


class BaseGeometry:
    """
    class
    """
    def area(self):
        """
        public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
