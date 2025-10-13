"""
List - Mutable Ordered Sequence:
    - Creation (empty, literal, list(), from iterable)
    - Indexing and Slicing [start:end:step]
    - List methods (append, extend, insert, remove, pop, clear)
    - Sorting (sort, sorted, reverse)
    - List comprehension [expr for item in iterable if condition]
    - Nested lists and flattening
"""

empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"Empty list: {empty_list}")
print(f"Number list: {numbers}")
print(f"Mixed list: {mixed}")
print(f"Nested list: {nested}")

# Use list(...)
from_string = list("Python")
from_range = list(range(5))
print(f"From string creted: {from_string}")
print(f"From range created: {from_range}")

# Index and Slice
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(f"The first item: {fruits[0]}")
print(f"The third item: {fruits[2]}")

print(f"The last item {fruits[-1]}")
print(f"Second to last: {fruits[-2]}")

# Slice [start:end:step]
# Not include end
print(f"First 3: {fruits[:3]}")
print(f"from 2nd to 4th: {fruits[1:4]}")
print(f"Last 2: {fruits[-2:]}")  # Count second to last to the end
print(f"Step 2: {fruits[::2]}")
print(f"Reverse: {fruits[::-1]}")


# Assigning value
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30]
print(f"After assigning value to sliced: {numbers}")

# append(...)
# extend([...])
# insert(idx, ...)
# remove(...)
# pop() delete the last by default
# pop(0) delete the first
# clear()
# count(...)
# list.sort(), list.sort(reverse=True)
# sorted() return new list
# reverse()
# len(), max(), min(), sum()

# list comprehension
# [expression for item in iterable]
squares = [x**2 for x in range(10)]
print(f"squares: {squares}")

# conditional comprehension
evens = [x for x in range(20) if x % 2 == 0]
print(f"evens: {evens}")

# *multi
pairs = [(x, y) for x in [1, 2, 3] for y in ["a", "b"]]
print(f"pairs: {pairs}")

# complex
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row if num % 2 == 0]
print(f"Evens in matrix: {flattened}")

# String handling
words = ["Hello", "World", "Python", "Programming"]
lengths = [len(word) for word in words]
uppercase = [word.upper() for word in words if len(word) > 5]
print(f"Word length: {lengths}")
print(f"Long word uppercase: {uppercase}")
