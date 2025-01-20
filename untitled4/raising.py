class ShortInputException(Exception):
    ''' пользовательский класс исключения   '''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast =atleast

try:
    text = input("введите что небудь-->")
    if len(text) < 3:
       raise ShortInputException(len(text), 3)
    #здесь может происходить обычная работа
except EOFError:
    print('ну зачем вы сделали мне EoF')
except ShortInputException as ex:
    print('ShortInputException: длина введённоый строки -- {0}; \
           ожидалось, как  минимум , {1})' .format(ex.length, ex.atleast))
else:
    print('не было исключений')