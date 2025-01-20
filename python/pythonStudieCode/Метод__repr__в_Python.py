string = 'Hy! I am John'
print (repr(string))
print (repr(5.0/11.0))
# Output:
# 'Hy! I am John'
# 0.45454545454545453


import datetime
td = datetime.datetime.now()
print(td.__str__())
print(td.__repr__())
# Output:
# 2022-01-26 08:17:46.276609
# datetime.datetime(2022, 1, 26, 8, 17, 46, 276609)


class Test:
    def __init__(self, name, salary):
        self.v1 = name
        self.v2 = salary
val = Test('John', 50000)
print(val.__str__())
print(val.__repr__())
# Output:
# <__main__.Test object at 0x7f4656a7bbe0>
# <__main__.Test object at 0x7f4656a7bbe0>


class Test:
    def __init__(self, name, salary):
        self.v1 = name
        self.v2 = salary
    def __str__(self):
        return f'User name is {self.v1} and his/her salary is {self.v2}'
    def __repr__(self):
        return f'User(name={self.v1}, salary={self.v2})'
val = Test('John', 50000)
print(val.__str__())
print(val.__repr__())
# Output:
# User name is John and his/her salary is 50000
# User(name=John, salary=50000)
