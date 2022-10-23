# licznik liter

zadany_tekst = "ala ma kota"

# napisz skrypt, który utworzy słownik zawierający liczbę wystąpień danego znaku w zadanym tekście

slownik = {}

for i in zadany_tekst:
    slownik[i] = 0

for i in zadany_tekst:
    slownik[i] += 1

print(slownik)

#drugi sposób:

slownik = {}

for i in zadany_tekst:
    slownik[i] = slownik.get(i, 0) + 1

print(slownik)