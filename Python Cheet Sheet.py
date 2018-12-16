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

# If Statements 
# Python uses indentation to define code blocks, instead of brackets.
# The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent.

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12: 
    print('You are not Alice, kiddo.')
else: 
    print('You are neither Alice nor a little kid')

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

for x in mylist:
print(x)

# Loops - Only two types, for and while.

#For Loops 
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# While Loops
goals = 0
while goals < 5:
    print('Game not over yet')
    goals += 1

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

while True: 
    print('Who are you?')
    name = input() 
    if name != 'George':
        continue         # Go back to start of Loop if name not George
        print('Hello, George. What is the password?')
        password = input()
        if password == 'pikachu'
            break 
            print('Access granted.')

# Functions
def my_function():
    print("Hello From My Function!")


def hello(name):
    print('Hello ' + name)
hello('George')

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

# Lists (Arrays equivalent)
# Contain any type of variable and hold as many as wish.
mylist = ['robot', 'monster', 'zombie']
mylist[2] = 'witch'
del mylist[2]
mylist.append('wizard') # add to end
mylist.insert(0, 'dragon') # choose position
mylist.remove('wizard')
mylist.sort()
print(mylist[0])
# Slice - Multiple values except at second index, returns one before that
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1:3] # = ['bat', 'rat']

# Tuples - Immuatable like strings (cannot be modified), as opposed to Lists (mutable)
stuff = ('hello', 42, 0.5)

# Dictionaries - Keys and Values instead of indexes.
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

""" 
 \'Single quote
 \" Double quote
 \t Tab
 \n Newline (line break)
 \\ Backslash
"""
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


# Magic 8 Ball

import random 
 def getAnswer(answerNumber):
     if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

 r = random.randint(1, 9)
 fortune = getAnswer(r)
 print(fortune)

 # Guess the Number 
 import random
 secretNumber = random.randint(1, 20)
 print('I am thinking of a number between 1 and 20')

 # Ask the player to guess 6 times 
 for guessesTaken in range (1, 7):
     print('Take a guess.')
     guess = int(input())

     if guess < secretNumber:
         print('Your guess is too low.')
    elif guess > secretNubmer:
        print('Your guess is too high.')  
    else: 
        break   # This condition is the correct guess
    
    if guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) + ' guessess!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))

