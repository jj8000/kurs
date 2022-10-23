def max_of_three(x: float, y: float, z: float) -> float or str:
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    elif x == y == z:
        return x
    elif x == y:
        if x > z: return x
        else: return z
    elif z == y:
        if x > z: return x
        else: return z
    elif x == z:
        if y > z: return y
        else: return x



assert max_of_three(1, 3, 4) == 4
assert max_of_three(1, 6, 4) == 6
assert max_of_three(1, -3, 0) == 1
assert max_of_three(145, 144, 144) == 145
assert max_of_three(-1, -3, -40) == -1
assert max_of_three(67, 67, 67) == 67
assert max_of_three(90, -25617, 90) == 90