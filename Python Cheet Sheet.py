# This is a comment

print('Hello World!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

# Variables and Types
# Do not need to declare variables before using them, or declare their type. Every variable is an object
firstName = 'George'
myLocation = "England" # Either quotes can be used
myInt = 5
myFloat = float(5)

# Lists (Arrays equivalent)
# Contain any type of variable and hold as many as wish.
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])

# prints out all
for x in mylist:
    print(x)

# Basic Operators
number = 1 + 2 * 3 / 4.0
print(number)
remainder = 11 % 3
print(remainder)
squared = 7 ** 2
helloWorld = "hello" + " " + "world"
lotsofhellos = "hello" * 10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# Boolean Operators 
# Python uses boolean varaibles to evaluate conditons. The values True and False are returned.
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# Python uses indentation to define code blocks, instead of brackets.
# The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent.

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# Loops - Only two types, for and while.
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# Functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)


# Classes and Objects
# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your objects.

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)
myobjectx.function()

# Dictionaries - Keys and Values instead of indexes.
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

#Built-in functions
input(s) # - Prints s and waits for an input that will be returned
len(x)   # returns length of x
min(L) # returns the minimum value in L
max(L) # returns the maximum value in L
sum(L) # returns the sum of the values in L
type(x) # returns type of x (string, float etc.)
str(x)  # Converts x to string
int(x)  # Converts x to int
float(x) # Convertx x to float number
