"""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered and changeable. No duplicate members.

Lists are one of 4 built-in data types in Python used to store collections of data
"""
''' ordered means that the items have a defined order, and that order will not change.
 If you add new items to a list, the new items will be placed at the end of the list '''

''' The list is changeable, meaning that we can change, add, and remove items in a list after it has been created '''

''' Since lists are indexed, lists can have items with the same value '''

# *** Lists are created using square brackets
list=["one","Two","Five","Three","Four","Two"]
print(list)
print(len(list)) # it will print length of list

print("length of list is {}".format(len(list)))

# list items can be any data type
list1 = ["abc", 34, True, 40, "male"]
print(list)
print("lenght of \"list1\" is {} ".format(len(list1)))
