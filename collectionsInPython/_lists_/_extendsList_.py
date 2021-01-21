"""
To append (add) elements from another list to the current list, use the extend() method.
The elements will add to the end of the list.
"""
list1=["Mango","Promogranate","apple"]
list2=["Carrot","Brocoli","Beatroute"]
list2.extend(list1)
print("This is list one = " , list1)
print("This is list Two = " , list2)

""" Note:  The extend() method we can add any iterable object (tuples, sets, dictionaries etc.)."""
thistuple=("Kiwi","Orange")
list1.extend(thistuple)
print(list1)