import tkinter
from tkinter import messagebox

def addTask():
    with open('task.json', 'a') as file:
        file.write(f'Задача: {entry_task.get()} Категория:{entry_cat.get()} Время: {entry_time.get()} \n')
        file.close()
        messagebox.showinfo(message = 'Задача добавлена!')

    printTask()

def printTask():
    print('\n')
    with open('task.json', 'r') as file:
        #label.config(text = file.read())
        text.insert(1.0, file.read())
        file.close()

window = tkinter.Tk()

frame_top = tkinter.Frame(window)
frame_top.pack(side = 'top')

frame_left= tkinter.Frame(window)
frame_left.pack(side = 'left')

frame_right = tkinter.Frame(window)
frame_right.pack(side = 'right')

label = tkinter.Label(frame_top, text = 'Менеджер задач')
label.pack()

# Ввод задачи

frame1 = tkinter.Frame(frame_left)
frame1.pack()
label_task = tkinter.Label(frame1, text = 'Задача    ')
label_task.pack(side = 'left')
entry_task = tkinter.Entry(frame1)
entry_task.pack(side = 'right')

# Ввод категории

frame2 = tkinter.Frame(frame_left)
frame2.pack()
label_cat = tkinter.Label(frame2, text = 'Категория')
label_cat.pack(side = 'left')
entry_cat = tkinter.Entry(frame2)
entry_cat.pack(side = 'right')

# Ввод времени

frame3 = tkinter.Frame(frame_left)
frame3.pack()
label_time = tkinter.Label(frame3, text = 'Время      ')
label_time.pack(side = 'left')
entry_time = tkinter.Entry(frame3)
entry_time.pack(side = 'right')

# Кнопка Добавления

frame4 = tkinter.Frame(frame_left)
frame4.pack()
button_add = tkinter.Button(frame4, text = 'Добавить задачу', command=addTask)
button_add.pack()

# Кнопка Вывода

frame5 = tkinter.Frame(frame_left)
frame5.pack()
button_view = tkinter.Button(frame5, text = 'Вывод списка', command=printTask)
button_view.pack()

# Кнопка Выхода

frame6 = tkinter.Frame(frame_left)
frame6.pack()
button_exit = tkinter.Button(frame6, text = 'Выход', command=window.destroy)
button_exit.pack()

# Вывод справа

frame8 = tkinter.Frame(frame_right)
frame8.pack(side = 'left')
text = tkinter.Text(frame8, width = '36', height = '12', font = 'Arial 14')
text.pack()

frame9 = tkinter.Frame(frame_right)
frame9.pack(side = 'right')
scrollbar = tkinter.Scrollbar(frame9)
scrollbar.pack(side = 'right', fill = 'y')
scrollbar['command'] = text.yview
text['yscrollcommand'] = scrollbar.set

window.mainloop()

    
