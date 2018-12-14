import random 
b = random.randint(1, 4)
for i in range(3): 
    a = str(input('Введите число: '))
    if a == 'Выход':
        break
    else:
        if a.isnumeric():
            if int(a) == b:
                print('Победа!')
                break
            elif int(a) < b: 
                print('Загаданное число больше') 
            elif int(a) > b: 
                print('Загаданное число меньше')
        else:
            print('Некорректный ввод')
