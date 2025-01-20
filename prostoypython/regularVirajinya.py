import re
source = 'young Frankenstein'
m = re.match('you', source)  # функция начинает работать с начала источника
if m:  # функция возвращает объект; делайте это, чтобы увидеть, что совпало
    print(m.group())

m = re.match('^You', source)   # якорь в начале строки делает то же самое
if m:
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())


m = re.match('.*Frank', source)
if m:
    print(m.group())

m = re.findall('n', source)
m #findall returns a list
print(m)
print('Found', len(m), 'matches')

m = re.findall('n.?', source)
print(m)  # функция split возвращает список

m = re.split('n', source)
print(m)

m = re.sub('n', '?', source)
print(m)  # sub returns a string