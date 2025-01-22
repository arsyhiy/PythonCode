p = (4,5)
x, y = p 

print("x=", x)
print("y=", y)


data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data

print("name=",name)

name, shares, price, (year, mon, day) = data
print("name=",name)
print("year",year)
print("mon=",mon)
print("day=",day)
