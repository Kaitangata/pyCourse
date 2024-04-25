#2
print(list(range(101))[2::2])

#3
print('Сумма чисел в указанном диапазоне: ', sum(range(	
	int(input('\nВведите начало диапозона: ')),	
	int(input('Введите окончание: '))	+ 1	
)))

#10
import re
print('В числе {}встречаются повторяющиеся подряд цифры'.format(
	'' if re.search(r'(.)\1', input('\nВведите проверяемое число: ')) else 'не '
))

#15
def iRecursive(num, base, result, alias):
    integer = num // base
    if integer != 0:
        result.append(iRecursive(integer, base, result, alias))
        return alias[num % base]
    else:
        return alias[num]

def fCycle(num, base, result, alias, nest = 10):
    if num == 0: return

    while True:
        if nest == 0: break

        integer = int(num * base)
        remainder = num * base - integer
        if remainder == 0:
            result.append(alias[integer])
            break
        else:
            result.append(alias[integer])
            num = remainder
        
        nest -= 1
        
enter = [int(num) for num in input('\nВведите число в 10-ой системе счисления: ').split('.')]
if len(enter) == 1:
    enter.append(0)
    
alias = [str(num) for num in range(0, 10)] + ['A', 'B', 'C', 'D', 'E', 'F']
iRes = []; fRes = []
for b in [2, 8, 16]: 
    iRes.clear(); fRes.clear();
    iRes.append(iRecursive (enter[0],   b, iRes, alias)) #целая часть числа в новой системе
    fCycle(float('0.' + str(enter[1])), b, fRes, alias)  #вещественная

    print('Указанное число в {}-ой системе счисления: {}{}'.format(
        b, 
        ''      .join(iRes), 
        '.' + ''.join(fRes) if len(fRes) != 0 else ''
    ))
