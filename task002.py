import math

def prod(list, length):
    result = 1;
    for i in range(0, length):
        result *= list[i]
    return result

#1
print('#1\n');
count = 3
iArr = []
sArr = []
inputStr = ''

for i in range(1,count + 1):
    inputStr = input('Введите число №{0}: '.format(i))
    sArr.append(inputStr)
    iArr.append(int(inputStr))

arrLength = len(iArr)
iSum = sum(iArr)
print('Сумма: {0} = {1}'                .format(' + '.join(sArr), iSum))
print('Произведение: {0} = {1}'         .format(' * '.join(sArr), prod(iArr, arrLength)))
print('Ср. арифм.: ({0}) / {1} = {2:.3f}'.format(' + '.join(sArr), arrLength, iSum/arrLength))

#2
print('\n#2\n');
print('Введите координаты точки A:')
x = float(input('A[x] <-- '))
y = float(input('A[y] <-- '))
print('Введите координаты точки B:')
x -= float(input('B[x] <-- '))
y -= float(input('B[y] <-- '))
print('Длина отрезка AB = {0:.3f}'.format(math.sqrt(x**2 + y**2)))