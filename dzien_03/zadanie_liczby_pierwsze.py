def primechk(arg:int):
        for i in range(2, arg):
            if arg % i == 0:
                return False
        return True

while True:

    liczba = int(input(f"Podaj liczbę naturalną: "))

    print(primechk(liczba))