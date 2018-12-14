print('''Простой todo: 
    1. Добавить задачу.
    2. Вывести список задач.
    3. Выход.''')
task = []
while True:
    n = int(input('Укажите число: '))
    if n == 1:
        zad = str(input('Введите задачу: '))
        kat = str(input('Введите категорию к задаче: '))
        time = str(input('Добавьте время к задаче: '))
        task.append([zad, kat, time])
        print(task)
        
    elif n == 2:
        for i in range(len(task)):
            print(f'Задача: {task[i][0]} \nКатегория: {task[i][1]} \nВремя: {task[i][2]}')
    elif n == 3:
        break
    
    
    
