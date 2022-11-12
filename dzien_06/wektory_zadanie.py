class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"[{self.x}, {self.y}]"

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __mul__(self, other):
        if type(other) == int:
            return self.__class__(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

a = Vector(1, 2)
b = Vector(2, 3)
c = Vector(0, -1)
w = Vector(2, 4)

print(a + b)
print(a - b)
print(b - a)
print(a + b + c)


def test_multiply():
    assert a + b == Vector(3, 5)
    assert 2 * a == Vector(2, 4)
    assert a * 2 == Vector(2, 4)
#
#
#
# @pytest.mark.skip("not yet")
# def test_multiply_vector(self):
#     a = Vector(1, 2)
#     b = Vector(2, 3)
#     c = Vector(0, -1)