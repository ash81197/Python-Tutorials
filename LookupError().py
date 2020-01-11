#h = histogram('Hello World')
#k = reverse_lookup(h, 2)

# to check every element of a string and count the repeated letter
def histogram(s):
    d = {} # or d = dict()
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d
    #print(d)

h = histogram('hello world')
print(h)

# if u know the value and u want to find the key
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('The Value that you searched for is not present in Dictionary')
