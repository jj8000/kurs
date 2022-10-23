l = [1, 2, 3, [4, 5, [6]], 7]

def splaszcz(l: list) -> list:
    '''
    >>> splaszcz([1, 2, 3, [4, 5, [6]], 7])
    [1, 2, 3, 4, 5, 6, 7]
    '''
    splaszczona_lista = []
    for i in l:
        if type(i) is not list:
            splaszczona_lista.append(i)
        else:
            for i_zagniezdzone in splaszcz(i):
                splaszczona_lista.append(i_zagniezdzone)

    return splaszczona_lista

w = splaszcz(l)

print(w)