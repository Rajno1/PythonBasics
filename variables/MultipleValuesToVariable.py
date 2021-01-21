"""
Python allows you to assign many values to multiple variables
we can assign one value to multiple variables
if you have a collection of values in a list, Python allows you to extract the values to
variables- this called unpacking
"""
# assigning many values to multiple variables
x,y,z="Raju",2,True
print(x+" is",type(x),"datatype")

print(type(y),y)
print(type(z),z)

# we can assign one value to many variables as well
x=y=z="orange"
print(x,y,z)

# unpacking
fruits = ["Apple","Banana","Mango"]
a,b,c =fruits
print(a)
print(b)
print(c)