

ceny = {"marchew": 3, "cebula": 3.5, "śliwki": 5.5, "grzyby": 19}
stan = {"marchew": 6, "cebula": 8, "śliwki": 11, "grzyby": 7}

print("Witaj w warzywniaku!")

tryb = input("Rodzaj pracy: m-magazyn, k-kasa, z-zakończ")

if tryb == "k":

print("Oferujemy: ")
for produkt, cena in ceny.items():
    print(f" - {produkt:20}: {cena:5.2f} zł/kg")

# print(f' - Marchew - {ceny["marchew"]:.2f} zł/kg')
# print(f' - Cebulę  - {ceny["cebula"]:.2f} zł/kg')
# print(f' - Śliwki  - {ceny["śliwki"]:.2f} zł/kg')
# print(f' - Grzyby  - {ceny["grzyby"]:.2f} zł/kg')

naleznosc = 0
while True:

    produkt = input("Co chcesz kupić? (Enter by zakończyć)")
    if produkt == "":
        break
    ilosc = float(input(f"Ile kg '{produkt}' chcesz kupić? "))

    if ilosc > stan[produkt]:
        print(f"Dostepne tylko {stan[produkt]} kg {produkt}")

    else:
        naleznosc += ilosc * ceny[produkt]

if naleznosc:
    print(f'Należy się {naleznosc:.2f} zł')
else:
    print("może innym razem...")


