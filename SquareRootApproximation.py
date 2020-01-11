x = 0.0001 #x can have different values
a = 4

while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    else:
        x = y
