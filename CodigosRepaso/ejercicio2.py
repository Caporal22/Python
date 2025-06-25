# Enunciado
"""
Dado un arreglo de enteros nums y un entero target, encuentra dos índices diferentes i y j tal que:

nums[i] + nums[j] == target
Devuelve una lista con ambos índices [i, j].
Debe ser la primera combinación válida que encuentres.
"""
# Salida [0, 1]
"""
Lo que vas a practicar aquí:
Recorrer con for usando range().

Uso eficiente de dict (hash map) para encontrar complementos.

Pensamiento de eficiencia (O(n) vs O(n²)).

"""

nums = [2, 7, 11, 15]
target = 9
hashmap = {}

for i, num in enumerate(nums):
    complemento = target - num
    if complemento in hashmap:
        print([hashmap[complemento], i])
        break
    hashmap[num] = i







