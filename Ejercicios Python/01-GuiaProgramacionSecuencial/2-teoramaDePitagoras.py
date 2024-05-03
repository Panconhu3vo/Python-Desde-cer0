import math

c1 = int(input("Ingresa un valor numerico del primer cateto: "))
c2 = int(input("Iigresa el segundo valor numerico del cateto: "))

h = (c1**2) + (2**2)

h= int(math.sqrt(h))
print(f"La hipotenusa mide aproximadamente: {h}")