from random import choice 
digits = '0123456789'
uppercase = 'ABDCEFGHIJKMNOPQRSTUWXYZ'
lowercase = 'abcdefghijkmnopqrstuwxyz'
punctuation = '!#$&*+-=&@^_'
ally = digits + uppercase + lowercase + punctuation

chars = ''

pwd_length = int(input('Введите желаемую длину пароля: '))
pwd_auto =  input('Сгенерировать пароль автоматически? (y, n): ')

if pwd_auto == 'y':
    chars += ally
else:
    pwd_digits = input('Включит цифры (y, n): ')
    pwd_uppercase = input('Включить uppercase (y, n): ')
    pwd_lowercase = input('Включить lowercase (y, n): ')
    pwd_punctuation = input('Включить спец. символы (y, n): ')
    if pwd_digits == 'y':
        chars += digits
    if pwd_uppercase == 'y':
        chars += uppercase
    if pwd_lowercase == 'y':
        chars += lowercase
    if pwd_punctuation == 'y':
        chars += punctuation

password = ''

for i in range(pwd_length):
    password += choice(chars)

print('\n', password, '\n', sep='')
