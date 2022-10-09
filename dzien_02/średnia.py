suma = 0
ilosc = 0
max_number = None
min_number = None

while True:

    x = input("podaj liczbę całkowitą lub k aby zakończyć: ")
    if x == "k":
        break
    x = int(x)
    suma += x
    ilosc += 1

    if max_number is None or x > max_number:
        max_number = x

    if min_number is None or x < min_number:
        min_number = x

srednia = suma/ilosc
print(f"Średnia wynosi {srednia:.2f}")
print("Max: ", max_number)
print("Min: ", min_number)
