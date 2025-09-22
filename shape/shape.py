"""This module defines the Shape class."""

__author__ = "Kailine Lima"
__version__ = "1.0.0"

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes.

    args:
        color (str): The color of the shape.
    attributes:
        _color (str): The color of the shape.
    methods:
        color() -> str: Accessor for the color of the shape.
    """
    

    def __init__(self, color: str):
        """Initialize the shape with a color."""
        if isinstance(color, str):
            self._color = color
        else:
            raise ValueError("Color cannot be blank.")

    
    def color(self) -> str:
        """Accessor for the color of the shape."""
        return (f"The color shape is {self._color}.\n")
    
    @abstractmethod
    def area(self) -> float:
        """Abstract method to compute the area of the shape."""
        pass
    @abstractmethod
    def perimeter(self) -> float:
        """Abstract method to compute the perimeter of the shape."""
        pass