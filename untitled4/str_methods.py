name = 'swaroop' #это обьект строки

if name.startswith('swa'):
    print('да, строка начинается на"swa"')

if 'a' in name:
    print('да, она содержит строку "a"')

if name.find('war')    != -1:
    print('да, она содержит строку "war"')

delimiter = '_*_'

mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter .join(mylist))