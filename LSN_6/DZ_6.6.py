a = str(input('Введите число: '))
b = list(a)
s = 0
for i in range(len(b)): 
    if i % 2 == 0:
        continue
    s = s + pow(int(b[i]), 2)  
else:
    print(s)
