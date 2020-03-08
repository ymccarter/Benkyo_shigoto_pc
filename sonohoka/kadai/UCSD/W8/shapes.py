"""Python Fundamentals Final Project - shapes module."""
# Yukie McCarter
import math


class Point:
    """Two-Dimensional Point(x, y)"""

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

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    @property
    def magnitude(self):
        """Return the magnitude of vector from (0,0) to self."""
        return math.sqrt(self.x**2 + self.y**2)

    def distance(self, otherpoint):
        dx = self.x - otherpoint.x
        dy = self.y - otherpoint.y
        return math.sqrt(dx**2 + dy**2)

    @classmethod
    def from_tuple(cls, coords):
        if type(coords) == tuple:
            return (cls(*coords))

        else:
            raise TypeError

    def loc_from_tuple(self, coords):
        if type(coords) == tuple:
            self.x = coords[0]
            self.y = coords[1]
        else:
            raise TypeError


class Circle:
    """Circle(center, radius) where center is a Point instance"""

    def __init__(self, center=None, radius=1):
        """Initialize the instance"""
        if center is None:
            center = Point(0, 0)
        self.center = center
        self.radius = radius

    @classmethod
    def from_tuple(cls, center, radius=1):
        """Create a Circle instance, center input is an (x, y) tuple"""
        point = Point(*center)
        return cls(center=point, radius=radius)

    def center_from_tuple(self, center):
        self.center = Point(*center)

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius**2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, center):
        if not isinstance(center, Point):
            raise TypeError('The center must be a Point!')
        self._center = center

    @property
    def radius(self):
        """Return the actual radius value"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Set the radius value, checking validity and logging changes."""
        if radius < 0:
            raise ValueError("The radius cannot be negative!")
        self._radius = radius

    def __repr__(self):
        """Developer-friendly printing"""
        return f'Circle(center=Point{(self.center.x, self.center.y)}, ' \
            f'radius={self.radius})'

    def __str__(self):
        """User-friendly printing"""
        return f'Circle with center at {(self.center.x, self.center.y)} ' \
            f'and radius {self.radius}'

    def __add__(self, other):
        return Circle(self.center + other.center, self.radius + other.radius)

    def __iadd__(self, other):
        self.center += other.center
        self.radius += other.radius
        return self
