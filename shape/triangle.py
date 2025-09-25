"""This module defines the Triangle class.
- The Triangle class is a subclass of Shape.
- It represents a triangle with a color and three sides.
- It includes super() to call the constructor of the Shape class.
- It includes methods to calculate area and perimeter.
- The class ensures that the sides satisfy the Triangle Inequality 
Theorem.
"""

__author__ = "Kailine Lima"
__version__ = "1.0.0"

import math
from shape.shape import Shape


class Triangle(Shape):
    """  The class Triangle is a subclass that is created by inheriting 
    from super class Shape.
    Attributes:
        color (str): The color shape.
        side_1 (int): The length of side 1 of the triangle in centimeters.
        side_2 (int): The length of side 2 of the triangle in centimeters.
        side_3 (int): The length of side 3 of the triangle in centimeters.
    """

    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        """Initialize the triangle with a color and three sides.

        Args:
            color (str): The color shape. 
            side_1 (int): The length of side 1 of the triangle in centimeters.
            side_2 (int): The length of side 2 of the triangle in centimeters.
            side_3 (int): The length of side 3 of the triangle in centimeters.
        Raises:
                ValueError: when the color cannot be blank,
                when side_1 must be numeric.
                when    side_2 must be numeric.
                when    side_3 must be numeric.
        """
        super().__init__(color)
        if isinstance(side_1, int):
            self.__side_1 = side_1
        else:
            raise ValueError("Side 1 must be numeric.")
        if isinstance(side_2, int):
            self.__side_2 = side_2
        else:
            raise ValueError("Side 2 must be numeric.")
        if isinstance(side_3, int):
            self.__side_3 = side_3
        else:
            raise ValueError("Side 3 must be numeric.")

        Triangle_Inequality_Theorem = (side_1 + side_2 > side_3 and
                                       side_1 + side_3 > side_2 and
                                       side_2 + side_3 > side_1)

        if (Triangle_Inequality_Theorem):
            self.__side_1 = side_1
            self.__side_2 = side_2
            self.__side_3 = side_3
        else:
            raise ValueError("The sides do not satisfy the Triangle "
                             "Inequality Theorem")

    def __str__(self) -> str:
        """
        String returns the color shape and the sides of the triangle.
        Returns:
            str: The shape color is {color}.
            This triangle has three sides with lengths of {side_1}, 
            {side_2} and {side_3} centimeters.
        """
        shape_string = super().__str__()
        triangle_string = (f"This triangle has three sides with lengths "
                           f"of {self.__side_1}, {self.__side_2} and "
                           f"{self.__side_3} centimeters.")

        return (shape_string + "\n" + triangle_string)

    def calculate_area(self) -> float:
        """
        Calculates the area of the triangle using Heron's formula.

        Returns:
            float: The area of the triangle in square centimeters.
        """
        sp = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        area = math.sqrt(sp * (sp - self.__side_1) * (sp - self.__side_2) *
                         (sp - self.__side_3))
        return area

    def calculate_perimeter(self) -> float:
        """
        Calculates the perimeter of the triangle.

        Returns:
            float: The perimeter of the triangle in centimeters.
        """
        perimeter = self.__side_1 + self.__side_2 + self.__side_3
        return perimeter
