from collections import deque

def bfs_lista(grafo, inicio):
    visitados = set()
    cola = deque([inicio])

    while cola:
        actual = cola.popleft()
        if actual not in visitados:
            print(actual, end=" ")
            visitados.add(actual)
            for vecino in grafo[actual]:
                if vecino not in visitados:
                    cola.append(vecino)
    print()

def dfs_lista(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    print(inicio, end="  ")
    visitados.add(inicio)
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            dfs_lista(grafo, vecino, visitados)