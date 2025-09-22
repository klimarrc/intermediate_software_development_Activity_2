"""This module defines the Shape class."""

__author__ = "Kailine Lima"
__version__ = "1.0.0"

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes.

    args:
        color (str): The color of the shape.
    attributes:
        _color (str): The color of the shape. Protected attribute.
    methods:
        init__(color: str): Initializes the shape with a color.
        abstract area() -> float: Abstract method to compute the 
        area of the shape.
        abstract perimeter() -> float: Abstract method to compute 
        the perimeter of the shape.
        color() -> str: Accessor for the color of the shape.
    raises:
        ValueError: If the color is not a string.
    examples:
        >>> shape = Shape("red")
        >>> shape.color()
        'The color shape i red.'
    returns:
        Color shape is {color}.
    """
    

    def __init__(self, color: str):
        """Initialize the shape with a color.
        Args:
            color (str): The color shape. 
            Raises:
                ValueError: If the color cannot be blank."""
        if len(color.strip()) > 0:
            self._color = color
        else:
            raise ValueError("Color cannot be blank.")
    
    def __str__(self):
        """String returns the color shape."""

        return super().__str__(f"The color shape is {self._color}.\n")

    @abstractmethod
    def area(self) -> float:
        """Abstract method to compute the area of the shape."""
        pass
    @abstractmethod
    def perimeter(self) -> float:
        """Abstract method to compute the perimeter of the shape."""
        pass