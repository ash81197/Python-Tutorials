##string = str("Hello World")
##i=0
##for s in string:
##    if(s == ' '):
##        break
##    else:
##        print(string[i], end = '')
##        i+=1

## Palindrome

flag = 0
x = 0
y = -1
for x in string:
    for y in string:
        if (x == y):
            flag+=1
            print(y)


if flag > 0:
    print("it is palindrome")
    print(flag)
else:
    print("Not palindrome")
