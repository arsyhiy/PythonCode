class Person:
  def __init__(self, name):
      self.name = name

  def say_hi(self):
       print('привет! меня зовут', self.name)


p = Person('swaroop')
p.say_hi()

# Предыдущие 2 строки можно
# Person('Swaroop').say_hi()