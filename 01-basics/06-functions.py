"""
Functions:
    - Definition
    - Parameters (*args, **kwargs)
    - local, global
    - lambda
"""


def greet_0():
    print("Hello World!")


greet_0()


def greet(name):
    print(f"Hello {name}")


greet("bingoopy")


# Return value
def add(a, b):
    return a + b


def calculate(a, b):
    sum = a + b
    diff = a - b
    prod = a * b
    return sum, diff, prod


s, d, p = calculate(10, 3)
print(f"Sum: {s}, Diff: {d}, Product: {p}")


# Default parameter
def describe_pet(name, animal="dog"):
    print(f"I have a {animal}, named {name}")


describe_pet("Buddy")
describe_pet(animal="Cat", name="MeowMeow")


# *args To receive many parameters
def sum_all(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total


print(f"Sum of: {sum_all(1, 2, 3, 4, 5, 10)}")


# **kwargs
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


print("\nUser info:")
print_info(name="Bob", age=30, city="Lodon", email="bob@example.com")


# Combined
def advanced_func(required, *args, default="default", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")


print("\nAdvanced function: ")
advanced_func("must_have", 1, 2, 3, default="cumstom", extra1="value1", extra2="value2")


# nonlocal
def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
        print(f"Inner x: {x}")

    inner()
    print(f"Outer x: {x}")


outer()

# lambda
# basic
square = lambda x: x**2
print(f"5 squared: {square(5)}")

# map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Sorted
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Cahrlie", "grade": 78},
]
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
print("\nStudents sorted by grade:")
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")
