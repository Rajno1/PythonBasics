"""
To change the value of a specific item, refer to the index number
"""
list=["ubuntu","windows","linux"]
print(list) # it will print the list above

list[0]="iOS"
print(list) # it will update the item at index 0 with 'iOS' and do print

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second value by replacing it with two new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# *** insert and Add ***
"""
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:
"""
list=["Apple","Banana","Pomegranate"]
list.insert(1,"Mango")
print(list)

'''{ if we want to add list item at particular index we are using 'insert()' method
    in the  same way , we can use 'append()' method to add list item at the end of list items }'''

list1=["father","mother","Daughter"]
list1.append("first son")
list1.append("second son")
print(list1)