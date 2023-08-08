#Day 6
"""
Advanced concepts in python
"""
#Regular expressions
"""
summary
\d: matches any digit
\w: matchesa any alphanumeric character
\s: matches any white space character(tab space or newline)
.: matches any character except a newline
*: matches zero or more occurences of the preceding character or group
+: matches one or more occurences of the preceding character or group
?: matches one or one occurences of the preceding character
[]: matches any character within the square brackets
[^]: matches any character not within the square brackets
^: matches the start of a line
$: matches the end of a line"""

#\b is for boundaries

#Matching and searching
#regex re.match(), re.search(), re.findall()

#Example1 Demonstrating regex |Match first word, match group word, match all work numbers
import re
text = "hello my name is collins, I am a programmer"

#Match first word
match = re.search(r"\b\w+\b", text)

if match:
    print("Matches:", match.group())

matches = re.findall(r"\d+", text)

if matches:
    print("Matches:", matches)
print("============================================================")
#Example 2 validate email format
import re

def validate_email(email):
   pattern = r'^[\w\.-]+@[\.\w\.-]+\.\w+$' 

   if re.match(pattern, email):
    return True
   else:
    return False
   
email1 = "ckato123@gmail.com"
email2 ="collin.com"
print(validate_email(email1))
print(validate_email(email2))
print("============================================================")
#Generators and Iterators
""" Generators allows efficient and iterative 
defined using the 'yield' keyword
Iterators are objects that implement inter objects
'__iter__' 
 '__next__'
"""
#Example generator
def factorial(n):
   #Return the factorial of  a number
   if n == 0:
      return 1
   else:
      return n*factorial(n-1)
   
#Print the factorial of a number from 1 - 10
for i in range(1,10):
   print(factorial(i))

def factorial_generator(n,m):
    for i in range(n,m):
        yield factorial(i)

factorial_generator(10,15)
for factorial_value in factorial_generator(1, 10):
   print(factorial_value)
   
   
def fact(n):
   #Return the factorial of  a number
   if n == 0:
      yield 1
   else:
      fac = 1
      for i in range(1, n+1):
        fac *= i
      yield fact

for i in range(1,6):
   print(factorial(i))
print("============================================================")

#Example 3
#Generate function that yields the square of numbers from 1 to 10
def squares():
   for i in range(1,10):
      yield i**2

#Create an iterator object that yields the square of numbers 1-10
squares_iterator = squares()

#Print the first 5 squares of numbers 1-10
for i in range(5):
   print(next(squares_iterator))

print("============================================================")
#Decorators @my_decorator
#modify the behavior of functions or classes without directly changing thier source code
#Takes a fuction and returns a function that

def my_decorator(func):
   def inner():
      print("Hello, this is my decorator")
      func()

   return inner

@my_decorator
def outer_decorator():
   print("This is outer decorator")

outer_decorator()
print("================================================")


#Assignment
#Show a context manager for file handling that automatically opens and closes a file
#Context manager is an object that defines temporary context for a block of code
#Useing context manager fo file handling ensures that the file is closed properly and helps prevent 
#resource leaks or errors
with open('kato.txt', 'r') as file:
   data = file.read()
   print(data)
#Theres no need to explicitly close the file
print("================================================")
#Show a context manager for managing database connections
#Use the contextlib module and define a class that implements the __enter__() and __exit__() methods
import sqlite3 
from contextlib import contextmanager

@contextmanager
def database_connection(database):
   connection = sqlite3.connect(database)
   try:
      yield connection
   finally:
      connection.close()

#usage example
database_name = "mydatabase.db"
with database_connection(database_name) as connection:
   cursor = connection.cursor()

#the connection is automatically closed at the end
#the connection is closed and not accessible outside of the with block

#show a multithreading and procesing that allows us to run the function for different amounts of time
import time
import threading
import multiprocessing
#Define a function that takes a duration in seconds

def process_data(duration):
   print(f"Starting processing for {duration} seconds")

   time.sleep(duration)

   print(f"Processing completed for {duration} seconds")

#Using multithreading
def run_with_threads():
   durations = [1,2,3,4,5]

#Create and start threads for each duration
   threads = [] 
   for duration in durations:
      t = threading.Thread(target=process_data, args=(duration,))
      t.start()
   threads.append(t)

#wait for all threads to complete 
   for t in threads:
     t.join()

#Using multiprocessing
def run_with_processes():
   durations = [1,2,3,4,5]

#Create and start processes for each duration
   processes = [] 
   for duration in durations:
      p = multiprocessing.Process(target=process_data, args=(duration,))
      p.start()
   processes.append(p)

#wait for all processes to complete:
   for p in processes:
        p.join()

#Run with multithreading
run_with_threads()
print("================================================================")

#run with multiprocessing
#placing  the run_with_processes code inside 'if_name_" == "__main__" block ensures that the multiprocessing code
# is run directly as the main module. it prevents issues related to spawning child processes recursively

if __name__ == "__main__":
   run_with_processes()
