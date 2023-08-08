my_dict = {
"name": "Kato",
"age": 100,
"country": "USA",
}
# Accessing a value in a dictionary
name = my_dict["name"]
print(name)

# Adding a key-value pair to a dictionary
my_dict.update({"city": "New York"})
print(my_dict)

# Removing a key-value pair from a dictionary
my_dict.pop("age")
print(my_dict)

# Iterating over a dictionary
for key, value in my_dict.items():
   print(key, value)

my_string = "This is a string"
# Accessing a character in a string
first_character = my_string[0]
print(first_character)

# Slicing a string
sliced_string = my_string[2:5]
print(sliced_string)

concatenated_string = my_string + " and this is another string"
print(concatenated_string)

# Checking if a string contains a substring
if "string" in my_string:
   print("The string contains the substring 'string'")

# Formatting a string
formatted_string = "The value of pi is {:.2f}".format(3.14159)
print(formatted_string)

# Define some variables
int_value = 10
float_value = 10.5
complex_value = 10 + 2j
# Convert int to float
float_from_int = float(int_value)
print(float_from_int)

# Convert float to int
int_from_float = int(float_value)
print(int_from_float)

# Convert complex to float (Not POssible)
#float_from_complex = float(complex_value)
#print(float_from_complex)

# Convert complex to int(NOt POssible)
#int_from_complex = int(complex_value)
#print(int_from_complex)

def exercise():
# Create a dictionary
dict = {"name": "John Doe", "age": 30, "occupation": "Software Engineer"}
# Use the values() method to create a list of items from a dictionary
values = dict.values()
print(values)
# Check if a specific key exists in a dictionary
if "name" in dict:
  print("The key 'name' exists in the dictionary.")
# Change and update items in a dictionary
dict["age"] = 31
print(dict)
# Add and remove items from a dictionary
dict["city"] = "San Francisco"
print(dict)
del dict["occupation"]
print(dict)
# Demonstrate looping through a dictionary and nesting dictionaries within dictionaries
for key, value in dict.items():
print(key, value)
# Determine the length of a string using the len() function
str = "This is a string."
print(len(str))
# Iterate through each character in a string using a for loop
for char in str:
print(char)
# Slice a string to extract specific portions of it
slice_str = str[0:5]
print(slice_str)
# Perform arithmetic operations with numbers and print the results
num1 = 10
num2 = 20
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)print(num1 / num2)
# Use boolean values and conditions to control program flow
if num1 > num2:
print("num1 is greater than num2.")
else:
print("num2 is greater than num1.")
