"""
Dada una lista de palabras, regresa las k más frecuentes. Si hay empate en frecuencia, usa orden alfabético.
Entrada:words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
Salida: ["i", "love"]
"i" aparece 2 veces, "love" 2 veces, pero "i" va primero alfabéticamente.
"""
from collections import Counter
import heapq

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
def topKFrequentWords(words, k):
    freq = Counter(words)
    heap = heapq.nsmallest(k, freq.items(), key=lambda x: (-x[1], x[0]))
    return [word for word, count in heap]

frecuent = topKFrequentWords(words, k)
print(frecuent)



