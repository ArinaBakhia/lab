def is_happy_ticket(ticket: str) -> bool:
    midl = len(ticket) // 2
    sum_1 = 0
    sum_2 = 0
    left, right = ticket[:midl], ticket[midl:]
    for num in left:
        sum_1 += int(num)
    for num in right:
        sum_2 += int(num)
    return sum_1 == sum_2
print(is_happy_ticket('28194655'))