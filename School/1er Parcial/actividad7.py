import sys
import time
import random

def bubble_sort(arr):
    """Nuestro método de burbuja"""    #Tutoriales M-E
    n = len(arr)  #Asigno 'n' a la longitud del arreglo con el que vamos a trabajar
    for i in range(n):
        for j in range(0, n - i - 1):  #Segundo bucle para intercambiar elementos
            if arr[j] > arr[j + 1]:  #Comprobación de burbuja, estamos comprobando con la siguiente posición
                arr[j] =  arr[j + 1] #Cambio de posición una vez que se hace la comparación
                arr[j + 1] = arr[j]  #Hacemos el cambio de posición para no perder el dato
    return arr  #Nuestra lista ordenada

def merge_sort(arr):
    """Nuesto método de merge"""  #Pepe Cantoral, Chio Code
    if len(arr) > 1:  #Condición base para la recursión
        mid = len(arr) // 2  #Encontramos el punto medio dividiendo a la mitad el arreglo
        left_half = arr[:mid]  #Los separamos con slicing... del inicio a la mitad
        right_half = arr[mid:]  #Los separamos con slicing... de la mitad al final

        merge_sort(left_half)  #Función recursiva para ordenarlos a la izquierda
        merge_sort(right_half)  #Función recursiva para ordenarlos a la derecha

        i = j = k = 0  #Recorremos las mitades (i = left_half; j = right_half; k = arreglo original)

        #Comparación y fusión
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]: #Si nuestro índice de la izquierda es menor
                arr[k] = left_half[i] #Lo agregamos a nuestro arreglo original
                i += 1 #Avanzamos posición en left_half
            else:
                arr[k] = right_half[j] #Agregamos posición en right_half
                j += 1 #Avanzamos posición en right_half
            k += 1 #Avanzamos posición en nuestro arreglo original

        # Si quedan elementos en la mitad izquierda, los agregamos
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        #Juntamos todos los datos de la mitad derecha
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr  #Devolvemos el arreglo ordenado


# Definimos el algoritmo Quick Sort
def quick_sort(arr):  #Chio code
    """"Nuestro método de quicksort"""
    if len(arr) <= 1:  #Primer caso cuando ya estar ordenados
        return arr
    pivot = arr[len(arr) // 5]  #Seleccionamos el pivote... le puse 5 para comprobar funcionamiento
    left = [x for x in arr if x < pivot]  #Elementos menores al pivote
    middle = [x for x in arr if x == pivot]  #Elementos iguales al pivote
    right = [x for x in arr if x > pivot]  #Elementos mayores al pivote
    return quick_sort(left) + middle + quick_sort(right)  #Ordenamos recursivamente según la norma


# Función para medir tiempo y memoria de cada algoritmo
def medir_algoritmo(algoritmo, datos):

    memoria_antes = sys.getsizeof(datos) #Analizamos la memoria antes de iniciar algoritmo
    tiempo_inicio = time.time() #Analizamos el tiempo antes de iniciar el algoritmo
    resultado = algoritmo(datos.copy()) #Iniciamos el proceso con la copia(recomendación para no dañar el original)

    tiempo_fin = time.time() #Tiempo al finalizar el algoritmo
    memoria_despues = sys.getsizeof(resultado) #Memoria al finalizar el algoritmo

    tiempo_total = tiempo_fin - tiempo_inicio #Tiempo total restando final con inicio

    print(f"\nAlgoritmo: {algoritmo.__name__}")
    print(f"Tiempo de ejecución: {tiempo_total:.6f} segundos")
    print(f"Memoria antes: {memoria_antes} bytes")
    print(f"Memoria después: {memoria_despues} bytes")


tamaños = [10_000, 15_000, 20_000]  #Use esos tamaños para no hacer explotar la pc

for tamaño in tamaños:
    print(f"\n--- Pruebas con {tamaño} elementos ---")

    lista_original = [random.randint(0, 9999) for _ in range(tamaño)] #Lista aleatoria de numeros del 0 al 9999

    """Mandamos llamar la función de medir algoritmo y cumplir práctica"""
    medir_algoritmo(bubble_sort, lista_original)
    medir_algoritmo(merge_sort, lista_original)
    medir_algoritmo(quick_sort, lista_original)


"""
1. ¿Cuál de los algoritmos usa más memoria y por qué?
    R = Merge, ya que genera mas memoria para las listas left y right durante su recursión
2. ¿Cómo afecta el uso de memoria a la eficiencia del algoritmo?
    R = Puede hacer el algoritmo (nuestros métodos de ordenamiento) más lentos
3. ¿Cuál es la complejidad temporal de cada algoritmo?
    R = Bubble Sort : O(n^2)
        Merge Sort : O(nlog(n))
        Quick Sort : O(nlog(n)) y según investigue se puede hacer la recursividad mal y ser O(n^2) //Me paso :(
"""