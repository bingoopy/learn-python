"""
Tuple - Immutable Ordered Sequence:
    - Creation (empty, single element, packing)
    - Immutability (cannot modify elements)
    - Unpacking and destructuring
    - Multiple assignment and swapping
    - Extended unpacking with *
    - Function return values
    - Dictionary keys and named tuples
"""

empty_tuple = ()
single = (1,)
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14)
nested = ((1, 2), (3, 4))

print(f"Empty tuple: {empty_tuple}")
print(f"Single element tuple: {single}")
print(f"Numbers tuple: {numbers}")
print(f"Mixed tuple: {mixed}")
print(f"Nested tuple: {nested}")

# Create without ()
coordinates = 10, 20
print(f"Coordinates: {coordinates}, type: {type(coordinates)}")  # type: <class 'tuple'>

# Immutable

t = (1, 2, 3)
print(f"Origin tuple: {t}")

# t[0] = 10 # Error: 'tuple' object does not support item assignment

# destruct
point = (3, 5)
x, y = point

a, b, c = 1, 2, 3

# Swap
a, b = b, a


# * to collect the rest
first, *middle, last = (1, 2, 3, 4, 5, 6)
print(f"first = {first}, middle = {middle}, last = {last}")


# Ignore some
_, y, _ = (10, 20, 30)


# Return multi values
def get_min_max(numbers):
    return min(numbers), max(numbers)


minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Minimum: {minimum}, Maximum: {maximum}")


# As the key of dict
locations = {(0, 0): "Origin", (1, 0): "East", (0, 1): "North"}
print(f"Location dict: {locations}")

# Named tuple (advanced)
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(11, y=22)
print(f"Named tuple: {p}, x={p.x}, y={p.y}")
