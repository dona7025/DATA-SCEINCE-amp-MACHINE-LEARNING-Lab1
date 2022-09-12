# Write a program to find the sum of 2 matrices using nested List.
print('Dona T John')
print('21/MCA/018')

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
print('Elements of First Matrix:')

for r in X:
   print(r)
print('Elements of Second Matrix:')

for r in Y:
   print(r)

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
print('Elements of Sum Matrix:')
for r in result:
   print(r)