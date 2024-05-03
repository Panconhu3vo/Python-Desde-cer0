
num1 = int(input("Ingresa el primer valor numerico: "))
num2 = int(input("Ingresa el segundo valor numerico: "))
if num1==num2:
    print("Debes ingresar valores diferentes")
num3 = int(input("Ingresa el tercero valor numerico: "))
if num1==num3 or num2==num3:
    print("Debes ingresar valores diferentes")
num4 = int(input("Ingresa el cuarto valor numerico: "))
if num4==num1 or num4==num3 or num4==num2:
    print("Debes ingresar valores diferentes")


if num1>num2 and num1>num3 and num1>num4:
    print(f"El numero mayor es {num1}")

elif num2>num1 and num2>num3 and num2>num4:
    print(f"El numero mayor es {num2}")

elif num3>num1 and num3>num2 and num3>num4:
    print(f"El numero mauor es {num3}")
    
else:
    print(f"El numero mayor es {num4}")
