import random
b = random.randint(1, 4)
a = int(input('Введите число: '))
if a == b:
    print('Победа!')
else:
    if b>a:
        print('Введенное число меньше')
    else:
        print('Введенное число больше')
