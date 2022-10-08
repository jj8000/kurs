
#kalkulator

l_1=float(input("Podaj pierwszą liczbę: "))
l_2=float(input("Podaj drugą liczbę: "))
op=(input("Podaj rodzaj operacji: "))

if op=='+':
	print(l_1+l_2)   
elif op=="-":
    print(l_1-l_2)
elif op=="*":
    print(l_1*l_2)
elif op=="/":
    if l_2==0:
        print("dzielenie przez zero!")
    else:
        print(l_1/l_2)    
elif op=="**":
    print(l_1**l_2)
else:
    print("nieprawidłowa operacja")