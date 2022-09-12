'''14. Write a Python program that accepts a 10 digit mobile number, and find the digits
which are absent in a given mobile number'''
print('Dona T John')
print('21/MCA/018')

def absent_digits(n):
  all_nums = set([0,1,2,3,4,5,6,7,8,9])
  n = set([int(i) for i in n])
  n = n.symmetric_difference(all_nums)
  n = sorted(n)
  return n

str = input("\nPlease enter the mobile number:")
str_set = set(str)
print('\nThe Mobile Number is:')
print(str_set)
print('\nThe Missing digits ofnmMobile Number is:')
print(absent_digits(str_set))


