set1 = set([1,2,3,4,5,6,7,8,9,10]) #en un set no podemos tener datos duplicados
set2 = set([0,2,4,6,8,10,12,14,16,18,20])

print(set1)
print(set2)

#Si tengo una lista de datos duplicados y quiero rápidamente sacar cuáles son los únicos valores que tengo sin importar cuantas veces aparece uno
# podríamos transformar nuestra lista.

#Cosas que podemos hacer con los sets
#- Operacioens de conjuntos matemáticos estandares, (buscar intersección, union o que elementos esta en cada unos)

print(set1 - set2)  #Que elementos hay en el set1 que no hay en el set 2
print(set2 - set1)  #Que elementos hay en el set2 que no hay en el set 1
print(set1 & set2)  #Intersección de los dos conjuntos //Que elementos hay en ambos conjuntos
print(set1 | set2)  #Cual es conjunto union que incluye todos los elementos del set1 y el set2