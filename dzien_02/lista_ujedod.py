lista = [1, 3, 5, -2, 6, 0, -7]

dodatnich = 0
ujemnych = 0

for el in lista:
    if el > 0:
        dodatnich +=1
    elif el < 0:
        ujemnych += 1


print(f"{dodatnich=} {ujemnych=}")