#Regular Expressions
import re

tep = "Makerere UNiversity"
tem = re.search(r"\w+", tep)

if tem:
    print("Matches:", tem.group())

# Pattern to search for 'apple' or 'banana'
pattern = r'apple|banana'

text = 'I like apples and bananas'
matches = re.findall(pattern, text)
print(matches)

# Pattern to replace 'apple' with 'orange'
pattern = r'apple'

text = 'I have an apple'
replaced_text = re.sub(pattern, 'orange', text)
print(replaced_text)

# Pattern to split a string at every occurrence of a comma
pattern = r','

text = 'apple,banana,orange'
splitted_text = re.split(pattern, text)
print(splitted_text)

# Pattern to extract a name and age from a string
pattern = r'(\w+) is (\d+) years old'

text = 'John is 25 years old, and Jane is 30 years old'
matches = re.findall(pattern, text)
for match in matches:
    name, age = match
    print(f'{name} is {age} years old')

#Generators and Iterators
def factorial_generator(n):
    current = 0
    while current <= n:
        yield factorial(current)
        current += 1

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Using the generator
factorial_generator_obj = factorial_generator(5)
for num in factorial_generator_obj:
    print(num)


class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            value = self.start
            self.start += 1
            return value
        else:
            raise StopIteration


# Using the iterator
my_iterator = MyIterator(1, 5)
for num in my_iterator:
    print(num)


#Decorators
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result
    return wrapper

# Applying the decorator
@measure_time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the decorated function
result = factorial(5)
print(result)

#Email Validation with Regex
def validate_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True, "Email is Valid"
    else:
        return False, "Invalid Email"

# Testing the function
e1 = "ckato131@gmail.com"
e2 = "frandj.com"

print(validate_email(e1))
print(validate_email(e2))

#Password Validator
def validate_password(password):
    # Minimum length of 8 characters
    if len(password) < 8:
        return False, "Must be 8 and above characters"

    # At least one uppercase letter, one lowercase letter, and one digit
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)'
    if re.search(pattern, password):
        return True, "Valid Password"
    else:
        return False, "Invalid Password"

# Testing the function
pass1 = "passwr"
pass2 = "Kcoll32&"

print(validate_password(pass1))
print(validate_password(pass2))