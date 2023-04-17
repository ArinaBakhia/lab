def div_100(num: int):
    try:
        return 100/num
    except (ZeroDivisionError, TypeErrorError) as err:
        print(f'Ошибка: {err}')

print(div_100(4))
