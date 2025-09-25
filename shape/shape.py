"""
This module defines the Shape class:
- Shape is an superclass for geometric shapes.
- It includes attribute color that represents string value.
- import ABC and abstractmethod from abc module.
- It has an abstract method calculate_area  and calculate_perimeter to 
compute the area of the shape in centimeters.
- It has a __str__ method that returns message "Color shape is {color}."
"""

__author__ = "Kailine Lima"
__version__ = "1.0.0"

from abc import ABC, abstractmethod


class Shape(ABC):
    """ class Shape is a Superclass for geometric shapes."""

    def __init__(self, color: str):
        """Initialize class attributes to correspond arguments values.

        Args:
            color (str): The color shape. 

        Raises:
                ValueError: when the color cannot be blank.
        """
        
        if len(color.strip()) > 0:
            self._color = color
        else:
            raise ValueError("Color cannot be blank.")

    def __str__(self) -> str:
        """String returns the color shape.
        
        Returns:
            str: A string representation of the color shape 
            with the message - "Color shape is {color}."
        """
        return (f"Color shape is {self._color}.")

    @abstractmethod
    def calculate_area(self) -> float:
        """Abstract method to compute the area of the shape in 
        centimeters.
        """
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """Abstract method to compute the perimeter of the shape 
        in centimeters.
        """

        pass
