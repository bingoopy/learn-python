"""
Control Flow:
    - if/elif/else
    - Conditional express
    - match-case (python 3.10+)
"""

# if/else/elif
number = 99
if number > 100:
    print("> 100")
elif number <= 50:
    print("<= 50")
else:
    print(">50, <=100")


score = 55
result = "A" if score >= 90 else "B" if score >= 60 else "Failed"
print(f"{result}")

# False values
false_values = [False, None, 0, 0.0, "", [], (), {}, set()]
for value in false_values:
    if not value:
        print(f"{repr(value)} is false")


# and, or, not

# match-case
command = "start"
match command:
    case "start":
        print("Start the program")
    case "end":
        print("End the program")
    case "restart":
        print("Restart the program")
    case _:  # Default
        print("Unknown command")

# Pattern match
point = (0, -1)
match point:
    case (0, 0):
        print("(0, 0)")
    case (x, 0):
        print(f"In x={x}")
    case (0, y):
        print(f"In y={y}")
    case (x, y):
        print(f"{(x, y)}")

# Match data strucutre
data = {"name": "Alice", "age": 25}
match data:
    case {"name": name, "age": age} if age >= 18:
        print(f"{name} is adult")
    case {"name": name, "age": age}:
        print(f"{name} is under 18")
    case _:
        print("Data format incrrect")
