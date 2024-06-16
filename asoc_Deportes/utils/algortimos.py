import timeit
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

def compare(a, b, key):
    return key(a) < key(b)

def merge_sort(lista, key=lambda x: x):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio], key)
    derecha = merge_sort(lista[medio:], key)

    return merge(izquierda, derecha, key)

def merge(izquierda, derecha,key):
    if not izquierda:
        return derecha
    if not derecha:
        return izquierda

    result = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if compare(izquierda[i], derecha[j], key):
            result.append(izquierda[i])
            i += 1
        else:
            result.append(derecha[j])
            j += 1

    result.extend(izquierda[i:])
    result.extend(derecha[j:])
    return result

""" # Casos de prueba (Merge Sort)
start_time = timeit.default_timer()
merge_sort([3, 5, 2, 1, 6])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el primer caso de prueba (Merge Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

start_time = timeit.default_timer()
merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el segundo caso de prueba (Merge Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

start_time = timeit.default_timer()
merge_sort([])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el tercer caso de prueba (Merge Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

start_time = timeit.default_timer()
merge_sort([5])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el cuarto caso de prueba (Merge Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

start_time = timeit.default_timer()
merge_sort([6,5,4,3,2,1])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el quinto caso de prueba (Merge Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

start_time = timeit.default_timer()
merge_sort([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el sexto caso de prueba (Merge Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

# Casos de prueba para Quick Sort
start_time = timeit.default_timer()
quicksort_Algorit([3, 5, 2, 1, 6])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el primer caso de prueba (Quick Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

start_time = timeit.default_timer()
quicksort_Algorit([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el segundo caso de prueba (Quick Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

start_time = timeit.default_timer()
quicksort_Algorit([])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el tercer caso de prueba (Quick Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

start_time = timeit.default_timer()
quicksort_Algorit([5])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el cuarto caso de prueba (Quick Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

start_time = timeit.default_timer()
quicksort_Algorit([6,5,4,3,2,1])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el quinto caso de prueba (Quick Sort): {(end_time - start_time) * 1000:.6f} milisegundos")

start_time = timeit.default_timer()
quicksort_Algorit([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
end_time = timeit.default_timer()
print(f"Tiempo de ejecucion para el sexto caso de prueba (Quick Sort): {(end_time - start_time) * 1000:.6f} milisegundos") """