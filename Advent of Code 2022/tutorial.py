# Casting
import math

print("Casting:")
a = "5"
print('print 5 as sting')
print(a)
a = int(a)
print('cast to integer')
print(a, '\n')

# Variable assignment
print("Variable assignment:")
a, b, c = 'This', "that", 'or this'
d = e = f = "three"
print(d, e, f)

# unpack list
print("Unpack list:")
items = ["item1", 'item2', 'item3']
a, b, c = items
print(a, b, c + '\n')

# printing
print("Printing:")
x = 5
y = 'john'

# use comma to support different data types
print(x, y + '\n')

# Functions: need two blank lines before and after
print("Functions:")


def first_function():
    print("Let's go!")


first_function()

# Global space
print("Global space/key word")

global_var = 5


def global_function():
    # When adding comments do so inside the function as opposed to
    # Before like in java. Max of 72 characters in a line
    global global_var
    global_var += 10


global_function()
print(global_var)

# Data types
print("Data Types:")

x = "hello world"
print(x, type(x))
x = 20
print(x, type(x))
x = 20.4
print(x, type(x))
x = 1j
print(x, type(x))
# This is a list (mutable)
x = ["one", "two", "three"]
print(x, type(x))
# this is a tuple (immutable)
x = ("one", "two", "three")
print(x, type(x))
# sequence from 0 (by default) to x
x = range(5)
print(x, type(x))
# Dictionary stores key value pairs
x = {
    "key": "value",
    "key2": "value2"
    }
print(x, type(x))
# Creates a set (set theory applies)
x = {"one", "two", "three"}
print(x, type(x))
# Frozen set (immutable) generated from an iterable.
# Iterable type declaration
y = ["one", "two", "three"]
x = frozenset(y)
print(x, type(x))
x = True
print(x, type(x))
# Bytes type (immutable)
x = b"Hello"
print(x, type(x))
# Mutable array of x bytes (each representing a character)
x = bytearray(5)
print(x, type(x))
# Uses c like buffer system to reference data rather than making copies
# think of as pointer
x = memoryview(bytes(5))
print(x, type(x))
# Data type to show that variable simply has no value
x = None
print(x, type(x))

# To set specific data types use their name followed by parentheses
# as a constructor

x = float(4.5)
# Notice here we don't use square brackets. This follows for all constructors
x = list(("one", "two", "three"))

# Only three numeric values in python int float and complex
# Convert between by casting
y = 2.5
a = int(y)

# Random Numbers
print("Random Numbers:")
import random  # Should be at the top of the file

# print random number between 1 and 9 using a range
print("Random number: ", random.randrange(1, 10), "\n")


# Strings
print("Strings:")

# Multiline:
a = """this is an example
of how you can create 
long multiline strings
"""

print(a)
print("the length of the previous string is: ", len(a))

# Strings are just arrays of bytes. So you can access characters using array
# notation

print("The 8th char:", a[8])

# Looping over strings:

print("Loop over string:")
for x in "banana":
    print(x)

print("Check if sequence is present in string")

print("this" in a)
print("that" in a)

if "this" in a:
    print("the word this in present the string a")

if "that" not in a:
    print("The word that is not present in the string a")

print("\n" + "Slicing and arrays")

b = "Hello World"
print(b)
# From character 1 though 10 range
print(b[1:10])
# from the end on
print(b[:5])
# From the beginning on
print(b[6:])
# Start from the end. Calculate the same range tho so from 6 to 9
print(b[-5:-2], "\n")

print("String manipulation:")
# Everything to upper case
print(b.upper())
# Everything to lower case
print(b.lower())
# Remove all white space
print(b.strip())
# Replace x with y
print(b.replace("Hello", "World"))
# Split by substring
a = "This, that, and this"
# Returns a list
a = a.split(",")
print(a, "\n")

print("String Concatenation:")
a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b
print(c, "\n")

print("String formatting:")
number = 87
text = "The lucky number is: {}"
# Value place holders are {}
text = text.format(number)
print(text)
# Format can take any number of arguments
weather = "Snowy"
temp = 23
pressure = 2.5
# Insert many arguments using {} and the format function
text = "The weather today is {}, with the temperature being {}, and the pressure being {}."
print(text.format(weather, temp, pressure))
# Specify the location of replacements by using index numbers
text = "The weather today is {2}, with the temperature being {0}, and the pressure being {1}."
print(text.format(temp, pressure, weather), "\n")

print("Escape character:")
# use backslash to indicate the start of an escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
print()
txt = "Backspace \b, Force Feed: \f, Octal Value: \110, Hex Value: \x1f Backslash: \\, Tab \t,  return character: \r"
print(txt, "\n")

# Booleans
print("Booleans:")
# Check if a variable is a particular type
x = "string"
if isinstance(x, str):
    print(x, "is a string\n")
else:
    print(x, "is not a string")

# Operators
print("Operators:")
print("Addition 5 + 5 ", 5+5)
print("Subtraction 5 - 5 ", 5-5)
print("Multiplication 5 * 5 ", 5*5)
print("Division 5 / 5 ", 5/5)
print("Mod math 5 % 5", 5 % 5)
print("Exponents 5**5", 5**5)
print("Floor division 7//53", 7//3)

# And equals
false_list = [True, True, True, False, True]
true_list = [True, True, True]
all_false = [False, False, False, False, False, False]


def check_all_true(input_list):
    state = True
    for element in input_list:
        state &= element
    return state


def check_at_least_one_true(input_list):
    state = False
    for element in input_list:
        state |= element
    return state


print(check_all_true(false_list))
print(check_all_true(true_list))
print(check_at_least_one_true(all_false))

# List stuff
print("List Stuff")

lst = list((True, "False", 'that', False, True, "What", "Frog"))
print("Full list", lst)
# Use list notation to select a range
print("From 2 to the end of list -1", lst[2:len(lst)-1])
# Get the first half
print("Get the first half", lst[:(len(lst)//2)-1])
# Get the last half
print("Get the last half", lst[math.ceil(len(lst)/2):])

# Exists in list
if True in lst:
    print("True in lst")

if "Banana" in lst:
    print("Banana in lst")

# Change value
lst[0] = "New Value!"
print(lst)

# Change range
lst[2:4] = ["New Val 2", "new Val 3"]
print(lst)

# if the range is not
lst[0:3] = ["New"]
print(lst)

f = 50



