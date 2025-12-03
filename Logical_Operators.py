x = 5
y = 10

# and operator

print(x > 3 and y < 20)
print(x > 7 and y < 20)

# or operator

print(x > 3 or y < 5)
print(x > 7 or y < 5)

# not operator

print(not(x > 3))
print(not(x < 3))

# Classes and Objects

class Dog:
   def bark(self):
      print("Woof woof!")

my_dog = Dog()
my_dog.bark()

class Car:
   def drive(self):
      print("The car is moving")

my_car = Car()
my_car.drive()