try:
    text = input('ведите что нибудь -->')
except EOFError:
    print('ну зачем вы сделали мне EOF?')
except KeyboardInterrupt :
    print('вы отменили операцию')
else:
    print('вы ввели {0}' .format(text))