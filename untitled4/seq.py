shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'

# Операция индексирования
print('элемент 0 -', shoplist[0])
print('элемент 1 -', shoplist[1])
print('элемент 2 -', shoplist[2])
print('элемент 3-', shoplist[3])
print('элемент -1', shoplist[-1])
print('элемент -2 -', shoplist[-2])
print('символ 0 -', name[0])

# Вырезка из списка
print('элементы с 1 по 3:', shoplist[1:3])
print('элементы с 2 до конца', shoplist[2:])
print('элементы с 1 по -1 :', shoplist[1:-1])
print('элементы от начала до конца:', shoplist[:])

# Вырезка из строки
print('символы с 1 по 3:', name[1:3])
print('символы с 2 до конца :', name[2:])
print('символы с 1 до -1', name [1:-1])
print('символы от начала до конца :', name[:])