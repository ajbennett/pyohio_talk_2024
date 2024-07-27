""" Example 3: Type annotations in a Pydantic model """

from pydantic import Field, BaseModel, ValidationError


class Rectangle(BaseModel):
    length: float
    width: float

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


if __name__ == "__main__":
    # Creating an instance of a Pydantic model uses keyword arguments
    # based on the schema defined in the class derived from BaseModel.

    # Constructor arguments match the type annotations in the class
    # definition. mypy finds no errors in the following statements.
    #
    # The arguments match the types specified in the type annotations,
    # so the constructor call will run without error.
    r1 = Rectangle(length=5, width=10)
    print(f"r1 area is      : {r1.area()}")
    print(f"r1 perimeter is : {r1.perimeter()}")
    print("")

    # ------------------------------------------------------------

    # Constructor arguments do NOT match the type annotations in the
    # class definition. mypy flags the arguments to the Rectangle
    # constructor as errors.
    #
    #
    # The arguments do NOT match the types specified in the type
    # annotations, so the constructor call will throw a
    # pydantic.ValidationError
    try:
        r2 = Rectangle(length="foo", width="bar")
        print(f"r2 perimeter is : {r2.perimeter()}")
        print(f"r2 area is       : {r2.area()}")
    except ValidationError as e:
        print(f"Exception reported for r2:\n\n{e}\n")

    # ------------------------------------------------------------

    # Pydantic does some clever conversion by default (when strict=False).
    #
    # Example: If you give it the string representation of a number,
    # it recognizes that this is convertible to a number and works with it.
    #
    try:
        r3 = Rectangle(length="4", width="20")
        print(f"r3 perimeter is  : {r3.perimeter()}")
        print(f"r3 area is       : {r3.area()}")
    except ValidationError as e:
        print(f"Exception reported for r3:\n\n{e}\n")
