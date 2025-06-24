class GrafoListaPonderado:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def agregar_arista(self, origen, destino, peso):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        # Al agregar la arista, se guarda como una tupla (destino, peso)
        self.grafo[origen].append(destino, peso)
        self.grafo[destino].append(origen, peso) #Para no dirigido

    def mostrar_grafo(self):
        for vertice in self.grafo:
            print(f"{vertice} -> {self.grafo[vertice]}")

# Ejemplo de uso
grafo_ponderado = GrafoListaPonderado()
grafo_ponderado.agregar_arista("A", "B", 4)
grafo_ponderado.agregar_arista("A", "C", 2)
grafo_ponderado.agregar_arista("B", "D", 5)
grafo_ponderado.agregar_arista("C", "D", 8)
grafo_ponderado.agregar_arista("B", "C", 1)
print("Grafo Ponderado No Dirigido (Lista de adyacencia): ")
grafo_ponderado.mostrar_grafo()