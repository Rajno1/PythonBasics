"""
To insert characters that are illegal in a string, we use an escape character.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

Example
txt = "We are the so-called "Vikings" from the north."

To fix this problem, use the escape character \":
"""

# txt = "We are the so-called "Vikings" from the north."
txt = "We are the so-called \"Vikings\" from the north."
print(txt)