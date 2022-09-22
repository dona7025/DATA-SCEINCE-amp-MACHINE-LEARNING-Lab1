#10.Demonstarte the use of append() function in 1D and 2D array.
print('Dona T John')
print('21/MCA/018')

import numpy as np
arr=np.array([1,2,3,4])
arr1=np.array([

   [1,2],

   [4,5]


])
arr2=np.array([

   [7,8],

   [9,10]

])

print('arr:\n',arr)
print("arr1:\n",arr1)
print("arr2:\n",arr2)
arr3=np.append(arr1,arr2,axis=0)
arr4=np.append(arr1,[1,0,1])
print('append on arr1\n',arr4)
print("after append of arr1,arr2\n",arr3)
