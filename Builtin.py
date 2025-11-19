print("Hello world")
#len()
lent = len("SIXSEVEN!!!!!!")
print(lent)
# type()
wording = type(True)
print(wording)
# int()
num = int(67)
print(num)
# float()
deci = float(6.7)
print(deci)
# str()
word = str("SIXSEVEN")
print(word)
# max()
Biggest = max(6,7,67)
print(Biggest)
# min()
Smallest = min(6,7,67)
print(Smallest)
# sum()
# range()
# input()
# list
numbers = [1,4,7,4,2,9,6,3,15,6,7]
for i in range(3,15,2):
    print(i)

print(sum(numbers))

# Functions with parameters
def greet(name):
    print("Hello, " + name + ".")

greet("Kamsi")
greet("Bohdan")

def add(x, z):
    result = x + z
    print("The result is:", result)

x = int(input("Enter a number for x: "))
z = int(input("Enter a number for z: "))

add(x, z)

#User defined functions
number = int(input("Enter a number to check if it is even "))

def check_even (number):
    if number % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

check_even(number)

#Coding Challenge
def find_largest(a, b, c):
    return max(a, b, c)
print(find_largest(6, 7, 8))