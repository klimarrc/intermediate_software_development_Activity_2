"""This module defines the TestTriangle class.

Contains the test cases for the Triangle class.
- Successful initialization valid inputs for color and sides.
- Handling of invalid inputs for color sides and
    triangle inequality theorem.

"""

__author__ = "Kailine Lima"
__version__ = "1.0.0"

import unittest
from shape.triangle import Triangle

class TestTriangle(unittest.TestCase):
    """Test cases for the Triangle class."""

    def setUp(self):
        """Set up test with a valid triangle instance."""
        
        self.triangle = Triangle("Red", 5, 5, 6)

    def test_init_valid_triangle_attributes_set(self):
        """
        Test that the attributes are set correctly when a valid
        Triangle is created.
        """
        # Arrange

        # Act
        triangle = Triangle("Red", 5, 5, 6)

        # Assert 
        self.assertEqual("Red", self.triangle._color)
        self.assertEqual(5, self.triangle._Triangle__side_1)
        self.assertEqual(5, self.triangle._Triangle__side_2)
        self.assertEqual(6, self.triangle._Triangle__side_3)
    
    def test_init_blanck_color_valueError_raised(self):
        """ 
        Test when the color cannot be blank, if not raised the ValueError.
        """
        # Arrange
        # Act
        with self.assertRaises(ValueError):
            Triangle("", 5, 5, 6)
    
    def test_init_non_numeric_side_one_valueError_raised(self):
        """
        Test when side 1 must be numeric, if not raised the ValueError.

        """
        with self.assertRaises(ValueError):
            Triangle("Red", "five", 5, 6)
    def test_init_non_numeric_side_two_valueError_raised(self):
        """
        Test when side 2 must be numeric, if not raised the ValueError.

        """
        with self.assertRaises(ValueError):
            Triangle("Red", 5, "five", 6)
        
    def test_init_non_numeric_side_three_valueError_raised(self):
        """
        Test when side 3 must be numeric, if not raised the ValueError.

        """
        with self.assertRaises(ValueError):
            Triangle("Red", 5, 5, "six")

    def test_str_correct_string_returned(self):
        """
        Test that the __str__ method returns the correct string representation
        of the triangle.
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
            # Arrange
            expected_area = 12
            
            # Act
            area = self.triangle.calculate_area()

            # Assert
            self.assertAlmostEqual(expected_area, area)


    def test_calculate_perimeter_correct_perimeter_returned(self):
            
            """ 
            Test that the calculate_perimeter method returns the correct 
            perimeter of the triangle.
            """
            # Arrange
            expected_perimeter = 16
            
            # Act
            perimeter = self.triangle.calculate_perimeter()

            # Assert
            self.assertEqual(expected_perimeter, perimeter)