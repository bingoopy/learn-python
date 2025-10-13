"""
Dictionary - Key-Value Mapping:
    - Creation (literal, dict(), from sequences, kwargs)
    - Access and modification ([], get, setdefault)
    - Deletion (del, pop)
    - Dictionary methods (keys, values, items, update)
    - Iteration patterns
    - Dictionary comprehension {k:v for item in iterable}
    - Key-value manipulation (zip, invert, filter)
"""

empty_dict = {}
empty_dict2 = dict()
person = {"name": "Alice", "age": 30, "city": "New York"}
from_tuple = dict([("a", 1), ("b", 2), ("c", 3)])
from_kwargs = dict(x=1, y=2, z=3)

print(f"Empty dict: {empty_dict}")
print(f"person: {person}")
print(f"Create from tuple {from_tuple}")
print(f"Create from key word args: {from_kwargs}")


# Dict operations
# Access
student = {"name": "Bob", "age": 20, "grades": [85, 90, 92]}

print(f"Student name: {student['name']}")
print(f"Student age: {student.get('age')}")
print(f"Student major: {student.get('major', 'unknown')}")

# Update and Add
student["age"] = 18
student["major"] = "Computer Science"

print(f"Updated student {student}")

# Delete
del student["grades"]
age = student.pop("age")
print(f"After deltetion: {student}, deleted age: {age}")

# keys(), values(), items()
info = {"a": 1, "b": 2, "c": 3}
print(f"Info keys: {list(info.keys())}")
print(f"Info values: {list(info.values())}")
print(f"Info items: {list(info.items())}")

# Traverse Dict
for key in info:
    print(f"{key}: {info[key]}", end=" ")
print()

for key, value in info.items():
    print(f"{key}: {value}", end=" ")
print()

info.update({"d": 4, "e": 5})
info.update(f=6, g=7)
print(f"Updated info: {info}")

# setdefault(), get the value, set it default if it's not exist
count = {}
for letter in "HelloWorld":
    count.setdefault(letter, 0)
    count[letter] += 1
print(f"Counting words: {count}")

# dict comprehension: {key: value for item in iterable}
squares = {x: x**2 for x in range(6)}
print(f"Squares {squares}")

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares {even_squares}")


# Create dict from two list
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print(f"Combined dict: {combined}")

# Invert
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Invert dict: {inverted}")

# Filter dict
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
high_scores = {k: v for k, v in scores.items() if v >= 90}
print(f"High scores filtered from dict {high_scores}")
