""" Example 1: Type annotations """

import typing as t

# Valid Python when the type of the data matches the hint.
good_int: int = 1
good_str: str = "string contents"

# STILL valid Python when the type of the data DOES NOT match the hint.
bad_str: str = -9999

# Annotating sequence types

# Tuple of ints of length 2
my_tuple: t.Tuple[int, int] = (1, 2)

# Types in a tuple can be mixed
mixed_typle: t.Tuple[str, int] = ("string value", 1)

# Arbitrary length tuple of strings
second_tuple: t.Tuple[str, ...] = ("one", "two", "three")

my_list: t.List[str] = []
my_list.append("foo")
# mypy won't like the following, but it is STILL valid Python syntax
# because Python lists can contain different types.
my_list.append(1)
my_list.append("bar")
print(f"my_list is: {my_list}")


# Annotating function arguments and return types.
def add(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    # Arguments match the type annotations above, so mypy will approve
    # the function call
    a = 10
    b = 20
    print(f"sum of {a} and {b} is {add(a, b)}")

    # These arguments don't match the type annotations, so mypy WILL
    # flag this type discrepancy in the function call.
    #
    # However, this is still valid Python. The "+" operator is defined
    # for string type, and performs string concatenation.
    #
    # Without static type checking, invalid data like this might
    # propagate further and cause corrupted results or mysterious
    # errors far away from the original error.
    #
    # This is why we use type hints and mypy!
    #
    c = "foo"
    d = "bar"
    print(f"sum of {c} and {d} is {add(c, d)}")
