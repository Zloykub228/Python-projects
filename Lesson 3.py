'''
try:
    a = int(input('a- '))
    b = int(input('b- '))

    print('a/b >>> ', a/b)
except:
    print('На ноль не делится')

try:
    print('Hi start code')
    print(code)
    print(125/0)
    print('no errors...')
except (NameError, ZeroDivisionError) as error:
    print(error)
print('The end')

try:
    a= int(input('a- '))
    print('2 * a', 2 * a)
except:
    print('Не целое число братанчик')

def checker(var 1)
    if type(var 1) != str:
        raise TypeError(f'Sorry, we can\'t work with {type(var_1)}'
                        f'we need class str')
    else:
        return car_1
first_var = 10
checker(first_var)


class BuildingError(Exception):
    def __str__(self):
        return f'With so much material the house can\' built!'
def check_material(amount_of_material, limit_value):
    if check_material > limit_value:
        return 'enough material'
    else:
        raise BuildingError(amount_of_material)
materials = 123
check_material(materials, 300)


import warnings

warnings.warn('Warning, no code here', SyntaxWarning)
warnings.warn('Warning, module not inmport', ImportWarning)
warnings.simplefilter('Always', ImportWarning)
warnings.simplefilter('ignore', SyntaxWarning)

str_1 = 'strings'
for i in str_1:
    print(i)
lst = [125, 'date', '456']
for i in lst:
    print(i)
tpl = ('qwerty', 125, '234')
for i in tpl:
    print(i)

set_1 = {123, 'mama', 'papa'}
for i in set_1:
    print(i)
froz = frozenset({456, 'family', 'mama'})
for i in froz:
    print(i)
dct = {'1': 'papa', '2': 'mama'}
for i in dct:
    print(i)
for i in dct:
    print(dct[i])
str1 = 'mamapapafamily'
print(set(str1))
print(list(str1))
lst = ['mama', 124, 'mama', 124]
print(set(lst))
lst_2 = [123,[178, 'str', 567], 'itstep']
iterator=iter(lst_2)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))

for elem in iterator:
    print(elem)
class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i
count = Counter(10)
#for elem in count:
    #print(elem)
print(count.__next__())
print(count.__iter__())
print(next(count))
print(next(count))
print(next(count))
'''
def raise_to_the_deegrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1
res = raise_to_the_deegrees(122345, 10)
print(res)

for _ in res:
    print(_)
print('************************')
for _ in res:
    print(_)

def raise_to_the_degrees_2(number):
    i = 0
    while True:
        #yield number ** i
        #i += 1
        result = number ** i
        yield result
        if result > 100 ** 20:
            return
        else:
            i += 1
res = raise_to_the_degrees_2(122345)
print(res)
for _ in res:
    print(_)

class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f'I will help you with {self.work}.'\
               f'Afterwards I will help you with {work}'

helper = Helper('homework')
print(helper('cleaning'))

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

calculate = checker(calculate)
calculate('2+2')
