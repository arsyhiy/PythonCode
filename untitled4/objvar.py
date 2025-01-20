class robot:
    '''Представляет робота с именем.'''
    # Переменная класса, содержащая количество роботов
    population = 0


    def __init__(self, name):
        '''Инициализация данных.'''
        self.name = name
        print('(инициализация {0})' .format(self.name))

        # При создании этой личности, робот добавляется
        # к переменной 'population'
        robot.population += 1

    def __del__(self):
        '''Я умираю.'''
        print('{0} уничтожается!' .format(self.name))

        robot.population -= 1

        if robot.population == 0:
            print('{0} был последним.' .format(self.name))
        else:
            print('осталось {0:d} работающих роботов.' .format( robot.population))

    def sayhi(self):
        '''Приветствие робота.
        Да, они это могут.'''
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
    def howmany():
        '''Выводит численность роботов.'''
        print('У нас {0:d} роботов.'.format(robot.population))

    howmany = staticmethod(howmany)
droid1 = robot('rd-d2')
droid1.sayhi()
robot.howmany()

droi2 = robot('c-3po')
droi2.sayhi()
robot.howmany()

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droi2

robot.howmany()