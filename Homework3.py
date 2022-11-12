print('Select the action of the calculator (1-adding numbers, 2-subtracting numbers, '
      '3-multiplying numbers, 4-dividing numbers, 5-exponentiation ')
choice = int(input('Your choice= '))
a = (int(input('a= ')))
b = (int(input('b= ')))
def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f'We have problems {exc}')
        else:
            print(f'No problems. Result-{result}')
    return checker
def calculate(expression):
    return eval(expression)


if choice==1:
    calculate = checker(calculate)
    calculate('a+b')
if choice==2:
    calculate = checker(calculate)
    calculate('a-b')
if choice==3:
    calculate = checker(calculate)
    calculate('a*b')
if choice==4:
    calculate = checker(calculate)
    calculate('a/b')
if choice==5:
    calculate = checker(calculate)
    calculate('a**b')