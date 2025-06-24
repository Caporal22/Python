#Implementación de DFS Recursivo en Python
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ") #Imprimir el nodo visitado
        visited.add(node)  #Marcar el nodo como visitado
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

#Grafp representado como un diccionario de listas de adyacencia
graph = {
    
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
dfs(graph, 'A', visited)