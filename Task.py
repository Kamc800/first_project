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