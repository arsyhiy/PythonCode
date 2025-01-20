import time

try:
    f = open(r'poem.txt' )
    while True: # наш обычный способ читать файлы
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)# Пусть подождёт некоторое время
except KeyboardInterrupt:
    print('!! вы отменили чтение файла.')
finally:
    f.close()
    print('(очистка: Закрытие файла)')
