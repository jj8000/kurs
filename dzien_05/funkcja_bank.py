class PoleKwadratu:
    def __init__(self, bok):
        self.bok = bok
        self.pole = bok ** 2

a = PoleKwadratu(4)
b = PoleKwadratu(6)

print(a.pole)
print(b.pole)