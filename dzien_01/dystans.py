

# koszty przejazdu

miasto_1=input("podaj miasto startowe: ")
miasto_2=input("podaj miasto docelowe: ")
odl=float(input("podaj odległość w km: "))
spalanie=float(input("podaj spalanie w l/100 km: "))
cena=float(input("podaj koszt paliwa w zł: "))


koszt=odl*spalanie*cena/100

print(f"Koszt podróży z {miasto_1} do {miasto_2} wynosi {koszt:.2f} zł")