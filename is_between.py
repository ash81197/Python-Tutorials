x = input("Enter the value of x: ")
y = input("Enter the value of y: ")
z = input("Enter the value of z: ")

def is_between(x, y, z):
    if (x<=y<=z)==True:
        return True

x = is_between(x, y, z)
print(x)
