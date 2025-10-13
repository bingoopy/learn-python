"""
Error Handling:
    - try/except
    - basic error types
    - else and finally
    - define error
"""

# result = 10 / 0
# ZeroDivisionError: division by zero

try:
    result = 10 / 0
except ZeroDivisionError:
    print("[ERROR] division by zeros")

try:
    result = 10 / 0
except Exception as e:
    print(f"Caught error: {e}")
    print(f"Error type: {type(e).__name__}")


def safe_convert(value):
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        print(f"Convert error: {e}")
        return None


# else nad finally
def read_file(filename):
    file = None
    try:
        print(f"Try to open file: {filename}")
        file = open(filename, "r")
        content = file.read()
    except FileNotFoundError:
        print(f"Error: file {filename} not exist")
        return None
    else:
        # Only execute when there is no error
        print(f"Read file, content length: {len(content)}")
        return content
    finally:
        # Execute whenever there is error
        print("Execute cleanning")
        if file:
            file.close()
            print("File is closed")


# Test
test_file = "/tmp/test_file.txt"
with open(test_file, "w") as f:
    f.write("Hello from test file!")

print("\nTest 1: read exist file")
read_file(test_file)

print("\nTest 2: read file not exist")
read_file("non_existent.txt")

import os

os.remove(test_file)


# raise
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be integer")
    if age < 0:
        raise ValueError("Age can't be negative")
    if age > 150:
        raise ValueError("Age can't over 150")
    print(f"Age {age} valid")


try:
    validate_age(25)
except Exception as e:
    print(f"Validate failed：{e}")

test_cases = ["25", -5, 200]
for test_age in test_cases:
    try:
        validate_age(test_age)
    except (TypeError, ValueError) as e:
        print(f"validate {test_age} failed：{e}")


def process_data(data):
    try:
        # some errors
        result = 10 / data
    except ZeroDivisionError:
        print("Logging error")
        raise


try:
    process_data(0)
except Exception as e:
    print("Caught")


class CustomError(Exception):
    pass


class ValidateError(CustomError):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code


def validate_username(username):
    """Validate the username"""
    if not username:
        raise ValidateError("Username cannot be empty", code="EMPTY_USERNAME")
    if len(username) < 3:
        raise ValidateError(
            "Username must be at least 3 characters long", code="USERNAME_TOO_SHORT"
        )
    if not username.isalnum():
        raise ValidateError(
            "Username can only contain letters and numbers", code="INVALID_CHARS"
        )
    return True


# Test custom exception
test_usernames = ["", "ab", "user123", "user@123"]
for username in test_usernames:
    try:
        validate_username(username)
        print(f"Username '{username}' is valid")
    except ValidateError as e:
        print(f"Username '{username}' validation failed: {e} (Error code: {e.code})")
