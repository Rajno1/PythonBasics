"""
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".

However, Python does NOT have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
"""
a = "Python"
print(a[3])  # python does NOT have a character data type, Square brackets can be used to access elements of the string.

# remember that the first character has the position 0

# looping to print each character of a string
for x in "banana":
    print(x)

# to get length of a string we use 'len()' function

a="Hello"
print('length of a is ',len(a))

# to check a phrase in string , we use 'in' keyword
print("Hello" in a)  # if 'Hello' is in a it will print 'True' , if not 'False'
print("World" in a)  # this will print false

if "World" in a:
    print("World is in a")
else:
    print("World is not in a ")
