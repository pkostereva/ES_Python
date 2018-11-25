discount=0
price=0
print("""Фильм «Пятница»,
сеансы:
12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб.
Фильм «Чемпионы»,
сеансы:
10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб.
Фильм «Пернатая банда»,
сеансы:
10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб. """)
f = input("Выберите фильм: ")
v = input("Выберите день (сегодня, завтра): ")
t = int(input("Выберите время: "))
k = int(input("Укажите колличество билетов: "))

def calc(a, b, c):
    return a * b * ((100 - c) / 100)

if v == "завтра":
    discount = discount + 5
if k >= 20:
    discount = discount + 20

if f == "Пятница":
    if v == 12:
        price = 250
        print("Стоимость билетов: ", calc(price, k, discount))
    elif t==16:
        price = 350
        print("Стоимость билетов: ", calc(price, k, discount))
    elif t == 20:
        price = 450
        print("Стоимость билетов: ", calc(price, k, discount))

if f == "Чемпионы":
    if t == 10:
        price = 250
        print("Стоимость билетов: ", calc(price, k, discount))
    elif t == 13 or t == 16:
        price = 350
        print("Стоимость билетов: ", calc(price, k, discount))    

if f == "Пернатая банда":
    if t == 10:
        price = 350
        print("Стоимость билетов: ", calc(price, k, discount))
    elif t == 14 or t == 18:
        price = 450
        print("Стоимость билетов: ", calc(price, k, discount))

if price == 0: print("Не корректные данные")
