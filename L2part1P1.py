print('Dona T John')
print('21/MCA/018')
import numpy as np

array = np.random.randint(10, size=(3, 3))
print("\nSquare Matrix is:\n",array)
print("\nInverse Matrix:\n",np.linalg.inv(array))
rank = np.linalg.matrix_rank(array)
print("\nRank of the given Matrix is : ",rank)
det = np.linalg.det(array)
print("\nDeterminant of given matrix:",int(det))
res = array.flatten()
print("\nNew resulting array: ", res)
w,v = np.linalg.eig(array)
print("\nPrinting the Eigen values of the given square array:\n",w)

print("\nPrinting Right eigenvectors of the given square array:\n",v)