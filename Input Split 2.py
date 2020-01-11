'''
m = int(input())
i=1
arr1 = []
while i<=m:
    a = int(input().split())
    arr1.append(a)
    i+=1
s1 = set(arr1)
n = int(input())
i=1
arr2 = []
while i<=n:
    b = int(input().split())
    arr2.append(b)
    i+=1
s2 = set(arr2)
print(len(s1.intersection(s2)))
'''
s1 = int(input())
sl1 = list(map(int,input().split()))
s2 = int(input())
sl2 = list(map(int,input().split()))
print (len(sl1.intersection(sl2)))
