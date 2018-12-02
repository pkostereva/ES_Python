a = 'Мой дядя самых честных правил, когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог'
b = list(a.split())
i = 0
while i < len(b):
    if b[i].startswith('м') or b[i].startswith('М'):
        del b[i] 
        i -= 1
    i += 1
print(' '.join(b))
