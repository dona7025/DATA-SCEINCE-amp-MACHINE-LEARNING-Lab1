
print('Dona T John')
print('21/MCA/018')

"""Write a Python program that accept a positive number and subtract from this
number the sum of its digits and so on. Continues this operation until the number is
positive(eg: 256-&gt;2+5+6=13
256-13=243
243-9=232…….."""

n=int(input("Enter a number:"))
while(n>0):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    print(n,'-',sum,end=" ")
    n=n-sum
    print('=',n)





