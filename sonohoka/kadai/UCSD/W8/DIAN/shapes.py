"""Shapes for Python Fundamentals Final Answers"""
import math


class Point:
    """Two-Dimensional Point(x, y)"""

    def __init__(self, x=0, y=0):
        """Create a Point instance given x and y location"""
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords):
        """Create a Point from tuple (x,y)"""
        return cls(*coords)

    def __str__(self):
        """Return human-friendly string of Point"""
        return "Point at ({}, {})".format(self.x, self.y)

    def __repr__(self):
        """Return dev-readable representation of Point."""
        return "Point(x={}, y={})".format(self.x, self.y)

    @property
    def magnitude(self):
        """Pretend it is a vector, return magnitude"""
        return math.sqrt(self.x**2 + self.y**2)

    def distance(self, other):
        """Return distance between two points."""
        xd, yd = self.x-other.x, self.y-other.y
        return math.sqrt(xd**2 + yd**2)

    def __add__(self, other):
        """Return copy of our point, shifted by other point."""
        return Point(self.x+other.x, self.y+other.y)

    # Python "works" without this, because it can extrapolate from __add__,
    # but this is a more correct mutating version.
    def __iadd__(self, other):
        """Shift self by the value of the other point, using +=."""
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, value):
        """Return new copy of our point, scaled by given value."""
        return Point(value*self.x, value*self.y)

    def __rmul__(self, value):
        """Return new copy of our point, scaled by given value."""
        return self.__mul__(value)

    # Python "works" without this, because it can extrapolate from __mul__,
    # but this is a more correct/efficient mutating version.
    def __imul__(self, value):
        """"Mutating multiply of self and value."""
        self.x *= value
        self.y *= value
        return self

    def __iter__(self):
        """Allow Point objects to be iterable"""
        yield self.x
        yield self.y
        # Or, you could also do:
        # return iter([self.x, self.y])

    def loc_from_tuple(self, coords):
        """Modify Point location from tuple (x,y)"""
        self.x, self.y = coords


class Circle:
    """Circle(center, radius) where center is a Point instance"""

    def __init__(self, center=None, radius=1):
        """Create a Circle instance, center must be a Point instance"""
        if center is None:
            center = Point()
        self.center = center
        self.radius = radius

    @classmethod
    def from_tuple(cls, center, radius=1):
        """Create a Circle instance, center input is an (x, y) tuple"""
        point = Point(*center)
        # Using "cls" is best practices.
        return cls(center=point, radius=radius)

    def __str__(self):
        """People-friendly Circle stringify"""
        return "Circle with center at ({}, {}) and radius {}".format(
            self.center.x, self.center.y, self.radius
        )

    def __repr__(self):
        """Developer-friendly Circle stringify"""
        return "Circle(center=Point({}, {}), radius={})".format(
            self.center.x, self.center.y, self.radius
        )

    @property
    def radius(self):
        """Return radius of circle"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Set radius of circle. Raises ValueError if negative"""
        if radius < 0:
            raise ValueError("The radius cannot be negative!")
        self._radius = radius

    @property
    def diameter(self):
        """Return diameter of circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set radius based on new diameter"""
        self.radius = diameter / 2

    @property
    def area(self):
        """Return area of circle"""
        return math.pi * self.radius ** 2

    @property
    def center(self):
        """Return center Point of circle """
        return self._center

    @center.setter
    def center(self, center):
        """Set new center of Circle. Raises error if not a Point"""
        if not isinstance(center, Point):
            raise TypeError("The center must be a Point!")
        self._center = center

    def __add__(self, other):
        """Create a new Circe by adding self to another Circle"""
        return Circle(
            center=self.center+other.center,
            radius=self.radius+other.radius
        )

    # Python "works" without this, because it can extrapolate from __add__,
    # but this is a more correct mutating version.
    def __iadd__(self, other):
        """Modify self, adding other to self"""
        self.center += other.center
        self.radius += other.radius
        return self

    def center_from_tuple(self, center):
        """Set new center of Circle from (x, y) tuple"""
        self.center = Point(*center)
