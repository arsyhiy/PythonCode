[x * x for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
(x * x for x in range(10))
# <generator object <genexpr> at 0x7fe76f7e5db0>

def print6(xs):
    for i, x in enumerate(xs):
        print(x)
        if i == 5:
            break

i = (x * x for x in range(10))
print6(i)
# => 0
# => 1
# => 4
# => 9
# => 16
# => 25
print6(i)  # Продолжаем перебирать элементы
# => 36
# => 49
# => 64
# => 81
print6(i)  # Больше ничего не осталось


# f((… for … in …))
any(x > 100 for x in range(1000000))
# True
