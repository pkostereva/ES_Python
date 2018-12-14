a = str(input('Введите число: '))
b = list(a)
s = 0
print(b)
for i in range(len(b)): 
    if int(i) % 2 == 0:
        s += pow(int(b[i]), 2)
else:
    print(s)
