'''
class Student():
    amount_of_students = 0
    def __init__(self, height = 160):
        self.height = height
        Student.amount_of_students +=1
    def grow(self, height=1):
        self.height +=height
Serhii = Student()
Oleg = Student(height=170)
print('Serhii - ', Serhii.height)
Serhii.grow(height=15)
print('Serhii - ', Serhii.height)
print('Oleg - ', Oleg.height)

class Student():
    def __init__(self, name=None):
        self.name=name
    def __str__(self):
        return f"I am student. My name is {self.name}"
    def __del__(self):
        print(f'Training is over. I {self.name} and I now an expert!')
serhii = Student(name = 'Serhii')
print(serhii)
oleg = Student(name = 'Oleg')
print(oleg)


class Student:
    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height
    def __bool__(self):
        return self.name !=None
    def __len__(self):
        return self.height

nick = Student(name='Nick', height=175)
jhon = Student(name='Jhon')
print(nick.name)
print(bool(nick))
print(nick.__bool__())
print(len(nick))
print(nick.__len__())

print(jhon.name)
print(bool(jhon))
print(jhon.__bool__())
print(len(jhon))
print(jhon.__len__())
'''
class Car:
    def __init__(self, model=None, color=None, speed=0, ):
        self.model = model
        self.color = color
        self.speed = speed
car1 = Car(model='mercedec', color = 'red', speed = 200)
car2 = Car(model='bmw', color = 'black', speed = 220)
car3 = Car(model='lamborgini', color = 'yellow', speed = 300)
print('my characteristics are(I am car 1):')
print('my model is- ', car1.model)
print('my color is- ', car1.color)
print('my speed is- ', car1.speed)
print('my characteristics are(I am car 2):')
print('my model is- ', car2.model)
print('my color is- ', car2.color)
print('my speed is- ', car2.speed)
print('my characteristics are(I am car 3):')
print('my model is- ', car3.model)
print('my color is- ', car3.color)
print('my speed is- ', car3.speed)
