from guard_decorator import guard

# =======================
# Example 1: Basic Usage
# =======================
print("=== Example 1: Basic Usage ===")

# Exception handler
def h_divide(e, *args, **kwargs):
    print(f"Caught exception: {e}")

# Adding safe-mode decorator to function
@guard(h=h_divide)
def divide_numbers(a, b):
    print(f"Dividing {a} by {b}")
    return a / b

# Calling function WITHOUT try-except block
print(f"Result: {divide_numbers(10, 2)}")   # OK
print(f"Result: {divide_numbers(10, 0)}")   # Raise Exception

# =======================
# Example 2: Handling Specific Exceptions
# =======================
print("\n=== Example 2: Handling Specific Exceptions ===")

# Exception handler
def h_value_error(e, *args, **kwargs):
    print(f"Handling ValueError: {e}")
    print(f"Arguments: {args}, Keyword Arguments: {kwargs}")

# Adding safe-mode decorator to function ONLY to handle ValueError exceptions
@guard(type=ValueError, h=h_value_error)
def risky_function(value):
    print(f"Processing value: {value}")
    if value < 0:
        raise ValueError("Negative value not allowed!")

risky_function(10)  # OK
risky_function(-10) # Raise Exception

# =======================
# Example 3: Cleanup Actions
# =======================
print("\n=== Example 3: Cleanup Actions ===")

# Exception handler
def h_open_file(e, *args, **kwargs):
     print(f"Caught exception: {e}")

# Cleanup handler
def f_open_file(*args, **kwargs):
    print(f"Cleaning up with args: {args}, kwargs: {kwargs}")

    # Here you place all cleanup actions...

@guard(h=h_open_file, f=f_open_file)
def open_file(file_name):
    print(f"Opening file: {file_name}")
    raise FileNotFoundError("File not found!")  # Simulate an error

open_file("non_existent_file.txt")  # Raise Exception

# =======================
# Example 4: Higher-Level Exception Handling
# =======================
print("\n=== Example 4: Higher-Level Exception Handling ===")

# Adding safe-mode decorator to function
# If you DONT provide any handler, the exception will be automatically raised
# so, you can catch it at higher level
@guard()
def access_dict(key):
    my_dict = {"name": "Alice", "age": 30}
    print(f"Accessing key: {key}")
    return my_dict[key]

try:
    access_dict("address")
except Exception as e:
    print(f"Exception caught at higher level: {e}")

# =======================
# Example 5: Using guard with a Class
# =======================
print("\n=== Example 5: Using guard with a Class ===")

# Cleanup handler
def f_class_method(*args, **kwargs):
    print(f"Performing class method cleanup with args: {args}, kwargs: {kwargs}")

class Calculator:
    def __init__(self):
        print("Calculator initialized.")

    # Exception handler
    def __h_divide(self, e, *args, **kwargs):
        print(f"Caught exception in class method: {e}")

    # Cleanup handler
    def f_divide(*args, **kwargs):
        print(f"Performing class method cleanup with args: {args}, kwargs: {kwargs}")

    # Applying the guard decorator to a method
    @guard(h=__h_divide, f=f_divide)
    def divide(self, a, b):
        print(f"Dividing {a} by {b}")
        return a / b

# Creating an instance of Calculator
calc = Calculator()

# Method calls
print(f"Result: {calc.divide(10, 2)}")  # OK
print(f"Result: {calc.divide(10, 0)}")  # Raise Exception
