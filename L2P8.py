#8.	Demonstrate the use of insert() function in 1D and 2D array
print('Dona T John')
print('21/MCA/018')
import numpy as np

arr1=np.array([1,2,3,4,5,6])

print("\narray 1:",arr1)

print("\narray 1 after insertion:",np.insert(arr1,3,9))


arr2=np.array([

   [1,2,3],

   [6,7,8]

])

print("\narray 2:",arr2)


print("\narray 1 after insertion:\n",np.insert(arr2, 1, np.array((1, 1, 1)), 0))



