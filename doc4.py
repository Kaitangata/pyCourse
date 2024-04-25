#4
print('Калькулятор:')
operators = ('+', '-', '*', '/', '%')
a, b = float(input('Введите первое число: ')), float(input('Введите второе число: '))
print('Операции над числами:')
for index, operator in enumerate(operators):
    print('{0}) a {1} b'.format(index, operator))
index = input('Укажите номер операции :')
if index.isdigit() :
    index = int(index)
    if index >= 0 and index < len(operators) :
        if not ((operators[index] == '/' or operators[index] == '%') and b == 0) :
            result = 0; exec('result = a {0} b'.format(operators[index]))
            print('Результат: {0} {1} {2} = {3}'.format(a, operators[index], b, result))
        else:
            print('Деление на ноль.')
    else:
        print('Введен некорректный номер операции.')
else :
    print('Введен некорректный номер операции.')
 
#8
number = int(input('\nВведите число для проверки его кратности (3, 5, 7): '))
print('Введенное число {0}кратно числам 3, 5, 7'.format(
    'не ' if (number % 3 + number % 5 + number % 7) != 0 else ''
))

#11
number = tuple(input('\nВведите число-палиндром: '))
isPalindrome = True
for i, val in enumerate(number[::-1]) :
    if val != number[i] :
        result = False
        break;
print('Число {0} {1}является полиндромом.'.format(''.join(number), '' if isPalindrome else 'не '))

#13
print('\nВведите 4 числа для определения максимального')
a,b,c,d = map(float, (input('№1: '), input('№2: '), input('№3: '), input('№4: ')))
print('Максимальное число - ',
    ((a if a > d else d) if a > c else (c if c > d else d)) if a > b else ((b if b > d else d) if b > c else (c if c > d else d))
)