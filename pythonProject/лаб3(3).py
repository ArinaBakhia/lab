#slovo = str(input("введите слово: "))
#if "ф" in slovo:
    #print("Ого! Это редкое слово!")
#else:
    #print("Эх, это не очень редкое слово...")

n = str(input())
for i in n:
    if i =='ф':
        print("Ого! Это редкое слово!")
        break
    else:
        print("Эх, это не очень редкое слово...")
        