import math

radio = int(input("Ingresa el radio de tu circunferencia: "))

p = int(math.pi * (radio*2))
a = int(math.pi * (radio**2))

print(f"El perimetro es {p}cm y el area es {a}cm2")

