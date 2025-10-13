"""
String Operations:
    - Creation: single quote '...', double quote "...", multi line
    - Raw string: r"..."
    - Concat: +, " ".join(["Hello", "Python"])
    - Immutable
    - Slice and Index
    - len()
    - for ... in ..., for i, xxx in ...
    - upper(), lower(), capitalize(), title(), swapcase()
    - find(), replace(), count()
    - strip(), lstrip(), rstrip()
    - split()
    - startswith(), endswith()
    - isdigit(), isalpha(), isalnum(), isspace(), istitle()
    - Format: var:.2f, var:5.2f, var:05d, var:,
    - Align string: var:<10, var:>10, var:^10, var:*^10
    - is_empty_or_whitespace()
"""

# Creations
single = "Hello World"

double = "Hello World"

multi = """
Hello
World
"""

# Raw string
# raw = "C:\Users\name\Documents" - Incorrect
raw = r"C:\Users\name\Documents"
print(f"Raw string: {raw}")

# Immutable
text = "Python"
# text[0] = "J" - Error
new_text = "J" + text[1:]
print(f"New string from concat and slice: {new_text}")

# Index and Slice
print("\nIndex and Slice -")
word = "Python Programming"

print(f"String: {word}")
print(f"Index 0: {word[0]}")  # P
print(f"Index -1: {word[-1]}")  # g
print(f"Index -2: {word[-2]}")  # n

# Slice [start:end:step]
print(f"First 6: {word[:6]}")  # [0, 6) Python
print(f"From the 7th to the end: {word[7:]}")  # Programming
print(f"From 2nd to 5th: {word[1:5]}")  # ytho
# Default step is 1 (0, 1, 2, 3, ...)
# Set to 2: (0, 2, 4, 6, ...)
print(f"Step 2: {word[::2]}")  # Pto rgamn
print(f"Reverse string: {word[::-1]}")  # gnimmargorP nohtyP

# Search/Find, Replace
text = "Python is great. Python is powerful."

print(f"Find 'Python': {text.find('Python')}")
print(f"Find 'is': {text.find('is')}")
print(f"Find 'Java': {text.find('Java')}")
print(f"Count 'Python': {text.count('Python')}")

new_text = text.replace("Python", "JavaScript")
print(f"New text with replace: {new_text}")


# Trim/Strip
text = "    Hello World  "
print(text.strip())
print(text.lstrip())
print("***Good**".strip("*"))

# Split
sentence = "Python,Java,C++,JavaScript"
languages = sentence.split(",")  # Default is split by space
print(f"Splited sentence: {languages}")

# start/end with
filename = "document.pdf"
print(f"start with docu: {filename.startswith('docu')}")
print(f"end with .pdf: {filename.endswith('.pdf')}")

# Check contents
print(f"'123'.isdigit(): {'123'.isdigit()}")  # True
print(f"'abc'.isalpha(): {'abc'.isalpha()}")  # True
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")  # True
print(f"'  '.isspace(): {'  '.isspace()}")  # True
print(f"'Title'.istitle(): {'Title'.istitle()}")  # True

# Format options
pi = 3.14159265359
print(f"{pi:.2f}")
print(f"{pi:5.2f}")
print(f"{42:05d}")
print(f"{1234567:,}")

# Alignment
text = "Python"
print(f"{text:<10}")  # Align left :10
print(f"{text:>10}")  # Align right
print(f"{text:^10}")  # Middle
print(f"{text:*^10}")  # Fill *
