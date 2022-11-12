dane = "logs.txt"


w ith open(dane) as f:
    for x in f:
        listy = x.split(';')
        print(listy)