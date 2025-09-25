"""
This module defines the TestTriangle class:
- Successful initialization valid inputs for color and sides.
- Handling of invalid inputs for color and sides.
- Color shape is set correctly with protected attribute.
- Calculation of area and perimeter.
- String representation of the triangle.
"""

__author__ = "Kailine Lima"
__version__ = "1.0.0"

import unittest
from shape.triangle import Triangle


class TestTriangle(unittest.TestCase):
    """Represents a triangle test cases for the Triangle class."""

    def setUp(self):
        """Set up test with a valid triangle instance."""

        self.triangle = Triangle("Red", 5, 5, 6)

    def test_init_valid_triangle_attributes_set(self):
        """Test that the attributes are set correctly when is a valid 
        triangle.
        """
        # Arrange
        triangle = Triangle("Red", 5, 5, 6)

        # Assert
        self.assertEqual("Red", self.triangle._color)
        self.assertEqual(5, self.triangle._Triangle__side_1)
        self.assertEqual(5, self.triangle._Triangle__side_2)
        self.assertEqual(6, self.triangle._Triangle__side_3)

    def test_init_non_blank_color_valueError_raised(self):
        """
        Test when the color cannot be blank, if not raised
        the ValueError.
        """
        with self.assertRaises(ValueError):
            Triangle("", 5, 5, 6)

    def test_init_non_numeric_side_one_valueError_raised(self):
        """
        Test when side 1 must be numeric, if not raised 
        the ValueError.
        """
        with self.assertRaises(ValueError):
            Triangle("Red", "five", 5, 6)

    def test_init_non_numeric_side_two_valueError_raised(self):
        """
        Test when side 2 must be numeric, if not raised 
        the ValueError.
        """
        with self.assertRaises(ValueError):
            Triangle("Red", 5, "five", 6)

    def test_init_non_numeric_side_three_valueError_raised(self):
        """
        Test when side 3 must be numeric, if not raised 
        the ValueError.
        """
        with self.assertRaises(ValueError):
            Triangle("Red", 5, 5, "six")

    def test_str_correct_string_returned(self):
        """ 
        Test __str__ method returns the correct string 
        representation.
        """
        # Arrange
        expected = ("Color shape is Red.\n"
                    "This triangle has three sides with lengths "
                    "of 5, 5 and 6 centimeters.")

        # Assert
        self.assertEqual(expected, str(self.triangle))

    def test_calculate_area_correct_area_returned(self):
        """
        Test that the calculate_area method returns the correct area 
        of the triangle.
        """
        expected_area = 12
        self.assertAlmostEqual(expected_area, self.triangle.calculate_area())

    def test_calculate_perimeter_correct_perimeter_returned(self):
        """
        Test that the calculate_perimeter method returns the correct 
        perimeter of the triangle.
        """
        expected_perimeter = 16
        self.assertEqual(expected_perimeter, self.triangle.calculate_perimeter())