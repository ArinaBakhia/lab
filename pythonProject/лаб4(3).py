def magic_date(date: str) -> bool:
    day, month, year = date.split('.')
    return int(day) * int(month) == int(year[2:])
print(magic_date('23.01.2023'))