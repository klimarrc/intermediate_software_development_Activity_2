# Intermediate Software Development Activity 2

This activity will help to reinforce learning of the Module 2 concepts of:

- Abstraction
- Inheritance
- Polymorphism
- Package Initialization

## Author

Kailine Lima

## Additional Information

The following are 3 components from Module 2 (Applying Object- Oriented Design)
that are implemented in this activity_2:

### 1. Super Class - Shape

- A `Shape` class was defined as a superclass that includes an *Italic meow*
font representing abstraction.
- It includes `_color` indicating the color of the shape and protected
attribute.
- A method `__str__`  that returns a string message. "Color shape is {color}."
- It also calculates the area and perimeter using the abstract method (the @abstractmethod decorator) along with the pass statement for implementation in subclasses.

### 2. Sub Class - Triangle

- A Triangle class was defined as a subclass that includes attribute validation
with integer input (`__side_1`, `__side_2`, and `__side_3`). They have to
satisfy the Triangle Inequality and Theorem.
- Attributes are kept private by using double underscore.
- Implemented `super()` for color initialization
- The method `__str__` that returns a string message.
- It also calculates the area and perimeter by implementing Hero's formula
and the perimeter formula. The methods return the calculated area and
perimeter.

### 3. Sub Class - Rectangle

- A Rectangle class was defined as a subclass that includes attribute validation (`__length` and `__width`)
- Attributes are kept private by using double underscore.
- Implemented `super()` for color initialization.
- The method `__str__` that returns a string message.
- It also calculates the area and perimeter by using two integer `length` and
`width` and implementing the calculate_area (length x width) and calculate_perimeter (length x 2 + width x 2)  method that return the result.

### 4. Unit test - Triangle and Rectangle

- All tests verify the correctness of area, perimeter, and string representation method for `Triangle` and `Rectangle`.
- Test ensure appropriate exceptions are raised for invalid input.
- If any test fails, the error message and traceback will be display.  

### 5. Package Initialization

- Configured the `shape` package's `__init__.py` is configured to support
all shape class (`Shape`, `Triangle`, and `Rectangle`) with a single line
from shape import * statement.

### 6. Client Program

- Imported from shape import * that means all shape class.
- Demonstrated creating shapes, printing message, and handling exceptions with `try`/`except` block.
