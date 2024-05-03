# Tipo de datos Compuestos
# Son el tipo de datos con mas datos simples dentro de el

# List
lista = ["Juan Yañez","Dania Torres",16,17,1.64] # Una lista puede almacenar distintos tipos de datos separados por una , y comenzando del 0, y esta puede ser modificada
# Tupla
tupla = ("Juan Yañez","Dania Torres",16,17,1.64) # Una tupla puede almacenar distintos tipos de datos separados por una , y comenzando del 0, y esta NO puede ser modificada

lista[1] = "Javier Orden" # Asi podremos modificar items de la lista
# tupla[1] = "Javier Orden" # No puede ser modificadas
print(lista[1])

# Conjunto (set)
conjunto = {"Juan Yañez","Dania Torres",16,17,1.64} 
# Al igual quem las tuplas no puede ser modificadas, No podemos imprimirlo con el indice, y los items repetidos no seran mostrados, y seran ordenados
print(conjunto)

# Diccionario (Dict)
Diccionario = { # Es unalista pero en vez del indice se cataloga por la calve, la forma de escribirlo es 'key' : "value"
    'nombre' : "Juan Yañez",
    'años' : 16,
    'altura' : 1.56
}
print(Diccionario['años']) # llamamos a la clave del diccionario