"""
class Human:
    def __init__(self, name='Human'):
        self.name=name

class Auto:
    def __init__(self, brand):
        self.brand=brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers !=[]:
            print(f'Names of {self.brand} passengers:')
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f'There are no passengers in {self.brand}')
nick=Human('Nick')
oleg=Human()
jhon=Human('Jhon')
car=Auto('Mercedes')
car_1=Auto('BMW')

car.add_passengers(jhon)
car.add_passengers(oleg)
car_1.add_passengers(nick)
car.print_passengers_names()
car_1.print_passengers_names()

data = 30
day = 'Sunday'
month = 'october'
print('Today is', data, month,'-', day, ".")
print('Today is {} {} - {}.'.format(data, month, day))
print('Today is {:_^6} {:*^15} - {:~^15}.'.format(data, month, day))
print('Today is {data:_^6} {month:*^15} - {day:~^15}.'.format(data=31, month='October', day='Monday'))

a=25
b=50
print(f'Периметр прямокутника-{a*2+b*2}.'
      f'Площа прямокутника - {a*b}.')

class Human:
    height = 170
    satiety = 50
class Student(Human):
    satiety = 0

class Worker(Human):
    satiety = 100

nick=Student()
jhon=Worker()

print('nick_height-', nick.height)
print('jhon_height-', jhon.height)

print('nick_satiety-', nick.satiety)
print('jhon_satiety', jhon.satiety)

class Grandparents:
    height = 100
    satiety = 100
    age = 60

class Parent(Grandparents):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print('height - ', self.height)
        print('statiety - ', self.satiety)
        print('age - ', self.age)
nick = Child()

class Wow:
    def __wow(self):
        print('WOW')

    def _hello(self):
        print('Hello')

obj_some = Wow()

obj_some._hello()
obj_some._Wow__wow()

class Hello_world:
    hello = 'Hello'
    _hello = '_Hello'
    __hello = '__Hello'
    def __init__(self):
        self.world = 'World'
        self._world = '_World'
        self.__world = '__World'
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hi(Hello_world):
    def hi_printer(self):
        print(self.hello)
        print(self._hello)
        print(self.world)
        print(self._world)
        print(self.__hello)
        print(self.__world)


hello = Hello_world()
hello.printer()
print('******************************')
hi = Hi()
hi.hi_printer()
"""
