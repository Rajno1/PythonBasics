"""
* In python a variable is created the moment you assign a value to it.
* In python variables do not need to be declared with any particular type, and even can change the type after they have been set
* if you want to specify the data type of a variable , this can be done with casting
* variable are case sensitive and do difference for single quote and double quote

a variable name must start with a letter or underscore '_'
variable CANNOT start with number
variable should contain (a-z,A_Z,0-9 and _ ){remember case sensitive}
variable with multi words
myVariableName  -> except first starts with capital letter (camel case)
MyVariableName -> each word starts with capital letter (pascal case)
my_variable_name -> each word is separated by underscore (snake case)
"""

# The moment you assign a value , variable will get create
x = 5
print(x)

# if you want to specify datatype you can do it in two ways
x=int(6)
print(x)

y:int=7
print(y)

s=str("Welcome")
print(s)

# you can get the data type of a variable using type()
print(type(s))
print(type(x))
print(type(y))

# variable are case sencitive and do difference for single quote and double quote

