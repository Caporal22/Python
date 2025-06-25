"""
Dadas dos cadenas s y t, devuelve True si t es un anagrama de s, y False en caso contrario.
Entradas:
s = "anagram", t = "nagaram"
Salida esperada:
True

 Otra entrada:
s = "rat", t = "car"
Salida esperada:
False
"""
from collections import Counter
s = "rat"
t = "car"

def checkAnagram(s,t):
    return Counter(s) == Counter(t)

resultado = checkAnagram(s,t)
print(resultado)