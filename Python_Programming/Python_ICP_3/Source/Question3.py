import numpy as np

# Create random vector of size 20 having only Integers in the range 1-20 by using Numpy
ranArray = np.random.randint(1, high=20, size=20, dtype='int')
print('Random Array :  ', ranArray)

# Array is reshaped by 4*5
newArr = np.reshape(ranArray, (4, 5))
print('\n Array after reshape:\n ', newArr)

# To replace the max in each row by 0
maxArr = np.where(newArr == np.max(newArr, axis=1, keepdims= True), 0*newArr, newArr)
print("\nNew array replacing with 0 instead of the max number row wise: \n", maxArr)
