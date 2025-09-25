"""This module defines the TestRectangle class.
- Contains the test cases for the Rectangle class.
- Successful initialization valid inputs for color, length and width.
- Handling of invalid inputs for color, length and width.
"""

__author__ = "Kailine Lima"
__version__ = "1.0.0"

import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Represents a rectangle test case
    """
    
    def setUp(self):
        """Set up test with a valid rectangle instance."""
        
        self.rectangle = Rectangle("Red", 5, 6)

    def test_init_valid_rectangle_attributes_set(self):
        """
        Test that the attributes are set correctly when a valid
        Rectangle is created.
        """
        # Arrange

        # Act
        rectangle = Rectangle("Red", 5, 6)

        # Assert 
        self.assertEqual("Red", self.rectangle._color)
        self.assertEqual(5, self.rectangle._Rectangle__length)
        self.assertEqual(6, self.rectangle._Rectangle__width)
    
    def test_init_blanck_color_valueError_raised(self):
        """ 
        Test when the color cannot be blank, if not raised the ValueError.
        """
        # Arrange
        # Act
        with self.assertRaises(ValueError):
            Rectangle("", 5, 6)
    
    def test_init_non_numeric_length_valueError_raised(self):
        """
        Test when length must be numeric, if not raised the ValueError.

        """
        with self.assertRaises(ValueError):
            Rectangle("Red", "five", 6)
    
    def test_init_non_numeric_width_valueError_raised(self):
        """
        Test when width must be numeric, if not raised the ValueError.

        """
        with self.assertRaises(ValueError):
            Rectangle("Red", 5, "six")

    def test__str__correct_string_representation_returned(self):
        """
        Test that the __str__ method returns the correct string representation.
        """
        # Arrange
        rectangle = Rectangle("Red", 5, 6)

        # Act

        # Assert
        expected = ("The shape color is Red.\n"
                    "This rectangle has four sides with the lengths "
                    "of 5, 6, 5 and 6 centimeters.")

        self.assertEqual(expected, str(rectangle))

    def test_calculate_area_correct_rectangle_area_returned(self):
            """
            Test that the calculate_area method returns the correct area 
            of the rectangle.
            """
            # Arrange
            expected_area = 30

            # Act
            area = self.rectangle.calculate_area()

            # Assert
            self.assertAlmostEqual(expected_area, area)


    def test_calculate_perimeter_rectangle_correct_perimeter_returned(self):
            
            """ 
            Test that the calculate_perimeter method returns the correct 
            perimeter of the rectangle.
            """
            # Arrange
            expected_perimeter = 22
            
            # Act
            perimeter = self.rectangle.calculate_perimeter()

            # Assert
            self.assertEqual(expected_perimeter, perimeter)
