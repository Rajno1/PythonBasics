"""
Variables that are created outside of a function are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
"""
x='awesome'    # this is golbal variable
def myfunc():  # we created a method
    print('Python is ' + x)
myfunc()  # we are executing the method by calling it.

"""
if you create a variable with same name(of global variable) inside a function, this variable will be local
and can be used inside that particular function only
The global variable with the same name will remain as it was
IMP -> we can also declare global inside a function using 'global' keyword 
"""
def secondfun():
    global x
    x='fantastic'  # this is local variable , in the above line since we declared it with the help of 'global' keyword now it is global variable.
    print('Python is '+ x)
secondfun()
print(x)  # global variable will be remains same
