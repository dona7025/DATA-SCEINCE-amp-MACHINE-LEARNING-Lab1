'''6.	Create a 2 Dimensional array with 4 rows and 4 columns.
a.	Display all elements excluding the first row
b.	Display  all elements excluding the last column
c.	Display the elements of 1st  and 2nd column in 2nd  and 3rd  row
d.	Display the elements of 2nd and 3rd column
e.	Display 2nd and 3rd element of 1st row
f.	Display the elements from indices 4 to 10 in descending order(use –values)
'''
import numpy as np
print('Dona T John')
print('21/MCA/018')
ar=np.array([[1,2,3,4],

            [4,6,7,3],

            [8,9,0,1],

            [5,6,3,2]

            ])

print("Display all elements excluding the first row\n",ar[1:4])

print("Display all elements excluding the last column\n",ar[:,0:3])

print("Display the elements of 1 st and 2 nd column in 2 nd and 3 rd row\n",ar[1:3,0:2])

print("Display the elements of 2 nd and 3 rd column\n",ar[:,1:3])

print("Display 2 nd and 3 rd element of 1 st row\n",ar[0,1:3])