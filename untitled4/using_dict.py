# 'ab' - сокращение от 'a'ddress'b'ook
ab = {'swaroop' : 'swaroop@swaroopch.com',
      'lary' : 'larry@wall.org' ,
       'matsumoto' : 'matz@ruby-lang.org',
       'spammer' : 'spammer@hotmaill.com'
      }

print("Адрес Swaroop'а:", ab['swaroop'])

# Удаление пары ключ-значение
del ab['spammer']

print('\nB  адресной книге {0} контакта\n' .format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}' .format(name, address))

# Добавление пары ключ-значение
ab['guido'] = 'guido@python.org'

if 'guido' in ab :
    print('\nАдрес guido:', ab['guido'])
