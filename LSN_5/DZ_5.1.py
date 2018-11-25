import random
st = ['самовар', 'весна', 'лето', 'парк', 'мороженное', 'запрос'] #рандомная строка
r_word = random.choice(st) #выбрали случайное слово
word_str = list(str(r_word)) #переделали слово в список
a = random.choice(word_str)
i = word_str.index(a) #индекс рандомной буквы
word_str[i]='?' #замена на ?
f_user =''.join(word_str)
#print('Выбираем случайное слово:', r_word)
#print('Слово - строка:', word_str)
#print('Индекс:', i)
#print(':', word_str)
print(f'Попробуйте угадать букву в слове {f_user)}')
n = str(input('Введите букву под знаком вопроса:'))
if n == a:
    print(f'Победа! \nСлово: {r_word)}')
else:
    print(f'Увы! Попробуйте в другой раз. \nСлово: {r_word)}')
