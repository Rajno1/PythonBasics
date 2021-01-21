class Person:                           # created Person class using 'class' keyword
    def __init__(self, name1,age1):     # The __init__() function is called automatically every time the class is being used to create a new object and we are passing two arguments as name1 and age1
        self.name=name1              
        self.age=age1
    def methodOne(self,rollnum):
        print("This is method one ")
        self.roll=rollnum

p1 =Person("Raj",30)
p1.methodOne(442)

print("Name of the persion is {} ".format(p1.name))
print("age of {} is {}".format(p1.name,p1.age))
print("And roll number is {} ".format(p1.roll))