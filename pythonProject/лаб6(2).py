word = input("Введите слово: ")
char_value = {
    'авеинорст': 1,
    'дклмпу': 2,
    'бгёья': 3,
    'йы': 4,
    'жзхцч': 5,
    'шэю': 8,
    'фщъ': 10
}
sum_word = 0
for char in word:
    for char_set, value in char_value.items():
        if char in char_set:
            sum_word += value
            break

print(sum_word)
