print('Dona T John')
print('21/MCA/018')
# Program to find the count of each vowel in a string(use dictionary)
# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'
print('Given Sting:')
print(ip_str)
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)
print('\nNo.of each Vowel:')
# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)