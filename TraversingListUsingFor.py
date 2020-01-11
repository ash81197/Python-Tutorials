numbers = [1,2,3,4,5]
num2 = []

for i in range(len(numbers)):
    num2 = numbers[i] * 2 # copying the data of one list into another list
    #print(numbers[i])
    print(num2)

for x in []:
    print('this is never gonna happen')

# list concatenation
a = [1,2,3,4]
b = [5,6,7,8]
c = a + b
print(c)

# Extending List
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l1.extend(l2)
print(l1)

# Sorting the Elements in a List
list = ['e','d','c','b','a']
list.sort()
print(list)

# Adding up all the elements of a list
def add_all(l1):
    total = 0
    for eachNumber in l1:
        total += eachNumber
    print(total)

add_all(l1) # or it can be used as print(sum(l1)) using built in fx

# Capitalizing all Letters of a List
def all_caps(list):
    res = []
    for eachLetter in list:
        res.append(eachLetter.upper()) # or res.append(eachLetter.capitalize())
        #print(eachLetter.upper())
    print(res)

# Alternative of this function is:
# This list is also called as 'map'
def all_caps2(list):
    for eachLetter in list:
        print(eachLetter.upper())
        
all_caps(list)
all_caps2(list)

# Printing Only Upper Case Letter from a List and is also called as filtered list
list2 = ['A', 'B', 'C', 'D', 'E']
def only_upper(list2):
    res = []
    for eachLetter in list2:
        if eachLetter.isupper():
            res.append(eachLetter)
            
print('All the capital Letters present in the list is: ',only_upper(list2))
