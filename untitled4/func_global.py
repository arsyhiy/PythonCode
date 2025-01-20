x = 50

def func():
    global x

    print("x ravno", x)
    x = 2
    print('заменяем значение глобального x на ', x)

func()
print('значение х ', x)