""" Homework assignment answers for week 5 """
import math
from functools import total_ordering


class Circle:
    """Class to create Circle objects"""

    def __init__(self, radius=1):
        """Initialize the instance"""
        self.radius_log = []
        self.radius = radius

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2

    @property
    def radius(self):
        """Return the actual radius value"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Set the radius value, checking validity and logging changes."""
        if radius < 0:
            raise ValueError("Radius cannot be negative!")
        self.radius_log.append(radius)
        self._radius = radius

    def __repr__(self):
        """Developer-friendly printing"""
        return f"Circle(radius={self.radius})"

    def __str__(self):
        """User-friendly printing"""
        return f"Circle of radius {self.radius}"


@total_ordering
class BankAccount:
    """ Simple BankAccount class """

    def __init__(self, balance=0):
        """Initialize account with balance"""
        self.balance = balance

    def deposit(self, amount):
        """Deposit amount to this instance"""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw amount from this instance"""
        self.balance -= amount

    def __str__(self):
        """User-friendly printing"""
        return f"Account with balance of ${self.balance}"

    def __repr__(self):
        """Developer-friendly printing"""
        return f"BankAccount(balance={self.balance})"

    def __eq__(self, rhs):
        """Implement equality comparison"""
        return self.balance == rhs.balance

    def __lt__(self, rhs):
        """Implement less than comparison"""
        return self.balance < rhs.balance

    def __bool__(self):
        """ Instance is truthy if balance is greater than zero"""
        return self.balance > 0
