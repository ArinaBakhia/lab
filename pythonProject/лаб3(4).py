from random import randint
counter = 0
MISTAKE = 3
answers = 0
while counter != MISTAKE:
    a = randint(0, 1000)
    b = randint(0, 1000)
    resp = int(input(f'{a} + {b} = '))
    if (a + b) == resp:
        print('Правильно!')
        answers += 1
    else:
        counter += 1
        print( f'Ответ неверный, осталось попыток {MISTAKE - counter}')

print(f'Игра окончена. Правильных ответов: {answers}')
