"""
Loops:
    - for loop
    - range()
    - loop (list, string, dict)
    - enumerate()
    - zip()
    - while loop
"""

for i in range(10):
    print(f"Count {i}")

"""
range(stop)
range(start, stop)
range(start, stop, step)
"""

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

word = "Python"
for char in word:
    print(f"Char: {char}")

person = {"name": "Alice", "age": 25, "city": "NewYork"}
for key in person:
    print(f"Key: {key}")

for value in person.values():
    print(f"Value: {value}")

for key, value in person.items():
    print(f"{key}: {value}")

colors = {"red", "green", "blue"}
for color in colors:
    print(f"Color: {color}")

# enumerate()
languages = ["Python", "Java", "C++", "JavaScript"]
for index, lang in enumerate(languages):
    print(f"{index}: {lang}")

# zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Beijing", "Shanghai", "Guangzhou"]
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")


# while loop
count = 0
while count < 5:
    print(f"while count: {count}")
    count += 1


# for else
for i in range(3):
    print(i)
else:
    print("for...else nomal exit")


for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("for...else normal exit")

# List comprehension
# Tradition
squares = []
for i in range(5):
    squares.append(i**2)

print(f"Squares {squares}")

squares = [i**2 for i in range(5)]
print(f"Squares {squares}")

even_squares = [i**2 for i in range(10) if i % 2 == 0]
print(f"Even squares: {even_squares}")
