s = 'У лукоморья 123 дуб зеленый 456'
a = s.find('я')
print('Индекс буквы я', a)
b = s.count('у')
print('Буква у встречается',b, 'раза')
if s.isalpha():
    print(s.upper())
if not s.isupper():
    print(s.upper())
if len(s) > 4:
    print(s.lower())
d = 'О'+s[1:]
print(d)
