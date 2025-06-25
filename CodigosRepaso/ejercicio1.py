"""
Dada una lista de palabras, imprime todas aquellas que estén en una posición impar y que tengan más de 3 letras.
"""

palabras = ["sol", "luna", "estrella", "mar", "universo"]
#Salida esperada
# luna
# universo

for i, palabra in enumerate(palabras):
    if i % 3 == 1 and len(palabra) > 3:
        print(palabra)
