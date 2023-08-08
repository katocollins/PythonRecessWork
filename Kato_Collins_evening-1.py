def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: Division by zero")
        result = None
        error_info = (type(e).__name__, str(e))
        return result, error_info
    except Exception as e:
        print("Error:", str(e))
        result = None
        error_info = (type(e).__name__, str(e))
        return result, error_info
    else:
        return result, None

# Example usage
numbers = [(10, 2), (7, 0), (15, 3)]

for a, b in numbers:
    result, error_info = divide_numbers(a, b)
    if error_info:
        print(f"Calculation failed: {error_info}")
    else:
        print(f"Result: {result}")

"""
#Custom Exception
class CustomException(Exception):
    def __init__(self, message):
        self.message = message


def process_data(data):
    try:
        if not data:
            raise CustomException("Empty data")
        # Process the data here...
        print("Data processed successfully.")
    except CustomException as e:
        print(f"Custom Exception: {e.message}")
    except Exception as e:
        print(f"General Exception: {str(e)}")


# Example usage
data_list = [None, [1, 2, 3], '', "Hello, World!"]

for data in data_list:
    process_data(data)


#File handling
# File Writing (w+ mode)
file_path = "example.txt"

# Writing to a file (creating a new file or overwriting an existing file)
with open(file_path, "w+") as file:
    file.write("Hello, World!\n")
    file.write("This is an example file.\n")
    file.write("Writing data using Python.\n")

# File Reading (r mode)
with open(file_path, "r") as file:
    contents = file.read()
    print("File Contents:")
    print(contents)

print()

# Appending to a file (a mode)
with open(file_path, "a") as file:
    file.write("Appending additional content.\n")

# File Reading after appending
with open(file_path, "r") as file:
    print("File Contents after Appending:")
    contents = file.read()
    print(contents)

print()

# File Reading and Writing (a+ mode)
with open(file_path, "a+") as file:
    file.write("Modifying the file using a+ mode.\n")
    file.seek(0)  # Move the file pointer to the beginning
    contents = file.read()
    print("File Contents with a+ mode:")
    print(contents)

print()

# File Reading and Writing (w+ mode)
with open(file_path, "w+") as file:
    file.write("Overwriting the file using w+ mode.\n")
    file.seek(0)  # Move the file pointer to the beginning
    contents = file.read()
    print("File Contents with w+ mode:")
    print(contents)

print()

# File Deletion
import os

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File does not exist.")


"""