import random

#2
def evenNumsSum():
    length = 10
    arr = [random.randint(0,100) for i in range(length)]        #10 случайных чисел (на диапазоне [0, 100])
    evenArr = [num if num % 2 == 0 else 0 for num in arr]

    print(arr, '-->', evenArr) #check
    print('Сумма четных чисел массива длиной {} элементов: '.format(length), 
        sum(evenArr) 
        #тоже самое, но в одну строчку
        #sum([
        #    (num if num % 2 == 0 else 0) 
        #    for num in [random.randint(0,100) for i in range(length)]
        #])      

    )

#5
def arrReverse():
    arr = [num for num in range(11)]
    temp = 0
    
    for i, num in enumerate(arr[:len(arr)//2], 0): #проходим первую половину массива
        temp = arr[i]
        arr[i] = arr[-i-1]
        arr[-i-1] = temp
    print('\nРезультат переворачивания массива: ', arr)

#6
def repetition():
    print('\nАнализ повторяющихся чисел: ')
    arr = [random.randint(0,10) for i in range(10)]
    rep = {}
    for num in arr:
        if num in rep:
            rep[num] += 1
        else:
            rep[num] = 1
    #ищем все индексы чисел с максимальным количеством вхождений
    maxEntry = max(rep.values())
    keys = [k for k, v in rep.items() if v == maxEntry]

    print(arr, '-->\n', rep, '-->\n', keys) #check
    print('Наиболее часто встречающееся число массива - {} ({} раз(а))'.format(keys[0], rep[keys[0]]))

def main():
    evenNumsSum() #2
    arrReverse()  #5
    repetition()  #6
main()