"""
Dada una lista de enteros arr, determina si existe un par de números donde uno sea el doble del otro.
Es decir, existe i y j tal que:
arr[i] == 2 * arr[j]   o   arr[j] == 2 * arr[i]
Y claro, i != j
Ejemplos de entrada:
Ejemplo 1:
arr = [10, 2, 5, 3]
📤 Salida esperada:
True
Porque 10 == 2 * 5

Ejemplo 2:
arr = [7, 2, 14, 11]
📤 Salida esperada:
True
Porque 14 == 2 * 7

Ejemplo 3:
arr = [3, 1, 7, 11]
📤 Salida esperada:
False
"""
arr = [10, 2, 5, 3]

def checkIfExist(arr):
    seen = set()
    for num in arr:
        if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False

impresion = checkIfExist(arr)
print(impresion)



