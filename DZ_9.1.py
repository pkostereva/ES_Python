from pprint import pprint
import json
n=0
z=0
task=dict()
while True:
    print('\n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.')
    n=input('Выберете пункт: ')
    if n.isnumeric():
        if int(n) == 1:
            print('\n')
            a=input('Задача: ')
            b=input('Категория: ')
            c=input('Время: ')
            task[z]={0 : a, 1 : b, 2 : c}  
            with open('task.txt', 'a') as file:
                print(task[z])
                file.write( json.dumps(task[z], ensure_ascii=False))
            z += 1
        elif int(n) == 2:
            print('\n')
            for i in range(len(task)):
                print(f'Задача: {task[i][0]}, Категория: {task[i][1]}, Время: {task[i][2]}')
        elif int(n) == 3:
            break
    else:
        print('\nОшибка ввода')
