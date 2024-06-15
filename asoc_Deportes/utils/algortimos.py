def quicksort_Algorit(lista, key=None):
    if len(lista) <= 1:
        return lista

    if key is None:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        mayores = [x for x in lista[1:] if x >= pivote]
    else:
        menores = []
        mayores = []
        pivote = lista[0]
        pivot_val = key(pivote)
        for x in lista[1:]:
            val = key(x)
            if val < pivot_val:
                menores.append(x)
            else:
                mayores.append(x)

    return quicksort_Algorit(menores, key) + [pivote] + quicksort_Algorit(mayores, key)