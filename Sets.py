# Sets can't have dublicate items

n=int(input("Please enter any number that you want to search:"))
naturalNumber = {1,2,3,4,5,6,7,9,9,8,7,6,5,4,3,2,1}

if n in naturalNumber:
    print("You already have Number", n, "in the Set...")
else:
    print("Need to enter Number", n, "in the set...")

print(naturalNumber)