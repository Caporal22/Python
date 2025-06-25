"""numeros = [1, 2, 2, 3, 1, 4, 2]
# {1: 2, 2: 3, 3: 1, 4: 1}

Uso de for para recorrer listas.

Uso de dict para almacenar resultados.

Condicionales (if) para verificar si ya viste un valor

frecuencia= {}

for numero in numeros:
    if numero not in frecuencia:
        frecuencia[numero] = 1
    else:
        frecuencia[numero] += 1
print(frecuencia)
"""


"""
Dada una lista de enteros nums y un número target, encuentra dos índices i y j donde nums[i] + nums[j] == target.
Devuelve los índices en una lista: [i, j].
Puedes asumir que siempre hay exactamente una solución válida.
No puedes usar el mismo elemento dos veces
"""

nums = [2, 7, 11, 15]
target = 9
hashmap = {}
#Salida esperada [0, 1]

for i, num in enumerate(nums):
    complement = target - num
    if complement in hashmap:
        print([hashmap[complement], i])
        break
    hashmap[num] = i
















