"""
Dado un array nums y un entero k, retorna los k elementos más frecuentes del array.
 Entrada:
nums = [1,1,1,2,2,3], k = 2
Salida esperada:
[1, 2]
"""
from collections import Counter
import heapq
nums = [1,1,1,2,2,3]
k = 2
def frecuentValues(nums, k):
    counter = Counter(nums)
    # print(counter)
    mostFrecuent =heapq.nlargest(k,counter.items(), key=lambda x:x[1])
    print(mostFrecuent)
    return [item for item, count in mostFrecuent]

comprobation = frecuentValues(nums, k)
print(comprobation)

top_k = [(1, 3), (2, 2), (6, 5)]
print([item for item, count in top_k])  # [1, 2]

reversed_list = list(reversed(nums))
print(reversed_list)