# For loop statements
# Example 1
fruits = ["apple","watermelon", "grape"]

for fruit in fruits:
    print(fruit)

# Example 2
letters = "International"

for letter in letters:
    print(letter)

# Example 3
for i in range(8):
    print(i)

#Example 4
for i in range(1, 12):
    print(i)

# Task
for i in range(2, 11, 2):
    print(i)

# For Loop and If statement
#Example 1
for i in range(1, 11):
#L 
# Looping through numbers from 1 to 10
 if i % 2 == 0:
# Check if the number is even
    print(i)

# Example 2
numbers = [5, -3, 12, -7, 9, -2]

positive_count = 0 # Initialize the counter

for num in numbers:
   if num > 0: # Check if the number is positive
      positive_count += 1 # Increment the counter

print("Number of positive numbers:", positive_count)

# Example 3
for i in range(1, 68):
   if i % 3 == 0 and i % 5 == 0:
      print("ChickenBanana")
   elif i % 3 == 0:
      print("Chicken")
   elif i % 5 == 0:
      print("Banana")
   else:
      print(i)

# While Loop and If Statement
# Example 1
number = 1


while number <= 20:
   if number % 2 == 0:  # Checks if the number is even
      print(number)
   number += 1   # Increment the number by 1

# Example 2
i = 1

while i <= 67:
   if i % 6 == 0 and i % 7 == 0:
      print("SIXSEVEN!!!")
   elif i % 6 == 0:
      print("SIX!!!")
   elif i % 7 == 0:
      print("SEVEN!!!")
   else:
      print(i)
   i += 1


# Lists
Fruits = ["apple", "watermelon", "banana"]
print(Fruits[0])
print(Fruits[1])

Fruits[2] = "grape"
print(Fruits)

Fruits.append("dragon fruit")
print(Fruits)

Fruits.insert(3, "pomegranate")
print(Fruits)

Fruits.remove("pomegranate")
print(Fruits)

Fruits.pop()
print(Fruits)

Fruits.pop(2)
print(Fruits)

Fruits.reverse()
print(Fruits)

Cars = ["Toyota Camry", "Ford Mustang", "Honda Civic"]
print(Cars[0])
print(Cars[1])
print(Cars[2])
print(Cars)

# Dictionary
#Example
friend = {
   "name": "Richard",
   "age": 11,
   "Gender": "Male",
   "year_of_birth": 2013,
}
print(friend)
print(friend["year_of_birth"])
friend["year_of_birth"] = 2014
print(friend)
friend["country"] = "?"
print(friend)
if("colour" in friend):
   print("Yes there is colour")
else:
   print("No colour 😢")
for key in friend:
   print(key, ":", friend[key])

# Functions
def greet():
   print("Hello, friend!")

greet()

def add(a, b):
   return a + b
print(add(6,7))

name = input("What is your name? ")
age = input("How old are you? ")
print("Hello, " + name + "!. " "I believe you are " + age + " years old " + name + ".")

# Test
Name = input("What is your name? ")
print("Hello, " + Name + ".")
Word_Length_Checker = input("Please write any word ")
print(len(Word_Length_Checker))
Num1 = int(input("Enter a number "))
Num2 = int(input("Enter a second number "))
def sum(Num1, Num2):
   return Num1 + Num2
print(sum(Num1, Num2))
Biggest_number = max(3,7,8)
print(Biggest_number)
Data_Type = type("Enter anything ")
print(Data_Type)