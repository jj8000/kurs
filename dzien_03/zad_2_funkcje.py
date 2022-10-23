def wiecejniz(arg1: str, arg2: int) -> set:
    w = set()
    for i in arg1:
        if arg1.count(i) > arg2:
            w.add(i)
    return w

print(w)