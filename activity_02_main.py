""""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Kailine Lima"

from shape import *


def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """

    # In the statements coded below, ensure that any statement that
    # could result in an exception is handled.  When exceptions are
    # 'caught', display the exception message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")

    # 1. Create an empty list of Shape objects.
    shapes = []

    # 2. Code a statement which creates an instance of the Triangle
    # class.
    # Append the Triangle to the list of shapes.
    try:
        triangle = Triangle("Red", 5, 5, 6)
        shapes.append(triangle)
    except Exception as e:
        print(e)
    # 3. Code a statement which creates an instance of the Rectangle
    # class.
    # Append the Rectangle to the list of shapes.
    try:
        rectangle = Rectangle("Red", 5, 6)
        shapes.append(rectangle)
    except Exception as e:
        print(e)

    # 4. Code 3 additional statements which creates an instance of
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    try:
        triangle2 = Triangle("Blue", 3, 4, 5)
        shapes.append(triangle2)
    except Exception as e:
        print(e)
    try:
        rectangle2 = Rectangle("Green", 4, 7)
        shapes.append(rectangle2)
    except Exception as e:
        print(e)
    try:
        triangle3 = Triangle("Yellow", 6, 8, 10)
        shapes.append(triangle3)
    except Exception as e:
        print(e)

    # 5. Iterate through the list of shapes.
    # On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places

    for shape in shapes:
        try:
            print(shape)
            print(f"Area: {shape.calculate_area():.2f} square centimeters.")
            print(f"Perimeter: {shape.calculate_perimeter():.2f} centimeters.")
        except Exception as e:
            print(e)
    # *** END PART 1 ***


if __name__ == "__main__":
    main()
