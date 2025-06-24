class GrafoListadoNoDirigido:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_artista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        # Agregar en ambos sentidos para un grafo no dirigido:
        self.grafo[origen].append(destino)
        self.grafo[destino].append(origen)

    def mostrar_grafo(self):
        for vertice in self.grafo:
            print(f"{vertice} -> {self.grafo[vertice]}")

# Ejemplo de uso
grafo_nd = GrafoListadoNoDirigido()
grafo_nd.agregar_artista("A", "B")
grafo_nd.agregar_artista("A","C")
grafo_nd.agregar_artista("B","D")
grafo_nd.agregar_artista("C","D")
print("Grafo no dirigido (Lista de adyacencia): ")
grafo_nd.mostrar_grafo()
