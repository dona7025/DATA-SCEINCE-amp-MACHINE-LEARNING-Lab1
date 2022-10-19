import numpy as np
print("Dona T John, 018")

A=np.matrix([[2,1,-2],
             [3,0,1],
             [1,1,-1]])

b=np.matrix([-3,5,-2])
y = np.linalg.inv(A)
X=np.matmul(b,y)
print("X:\n\n{}\n".format(X))
