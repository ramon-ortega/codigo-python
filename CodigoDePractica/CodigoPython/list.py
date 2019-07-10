#Una lista es una coleccion que esta ordenada y que puede ser intercambiable.
#Creamos una lista, 1era manera de hacerlo
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#creamos una lista
numbers2=list((1,2,3,4,5))

print(numbers,fruits)

#Obtenemos un valor de la lista, en este caso 0

print(fruits[0])

#Obtenemos la longitud

print(len(fruits))

#Append to the list-Adjuntamos datos a la lista

fruits.append('Mangos')

print(fruits)

#REMOVER DE LA LISTA

fruits.remove('Grapes')
print(fruits)

#insertar a posicion
fruits.insert(2,'Fresa')
print(fruits)

#Remover de una posicion con pop
fruits.pop(2)
print(fruits)

#Reverse the list
fruits.reverse()
print(fruits)

#acomodar alfabeticamente
fruits.sort()
print(fruits)
