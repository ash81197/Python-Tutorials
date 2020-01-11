'''
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)
'''

def f(n):
    if n == 0:
       return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)

#x = fibo(5)
#print(x)
