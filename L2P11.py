#11. Demonstarte the use of sum() function in 1D and 2D array.
print('Dona T John')
print('21/MCA/018')
import numpy as np


arr=np.array([1,2,3,4])


arr1=np.array([

   [1,2],

   [4,5]


])

print("arr:\n",arr)

print("arr1:\n",arr1)

print("\nSum of arr : ", np.sum(arr))

print("\nSum of arr2 : ", np.sum(arr1))

print("Sum of arr(axis = 0) : ", np.sum(arr1, axis = 0))

print("Sum of arr(axis = 1) : ", np.sum(arr1, axis = 1))

