n = int(input("Please Enter your Bitcoin Amount to calculate: "))
def btc_to_inr(n):
    return n*952843.33

amount = btc_to_inr(n)
print(amount, "is the price of", n, "Bitcoins")