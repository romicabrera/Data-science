#listas en python
#estructura para almacenar datos con un orden especifico de inseccion

#positivos [0,1,2,3,4,...]
#negativos [0,-1,-2,-3,-4]

lista = [1,2,3,4]
lista_diferentes_valores = [1,"2",3,"4",1.5,True,False,lista]

print(lista_diferentes_valores) #[1, '2', 3, '4', 1.5, True, False, [1, 2, 3, 4]]

#para acceder a los valores de un arreglo se utilizan los indices
#0 a n-1, pero tambien pueden ser negativos

print(lista[0]) #accediendo al indice 0 de la lista, 1
print(lista[-1]) #accediendo al indice -1 de la lista, 4

#algunos metodos de las listas
#agregar, anexar valor
#nombre.append()
lista.append(5)
print(lista) # [1, 2, 3, 4, 5]

#remove por elemento existen en la lista .remove(elemento)
lista.remove(5)
print(lista) # [1, 2, 3, 4]

#pop elimina por indice .pop(indice)
a = lista.pop(1)
print(a) # 2
print(lista) # [1, 3, 4]

#inserccion por indice insert(indice,valor)
lista.insert(1,2) 
print(lista) # [1, 2, 3, 4]

#indice por elemento index(elemento)
indice = lista.index(2)
print(indice) # 1

#ordenar elementos dentro de la lista
lista.sort()