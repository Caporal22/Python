"""
Problema: Kth Largest Element in a Stream
Vas recibiendo números uno por uno, como en un stream infinito.
En cada punto, debes ser capaz de decir cuál es el K-ésimo
más grande de todo lo que has visto hasta ahora.
"""

from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())

comprobation = groupAnagrams(strs)
print(comprobation)
