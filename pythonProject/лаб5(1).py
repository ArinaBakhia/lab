def is_in_list(num: int, list_nums: list):
    if num in list_nums:
        print('Поздравляю, Вы угадали число!')
    else:
        print('Нет такого числа!')


LIST_NUMS = [12, 23, 34, 45, 56]
num_ = int(input('Введите число: '))
is_in_list(num_, LIST_NUMS)