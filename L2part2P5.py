import numpy as np
print("Dona T John, 018")
import numpy as np

#A=np.random.randint(0,8,size=(3,3))
A=np.matrix([[0,1,-2],
             [-1,0,3],
             [2,-3,0]])
print(A)
B=A.transpose()
if A.all() == B.all():
    print("matrix is symmetric ")
else:
    print("not  symmetric")
if np.allclose(-A,B)==True :
    print("matrix is skew symmetric")
else:
    print("not skew symmetric")