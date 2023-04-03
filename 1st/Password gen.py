# pypassword genreator:
import random
letters = [
    'A','B','C','D','E','F','G','H','I','J','K','I','K','J','L','M','N','O','P','Q','R','S','T','U','V','B',
    'Z','X','Q','W'
]
symbol = [
    '!','@','£','#','$','%','(',')','+','^','*','-','"','?'
]
print('Welcome to password genreator')
in_letters = int(input("how many letters you want in password: "))
in_symbols = int(input('how many characters you want in password: '))
password= []
for char in range(0,in_letters+1):
    random_character = random.choice(letters)
    password.append(random_character)
for char in range(0,in_symbols+1):
    random_symbol = random.choice(symbol)
    password.append(random_symbol)
print(password)
random.shuffle(password)
print(('').join(password))

