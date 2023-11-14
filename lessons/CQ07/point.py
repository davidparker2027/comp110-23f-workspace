"""CQ07."""

from __future__ import annotations


class Point:
    """Lil Docstring!"""
    # Attributes
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor is a real one."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Mutating Point!"""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creating a new point!"""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Lil Docstring CUh!"""
        stringed: str = f"x: {self.x}; y: {self.y}"
        return stringed
    
    def __mul__(self, factor: int | float) -> str:
        """Another Docstring Cuh!"""
        self.x *= factor
        self.y *= factor
        num: str = f"{self.x}, {self.y}"
        return num

    def __add__(self, value: int | float) -> Point:
        """The Last Docstring Cuhhhh!"""
        new_x = self.x + value
        new_y = self.y + value
        add_point = Point(new_x, new_y)
        return add_point