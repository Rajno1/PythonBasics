'''
List items are indexed and you can access them by referring to the index number:
'''

list1 = ["abc", 34, True, 40, "male", 2.5, False]
print(list1[2])  # the first item has index 0

''' Negative indexing
 Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc.'''
print(list1[-1])

''' You can specify a range of indexes by specifying where to start and where to end the range '''
print(list1[1:5])  # Note: The search will start at index 1 (included) and end at index 5 (not included).
