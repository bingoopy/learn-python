"""
File Operation:
    - open and close
    - file mode (r, w, a, x, b)
    - read(), readline(), readlines()
    - write(), writelines()
    - with
"""

from pathlib import Path

temp = "/tmp/temp_files/example.txt"
temp = Path(temp)
temp.parent.mkdir(parents=True, exist_ok=True)

# Write to file (Tradition)
file = open(temp, "w")
file.write("Hello World!\n")
file.write("This is a test file.\n")
file.close()

# Read from file (Tradition)
file = open(temp, "r")
content = file.read()
print(content)
file.close()

# with
temp2 = "/tmp/temp_files/example2.txt"
with open(temp2, "w") as f:
    f.write("Try to use with\n")
    f.write("File will close automatically\n")
    f.write("The best practice!\n")

with open(temp2, "r") as f:
    content = f.read()
    print(content)

# 'r' - Read (default)
# 'w' - Write (overwrite)
# 'a' - Append
# 'x' - Exclusive creation
# 'b' - Binary mode
# '+' - Read and write mode
