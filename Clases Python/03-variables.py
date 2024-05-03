# Las variables pueden almacenar distintos tipos de datos, este varia por esto se llaman variables

# Para declarar variables usan este esquema {Nombre} = {Definicion segun el tipo de dato}
# Los nombres deben tener un nombre unico al usar el mismo nombre repetidas veces simplemente le cambiariamos el valor

nombre = "Juan"
bienvenida = f"Hola {nombre} ¿como estas?"

# in / not in podemos usarlos para busacr caracteres dentro de cadenas de texto
# in : Dara True si los caracteres consultados se encuentran en la cadena
# not in : Dara Flase si los caracteres consultados se encuentran en la cadena

print("Juan" in bienvenida) #True
print("Juan" not in bienvenida) #False