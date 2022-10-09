import random

DEBUG = True

gracz_x=random.randint(1,10)
gracz_y=random.randint(1,10)

skarb_x=random.randint(1,10)
skarb_y=random.randint(1,10)

ruchy=0

while True:
    odleglosc_przed = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    polecenie=input("Wykonaj ruch (wasd): ")

    if polecenie in "wasd" and len(polecenie) == 1:
        ruchy += 1

    if polecenie == "w":
        gracz_y += 1
    elif polecenie == "s":
        gracz_y -= 1
    elif polecenie == "a":
        gracz_x -= 1
    elif polecenie == "d":
        gracz_x += 1
    else:
        print("złe polecenie")

    if gracz_y == skarb_y and gracz_x == skarb_x:
        print(f"Znalazłeś skarb po {ruchy}. ruchach!")
        break

    if  gracz_y > 10 or gracz_x > 10 or gracz_y < 1 or gracz_x < 1:
        print("Wypadłeś za planszę!")
        break

    odleglosc_po = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

    if random.randint(1,5) != 1:
        if odleglosc_po < odleglosc_przed:
            print("Ciepło")
        elif odleglosc_po > odleglosc_przed:
            print("Zimno")
    else:
        print("Nic nie czujesz")

    if DEBUG:

        print(f"Pozycja gracza: {gracz_x=} {gracz_y=}")
        print(f"Pozycja skarbu: {skarb_x=} {skarb_y=}")



