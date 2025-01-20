import  string
import re
printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])
print(re.findall('\d', printable))
print(re.findall('\w', printable))
print(re.findall('\s', printable))