#        012345678910
napis = "Ala ma kota"

print(len(napis))
print("A" in napis)

print(napis.lower().count("a"))
print(napis.index("A"))

print(napis[4])
print(napis[3:6])
print(napis[1:10:2])
print(napis[1:])
print(napis[:6])
print(napis[:6:2])
print(napis[::3])
print(napis[1]+napis[5]+napis[8])

# [początek:koniec_otwarty:krok]

print(napis[-1])
print(napis[::-1])

napis2 = "O" + napis[1:]
print(napis2)

# tuple

t = (1, 2, 3, 2, 2, "a")
print(t)
print(type(t))
#print(dir(t))

print(t.count(2))
print(t.index(3, 2))

print(t[1::-2])

print(tuple("123"))

print(type(1))
print(type((1,)))

# lista

l = [1, 2, 3, 2, 2, 2.0]
print(l)
print(dir(l))

print("0", sorted(l))
print("1", l.sort())
print("2", l)

l.append("a")

print(l)

print("----------")

l.insert(1, "b")
print(l)

print(l[2::2])

print(l.count(2))


# pętle for



t=(1, 3, 67, 8, 0, 0, 2.5, "k", "m", 0)

print(t[1])
print(t[-2])
print(t[2:7])
print(t[0::3])
print(t[-1::-1])

n="Warszawa"

print(n[1])
print(n[-2])
print(n[2:7])
print(n[0::3])
print(n[-1::-1])

k=[0, 0, 1, 4, 0, 1, 8, 7, "j", "A"]

k.append(33)
print(k)

k.insert(2, 99)

print(k)
print()

k[5] = "u"

print(k)

k.pop(-1)

print(k)

