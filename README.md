# Intermediate Software Development Activity 2

This activity will help to reinforce learning of the Module 2 concepts of:

- Abstraction
- Inheritance
- Polymorphism
- Package Initialization

## Author

Kailine Lima

## Additional Information

The following are 3 components from Module 2 (Applying Object- Oriented Design) that are implemented in this activity_2:

1. **Super Class - Shape

- A Shape class was defined as a superclass that includes an Italic font representing abstraction, an attribute #colour indicating the colour of the shape, a protected attribute #, and a method str that returns a string message. It also calculates the area and perimeter using the abstract method (the @abstractmethod decorator) along with the pass statement for implementation in subclasses.

2. **Sub Class - Triangle

- A Triangle class was defined as a subclass that includes attribute validation with integer input (side_1, side_2, and side_3), which are kept private , added to the Triangle Inequality and Theorem, implemented super() to call the methods from superclass as color, and a method str that returns a string message. It also calculates the area and perimeter by implementing Hero's formula and the perimeter formula. The methods return the calculated area and perimeter.

3. ** Sub Class - Rectangle

- A Rectangle class was defined as a subclass that includes attribute validation (length and width), which are kept private, implemented super() to call the methods from superclass as color,  and a method str that returns a string message. It also calculates the area and perimeter by using two integer length and width and implementing the calculate_area (length x width) and calculate_perimeter (length x 2 + width x 2)  method that return the result.


4. ** Unit test - Triangle and Rectangle

- All tests verify the correctness of area, perimeter,  and string representation method for Triangle and Rectangle. If any test fails, the error message and traceback will be display.  

5. ** Package Initialization

- Configured the shape package's __init__.py to support importing all shape classes (Shape, Triangle, and Rectangle) with a single from shape import * statement.

6. ** Client Program

- Demonstrated creating shapes, printing message, and handling exceptions with try/except block. 