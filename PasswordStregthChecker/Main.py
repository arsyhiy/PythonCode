import string
import getpass


def PasswordStregthChecker():
   password = getpass.getpass('введите пароль: ')
   strength = 0
   remarks = ' '
   lower_count = upper_count = num_count = wspace_count = special_count = 0

   for char in list(password):
       if char in string.ascii_lowercase:
           lower_count += 1
       elif char in string.ascii_uppercase:
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1
       else:
           special_count += 1

   if lower_count >= 1:
       strength += 1
   if upper_count >= 1:
       strength += 1
   if num_count >= 1:
       strength += 1
   if wspace_count >= 1:
       strength += 1
   if special_count >= 1:
       strength += 1

   if strength == 1:
       remarks = ('это очень слабый пароль.'
           ' если у вас акаунт с таким паролем прошу как можно скорее сменить его на более сложный.')
   elif strength == 2:
       remarks = ('это плохой пароль.'
           ' вам стоит сделать более сложный пароль.')
   elif strength == 3:
       remarks = 'ваш пароль нормальный, но вы можете сделать лучше.'
   elif strength == 4:
       remarks = ('ваш пароль сложно отгадать.'
           ' но сделайте его сложнее чтоб наверняка.')
   elif strength == 5:
       remarks = ('теперь это сложный пароль!!!'
           ' хакеры точно не узнают пароль!')

   print('вашем пароле есть такие знаки как:-')
   print(f'{lower_count} lowercase letters')
   print(f'{upper_count} uppercase letters')
   print(f'{num_count} digits')
   print(f'{wspace_count} whitespaces')
   print(f'{special_count} special characters')
   print(f'Password Score: {strength / 5}')
   print(f'Remarks: {remarks}')


def check_pwd(another_pw=False):
   valid = False
   if another_pw:
       choice = input(
           'хотите проверить сложность пароля ? (y/n) : ')
   else:
       choice = input(
           'хотите проверить сложность пароля ? (y/n) : ')

   while not valid:
       if choice.lower() == 'y':
           return True
       elif choice.lower() == 'n':
           print('выход из программы...')
           return False    
       else:
           print('Invalid input...please try again. \n')
           return check_pwd()   # my first bug that i solved
          



if __name__ == '__main__':
   print('===== добро пожаловать в программу проверки сложности пароля  =====')
   check_pw = check_pwd()
   while check_pw:
       PasswordStregthChecker()
       check_pw = check_pwd(True)