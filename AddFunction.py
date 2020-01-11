#Function without return values
def sum(a,b):
    c=a+b
    print("Sum of a & b is: ",c)
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
sum(a,b)

#Function with return values
def sum(a,b):
    c=a+b
    return c
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
addition=sum(a,b)
print("Addition of a & b is: ",addition)