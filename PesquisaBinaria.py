def pesquisabinaria(lista, item):
    menor = 0
    maior = len(lista) - 1
    while menor <= maior:
        meio = (maior + menor)//2
        chute = lista[meio]
        if chute == item:
            return chute
        if chute > item:
            baixo = meio + 1
        else:
            alto = meio - 1
    return None
lista = [2,3,4,5,6,7,8,9,10]
print(pesquisabinaria(lista,4))
