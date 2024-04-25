#1
def randomNumbers():
    import random
    #0 pos, 1 neg, 2 even, 3 odd, 4 zero
    arr = [0,0,0,0,0]
    val = 0
    for i in range(100):
        val = random.randint(-100, 100)
        if      val > 0: arr[0] += 1
        elif    val < 0: arr[1] += 1
        elif    val ==0: arr[4] += 1

        if val % 2 == 0 : arr[2] += 1
        else            : arr[3] += 1
    print(('Процентное соотношение положительных - {}%, отрицательных - {}%,\nчетных - {}%, ' +
          'нечетных - {}% чисел и нулей - {}%.').format(
          *arr
    ))

#14
def printCalendar():
    import calendar
    a = calendar.LocaleTextCalendar(locale='en_US.UTF-8')
    print(a.formatyear(2014, w=4))

#19
def printTree():
    fragmentsCount, fragH = int(input('Введите количество ярусов елки: ')), int(input('Высоту яруса: '))
    maxWidth = (1 + (fragH - 1)*2 + (fragmentsCount - 1)*2)*2

    fragStart = 1
    for frag in range(fragmentsCount):
        for line in range(fragH):
            print(('<>'*fragStart + '<>'*line*2).center(maxWidth))
        fragStart +=2
    print(('<><><>'.center(maxWidth) + '\n')*4)

def main():
    randomNumbers() # 1
    printCalendar() #14
    printTree()     #19

main()