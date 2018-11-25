s = 'У лукоморья 123 дуб зеленый 456'
a = s.find('я')
print('Индекс буквы я', a)
b = s.count('у')
print('Буква у встречается',b, 'раза')
if not s.isupper():
    print(s.upper())
if len(s) > 4:
    print(s.lower())
d = s.replace('У', 'О')
print(d)
