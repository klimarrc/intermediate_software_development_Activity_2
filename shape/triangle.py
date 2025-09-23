"""This module defines the Triangle class."""

__author__ = "Kailine Lima" 
__version__ = "1.0.0"

from shape.shape import Shape


class Triangle(Shape):
    """ class Triangle is a subclass of super classShape for triangles."""
    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        
        """
        Initialize the triangle with a color, base, height and sides.

        Args:
            color (str): The color shape. 
            side_1 (int): The length of side 1 of the triangle in centimeters.
            side_2 (int): The length of side 2 of the triangle in centimeters.
            side_3 (int): The length of side 3 of the triangle in centimeters.
        Raises:
                ValueError: when the color cannot be blank,
                when side_1 is not numeric.
                when side_2 is not numeric.
                when side_3 is not numeric.
        """

        super().__init__(color)
        if isinstance(side_1, (int)):
            self.__side_1 = side_1
        else:
            raise ValueError("Side 1 must be numeric.")
        if isinstance(side_2, (int)):
            self.__side_2 = side_2
        else:
            raise ValueError("Side 2 must be numeric.")
        if isinstance(side_3, (int)):
            self.__side_3 = side_3
        else:
            raise ValueError("Side 3 must be numeric.")

        if (self.__side_1 + self.__side_2 > self.__side_3 and
            self.__side_1 + self.__side_3 > self.__side_2 and
            self.__side_2 + self.__side_3 > self.__side_1):
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

        return (f"The shape color is {self._color}.\n"
                    f"This triangle has three sides with lengths "
                    f"of {self.__side_1}, {self.__side_2} and "
                    f"{self.__side_3} centimeters.")


        
    
    def area(self) -> float:
        """
        Calculates the area of the triangle using Heron's formula.

        Returns:
            float: The area of the triangle in square centimeters.
        """
        sp = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        area = (sp * (sp - self.__side_1) * (sp - self.__side_2) * 
                (sp - self.__side_3))
        return area
    
    # Removed undefined decorator
    def perimeter(self) -> float:
        """
        Calculates the perimeter of the triangle.

        Returns:
            float: The perimeter of the triangle in centimeters.
        """
        perimeter = self.__side_1 + self.__side_2 + self.__side_3
        return perimeter