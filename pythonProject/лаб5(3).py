WEEK = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
d = 7 - int(input('Введите количество выходных: '))
print(f'''Ваши выходные дни: {WEEK[d:]}
Ваши рабочие дни: {WEEK[:d]}''')
