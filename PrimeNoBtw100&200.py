flag=0
for i in range(100,200):
    for j in range(2,i//2):
        if j//2==0:
            flag=1

            break
        else:
            i+=1
            j+=1


if flag==0:
    print("Number is not Prime")
else:
    print("Number is Prime")