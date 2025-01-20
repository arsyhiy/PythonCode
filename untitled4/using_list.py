# Это мой список покупок
shoplist = ['яблоки', 'mango', 'morkov', 'bananas']

print('Я должен сделать', len(shoplist), 'покупки')

print('покупки:', end='')
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print('Первое, что мне нужно купить, это' , shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('я купил', olditem)
print('теперь мой список покупок:', shoplist)