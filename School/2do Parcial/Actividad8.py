"""
Daniel Alejandro Sánchez Ahumada
23310411
Actividad 8
"""


def funcion_hash(clave):
    valor_hash = 0
    valor_hash = sum(ord(c) - ord('a') for c in str(clave))
    for c in clave:
        valor_hash = valor_hash + ord(c) - ord('a') + 1
    return valor_hash

tabla_hash = {}

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

for string in strings:
        indice = funcion_hash(string)
        tabla_hash[string] = indice

print("Tabla Hash generada:")
for clave, valor in tabla_hash.items():
    print(f"Clave: {clave}\t\t Hash: {valor}")

print("\nAccediendo a valores con claves:")
print("El hash de 'mirna' es:\t", tabla_hash["mirna"])
print("El hash de 'natalia' es:", tabla_hash["natalia"])

"""
1) 	- ¿Qué ventaja tiene una tabla hash sobre un arreglo para búsquedas?
R= Bueno al inicio estaba utilizando lo que viene siendo las listas pero vi que no era, y al usarlo estaba haciendo un poco más lenta mi computadora
por lo que analizanod lo que vimos la clase anterior en el diccionario es es O(1) y en la lsta creo que era O(n) y aparte no se necesitan recorrer todos
los arreglos solo se calcula el hash y el sistema en corto lo encuentra
"""