import random
import time

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
time.sleep(1)
print('His height-', student.height)
time.sleep(1)
print('His age-', student.age)
time.sleep(1)
print('His intelligence-', student.intelligence)
time.sleep(1)
print('His money-', student.money)
time.sleep(1)
print('Starting the game...')
time.sleep(1)
print('------------------------------------')
time.sleep(1)
print('STUDENT LIFE')
time.sleep(1)
print('Rules:')
time.sleep(1)
print('Every day you will lose 2 value of intelligence and random value of money because of food etc. 1 day in university will give you 3 value of it, ')
time.sleep(1)
print('you will earn different value of money because every day you have not stability spots of work and it is unreal for you to have stability earning of money')
time.sleep(1)
print('------------------------------------')
time.sleep(1)
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('Day', day.day, ':')
print('Your intelligence-', student.intelligence)
print('Your money-', student.money)
x=random.randint(1, 3)
y=random.randint(1, 6)
if(student.intelligence==0 or student.intelligence<0):
    print('Your intelligence is over you can go on work or in university, but until it you will go in university forced without choice to compansate missing value')
    student.money = student.money + y
if(student.money==0 or student.money<0):
    print('Your money is over you can go on work or in university, but until it you will go on work forced without choice to compansate missing value')
    student.money = student.money + y
print('Will you go on work or in university?')
print('write bellow 1(work) or 2(university)')
choose=int(input('choose= '))
if(choose==1):
    student.money=student.money+y
if(choose==2):
        student.intelligence=student.intelligence+3
student.intelligence=student.intelligence-2
student.money=student.money-x
day.day=day.day+1
print('------------------------------------')
print('You did student challenge ')



