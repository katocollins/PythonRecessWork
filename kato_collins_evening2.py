#Exercise 1(Lists)
#No.1 
company = ["Microsoft","Apple","Meta","Amazon","Twitter"]
print(company[1])
#No.2
company[0] = "Alibaba"
print(company)
#No.3
company.append("Google")
print(company)
#No.4
company[2] = "Bathel"
print(company)
#No.5
company.remove("Amazon")
print(company)
#No.6
print(company[-1])
#No.7
fruits = ["Banana","Pineapple","Apple","Grapes","Mangoes","Peas","bread"]
for element in fruits[2:5]:
	print(element)
#No.8
countries = ["Uganda", "Kenya", "Tanzania","Canada","South-Korea"]
countries2 = countries.copy()
print(countries)
print(countries2)
#No.9
for item in countries:
	print(item)
#No.10
animals = ["Monkey","Ape","Lion","Tiger","Cow","Goat","Giraffe"]
print(sorted(animals))
print(sorted(animals, reverse=True))

#No.11
for animal in animals:
  if "a" in animal:
     print(animal)
#No.12
list1 = ["Kato"]
list2 = ["Collins"]
list1 += list2
print(list1)
print("======================================================")

#Exercise2
#No.1
x = ("Samsung","iphone","tecno","redmi")
print(x[1])
#No.2
print(x[-2])
#No.3
#x[1] = "itel" Not possible because tupples are immutable
#No.4
#x.append("Hauwei")Not possible because tuples are immutable
#No.5
for i in x:
  print(i)
#No.6
#del x[0]Not possible because tuples are immutable
#No.7
cities = tuple(["Kampala","Mbale","Mbarara","Jinja","Arua"])
print(cities)
#No.8
a,b,c,d,e = cities
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
#No.9
for v in cities[1:4]:
  print(v)
#No.10
fname = ("Edin")
lname = ("Faith")
full_name = fname + lname
print(full_name)
#No.11
colors =("yellow","green","blue","red")
print(colors*3)
#No.12
thistuple = (1,3,7,8,7,5,4,6,8,5)
print(thistuple.count(8))
print("======================================================")

#Exercise 3
# Create a set of 3 favorite beverages
favorite_beverages = {"coffee", "tea", "water"}
# Add 2 more items to the beverages set
favorite_beverages.update(["milk", "soda"])
# Check if microwave is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
  print("Microwave is present in the set")
else:
  print("Microwave is not present in the set")
# Remove "kettle" from the set
mySet.remove("kettle")
# Loop through the set
for item in mySet:
  print(item)
# Create a set of 4 items and a list of two items
set_of_items = {"apple", "banana", "orange", "grape"}
list_of_items = ["pear", "kiwi"]
# Add elements in the list to elements in the set
set_of_items.update(list_of_items)
# Write two sets, one containing your ages and the other your first names
ages = {18, 21, 25}
first_names = {"Kato", "Mary", "Lule"}
# Join the two sets
joined_sets = ages | first_names
# Print the joined sets
print(joined_sets)
print("======================================================")

#Excersise 4
""" Declare two variables, an integer and a string and use the correct method to concatenate the
two variables."""
integer = 10
string = "Hello, Uganda!"
concatenated_string = str(integer) + string
print(concatenated_string)
# Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "
txt = txt.strip()
print(txt)
# Write a python program to convert the value of ‘txt’ to uppercase.
txt = txt.upper()
print(txt)
# Write a python program to replace character ‘U’ with ‘V’ in the string above.
txt = txt.replace("U", "V")
print(txt)
"""Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position."""
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print(range_of_characters)
# The piece of code below will give an error when output;
# x = “All “Data Scientists” are cool!”
# Write a python program to correct it.
x = "All \"Data Scientists\" are cool!"
print(x)
print("======================================================")

#Exercise 5
# Create a dictionary of shoes
Shoes = {
"brand": "Nick",
"color": "black",
"size": 40,
}
# Print the value of the shoe size
print(Shoes["size"])
# Change the value of "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
# Add a key/value pair "type": "sneakers" to the dictionary
Shoes["type"] = "sneakers"# Return a list of all the keys in the dictionary
keys = Shoes.keys()
print(keys)
# Return a list of all the values in the dictionary
values = Shoes.values()
print(values)
# Check if the key "size" exists in the dictionary
if "size" in Shoes:
  print("The key 'size' exists in the dictionary.")
else:
  print("The key 'size' does not exist in the dictionary.")
# Loop through the dictionary
for key, value in Shoes.items():
  print(f"Key: {key}, Value: {value}")
# Remove "color" from the dictionary
Shoes.pop("color")
# Empty the dictionary
Shoes.clear()
# Create a dictionary of your choice and make a copy of it
dictionary = {
"name": "Daily Dev",
"age": 30,
"occupation": "Software Engineer",
}
copy_of_dictionary = dictionary.copy()
# Write a python program to show nested dictionaries
nested_dict = {
"name": "Daily Dev",
"age": 32,
"occupation": "Software Engineer",
"address": {
"street": "123 Main Street",
"city": "Kampala",
"state": "CA",
"zipcode": 12345
}}
print(nested_dict)

