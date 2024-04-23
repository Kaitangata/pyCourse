#1
lastDigit = (input('Вывод младшего разряда натурального числа: ') or 0)[-1]
print ('Младший разряд: ', lastDigit)

#2
string = input('\nВывод десятков двузначного натурального числа: ') or 0
print('Количество десяктов числа : ', string[0] if len(string) > 1 else 0)

#3
n = int(input('\nВывод четного числа, следующего за числом: ') or 0) + 2
print('Четное число : ', n - n % 2)

#4
count = 3
iArr = []

print ('\nРасчет среднего арифметического чисел: ')
for i in range(1,count + 1):
    iArr.append(float(input('Введите число №{0}: '.format(i))))
print('Ср. арифм.: ({0}) / {1} = {2:.3f}'.format(' + '.join(map(str, iArr)), len(iArr), sum(iArr)/len(iArr)))

#5
print ('\nНайти корень уравнения ax + b = 0 : ')
print ('x = ', -float(input('Введите b: ')) / int(input('Введите а: ')))