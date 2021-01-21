"""
slicing - particular portion of a string
Specify the start index and the end index, separated by a colon, to return a part of the string , it will exclude the character at
last index
"""
a="Python is awesome"
print(a[2:9])

# slice from start - to get the characters from the start to position 5(not included)
print(a[:5])

# slice to the end - getting characters from perticular position to end
print(a[6:])