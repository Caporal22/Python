import sys
import matplotlib.pyplot as plt
import random
import string

"""
Daniel Alejandro Sánchez Ahumada
23310411    4O
Actividad 6   Primer parcial
"""

#Función para generar una cadena aleatoria de longitud fija //Función sacada de git
def generar_cadena(longitud=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=longitud))

#Función para medir el tamaño de una estructura con "n" elementos
def medir_tamano(n):
    lista = [generar_cadena() for _ in range(n)]  #Lista con las cadenas aleatorias
    diccionario = {generar_cadena(): generar_cadena() for _ in range(n)}  #Diccionario con claves y valores aleatorios
    conjunto = {generar_cadena() for _ in range(n)}  #Conjunto con cadenas únicas aleatorias

    return sys.getsizeof(lista), sys.getsizeof(diccionario), sys.getsizeof(conjunto) #Obtenemos nuestros datos para ver cual es la mas pesada (ocupa mas memoria...Mi compu se trabo despues de esto xd

#Rango de tamaños a probar
rangos = [10, 100, 1000, 10000, 100000, 1000000]

"""
    La verdad esto lo hizo chat
"""
tam_listas = []
tam_dicts = []
tam_sets = []

# Medir tamaños para cada cantidad de elementos
for n in rangos:
    tam_lista, tam_dict, tam_set = medir_tamano(n)
    tam_listas.append(tam_lista)
    tam_dicts.append(tam_dict)
    tam_sets.append(tam_set)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(rangos, tam_listas, marker='o', label="Lista (list)")
plt.plot(rangos, tam_dicts, marker='s', label="Diccionario (dict)")
plt.plot(rangos, tam_sets, marker='^', label="Conjunto (set)")

plt.xlabel("Número de elementos")
plt.ylabel("Tamaño en bytes")
plt.title("Crecimiento del tamaño en memoria según la estructura de datos")
plt.xscale("log")  # Escala logarítmica para mejor visualización
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.show()
