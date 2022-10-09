Program do BMI


waga=int(input("podaj swoją wagę w kg "))
wzrost=float(input("podaj swój wzrost w metrach "))

bmi=waga/(wzrost**2)

print("Współczynnik BMI: ", round(bmi,2))