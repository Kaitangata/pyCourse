#14
import random, re
from math import ceil, pow

reward = [0,0,300, 4000, 50000]
numbers = []
count = 0
num = 0

while count < len(reward):
    num = random.randint(0, 42)
    if not (num in numbers):
        numbers.append(num)
        count += 1
#print(numbers) -- cheat
print('Угадайте пять чисел (вероятность угадать {:.10f}%): '.format(pow(1/42, 5)))
count = 0
index = 0
for i in range(len(reward)):
    try:
        index = numbers.index(int(input('Число №{} : '.format(i+1))))
        del numbers[index]
        count += 1
    except:
        continue

print('Вы угадали {0} из {1} чисел. Ваш выигрыш составляет {2} рублей!'.format(
    count, 
    len(reward), 
    0 if count <= 0 else reward[count-1]
))

#16
print('\nРасчет окупаемости яичного бизнеса: ')
chickens, chCost, chSpeed, eggCost = \
    int     (input('Введите количество куриц: ')), \
    float   (input('Стоимость одной курицы: ')), \
    int     (input('Укажите яйценоскость (яйцо/неделя) : ')), \
    float   (input('Стоимость десятка яиц : '))
#НДС 10% на продовольственные товары
#x = y - y * 0.1 --> x = y * 0.9 --> y = x * 10/9
# debt = chickens * chCost * 10 / 9 - долг
# debt / eggCost * 10 - количество яиц
#(debt / eggCost * 10) / chSpeed - количество недель
# * 7 - количество дней
print('Бизнес окупится за {} дн(я)(ей)'.format(ceil(
    ((((chickens * chCost * 10/9) / eggCost) * 10) / chSpeed) * 7
)))

#17
def win(roll, combinations, out):
    for k, v in combinations.items():
        if re.fullmatch(k, roll):
            out[0] = v
            return True
    return False

rollCost = 10
balance = 100
print('\nОднорукий бандит: \
\nВаш баланс: {} у.е. \
\nДля выхода введите символ \"Х\" или любой другой символ для броска.'.format(balance))

enter = ''
roll = ''
combinations = {'000':50, '111':50, '222':50, '333':50, '444':50, '555':50, '55\d':25, '5\d\d':15, '77\d':25, '7\d\d':15}
reward = [0]

while True:
    enter = input()
    if enter.lower() in ['x', 'х']: 
        break

    if balance - rollCost < 0 :
        print('На вашем балансе недостаточно средств!')
        break

    balance -= rollCost
    roll = str(random.randint(0, 777)).zfill(3)
   
    if roll == '777':
        balance += 5000
        print('Победа! Вы сорвали джек-пот!')
        break
    elif roll == '666':
        balance = 0
        print('Поражение! Средства с вашего счета ушли казино!')
        break
    elif win(roll, combinations, reward):
        balance += reward[0]
        print('Выпавшая комбинация: {}, баланс: {} у.е (+{})'.format(roll, balance, reward[0] - rollCost))
    else:
        print('Выпавшая комбинация: {}, баланс: {} у.е (-{})'.format(roll, balance, rollCost))

print('Вы завершили игру с балансом: {} у.е'.format(balance))
