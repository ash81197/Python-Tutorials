t = ['a', 'b', 'c', 'd', 'e']
x = t.pop(1) # giving the index of the element to be deleted
print(t)

t = ['a', 'b', 'c', 'd', 'e']
x = t.pop() # if no index is given then it deletes the last element of the list
print(t)

# Alternative way to delete the element of a list if index is known
t2 = [1, 2, 3, 4, 5]
del t2[4]
print(t2)

# Another way to delete the element of a list if element is known and index isn't
t3 = [6, 7, 8, 8, 9]
t3.remove(8)
print(t3)

# To Remove more than one Element
t4 = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
del t4[5:]
print(t4)

# To convert the string into list
str = 'spam'
t5 = list(str)
print(t5)

# Splitting the string into individual words
str2 = 'This is a sentence'
t6 = str2.split()
print(t6)

# Word boundaries Using Delimiter
str3 = 'spam-spam-spam'
delimiter = '-'
t7 = str3.split(delimiter)
print(t7)

# Joining the words to make a sentence
t7 = ['This', 'is', 'the', 'whole', 'sentence']
delimiter = ' '
str4 = delimiter.join(t7)
print(str4)
