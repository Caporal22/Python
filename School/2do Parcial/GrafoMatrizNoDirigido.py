class GrafoMatrizNoDirigido:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]

    def agregar_arista(self, origen, destino ):
        self.matriz[origen][destino] = 1
        self.matriz[destino][origen] = 1 #Para no dirigido

    def mostrar_martriz(self):
        for fila in self.matriz:
            print(fila)

#Ejemplo de uso:
grafo_matriz_nd = GrafoMatrizNoDirigido(4)
grafo_matriz_nd.agregar_arista(0, 1)
grafo_matriz_nd.agregar_arista(0, 2)
grafo_matriz_nd.agregar_arista(1, 3)
grafo_matriz_nd.agregar_arista(2, 3)
print("Grafo No Dirigido (Matriz de Adyacencia): ")
grafo_matriz_nd.mostrar_martriz()