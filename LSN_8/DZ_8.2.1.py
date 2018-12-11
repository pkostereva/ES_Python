stack = []

s = input('Введите выражение:')
    
#def polska(s)
b = s.split()
#print (len(b))
for i in range(len(b)):
    if b[i].isdigit():
        stack.append(int(b[i]))
    elif b[i] =='+' and len(stack)>=2:
        op2=stack.pop()
        op1=stack.pop() 
        stack.append(float(op1)+(float(op2)))
        #print (int(op1)+(int(op2)))
    elif b[i] =='-' and len(stack)>=2:
        op2=stack.pop()
        op1=stack.pop()
        stack.append(float(op1)-(float(op2)))
        #print (int(op1)-(int(op2)))
    elif b[i] =='*' and len(stack)>=2:
        op2=stack.pop()
        op1=stack.pop()
        stack.append(float(op1)*(float(op2)))
        #print (int(op1)*(int(op2)))
    elif b[i] =='/' and len(stack)>=2:
        op2=stack.pop()
        op1=stack.pop()
        stack.append(float(op1)/(float(op2)))
        #print (float(op1)/(float(op2)))
print(stack[0])
