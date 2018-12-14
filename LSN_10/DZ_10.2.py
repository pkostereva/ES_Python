import tkinter
import random

window = tkinter.Tk()

A = {'dog' : 'собака', 'cat' : 'кошка', 'ball' : 'мяч', 'bed' : 'кровать', 'milk' : 'молоко'}
m = tkinter.StringVar()
e = random.choice((list(A.keys())))
def click():
    if m.get() == A[e]:
        a = 'Верно!'
    else:
        a = 'Неверно!'
    label.config(text = a)
    print(e)
    print(A[e])
    print(entry)

frame = tkinter.Frame(window)
frame.pack()

label = tkinter.Label(frame, text=e)
label.pack()

label = tkinter.Label(frame, text='Укажите перевод слова:')
label.pack()

entry = tkinter.Entry(frame, textvariable=m)
entry.pack()

button = tkinter.Button(frame, text = 'Готово!', command=click)
button.pack()

button = tkinter.Button(frame, text = 'Выход', command=window.destroy)
button.pack()

window.mainloop()


