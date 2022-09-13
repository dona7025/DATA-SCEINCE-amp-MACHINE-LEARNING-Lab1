print('Dona T John')
print('21/MCA/018')

import numpy as np

print("\n a)	an uninitialized array\n")
mat1 = np.empty(4, dtype=int)
print("Matrix mat1 : \n", mat1)

mat2 = np.empty([3, 3], dtype=int)
print("\nMatrix mat2 : \n", mat2)

mat3 = np.empty([2, 2])
print("\nMatrix mat3 : \n", mat3)

print(" \nb)	array with all elements as 1\n")
a = np.ones(3, dtype=int)
print("Matrix a : \n", a)

b = np.ones([3, 3], dtype=int)
print("\nMatrix b : \n", b)

print("\n c)	 all elements  as 0\n")
a = np.zeros(3, dtype=int)
print("Matrix a : \n", a)

b = np.zeros([3, 3], dtype=int)
print("\nMatrix b : \n", b)