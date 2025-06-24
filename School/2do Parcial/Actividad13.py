G = {'S' : ['A', 'B', 'C', 'D', 'E'] }

class Directed_Graph: #Pepe Cantoral
    def __init__(self ):
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Function to add a vertex to the graph
        :param vertex: Lo definimos como objeto de tipo vértice
        :return: Si existe mencionamos que ya existe,
        """
        if vertex not in self.graph:
            self.graph[vertex] = []
        else: return "Vertex already exists"

    def add_edge(self, edge):
        """
        Agregaremos el vertice
        :param source: self y source ( nodo origen)
        :return: El vertice ya agregado
        """
        vertex1 = edge.get_vertex1()
        vertex2 = edge.get_vertex2()
        if vertex1 not in self.graph and vertex2 not in self.graph[vertex1]:
            raise ValueError(f"Vertex {vertex1.get_name()} doesn't exists")
        self.graph[vertex1].append(vertex2)

    def count_vertex_and_edges(self):
        """
        Contamos los nodos que componen a la arista (edge)
        :return: Number of vertex and edges
        """
        num_vertex = len(self.graph)
        num_edge = sum(len(count) for count in self.graph.values())
        return num_vertex, num_edge

    def adejacency_matrix(self):
        """
        Generamos la matriz de adyacencia
        :return: vertex and maxtrix
        """
        vertex = list(self.graph.keys())
        n = len(vertex)
        matrix = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if vertex[j] in self.graph[vertex[i]]:
                    matrix[i][j] = 1
        return vertex, matrix

class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

    def get_vertex1(self):
        return self.vertex1

    def get_vertex2(self):
        return self.vertex2

    def __str__(self):
        return str(self.vertex1.get_name()) + ":" + str(self.vertex2.get_name())

class Vertex:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

#Creamos los vertices como objetos (vertex)
vA = Vertex('A')
vB = Vertex('B')
vC = Vertex('C')
vD = Vertex('D')
vE = Vertex('E')

#Nuestro grafo dirigido 'g'
g = Directed_Graph()
for v in [vA, vB, vC, vD, vE]: #Esto me lo dio en automatico la IA de interpretador
    g.add_vertex(v)

#Los agregue en orden para tener mejor visualización
g.add_edge(Edge(vA, vB))
g.add_edge(Edge(vA, vC))
g.add_edge(Edge(vB, vC))
g.add_edge(Edge(vB, vD))
g.add_edge(Edge(vC, vD))
g.add_edge(Edge(vD, vE))

#Mostramos la lista de adyacencia
print("Lista de adyacencias:")
for v in g.graph:
    print(f"{v}: {[str(n) for n in g.graph[v]]}")

#Mostramos la matriz de adyacencia
print("\nMatriz de adyacencia:")
vertices, matrix = g.adejacency_matrix()
print("   " + "  ".join(v.get_name() for v in vertices))

for i, row in enumerate(matrix):
    print( vertices[i].get_name(), row)

#Contestando a la pregunta cuantos vértices y aristas con la funcion count
v_count, e_count = g.count_vertex_and_edges()
print(f"\nVértices: {v_count}, Aristas: {e_count}\n")

"""
    Indica si el grafo es dirigido o no dirigido y justifica tu respuesta
        R = Es dirigido porque nos dan desde un inicio las conexiones que debe de tener
            y pues no son bidireccionales (que desde el origen vaya al destino y desde 
            el destino al origen). 
"""
