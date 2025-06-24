"""
Daniel Alejandro Sánchez Ahumada
23310411
Actividad 9

"""

import time
#Implementación de una tabla hash con encadenamiento separado //ChioCode
class TablaHash:
        def __init__(self, tamanio_tabla):
            self.tamanio_tabla = tamanio_tabla
            #self.tabla_hash = {}
            #self.tabla = [[] for i in range(tamanio_tabla)]
            self.tabla = [None] * tamanio_tabla  #Lista con los espacios vacíos

        def funcion_hash(self, clave):
            #En este caso estamos calculando el índice usando la suma de los valores ASCII
            #De los caracteres mod en el tamaño de la tabla
            return sum(ord(c) for c in clave) % self.tamanio_tabla

        def insertar(self, clave, valor_hash):
            indice = self.funcion_hash(clave)
            #El sondeo lineal
            while self.tabla[indice] != None:
                indice = (indice + 1) % self.tamanio_tabla #Avanzamos al siguiente indice
            #Añadimos el par clave-valor en la lista del índice correspondiente
            #self.tabla[indice].append(valor_hash) #Aqui agregamos una tupla con clave y valor /No charcho
            self.tabla[indice] = (clave,valor_hash)

        def obtener(self, clave):
            indice = self.funcion_hash(clave)
            #Buscamos en la lista enlazada del índice por la clave
            """for k, v in self.tabla[indice]: #recorremos la lista comparando todo por la clave
                if k == clave:
                    return v
                return None
            """
            #Buscamos en la lista enlazada usando sondeo lineal
            tiros = 0
            while self.tabla[indice] != None and tiros < self.tamanio_tabla:
                k,v = self.tabla[indice]
                if k == clave:
                    return v
                indice = (indice + 1) % self.tamanio_tabla #Sigue haciendo iteraciones para buscar el bucket
                tiros += 1
            return None #No encontramos la clave

        def eliminar(self, clave):
            indice = self.funcion_hash(clave)
            tiros = 0
            while self.tabla[indice] != None and tiros < self.tamanio_tabla:
                if self.tabla[indice] != "ELIMINADO": #Agrego un marcador para que funcione
                    k, v = self.tabla[indice]
                    if k == clave:
                        self.tabla[indice] = "ELIMINADO"  #Lo eliminamos
                        return True  #Retorno true para decir que lo eliminamos

                indice = (indice + 1) % self.tamanio_tabla
                tiros += 1

            return False  #No encontramos el bucket a buscar

        def mostrar_tabla(self):
            print("\nTabla Hash:")
            for i, elemento in enumerate(self.tabla):
                print(f"Índice {i}: {elemento}")

#Creamos la tabla hash con encadenamiento separado
hash_table = TablaHash(8)

#Insertamos valores, incluyendo colisiones
hash_table.insertar("juan", 10)
hash_table.insertar("daniel", 20)
#Colisionará con "juan" y en teoría se reubica
hash_table.insertar("carlos", 30)

#Imprimimos la tabla hash
for i, lista in enumerate(hash_table.tabla):
    print(f"Indice {i}:\t {lista}")

#Obtener el valor de una clave
print("Valor de 'juan':", hash_table.obtener("juan"))
print("Valor de 'daniel':", hash_table.obtener("daniel"))
print("Valor de 'carlos':", hash_table.obtener("carlos"))

#Nuestra metodo de eliminar
print("\nEliminamos a 'juan' por colision jiji")
hash_table.eliminar("juan")
#print("Valor de 'juan':", hash_table.obtener("juan"))
hash_table.mostrar_tabla()


def prueba_factor_carga(factor_carga, tamanio_tabla):
    hash_table = TablaHash(tamanio_tabla)
    num_elementos = int(tamanio_tabla * factor_carga)

    inicio = time.time()
    for i in range(num_elementos):
        hash_table.insertar(f"clave{i}", i)
    fin = time.time()

    print(f"\nTiempo con factor de carga {factor_carga}: {fin - inicio:.6f} segundos")

tamanio_tabla = 20
prueba_factor_carga(0.5, tamanio_tabla)
prueba_factor_carga(0.75, tamanio_tabla)
prueba_factor_carga(0.9, tamanio_tabla)