"""
This module defines the Rectangle class.
- The Rectangle class is a subclass of Shape.
- It represents a rectangle with a color, four sides length, and width.
- It includes methods to calculate area and perimeter.
- The class ensures that length and width are numeric values.

"""

__author__ = "Kailine Lima"
__version__ = "1.0.0"


from shape.shape import Shape


class Rectangle(Shape):
    """ The class Rectangle is a subclass that is created by inheriting 
    from super class Shape.

    """

    def __init__(self, color: str, length: int, width: int):
        """
        Initialize the rectangle with a color, length and width.

        Args:
            color (str): The color shape. 
            length (int): The length of the rectangle in centimeters.
            width (int): The width of the rectangle in centimeters.
        Raises:
                ValueError: when the color cannot be blank,
                when length must be numeric.
                when width must be numeric.
        """

        super().__init__(color)
        if isinstance(length, int):
            self.__length = length
        else:
            raise ValueError("Length must be numeric.")
        if isinstance(width, int):
            self.__width = width
        else:
            raise ValueError("Width must be numeric.")

    def __str__(self) -> str:
        """
        String returns the color shape, four sides length and width 
        of the rectangle.

        Returns:
            str: The shape color is {color}.
            This rectangle has a length of {length} centimeters 
            and a width of {width} centimeters.
        """

        return (f"The shape color is {self._color}.\n"
                f"This rectangle has four sides with the lengths "
                f"of {self.__length}, {self.__width}, {self.__length} "
                f"and {self.__width} centimeters."
                )

    def calculate_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle in square centimeters.
        """
        area = self.__length * self.__width

        return area

    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle in centimeters.
        """
        perimeter = self.__length * 2 + self.__width * 2

        return perimeter
