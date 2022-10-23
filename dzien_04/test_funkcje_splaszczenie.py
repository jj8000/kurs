from funkcje_splaszczenie import splaszcz
# import funkcje_splaszczenie
print(dir())

def test_splaszcz_pusta():
    assert splaszcz([]) == []

def test_splaszcz_plaska():
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]

def test_splaszcz_zagn():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]
    assert splaszcz([1, [[2, 3]]]) == [1, 2, 3]