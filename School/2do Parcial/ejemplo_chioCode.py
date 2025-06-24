"""
Implementación de la tabla hash para almacenar los valores usando la función hash definida
"""

def funcion_hash(clave, tamanio_tabla):
    valor_hash = 0
    for c in clave:
        valor_hash = valor_hash + ord(c) - ord('a') + 1
    return valor_hash % tamanio_tabla

    #Inicializamos tabla hash con tamaño de 20
tabla_hash = [None] * 20

#Insertamos los valores en nuestra tabla hash
strings = ["ambar",
           "mirna",
           "karol",
           "natalia",
           "daniel",
           "sam",
           "alberto",
           "damian",
           "angel",
           "alejandro"
           ]
tamanio_tabla = len(tabla_hash)

for string in strings:
        indice = funcion_hash(string, tamanio_tabla)
        tabla_hash[indice] = string

for i, valor in enumerate(tabla_hash):
    print(f"Índice {i}: {valor}")