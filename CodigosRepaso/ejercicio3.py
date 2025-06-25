"""
Problema:
Dada una lista de números, imprime el doble de todos los números que estén en una posición par y sean mayores que 5.
"""

numeros = [4, 9, 6, 2, 8, 3, 7]
# Salida: 12, 16, 14

for i, numero in enumerate(numeros):
    if i % 2 == 0 and numero > 5:
        print(numero*2)
