import qrcode

img = qrcode.make(input('введите сылку или текст: '))

print(f'{type(img)}')

filename=input('введите название файла: ')
img.save(f'{filename}.png')
