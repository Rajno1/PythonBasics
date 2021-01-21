""" You can loop through the list item using 'for' loop """
list=["Apple","Windows","Mac","Iphone","Anar"]
print("printing list using for loop")
for x in list:
    print(x)

# we can loop list based on index,Use the range() and len() functions to create a suitable iterable.
# The iterable created in the example above is [0, 1, 2,3].
print("printing list using for loop based on item index")
for i in range(len(list)):
    print(list[i])

print("printing using while loop")
j=0
while j < len(list):
    print(list[j])
    j=j+1


''' List Comprehension offers the shortest syntax for looping through lists:
A short hand for loop that will print all items in a list:'''
print("Printing using loop comprehension")
[print(x) for x in list]

""" Loop comprehension
    using Loop comprehension , we can print list items with a letter in the name """

[print(x) for x in list if 'A' in x]
# syntax : newlist = [expression for item in iterable if condition == True]