def suma(*args, **kwargs) -> int:
    total = 0
    for i in args:
        if type(i) is dict:
            total += sum(i.values())
        elif type(i) is int:
            total += i
        else:
            total += sum(i)
    for k, v in kwargs.items():
        total += sum(v)

    return total

def test_suma1():
    assert suma() == 0

def test_suma2():
    assert suma(1, 2, 0, (4, 5, 7), [5, 7, 0] ) == 31

def test_suma3():
    assert suma(1, {2, 3, 5}) == 11

def test_suma4():
    assert suma(3, {"d": 5, 8: 7, 9: 0, 4: -4}) == 11

def test_suma5():
    assert suma(1, a={5, 6, 9}) == 21
