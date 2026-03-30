def busca_maior(arr):
    maior = arr[0]
    menor_indice = 0
    for i in range(1,len(arr)):
        if arr[i] > maior:
            maior = arr[i]
            menor_indice = i
    return menor_indice
def listamaismenos(arr):
    novoarr = []
    for i in range(len(arr)):
        maior = busca_maior(arr)
        novoarr.append(arr.pop(maior))
    return novoarr
print(listamaismenos([0,2,5,64,71,92,104]))
