"""
Set - Unordered Unique Elements:
    - Creation (set(), literal, from iterable)
    - Element operations (add, discard, remove, pop)
    - Set methods (update, clear)
    - Set operations (union |, intersection &, difference -, symmetric_difference ^)
    - Set relationships (issubset, issuperset, isdisjoint)
    - Set comprehension {expr for item in iterable}
    - Automatic deduplication
"""

empty_set = set()
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])
from_string = set("Hello")

print(f"Emtpy set: {empty_set}")
print(f"Numbers set: {numbers}")
print(f"Set from list: {from_list}")
print(f"Set from string: {from_string}")

# Operations
fruits = {"Apple", "Banana"}
fruits.add("Cherry")
print(f"Add: {fruits}")

fruits.discard("Banana")  # Delete if exist
fruits.remove("Apple")  # Delete, will throw error if not exist
print(f"After deletetion: {fruits}")

# Methods
numbers = {1, 2, 3, 4, 5}
numbers.update([6, 7, 8])
print(f"After update: {numbers}")

popped = numbers.pop()  # randomly delete and return
print(f"Popped {popped}, remain: {numbers}")

A = {1, 2, 3, 4}
B = {4, 5, 6, 7}
print(f"Union: A | B: {A | B}")
print(f"Union: A.unioin(B): {A.union(B)}")

print(f"Difference A - B: {A - B}")
print(f"Difference: A.dirrerence(B): {A.difference(B)}")

print(f"symmetric_diff A ^ B: {A ^ B}")
print(f"symmetric_diff A.symmetric_difference(B): {A.symmetric_difference(B)}")

# issubset, issuperset, isdisjoint

# {expression for item in iterable}
squares = {x**2 for x in range(10)}
print(f"Squares: {squares}")

evens = {x for x in range(20) if x % 2 == 0}
print(f"Evens: {evens}")
