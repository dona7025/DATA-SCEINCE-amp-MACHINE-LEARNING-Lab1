print('Dona T John')
print('21/MCA/018')

import numpy as np


arr = np.array([

           [1+4j,2+5j,3+6j],

           [4+6j,9+1j,5+2j],

              ],

           dtype=complex)

print(arr)

print("\nDimension of given array is :",arr.ndim)

print("\nNumber of rows and columns of given array is :",arr.shape)


newarr = arr.reshape(3,2)

print("\nNew array is :\n\n",newarr)