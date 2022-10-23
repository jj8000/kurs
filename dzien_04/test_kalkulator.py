from kalkulator import kalkulator


def test_kalk_dod():
    assert kalkulator(67, -45, 1) == 22

def test_kalk_odej():
    assert kalkulator(76, 9, 2) == 67

def test_kalk_mn():
    assert kalkulator(8, -2.5, 3) == -20

def test_kalk_dziel():
    assert kalkulator(81, 3, 4) == 27

def test_kalk_dziel0():
    assert kalkulator(5477, 0, 4) == "dzielenie przez zero niedozwolone"

def test_kalk_niezn():
    assert kalkulator(78, 234, 9) == "nieznana operacja"
