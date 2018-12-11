stack = []
b = []
def st(b):
    if b[y].isdigit():
        stack.append(int(a))
    elif b[y] =='+' and len(stack)>=2:
        op2=stack.pop()
        op1=stack.pop()
        stack.append(op1+op2)
    elif b[y] =='-' and len(stack)>=2:
        op2=stack.pop()
        op1=stack.pop()
        stack.append(op1-op2)
    elif b[y] =='*' and len(stack)>=2:
        op2=stack.pop()
        op1=stack.pop()
        stack.append(op1*op2)
    elif b[y] =='/' and len(stack)>=2:
        op2=stack.pop()
        op1=stack.pop()
        stack.append(op1/op2)
c = input('Введите число/ знак/ End для выхода: ')
d = c.split()
for i in len(d):
    st(d[i])    
print(d)
