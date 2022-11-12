result = []
import warnings
a = int(input('a= '))
b = int(input('b= '))

if (a<b):
    warnings.warn('a<b')
if (b>100):
    warnings.warn('b>100')




data = {10: 2, 2: 5, 123:4, 18:0, 8: 4}
for key in data:
    res = (key, data)
    result.append(res)

print(result)
