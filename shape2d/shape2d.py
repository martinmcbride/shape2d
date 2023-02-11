# Author:  Martin McBride
# Created: 2023-02-06
# Copyright (C) 2023, Martin McBride
# License: MIT
import math

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    """
    Check if two values a and b are equal to within a given tolerance
    :param a:
    :param b:
    :param rel_tol: Tolerance as a fraction of the absolute value of a or b (whichever is largest)
    :param abs_tol: Tolerance as an absolute value
    :return:
    """
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


class Vector(object):
    """
    Class to represent a 2-vector including most of its common operations
    This is based on easy_vector https://github.com/DariusMontez/easy_vector
    The main changes are to make the object immutable, and measuring angle sin radians rather than degrees
    """

    @staticmethod
    def polar(length, angle):
        """
        Create a vector based on a length and ag;e
        :param length: Lengh of vector
        :param angle: Angle in radians, measured counterclockwise from positive x direction
        :return: New vecto
        """
        x = length * math.cos(angle)
        y = length * math.sin(angle)
        return Vector(x, y)

    def __init__(self, *args):
        # first arg may be an iterable (list, tuple, etc...)
        if len(args) == 1 and hasattr(args[0], "__iter__") and len(args[0]) == 2:
            self.coords = tuple(args[0])
        elif len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
            self.coords = tuple(args)
        else:
            raise ValueError("Vector requires a sequence of length 2, or 2 numbers")

    def __iter__(self):
        return iter(self.coords)

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, index):
        return self.coords[index]

    def __eq__(self, other):
        return isclose(self.x, other.x) and isclose(self.y, other.y)

    def __neg__(self):
        return self * -1

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # add the negative of `other`
        return self + (-other)

    def __mul__(self, other):

        # vector * scalar
        if isinstance(other, (int, float)):
            return Vector(other * self.x, other * self.y)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):

        # vector / scalar
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        else:
            return NotImplemented

    def __floordiv__(self, other):

        # vector / scalar
        if isinstance(other, (int, float)):
            return Vector(self.x // other, self.y // other)
        else:
            return NotImplemented


    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]

    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    @property
    def angle(self):
        angle = math.atan2(self.y, self.x)
        return angle

    @property
    def unit(self):
        return self / self.length

    # String representation
    def __str__(self):
        return "Vector({0:.3f}, {1:.3f})".format(self.x, self.y)

    def __repr__(self):
        return "Vector({0}, {1})".format(self.x, self.y)
