import time
import random


class Ordenamientos:
    """Clase que contiene los 3 métodos de ordenamiento"""

    @staticmethod
    def bubble_sort(arr):
        """Nuestro método de burbuja"""  # Tutoriales M-E
        n = len(arr)  # Asigno 'n' a la longitud del arreglo con el que vamos a trabajar
        for i in range(n):
            for j in range(0, n - i - 1):  # Segundo bucle para intercambiar elementos
                if arr[j] > arr[j + 1]:  # Comprobación de burbuja, estamos comprobando con la siguiente posición
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambio usando desempaquetado
        return arr  # Nuestra lista ordenada

    @staticmethod
    def merge_sort(arr):
        """Nuestro método de merge"""  # Pepe Cantoral, Chio Code
        if len(arr) > 1:  # Condición base para la recursión
            mid = len(arr) // 2  # Encontramos el punto medio dividiendo a la mitad el arreglo
            left_half = arr[:mid]  # Los separamos con slicing... del inicio a la mitad
            right_half = arr[mid:]  # Los separamos con slicing... de la mitad al final

            Ordenamientos.merge_sort(left_half)  # Función recursiva para ordenarlos a la izquierda
            Ordenamientos.merge_sort(right_half)  # Función recursiva para ordenarlos a la derecha

            i = j = k = 0  # Recorremos las mitades (i = left_half; j = right_half; k = arreglo original)

            # Comparación y fusión
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:  # Si nuestro índice de la izquierda es menor
                    arr[k] = left_half[i]  # Lo agregamos a nuestro arreglo original
                    i += 1  # Avanzamos posición en left_half
                else:
                    arr[k] = right_half[j]  # Agregamos posición en right_half
                    j += 1  # Avanzamos posición en right_half
                k += 1  # Avanzamos posición en nuestro arreglo original

            # Si quedan elementos en la mitad izquierda, los agregamos
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            # Juntamos todos los datos de la mitad derecha
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        return arr  # Devolvemos el arreglo ordenado

    @staticmethod
    def quick_sort(arr):  # Chio code
        """Nuestro método de quicksort"""
        if len(arr) <= 1:  # Primer caso cuando ya están ordenados
            return arr
        pivot = arr[len(arr) // 5]  # Seleccionamos el pivote (le puse 5 para comprobar funcionamiento)
        left = [x for x in arr if x < pivot]  # Elementos menores al pivote
        middle = [x for x in arr if x == pivot]  # Elementos iguales al pivote
        right = [x for x in arr if x > pivot]  # Elementos mayores al pivote
        return Ordenamientos.quick_sort(left) + middle + Ordenamientos.quick_sort(
            right)  # Ordenamos recursivamente según la norma


def mostrar_resultados(algoritmo, datos):
    """Función para mostrar los resultados del algoritmo"""
    tiempo_inicio = time.time()  # Analizamos el tiempo antes de iniciar el algoritmo
    resultado = algoritmo(datos.copy())  # Iniciamos el proceso con la copia (para no dañar el original)
    tiempo_fin = time.time()  # Tiempo al finalizar el algoritmo
    tiempo_total = tiempo_fin - tiempo_inicio  # Calcular el tiempo total

    print(f"\nAlgoritmo: {algoritmo.__name__}")
    print(f"Tiempo de ejecución: {tiempo_total:.7f} segundos") # Mostramos 7 decimales para mejor visualización

    # Para facilitar la demostración uso slice para solo mostrar los primeros 10 y los ultimos 10
    print("Primeros 10 elementos ordenados:", resultado[:10])
    print("Últimos 10 elementos ordenados:", resultado[-10:])


def main():
    # Definir tres tamaños diferentes de datos para probar
    tamaños = [100, 1000, 5000]

    for tamaño in tamaños:
        print(f"\n--- Pruebas con {tamaño} elementos ---")
        lista_original = [random.randint(0, 9999) for _ in range(tamaño)]  # Lista aleatoria

        """Mandamos llamar la función de mostrar resultados para cada algoritmo"""
        # serán 3 llamadas
        mostrar_resultados(Ordenamientos.bubble_sort, lista_original)
        mostrar_resultados(Ordenamientos.merge_sort, lista_original)
        mostrar_resultados(Ordenamientos.quick_sort, lista_original)


if __name__ == "__main__":
    main()
