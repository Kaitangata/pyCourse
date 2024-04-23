#1
a, b = list(input('Введите первое число :')), list(input('Введите второе число :'))
temp = b[1]
b[1] = a[1]
a[1] = temp
print('Результат: {0}, {1}'.format(''.join(a), ''.join(b)))

#7
print('\nРасчет стоимости покраски комнаты: ')
params = [
float(input('Введите длину комнаты: ')),
float(input('Введите ширину комнаты: ')),
float(input('Введите высоту комнаты: ')),
float(input('Укажите расход краски (л/м^2): ')),
float(input('Площадь не под покраску (двери, окна) в %: ')),
float(input('Стоимость литра краски: '))
]

s = 2 * (
params[0] * params[1] + 
params[0] * params[2] +
params[1] * params[2]
)
s -= s * params[4]/100

print('На покраску комнаты будет затрачено {0} литров краски стоимостью {1} у.е'.format(s*params[3], s*params[3]*params[5]))

#9
num = list(input('\nВведите сдвигаемое число : ') or ['0'])
stride = int((input('Введите количество разрядов : ') or 0)) % len(num)
index = 0

if stride != 0 :
  while stride != 0 :
    num.append(num[index])
    index += 1
    stride-= 1
print(''.join(num[index:]))

