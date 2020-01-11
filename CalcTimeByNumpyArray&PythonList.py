# Calculating the time taken by both numpy and python list

size = 1000000
l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

# Python List
start = time.time()
result = [(x+y) for x,y in zip(l1, l2)]
print('Python List Took: ',(time.time()-start)*1000, ' seconds')

# NumPy Array
start = time.time()
result = a1 + a2
print('NumPy Array Took: ',(time.time()-start)*1000, ' seconds')
