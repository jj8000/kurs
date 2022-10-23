def kalkulator(x: float, y: float, o: int) -> float or str:
    if o == 1:
        return x + y
    elif o == 2:
        return x - y
    elif o == 3:
        return x * y
    elif o == 4:
        if y == 0:
            return "dzielenie przez zero niedozwolone"
        else:
            return x / y
    else:
        return "nieznana operacja"

if __name__ == "main":
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    o = int(input("Podaj rodzaj operacji(1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie): "))

    print(kalkulator(x, y, o))
