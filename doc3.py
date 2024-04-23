#2
#a, b = input('Введите первое число').split('.'), input('Введите второе число').split('.')
#print('f: {0}, s: {1}'.format(
#int(a[0]) + int(b[0]),
#int(a[1]) + int(b[1])
#))

print('Суммы целых и вещественных частей двух чисел: ')
arr = zip(map(int, input('Введите первое число: ').split('.')), map(int, input('Введите второе число: ').split('.')))
print('Результат : {0}, {1}'.format(*[sum(i) for i in arr]))

#10
from datetime import datetime, timedelta
print(str(timedelta(seconds=
    int(input('\nВведите размер файла в ГБ: ')) * 1024**3 * 8 /
    int(input('Укажите скорость интернет-соединения (бит/с): '))
)).split('.')[0].replace('days','дней').replace('day','день'))


#18
d = input('\nВведите количество дней : ')
print('Через {0} дней будет {1}'.format(
    d,
    (datetime.today() + timedelta(days=int(d))).strftime('%d.%m.%y')
))

