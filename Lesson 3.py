'''
try:
    a = int(input('a- '))
    b = int(input('b- '))

    print('a/b >>> ', a/b)
except:
    print('На ноль не делится')
'''
try:
    print('Hi start code')
    print(error)
    print(125/0)
    print('no errors...')
except (NameError, ZeroDivisionError):
    print('We have an error...'
          'or we have an ZerodivisionError...')