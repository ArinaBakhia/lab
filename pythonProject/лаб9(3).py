import csv

itog_sum = 0

with open('лаб9_3.csv', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)
    print('Нужно купить:')
    for name, count, price in reader:
        print(f"{name} - {count} шт. за {price} руб.")
        itog_sum += int(count) * int(price)
print(f'Итоговая сумма: {itog_sum} руб')

