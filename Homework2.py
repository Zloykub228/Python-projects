import random
x=0
y=0
class Student:
    def __init__(self, height=175, age = 19, intelligence = 100, money = 100):
        self.height = height
        self.age = age
        self.intelligence = intelligence
        self.money = money
class Day:
    def __init__(self, day=1):
        self.day = day
day = Day()
student = Student()
print('Your student parameters:')
print('His height-', student.height)
print('His age-', student.age)
print('His intelligence-', student.intelligence)
print('His money-', student.money)
print('Starting the game...')
print('------------------------------------')
print('STUDENT LIFE')
print('Rules:')
print('Every day you will lose 2 value of intelligence and random value of money because of food etc. 1 day in university will give you 3 value of it, ')
print('you will earn different value of money because every day you have not stability spots of work and it is unreal for you to have stability earning of money')
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
if(student.intelligence==0 or student.intelligence<0 or student.money==0 or student.money<0):
    print('Your intelligence or money is over you can not go on work or in university you will go on work in university to compansate missing value')
else:
    choose=int(input('choose= '))
    x=random.randint(1, 3)
    y=random.randint(1, 6)
    if(choose=='1'):
        student.money=student.money++y
    if(choose=='2'):
        student.intelligence=student.intelligence++3

    student.intelligence=student.intelligence-2
    #student.money=student.money-x
    day.day=day.day+1
    print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
if(student.intelligence==0 or student.intelligence<0 or student.money==0 or student.money<0):
    print('Your intelligence or money is over you can not go on work or in university you will go on work in university to compansate missing value')
else:
    choose=int(input('choose= '))
    x=random.randint(1, 3)
    y=random.randint(1, 6)
    if(choose=='1'):
        student.money=student.money + y
    if(choose=='2'):
        student.intelligence=student.intelligence+3

    student.intelligence=student.intelligence-2
    #student.money=student.money-x
    day.day=day.day+1
    print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
if(student.intelligence==0 or student.intelligence<0 or student.money==0 or student.money<0):
    print('Your intelligence or money is over you can not go on work or in university you will go on work in university to compansate missing value')
else:
    choose=int(input('choose= '))
    x=random.randint(1, 3)
    y=random.randint(1, 6)
    if(choose=='1'):
        student.money=student.money++y
    if(choose=='2'):
        student.intelligence=student.intelligence++3

    student.intelligence=student.intelligence-2
    #student.money=student.money-x
    day.day=day.day+1
    print('------------------------------------')
''''
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
if(student.intelligence==0 or student.intelligence<0 or student.money==0 or student.money<0):
    print('Your intelligence or money is over you can not go on work or in university you will go on work in university to compansate missing value')
else:
    choose=int(input('choose= '))
    x=random.randint(1, 3)
    y=random.randint(1, 6)
    if(choose=='1'):
        student.money=student.money+y
    if(choose=='2'):
        student.intelligence=student.intelligence+3

    student.intelligence=student.intelligence-2
    student.money=student.money-x
    day.day=day.day+1
    print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
if(student.intelligence==0 or student.intelligence<0 or student.money==0 or student.money<0):
    print('Your intelligence or money is over you can not go on work or in university you will go on work in university to compansate missing value')
else:
    choose=int(input('choose= '))
    x=random.randint(1, 3)
    y=random.randint(1, 6)
    if(choose=='1'):
        student.money=student.money+y
    if(choose=='2'):
        student.intelligence=student.intelligence+3

    student.intelligence=student.intelligence-2
    student.money=student.money-x
    day.day=day.day+1
    print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
if(student.intelligence==0 or student.intelligence<0 or student.money==0 or student.money<0):
    print('Your intelligence or money is over you can not go on work or in university you will go on work in university to compansate missing value')
else:
    choose=int(input('choose= '))
    x=random.randint(1, 3)
    y=random.randint(1, 6)
    if(choose=='1'):
        student.money=student.money+y
    if(choose=='2'):
        student.intelligence=student.intelligence+3

    student.intelligence=student.intelligence-2
    student.money=student.money-x
    day.day=day.day+1
    print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
if(student.intelligence==0 or student.intelligence<0 or student.money==0 or student.money<0):
    print('Your intelligence or money is over you can not go on work or in university you will go on work in university to compansate missing value')
else:
    choose=int(input('choose= '))
    x=random.randint(1, 3)
    y=random.randint(1, 6)
    if(choose=='1'):
        student.money=student.money+y
    if(choose=='2'):
        student.intelligence=student.intelligence+3

    student.intelligence=student.intelligence-2
    student.money=student.money-x
    day.day=day.day+1
    print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
if(student.intelligence==0 or student.intelligence<0 or student.money==0 or student.money<0):
    print('Your intelligence or money is over you can not go on work or in university you will go on work in university to compansate missing value')
else:
    choose=int(input('choose= '))
    x=random.randint(1, 3)
    y=random.randint(1, 6)
    if(choose=='1'):
        student.money=student.money+y
    if(choose=='2'):
        student.intelligence=student.intelligence+3

    student.intelligence=student.intelligence-2
    student.money=student.money-x
    day.day=day.day+1
    print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
if(student.intelligence==0 or student.intelligence<0 or student.money==0 or student.money<0):
    print('Your intelligence or money is over you can not go on work or in university you will go on work in university to compansate missing value')
else:
    choose=int(input('choose= '))
    x=random.randint(1, 3)
    y=random.randint(1, 6)
    if(choose=='1'):
        student.money=student.money+y
    if(choose=='2'):
        student.intelligence=student.intelligence+3

    student.intelligence=student.intelligence-2
    student.money=student.money-x
    day.day=day.day+1
    print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
if(student.intelligence==0 or student.intelligence<0 or student.money==0 or student.money<0):
    print('Your intelligence or money is over you can not go on work or in university you will go on work in university to compansate missing value')
else:
    choose=int(input('choose= '))
    x=random.randint(1, 3)
    y=random.randint(1, 6)
    if(choose=='1'):
        student.money=student.money+y
    if(choose=='2'):
        student.intelligence=student.intelligence+3

    student.intelligence=student.intelligence-2
    student.money=student.money-x
    day.day=day.day+1
    print('------------------------------------')
'''


