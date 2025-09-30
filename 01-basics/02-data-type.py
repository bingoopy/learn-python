"""
Data Type:
    - int
    - float
    - string
    - bool
    - None
    - Conversion
"""

print("int -----------------------------------")
int_var = 10
print(f"int value: {int_var}")
print(f"int type: {type(int_var)}")

print("\nfloat -----------------------------------")
float_var = 3.1415926
print(f"float value: {float_var}")
print(f"float type: {type(float_var)}")

print("\nstr -----------------------------------")
str_var = "Hi Python!"
print(f"str value: {str_var}")
print(f"str type: {type(str_var)}")

print("\nbool -----------------------------------")
bool_var = True
if bool_var:
    print("Condition is True")
else:
    print("False!")
print(f"bool type: {type(bool_var)}")

print("\nNone -----------------------------------")
none_var = None
print(f"None value: {none_var}")
print(f"None type: {type(none_var)}")

print("\n----------------------------------------")
f_2_i = int(3.14159)
print(f"Convert float to int: {f_2_i}")

sn_2_i = int("100")
print(f"Convert to int from string number: {sn_2_i}")

# sf_2_i = int("100.098341")
# ValueError: invalid literal for int() with base 10: '100.098341'

# s_2_i = int("a")
# ValueError: invalid literal for int() with base 10: '
