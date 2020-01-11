costOfBook=24.95
discount=40/100

def TotalCost():
    TotalCost=costOfBook-(costOfBook*discount)
    print("Total Cost of each book after 40% discount is: ",TotalCost)
    return TotalCost

x=TotalCost()

n=int(input("Enter the number of book you want to be shipped: "))
def shippingCost():
    shippingCost=3+((n-1)*.75)
    print("Shipping Cost of",n,"books:",shippingCost)
    return shippingCost

y=shippingCost()

FinalCost=x*n+y
print("Your Total bill:",FinalCost)
