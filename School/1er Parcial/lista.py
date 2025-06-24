def find_first(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i #Termina en la primera conicidencia
    return -1  #No encontrado
#O-N    0(1) + O(n)  ---> Respuesta final



def sum_pairs(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i] + arr[j], end=' ')  #Imprime todas las combinaciones
#0-n^2   ---> Respuesta final


def recursive_function(n):
    if n == 0:
        return
    print(n, end=' ')
    recursive_function(n // 2)
#O-LogOn   --> Respuesta al final
#Recursividad siempre es log(n)
#Se llaman así mismas, reduciendo las posibilidades


def quicksort(arr):
    if len(arr) <= 1:
        return arr  #caso base
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]  #Elementos menores
    middle = [x for x in arr if x == pivot]  #Elementos iguales
    right = [x for x in arr if x > pivot]  #Elementos mayores
    return quicksort(left) + middle + quicksort(right)
#O(n log N)  --> Respuesta final

def generate_subsets(arr):
    result = []
    n = len(arr)
    for i in range(2**n):  #Recorre todos los subconjuntos posibles
        subset = []
        for j in range(n):   #Verficia cada but del número i
            if(i & (1 << j)) != 0: subset.append(arr[j])
        result.append(subset)
    return result
#O-2**N  --> Respuesta final


