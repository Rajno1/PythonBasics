"""
As we learned in the Python Variables chapter, we cannot combine strings and numbers
But we can combine them using 'format()' method

The format() method takes the passed arguments, formats them,
and places them in the string where the placeholders {} are:
"""
a= 30
txt = "I am Raj,and i am {}"
print(txt.format(a))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders
message = "i want {} kfc leg pieces of {} for {} rupees"
b=250
c=3
d=150
print(message.format(c,b,d))