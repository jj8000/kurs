l = [9, 1, 6, 8, 4 ,3, 2, 0]
i = 0

for x in l[i:]:
    if x == min(l):
        l.pop(x)
        l.insert(0, x)
        i += 1






print(l)