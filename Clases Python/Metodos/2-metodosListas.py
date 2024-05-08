
lista = list(["hola",3,"bien",True,4])
lista2 = [1,5,2,4,3,True]
cantidadElementos = len(lista) # Muestra la cantidad de items en una lista

lista.append("Juan") #Agerega un valor a la lista, separado
lista.insert(2,"Pedro") #Agerega un valor a la lista dando el indice de donde lo pondremos
lista.extend([False,"Pepe"]) # Agerega un valor a la lista pero con valores dentro de una lista 

lista.pop(5) # Elimina el item de la lista segun su indice. Al poner numeros negativos emepzara por el ultimo item de la lista

lista.remove(False) # Elimina yn item segun su valor

lista2.sort()# Ordena la lista de mayor a menor(reversed=True lo hara de mayor a menor)

print(lista2)
lista.clear()# Elimina todos los items de la lista
