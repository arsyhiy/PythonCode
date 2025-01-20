#   Все следующие выражения возвращают словарь {"one": 1, "two": 2, "three": 3}
#   >>> a = dict(one=1, two=2, three=3)
#   >>> a
#   {'one': 1, 'two': 2, 'three': 3}
#   >>> b = {'one': 1, 'two': 2, 'three': 3}
#   >>> b
#   {'one': 1, 'two': 2, 'three': 3}
#   >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
#   >>> c
#   {'one': 1, 'two': 2, 'three': 3}
#   >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
#   >>> d
#   {'one': 1, 'two': 2, 'three': 3}
#   >>> e = dict({'three': 3, 'one': 1, 'two': 2})
#   >>> e
#   {'one': 1, 'two': 2, 'three': 3}
#   >>> a == b == c == d == e)
#   True
