

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 > numero2:
    print(numero2)
    print(numero1)
elif numero2 > numero1:
    print(numero1)
    print(numero2)
else:
    print("Error los numeros son iguales")
