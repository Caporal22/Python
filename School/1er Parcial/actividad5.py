"""
Daniel Alejandro Sánchez Ahumada
23310411    4O
Actividad 5   Primer parcial
"""

class Nodo:
    #Lista enlazada
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completado = False
        self.siguiente = None


class ListaTareas:
    #Manejo de lista enlazada
    def __init__(self):
        self.cabeza = None  #La lista inicia vacía... Primer nodo de la lista


    #Función para agregar una nueva tarea
    def agregar_tarea(self, descripcion, prioridad):
        nuevo_nodo = Nodo(descripcion, prioridad) #Creación de nodo
        nuevo_nodo.siguiente = self.cabeza #Apuntamos al nodo anterior
        self.cabeza = nuevo_nodo #Actualizamos cabeza de la lista


    #Función completar tarea si coincide con la descripción
    def completar_tarea(self, descripcion):
        actual = self.cabeza #Actual empieza desde el nodo cabeza
        while actual:
            if actual.descripcion == descripcion:
                actual.completado = True #Marcar como completada
                return
            actual = actual.siguiente #Apuntamos al siguiente nodo
        print("Tarea no encontrada.")


    #Funcion para eliminar tareas que han sido completadas
    def eliminar_tareas_completadas(self):
        while self.cabeza and self.cabeza.completado: #Si la cabeza está completada, se elimina
            self.cabeza = self.cabeza.siguiente

        actual = self.cabeza #Actual empieza desde el nodo cabeza
        while actual and actual.siguiente: #Verificación de todos los nodos
            if actual.siguiente.completado: #Iniciamos búsqueda simple
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente


    #Funcion para mostrar las tareas actualizadas
    def mostrar_tareas(self):

        actual = self.cabeza #Actual empieza desde el nodo cabeza
        while actual: #Verificación de todos los nodos
            estado = "Completada" if actual.completado else "Pendiente" #Obtenemos dato de estado
            print(f"Descripción: {actual.descripcion}, Prioridad: {actual.prioridad}, Estado: {estado}")
            actual = actual.siguiente

#Creamos nuestra lista enlazada
lista = ListaTareas()

#Agregamos tareas
lista.agregar_tarea("Viajar a guayabitos", 2)
lista.agregar_tarea("Estudiar para el examen", 4)
lista.agregar_tarea("Ir al gimnasio", 3)
lista.agregar_tarea("Terminar tarea estructura", 5)
lista.agregar_tarea("Bañarme", 1)

#Mostramos tareas
print("\n--- Tareas actuales: ---")
lista.mostrar_tareas()

#Cambiamos de estado a completada
lista.completar_tarea("Hacer la compra")
lista.completar_tarea("Ir al gimnasio")
lista.completar_tarea("Bañarme")

#Actualizar tareas
print("\n--- Después de completar una tarea: ---")
lista.mostrar_tareas()

#Eliminar tareas completadas
lista.eliminar_tareas_completadas()

#Terminamos el programa mostrando las tareas pendientes
print("\n--- Después de eliminar tareas completadas: ---")
lista.mostrar_tareas()
print("\n ----- Finalización ----")