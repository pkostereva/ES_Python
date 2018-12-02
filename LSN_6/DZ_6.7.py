s = 0
a = 0
while a != 'Стоп':
    a = str(input('Введите число: '))
    #print(a.isnumeric)
    if a.isnumeric():
        s = s + int(a)
    elif a:
        break
    else:
        print('Повторите ввод ')
print(s)
