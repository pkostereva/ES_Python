from pprint import pprint
import json
print('''
1. Добавить задачу.
2. Вывести список задач.
3. Выход.
''')
n=0
while True:
    n=input('Выберете пункт: ')
    if n.isnumeric():
        if int(n) == 1:
            print('\n')
            a=input('Задача: ')
            b=input('Категория: ')
            c=input('Время: ')
            print('\nЗадача добавлена!\n')
            with open('task.json', 'a') as file:
                file.write(f'Задача: {a} Категория:{b} Время: {c}'+'\n')
                file.close()
        elif int(n) == 2:
            print('\n')
            with open('task.json', 'r') as file:
                print(file.read())
                file.close()
            #for i in range(len(task)):
            #    print(f'Задача: {task[i][0]}, Категория: {task[i][1]}, Время: {task[i][2]}')
        elif int(n) == 3:
            break
    else:
        print('\nОшибка ввода')
