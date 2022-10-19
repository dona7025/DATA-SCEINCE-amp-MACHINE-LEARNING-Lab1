import numpy as np
print("\nDona T John(18)\n")
A = np.random.randint(0, 10, size=(5,6))
B = np.random.randint(0, 10, size=(3,3))
print("Matrix A:\n{}\n".format(A))
print("Matrix B:\n{}\n".format(B))
C = A[1:4,2:5] @ B
A[1:4,2:5] = C
print("Matrix A after submatrix multiplication:\n{}\n".format(A))