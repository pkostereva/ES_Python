import random
st = ['самовар', 'весна', 'лето', 'парк', 'мороженное', 'запрос']
r_word = random.choice(st)
word_str = list(str(r_word))
a = random.choice(word_str)
i = word_str.index(a)
word_str[i]='?'
f_user =''.join(word_str)
print(f'Попробуйте угадать букву в слове {f_user}')
n = str(input('Введите букву под знаком вопроса:'))
if n == a:
    print(f'Победа! \nСлово: {r_word}')
else:
    print(f'Увы! Попробуйте в другой раз. \nСлово: {r_word}')
