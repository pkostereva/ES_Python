def f(a, n):
    if len(a) > n:
        return a.upper()
    else:
        return a
string = str(input())
num = int(input())
result = f(string, num)
print(result)

