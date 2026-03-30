def maximo(lista):
    if len(lista) == 2:
        if lista[0] > lista [1]:
            return lista[0]
        else:
            return lista[1]

    sub_max = maximo(lista[1:])

    if lista[0] > sub_max:
        return lista[0]
    else:
        return sub_max

print(maximo([0,2,652,7,127,17,8]))
