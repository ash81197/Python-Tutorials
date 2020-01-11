def histogram(s):
    d = {} # or d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
    #print(d)

h = histogram('Hello World')
print(h)
print(h.get('l', 0))

'''
s = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
s = histogram('Hello World')
#histogram(s)
'''

def print_hist(h1):
    #for c in h1:
        #print(c, h1[c])
    for key in sorted(h1): # To print the letters in sorted order
        print(key, h[key])

h1 = histogram('Hello World')
print_hist(h1)
