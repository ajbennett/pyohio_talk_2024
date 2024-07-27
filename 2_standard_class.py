"""Example 2: Type annotations in a standard Python class definition"""


class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


if __name__ == "__main__":
    # Constructor arguments match the type annotations in the class
    # definition. mypy approves the following statements.
    r1 = Rectangle(5, 10)
    print(f"r1 area is      : {r1.area()}")
    print(f"r1 perimeter is : {r1.perimeter()}")
    print("")

    # Constructor arguments do NOT match the type annotations in the
    # class definition. mypy flags the arguments to the Rectangle
    # constructor as errors.
    try:
        r2 = Rectangle("foo", "bar")
        print(f"r2 perimeter is  : {r2.perimeter()}")

        # This is not valid Python because you can't multiply a string by
        # a string, so it causes a run-time TypeError exception.
        print(f"r2 area is       : {r2.area()}")
    except TypeError as e:
        print(f"Exception reported for r2:\n\n{e}\n")
