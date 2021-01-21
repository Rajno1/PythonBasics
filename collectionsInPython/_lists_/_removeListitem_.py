"""  The remove() method removes the specified item. """
list1 = ["iPhone","iMac","Reliance","iPod"]
list1.remove("Reliance")
print(list1)

""" the pop() removes list item specific index """
list=["One","three","Two","Three","Four","Five"]
list.pop(1)
print(list)

''' Note:  If you do not specify the index, the pop() method removes the last item '''

''' The 'del' keyword also removes the specified index: '''
del list[0]
print(list)
''' Note: The del keyword can also delete the list completely '''

""" The clear() method empties the list.
The list still remains, but it has no content."""
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)