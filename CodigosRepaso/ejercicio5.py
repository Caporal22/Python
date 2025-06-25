"""
Comprueba si la cantidad de ocurrencias de cada número en el array es única.
Salida: True
"""
arr = [1, 2, 2, 1, 1, 3]

def checkIfExist(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

comprobacion = checkIfExist(arr)
print(comprobacion)