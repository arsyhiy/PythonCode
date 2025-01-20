def total(intitial=5, *numbers, extra_number):
    count = intitial
    for number in numbers:
        count += number
     count =+ exrta_number
     print(count)

total(10, 1, 2, 3, extra_number=50)
total(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.
