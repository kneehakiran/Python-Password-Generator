import random
print('WELCOME TO PASSWORD GENERATOR')
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%'
length = int(input('Enter Password Length: '))
password = ''
for i in range(length):
    password += random.choice(characters)
print('Generated Password: ',password)
if length>=8:
    print('Strong Password')
else:
    print('Weak Password')
