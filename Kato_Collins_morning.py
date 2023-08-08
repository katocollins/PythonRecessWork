#CONTROL Flow in Python

#Conditional Statements
"""
These execute when a given conditional is met. 
They include the if, else if and the else.
"""
#Examples

age = int(input('Enter Your Age\n'))

if age <=25:
	print('You are YOUNG')
elif age >20 and age <=50:
	print('You are and ADULT')
else:
	print('You are OLD')

#LOOPS
"""
For Loops: These are essential in iterration of data structures.
We can use them to access elements of LIsts, tuples, ranges, etc.
"""
#Illutrations
mylist = ["Samsung","Apple","Microsoft","Amazon","Meta"]

for tech in mylist:
	print(tech)

""" 
I will iterate through a range of 2 to 30 to return
numbers  in a sequence with with comon difference of 3
"""
for y in range(2,30,3):
	print(y)

"""
WHILE loops: Continues to execute until the condition 
evaluates to false. Checks the condition repeatedly before iteration
"""

#Example

reem = list(range(2,30,3))

i = 0

while i< len(reem):
   if reem[i]%2==0:
     print(reem[i])   
   i+=1

# Break statement
for i in range(10):
  if i == 5:
    break
  print(i)
# Continue statement
for i in range(10):
   if i % 2 == 0:
     continue
   print(i)
# Pass statement
for i in range(10):
   if i == 5:
     pass
   print(i)

def divide_numbers(x, y):
 try:
   return x / y
 except ZeroDivisionError:
   print("Division by zero error")
 finally:
   print("This code is always executed")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))

mental_status = {
1: "Autism spectrum disorder",
2: "Dementia",
3: "Schizophrenia",
4: "Post-traumatic stress disorder (PTSD)",
5: "Anxiety disorder",
6: "Bipolar disorder",
7: "Moderate depression (score of 20-29 on the PHQ-9)",
8: "Mild depression (score of 10-19 on the PHQ-9)",
9: "Normal",
10: "Awesome"
}

status_code = int(input("On a SCale on 1-10, How do you feel now?\n"))

if status_code in mental_status:
    print(mental_status[status_code])
     




 

