# https://www.learnpython.org/


# hello world
print("HELLO WORLD")


print("Hello World")

x = 1
if x == 1:
    print("x == 1")
    print(x)

print("goodbye world")

# vars and types
print("VARS AND TYPES")

myint = 5
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(2)
print(myfloat)

mystring = "hello"
print(mystring)

## can use apostrophes (use double quotes "")
mystring = "amazing apostrophes aren't annoying at all"
print(mystring)

a = 1
b = 2
c = a + b
print(c)

d = "hello"
e = "world"
print(d + " " + e)
print(str(a) + " and " + str(b))


mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

# lists
print("LISTS")

mylist = []
mylist.append(1)
mylist.append("two")
mylist.append(3)

for x in mylist:
    print(x)


numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# basic operators
print("BASIC OPERATIONS")

number = 10 / 5 * 4 + 9
print(number)

remainder = number % 5
print(remainder)

number = number % 3
print("number = " + str(number))
## power is **
squared = remainder ** 2
cubed = number ** 3

print("squared = " + str(squared))
print("cubed = "  + str(cubed))

helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 5
print(lotsofhellos)

print([1,2,3] * 3)


x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# string formatting
print("STRING FORMATTING")

name = "john"
print("hello, %s" % name)

age = 34
print("%s is %d years old" % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

'''
%s = string
%d = ints
%f = floats
%.<number of digits>f = floats with fixed amt of digits 
%x/%X = ints in hex rep (lower and uppercase)
'''


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s." 

print(format_string % data)

# basic string operations
print("BASIC STRING OPERATIONS")

astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

print(astring.index("o"))

print(astring.count("l"))

print(astring[1:7])

print(astring[-4:-2])
print(astring[2:-2])

## [start:stop:step]
print(astring[3:7:2])

print(astring[3:7])
print(astring[3:7:1]) 

print(astring[2:8:2]) 

## reverse string
print(astring[::-1])

print(astring.upper())
print(astring.lower())

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")
print(afewwords)


s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

# conditions
print("CONDITIONS")

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

if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    print("true")
    pass
elif another_statement is True: # else if
    print("false")
    pass
else:
    print("huh")
    pass

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

print(not False) # Prints out True
print((not False) == (False)) # Prints out False


# change this code
number = 16
second_number = False
first_array = [True, True, True]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

# loops
print("LOOPS")

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

count = 0
while count < 5:
    print(count)
    count += 1

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

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)

# functions
print("FUNCTIONS")

def my_function():
    print("Hello From My Function!")

my_function()

def fizz_buzz(stop, fizz, buzz):
    num = 0
    while stop > num:
        if num%fizz == 0 and num%buzz == 0:
            print("fizzbuzz")
        elif num%fizz == 0:
            print("fizz")
        elif num%buzz == 0:
            print("buzz")
        else: 
            print(num)
        num += 1

fizz_buzz(31, 3, 5)

## skipping bc i know

# classes and objects
print("CLASSES AND OBJECTS")

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

print(myobjectx.variable)
myobjectx.function()

myobjecty.variable = "yackity"
print(myobjecty.variable)

class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
# your code goes here
car1 = Vehicle()
car1.name = "fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

# dictionaries
print("DICTIONARIES")

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

del phonebook["John"]
print(phonebook)

phonebook["John"] = 938477566
print(phonebook)

phonebook.pop("John")
print(phonebook)


phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here

phonebook["Jake"] = 938273443
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")

# modules
print("MODULES")

"""
# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
"""

import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))

# input and output
print("INPUT AND OUTPUT")

astring=input("input a message: ")
print(astring)

num=int(input("put a number: "))
print(num)
decimalnum=input("put a decimal num: ")
print(decimalnum)
decimalnum=float(input("put a float num: "))
print(decimalnum)

#give two integers in first line and more than two integers in third line
a, b = map(int, input("give two integers: ").split())
array = input("give more than two integers: ").split()
sum = 0
for each in array:
    sum = sum + int(each)
print(a, b, sum)  # prints first two integers from first line and sum of integers of second line

a = 5
b = 0.63
c = "hello"
print("a is : %d, b is %0.4f,c is %s" % (a,b,c))


# Taking the name input using input()
name = input("Enter your name: ")

# Taking the age input using input() and converting it to integer
age = int(input("Enter your age: "))

# Taking the country input using input()
country = input("Enter your country: ")

# Displaying the formatted sentence with name, age, and country
print("Hello, my name is {}, I am {} years old, and I am from {}.".format(name, age, country))