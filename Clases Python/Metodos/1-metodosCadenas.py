# Metodos de los caracteres 

c1 = "Hola, soy, Juan, Yañez"
c2 = "Eres muy wapo"

# La estructura es {Dato}.[Metodo()]
res = c1.upper() # upper() Convierte la cadena en mayusculas
res = c1.lower() # lower() Convierte la cadena en minusculas

res = c1.capitalize()# Capitalize() convierte todo en minuscula la primera letra en mayuscula

res = c2.find("u") # find() Busca el caracter dentro de alguna cadena, al no encontrar nada dara -1
res = c2.index("E") # index() Busca el caracter dentro de alguna cadena, al no encontrar nada dara un exception

res = c1.isnumeric() # isnumeric() Evlaua si la cadena es numerica, entregara false si no hay coincidencias
# isalpha() comprovara si hay numeros o caracteres dentro da la cadena(los espacios sern timados como caracter especial desde la A a la Z)
#entregara false si no hay coincidencias
res = c1.isalpha() 

res = c2.count("Eres") # count() Contara cuantas coincidencias encontramos dentro de un caracter
res = len(c2) # len({cadena}) Contara cuantos caracteres se encuantran dentro de la cadena 

res = c1.startswith("Hola") # Evalua si la primera palabara de la cadena de texto coincidie con lo que le pedimos
res = c1.endswith("Yañez") # Evalua si la ultima palbara de la cadena de texto coincidie con lo que le pedimos

res = c2.replace("Eres","Soy") # Cambia el valor de una cadena por otra

res = c1.split(",")
print(res)
