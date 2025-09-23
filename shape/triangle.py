"""This module defines the Triangle class."""

__author__ = "Kailine Lima" 
__version__ = "1.0.0"

from shape.shape import Shape


class Triangle(Shape):
    """ class Triangle is a subclass of super classShape for triangles."""

    def __init__(self, color: str, side_1: int, side_2: int, side_3: int,
        ):
        """Initialize the triangle with a color, base, height and sides.
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
            self._side_1 = side_1
        else:
            raise ValueError("Side 1 must be a number greater than zero.")