import pickle

# имя файла, в котором мы сохраним обьект
shoplistfile = 'shoplist.data'
# список покупок
shoplist = ['яблоки', 'mango', 'morkov']

# запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) #помещаем обькт в файл
f.close()
del shoplist # уничтожаем переменную shoplist
#считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) #загружаем обьект из файла
print(storedlist)