'''
7.	Create two  2D arrays using array object and
a.	Add the 2 matrices and print it
b.	Subtract 2 matrices
c.	Multiply the individual elements of matrix
d.	Divide the elements of the matrices
e.	Perform matrix multiplication
f.	Display transpose of the matrix
g.	Sum of diagonal elements of a matrix
'''
import numpy as np
print('Dona T John')
print('21/MCA/018')
m1=np.array([[1,2,3],
            [6,7,8],
           [1,4,5]
             ])
m2=np.array([[9,7,6,],
              [3,4,5],
              [4,5,6]
              ])
print("Matrix 1:\n",m1)
print("Matrix 2:\n",m2)
r1 = np.add(m1, m2)
print("Sum of Matrices:")
print(r1)
r2 = np.subtract(m1, m2)
print("Difference of Matrices:")
print(r2)
r3=np.multiply(m1,m2)
print('\n Multiplication of individual elements of matrix: \n',r3)
r4=np.divide(m1,m2)
print('\n Division: \n',r4)
r5 = np.matmul(m1,m2)
print('\nMultiplication: \n',r5)
print("\n Transpose of Matrix 1:\n",np.transpose(m1));
print("\n transpose of Matrix 2:\n",np.transpose(m2));
print("\n Sum of diagonal elements of Matrix 1:\n",np.trace(m1));
print("\n Sum of diagonal elements of Matrix 2:\n",np.trace(m2));


