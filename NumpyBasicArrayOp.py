import numpy as np
a = np.array([1,2,3])
print('a[0]:', a[0],'a[1]:', a[1],'a[2]:', a[2]) # Acts just like a List
print('a:',a)

a2 = np.array([[1,2], [3,4], [5,6]])
print('Elements of a2:\n', a2)
print('Arrays Dimension of a2:',a2.ndim) # To print the dimension of the array

# Printing the itemsize of individual item
print('Item size of individual item:',a2.itemsize)

# Printing the datatype of array elements of a2
print('Datatype of a2 Elements:', a2.dtype)

# Changing the datatype of 2d array
a3 = np.array([[1,2], [3,4], [5,6]], dtype=np.float64)
print('After changing the datatype of elements of array, Datatype of a2 Elements:', a3.dtype)

# Checking the total number of elements in an array
print('The Size of a3:', a3.size)
print('Elements of a3:\n', a3)

# Checking the No of Rows & Column of an array
print('The no of Rows & Columns of array a3:', a3.shape)
print('Elements of a3:\n', a3)

# Changing the datatype of the array to the complex numbers
a4 = np.array([[1,2], [3,4], [5,6]], dtype=complex)
print('After changing the datatype of elements of array, Datatype of a3 Elements:', a4.dtype)
print('Elements of a3:\n', a4)

# To initialize the array with only zeroes
print('Array with all zero elements:\n', np.zeros((3,4))) # 3 = rows, 4 = columns

# To initialize the array with only ones
print('Array with all one elements:\n', np.ones((3,4))) # 4 = rows, 3 = columns

# Creating a Python List with range fx
l = range(5) # 0 to 4
print('Elements of Python List', l[0], l[1], l[2], l[3], l[4], '& range is', l)

# Creating a Numpy Array with arange fx
a5 = np.arange(1,5) # arange = array range
                    # if we don't write 1 then array will start from 0 (zero)
print('Elements of NumPy Array:', a5)

# Taking steps of 2 numbers
a6 = np.arange(1,5,2)
print('Elements of NumPy Array after 2 steps:', a6)

# Generating the in-between linearly spaced numbers
print('10 Generated Numbers between 1&5, including 1&5:\n', np.linspace(1,5,10)) # 10 is the quantity of no you want to generate

# Reshaping the array
print('After reshaping:\n', a4.reshape(2,3))

# Flatening out your array
print('After flatening out array:', a4.ravel())
            # but it does not affect/alter the original array
print('Original array is still present, which is:\n', a4)

# Printing the minimum element of array a4
print('Minimum no of array a4:', a4.min())

# Printing the maximum element of array a4
print('Maximum no of array a4:', a4.max())
