mi_lista = ['uno','dos',3]
otra_lista = ['cuatro', 'cinco']
nueva_lista = mi_lista + otra_lista
nueva_lista[0] = 'Danielini'
print(mi_lista[1:])
print(mi_lista + otra_lista)
print(nueva_lista)
#Las listas si son mutables podemos trabajar y agregar
#append,format
nueva_lista.append('Seis')
print(nueva_lista)

item_popeado = nueva_lista.pop(-1)
print(item_popeado)

#ordenar lista
lista_ordenada = ['a', 'z', 'x', 'b', 'd']
num_list = [4,1,5,7,3]
lista_ordenada.sort(reverse=True)
print(lista_ordenada)
num_list.reverse()
print(num_list)
