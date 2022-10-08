#para liczb

while True:
 x=float(input("Podaj wartość x: "))
 y=float(input("Podaj wartość y: "))

 if 0 < x <= 10:
     if 0 < y <= 10:
         print("lewy dolny róg")
     elif 10<  y <=90:
         print("lewa krawędź")
     elif 90< y <=100:
         print("lewy górny róg")
     else:
         print("poza zakresem")
 elif 10< x <=90:
     if 0<y<=10:
         print("dolna krawędź")
     elif 10<y<=90:
         print("obszar środkowy")
     elif 90<y<=100:
         print("górna krawędź")
     else:
         print("poza zakresem")
 elif 90<x<=100:
     if 0<y<=10:
         print("prawy dolny róg")
     elif 10<y<=90:
         print("prawa krawędź")
     elif 90<y<=100:
         print("prawy górny róg")
     else:
         print("poza zakresem")
 else:
     print("poza zakresem")