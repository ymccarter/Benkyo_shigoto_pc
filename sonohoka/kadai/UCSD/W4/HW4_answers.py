"""Homework 4 Answers for CSE-41273"""
# Your name Here
import math


class Person:
    """Person with first and last name."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        """Return first and last name together."""
        return f'{self.first_name} {self.last_name}'

    @property
    def name(self):
        """Return last_name, first_name with comma in one string"""
        return f'{self.last_name}, {self.first_name}'


class Point:
    """2-D Point objects."""

    def __init__(self, x=0, y=0):
        """Initialize the Point instance"""
        self.x = x
        self.y = y

    def __repr__(self):
        """Developer-friendly string representation"""
        return f'Point(x={self.x}, y={self.y})'

    def __str__(self):
        """Human-friendly string representation"""
        return f'Point at ({self.x}, {self.y})'

    @property
    def magnitude(self):
        """Return the magnitude of vector from (0,0) to self."""
        return math.sqrt(self.x ** 2 + self.y ** 2)
